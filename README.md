# TubeTalker: Chat with YouTube Videos using RAG and Mistral

This application allows users to interact with any YouTube video by asking natural language questions. It uses Retrieval-Augmented Generation (RAG) to extract and embed transcripts, retrieve relevant information, and generate answers using a large language model (LLM).

The system leverages the `mistralai/Mistral-7B-Instruct-v0.2` model for question-answering and `bge-base-en-v1.5` for embedding. It is built with LangChain and deployed using Gradio for a simple web interface.

## Features

- Automatically extracts transcripts from YouTube videos
- Embeds transcripts using the `bge-base-en-v1.5` model
- Stores and retrieves context using FAISS vector store
- Generates answers using `Mistral-7B-Instruct` via LangChain
- Interactive UI powered by Gradio

## Project Structure

```
TubeTalker/
├── app.py                  # Gradio UI and orchestration logic
├── embeddings/             # Embedding model setup and functions (excluded via .gitignore)
├── model/                  # Chain, retriever, and LLM construction
├── utils/                  # Utility functions (e.g., extract YouTube video ID)
├── assets/                 # Screenshots or visual assets
├── requirements.txt        # Python package dependencies
├── LICENSE                 # MIT License
├── .gitignore              # Files and directories to exclude from version control
└── README.md               # Project overview and setup guide
```


## Getting Started

### Prerequisites

- Python 3.8 or higher
- Hugging Face API token (for access to Mistral-7B)

### Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/makwana-jaydeep/TubeTalker.git
cd TubeTalker
pip install -r requirements.txt
```

### Running the Application

To start the Gradio interface, run:

```python app.py```

Then open your browser and navigate to:

http://localhost:7860

## How It Works

1. The user provides a YouTube video URL.
2. The application extracts the transcript using `youtube-transcript-api`.
3. The transcript is embedded using the `bge-base-en-v1.5` model.
4. Embeddings are stored in a FAISS vector database.
5. LangChain retrieves relevant transcript chunks based on the user's query.
6. The `Mistral-7B-Instruct` model generates a response using the retrieved context.

## Models Used

- **Embedding Model**: [BAAI/bge-base-en-v1.5](https://huggingface.co/BAAI/bge-base-en-v1.5)
- **Language Model**: [mistralai/Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2)


## Screenshots

Screenshots and user interface images can be stored in the `assets/` directory.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

## Acknowledgements

This application is built using open-source tools including:

- [LangChain](https://www.langchain.com/)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
- [Gradio](https://www.gradio.app/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Mistral AI](https://huggingface.co/mistralai)
