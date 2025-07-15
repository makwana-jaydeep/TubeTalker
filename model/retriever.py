from youtube_transcript_api import YouTubeTranscriptApi
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings  
from utils.helpers import extract_video_id


def load_vector_store_from_youtube_url(url):
    video_id = extract_video_id(url)

    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        transcript = " ".join(chunk['text'] for chunk in transcript_list)
    except Exception as e:
        raise ValueError(f"No captions available: {e}")

    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.create_documents([transcript])

    # Use updated embedding class
    embedding = HuggingFaceEmbeddings(
        model_name="./embedding_model/bge-base-en-v1.5",
        encode_kwargs={"normalize_embeddings": True}
    )

    # Create FAISS vector store
    vector_store = FAISS.from_documents(chunks, embedding)
    retriever = vector_store.as_retriever()
    return retriever


if __name__ == '__main__':
    print(load_vector_store_from_youtube_url('https://www.youtube.com/watch?v=HZGCoVF3YvM'))
