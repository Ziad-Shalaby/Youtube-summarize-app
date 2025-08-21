# YouTube Video Summarizer

This is a web application that provides a concise summary of any YouTube video using the power of a large language model. Simply paste the video URL, and the app will generate a summary for you.

## About

The **YouTube Video Summarizer** is a web application built with Python and Streamlit designed to save you time by extracting the core information from long-form video content. It fetches the video transcript, processes it with a generative language model, and returns a clear, easy-to-read summary. It's an excellent tool for students, researchers, or anyone who wants to quickly grasp a video's key points without watching the entire thing.

## Features

-   **Paste & Go:** A simple and intuitive interface to input any YouTube URL.
-   **AI-Powered Summaries:** Utilizes the Gemini API to generate intelligent and accurate summaries.
-   **Real-time Processing:** Provides a summary quickly after processing the video's content.

## Technologies Used

-   **Frontend & Backend:**
    -   Streamlit: A Python library for building data-driven web applications.
    -   Python: The core programming language.
-   **API Integration:**
    -   Bart: The core large language model for generating the summaries.
    -   `youtube-transcript-api`: A Python library to fetch video transcripts.

## Getting Started

Follow these steps to get a local copy of the project up and running on your machine.

### Prerequisites

You must have **Python** and **pip** installed on your system.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Ziad-Shalaby/Youtube-summarize-app.git](https://github.com/Ziad-Shalaby/Youtube-summarize-app.git)
    cd Youtube-summarize-app
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### API Key Configuration

To use the Gemini API, you need to set up your API key.

1.  Create a new file in the root of the project named `.env`.
2.  Add your API key to this file in the following format:
    ```
    GEMINI_API_KEY=YOUR_API_KEY_HERE
    ```
    *Replace `YOUR_API_KEY_HERE` with your actual API key.*

### Running the App

Once you have installed the dependencies and configured your API key, you can run the app with this command:
```bash
streamlit run app.py
```

This will start the development server, and the app will be accessible at `http://localhost:8501`.

## Live Application

You can view and use the live deployed version of the application here:
[https://youtube-summarize-app-1.streamlit.app/](https://youtube-summarize-app-1.streamlit.app/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
