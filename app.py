import streamlit as st
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline

@st.cache_resource
def get_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")

def extract_video_id(url: str) -> str:
    parsed = urlparse(url)
    qs = parse_qs(parsed.query)
    video_ids = qs.get('v')
    if not video_ids:
        raise ValueError(f"No video id found in URL: {url}")
    return video_ids[0]

def fetch_transcript(video_id: str) -> str:
    ai = YouTubeTranscriptApi()
    fetched = ai.fetch(video_id, languages=['en'])
    return "\n".join(snippet.text for snippet in fetched)

def chunk_text(text, max_chunk_length=1000):
    return [text[i:i + max_chunk_length] for i in range(0, len(text), max_chunk_length)]

def summarize_chunks(chunks, summarizer):
    summaries = []
    for chunk in chunks:
        summary = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
        summaries.append(summary[0]['summary_text'])
    return " ".join(summaries)

st.title("YouTube Video Summarizer")

url = st.text_input("Enter YouTube video URL:")

if st.button("Summarize"):
    if url:
        try:
            video_id = extract_video_id(url)
            st.write(f"Video ID: {video_id}")
            with st.spinner("Fetching transcript..."):
                transcript = fetch_transcript(video_id)
            chunks = chunk_text(transcript)
            st.write(f"Transcript split into {len(chunks)} chunk(s).")
            summarizer = get_summarizer()
            with st.spinner("Summarizing..."):
                summary = summarize_chunks(chunks, summarizer)
            st.subheader("Summary")
            st.write(summary)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a YouTube video URL.")