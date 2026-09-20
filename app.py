import streamlit as st

from rag.retriever import build_vector_store, retrieve_similar_posts
from agents.generator import generate_post
from agents.critic import critic_agent
from agents.optimizer import optimizer_agent


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="LinkedInGenAI",
    page_icon="💼",
    layout="wide"
)


# ============================================================
# LOAD RAG SYSTEM
# ============================================================

@st.cache_resource
def load_rag_system():
    return build_vector_store()


try:
    index, data = load_rag_system()

except Exception as e:
    st.error("Failed to load the RAG system.")
    st.exception(e)
    st.stop()


# ============================================================
# HEADER
# ============================================================

st.title("LinkedInGenAI")

st.subheader(
    "RAG-Powered Multi-Agent LinkedIn Content Generator"
)

st.write(
    "Generate personalized LinkedIn posts using semantic retrieval, "
    "LLM generation, AI-based quality evaluation, and optional optimization."
)

st.divider()


# ============================================================
# USER INPUTS
# ============================================================

col1, col2 = st.columns(2)

with col1:

    topic = st.text_area(
        "Topic",
        placeholder="Example: My experience learning Python",
        height=120
    )

    tone = st.selectbox(
        "Tone",
        [
            "Professional",
            "Inspirational",
            "Humorous",
            "Casual",
            "Neutral"
        ]
    )

    audience = st.text_input(
        "Target Audience",
        value="Students and aspiring developers"
    )


with col2:

    language = st.selectbox(
        "Language",
        [
            "English",
            "Hindi",
            "Hinglish",
            "Spanish",
            "French"
        ]
    )

    length = st.selectbox(
        "Post Length",
        [
            "Short",
            "Medium",
            "Long"
        ]
    )


st.divider()


# ============================================================
# GENERATE BUTTON
# ============================================================

generate_button = st.button(
    "Generate LinkedIn Post",
    type="primary",
    use_container_width=True
)


# ============================================================
# GENERATION PIPELINE
# ============================================================

if generate_button:

    if not topic.strip():

        st.warning("Please enter a topic before generating.")

    else:

        # ----------------------------------------------------
        # Save user requirements
        # ----------------------------------------------------

        st.session_state["topic"] = topic
        st.session_state["tone"] = tone
        st.session_state["audience"] = audience
        st.session_state["language"] = language
        st.session_state["length"] = length

        # ----------------------------------------------------
        # Step 1: RAG Retrieval
        # ----------------------------------------------------

        with st.spinner("Finding relevant LinkedIn posts..."):

            query = f"""
            Topic: {topic}
            Tone: {tone}
            Audience: {audience}
            Language: {language}
            """

            try:

                retrieved_posts = retrieve_similar_posts(
                    query=query,
                    index=index,
                    data=data,
                    top_k=3
                )

                st.session_state["retrieved_posts"] = retrieved_posts

            except Exception as e:

                st.error("Failed during semantic retrieval.")
                st.exception(e)
                st.stop()

        # ----------------------------------------------------
        # Step 2: Generate Post
        # ----------------------------------------------------

        with st.spinner("Generating your LinkedIn post..."):

            try:

                generated_post = generate_post(
                    topic=topic,
                    tone=tone,
                    audience=audience,
                    language=language,
                    length=length,
                    retrieved_posts=retrieved_posts
                )

                st.session_state["generated_post"] = generated_post
                st.session_state["final_post"] = generated_post

            except Exception as e:

                if "429" in str(e) or "RateLimit" in str(e):

                    st.error(
                        "Gemini API rate limit reached. "
                        "Please wait before making another generation request."
                    )

                else:

                    st.error("Gemini generation failed.")
                    st.exception(e)

                st.stop()

        # ----------------------------------------------------
        # Step 3: Critic
        # ----------------------------------------------------

        with st.spinner("Evaluating generated content..."):

            try:

                evaluation = critic_agent(
                    post=generated_post,
                    topic=topic,
                    tone=tone,
                    audience=audience
                )

                st.session_state["evaluation"] = evaluation

            except Exception as e:

                if "429" in str(e) or "RateLimit" in str(e):

                    st.warning(
                        "The post was generated, but the Gemini quota "
                        "was reached before the quality evaluation."
                    )

                    st.session_state["evaluation"] = None

                else:

                    st.error("Critic evaluation failed.")
                    st.exception(e)

                    st.session_state["evaluation"] = None


# ============================================================
# DISPLAY GENERATED POST
# ============================================================

if "final_post" in st.session_state:

    st.divider()

    st.header("Generated LinkedIn Post")

    st.text_area(
        "Final Post",
        value=st.session_state["final_post"],
        height=400
    )


    # ========================================================
    # QUALITY EVALUATION
    # ========================================================

    evaluation = st.session_state.get("evaluation")

    if evaluation is not None:

        st.header("AI Quality Evaluation")

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "Overall",
                evaluation["overall_score"]
            )

        with col2:

            st.metric(
                "Relevance",
                evaluation["relevance"]
            )

        with col3:

            st.metric(
                "Originality",
                evaluation["originality"]
            )

        with col4:

            st.metric(
                "LinkedIn Suitability",
                evaluation["linkedin_suitability"]
            )

        st.write(
            "**Improvement feedback:**",
            evaluation["improvement_feedback"]
        )


        # ====================================================
        # OPTIONAL OPTIMIZATION
        # ====================================================

        st.divider()

        st.subheader("Improve the Post")

        st.write(
            "The optimizer uses the critic's feedback to rewrite the "
            "post. This makes one additional Gemini API request."
        )

        improve_button = st.button(
            "Improve Post",
            use_container_width=True
        )

        if improve_button:

            with st.spinner("Optimizing the post..."):

                try:

                    improved_post = optimizer_agent(
                        post=st.session_state["final_post"],
                        feedback=evaluation["improvement_feedback"],
                        topic=st.session_state["topic"],
                        tone=st.session_state["tone"],
                        audience=st.session_state["audience"],
                        language=st.session_state["language"],
                        length=st.session_state["length"]
                    )

                    st.session_state["final_post"] = improved_post

                    # ----------------------------------------
                    # Re-evaluate improved post
                    # ----------------------------------------

                    with st.spinner("Running final quality check..."):

                        final_evaluation = critic_agent(
                            post=improved_post,
                            topic=st.session_state["topic"],
                            tone=st.session_state["tone"],
                            audience=st.session_state["audience"]
                        )

                        st.session_state["evaluation"] = final_evaluation

                    st.success(
                        "Post improved successfully."
                    )

                    st.rerun()

                except Exception as e:

                    if "429" in str(e) or "RateLimit" in str(e):

                        st.error(
                            "Gemini API rate limit reached. "
                            "Please wait before trying again."
                        )

                    else:

                        st.error("Post optimization failed.")
                        st.exception(e)


    # ========================================================
    # RETRIEVED POSTS
    # ========================================================

    retrieved_posts = st.session_state.get(
        "retrieved_posts",
        []
    )

    if retrieved_posts:

        st.divider()

        with st.expander(
            "View Retrieved Reference Posts"
        ):

            st.write(
                "These are the semantically similar posts retrieved "
                "from the dataset and supplied to the generator as "
                "reference context."
            )

            for i, post in enumerate(
                retrieved_posts,
                start=1
            ):

                st.markdown(
                    f"### Reference {i}"
                )

                st.write(
                    post["text"]
                )

                st.caption(
                    f"Tone: {post['tone']} | "
                    f"Language: {post['language']} | "
                    f"Engagement: {post['engagement']} | "
                    f"Similarity: {post['similarity']:.3f}"
                )