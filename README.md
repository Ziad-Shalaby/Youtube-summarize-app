# YouTube Video Summarizer

This is a web application that provides a concise summary of any YouTube video. Simply paste the video URL, and the app will generate a summary for you.

## About

The **YouTube Video Summarizer** is a web application built with Python and Streamlit. It's designed to save you time by extracting the core information from long-form video content. It fetches the video transcript, processes it using the Bart language model from the `transformers` library, and returns a clear, easy-to-read summary. It's an excellent tool for students, researchers, or anyone who wants to quickly grasp a video's key points without watching the entire thing.

## Features

-   **Paste & Go:** A simple and intuitive interface to input any YouTube URL.
-   **AI-Powered Summaries:** Utilizes the Bart model to generate intelligent and accurate summaries.
-   **Real-time Processing:** Provides a summary quickly after processing the video's content.

## Technologies Used

-   **Frontend & Backend:**
    -   Streamlit: A Python library for building data-driven web applications.
    -   Python: The core programming language.
-   **API Integration:**
    -   `transformers`: A popular library for using pre-trained models like Bart.
    -   `youtube-transcript-api`: A Python library to fetch video transcripts.

## Getting Started

Follow these steps to get a local copy of the project up and running on your machine.

### Prerequisites

You must have **Python** and **pip** installed on your system.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [repository-url]
    cd [repository-name]
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *Note: The `requirements.txt` file should contain `streamlit`, `youtube-transcript-api`, and `transformers`.*

### Running the App

Once you have installed the dependencies, you can run the app with this command:
```bash
streamlit run app.py
```

This will start the development server, and the app will be accessible in your web browser, usually at `http://localhost:8501`.

## Live Application

You can view and use the live deployed version of the application here:
[https://youtube-summarize-app-1.streamlit.app/](https://youtube-summarize-app-1.streamlit.app/)

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.
