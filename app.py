import streamlit as st
import tempfile

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="PulsePoint AI",
    layout="centered"
)

# ================= UI =================
st.title("PulsePoint AI 🚀")
st.subheader("Turn long videos into viral shorts using GenAI")

st.markdown("""
Problem: Valuable emotional moments are hidden inside long videos.  
Solution: PulsePoint AI automatically detects viral-worthy moments.
""")

# ================= UPLOAD =================
video_file = st.file_uploader(
    "Upload a long video (mp4 only)",
    type=["mp4"]
)

if video_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp:
        temp.write(video_file.read())
        video_path = temp.name

    st.success("✅ Video uploaded successfully")
    st.video(video_path)

    if st.button("Generate Viral Moment"):
        st.info("🤖 AI is analyzing emotional intensity...")

        # ===== MOCK AI OUTPUT (PROTOTYPE) =====
        peak_segment = {
            "start": 6,
            "end": 18,
            "reason": "High emotional emphasis and strong audience hook"
        }

        st.success("🔥 Viral-worthy moment detected!")

        st.markdown("### ⏱️ Detected Viral Timestamp")
        st.write(f"Start: {peak_segment['start']} sec")
        st.write(f"End: {peak_segment['end']} sec")

        st.markdown("### 🔥 AI-Generated Caption")
        st.write(
            "This moment is buried in the video — but it can change everything."
        )

        st.markdown("### 🤖 Why this moment?")
        st.write(
            peak_segment["reason"]
        )