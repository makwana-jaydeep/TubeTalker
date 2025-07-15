import gradio as gr
from model.retriever import load_vector_store_from_youtube_url
from model.chain import build_chain
import time

# Global variable to store chain
chain = None

def process_video(video_url):
    global chain
    if not video_url:
        return "Please enter a YouTube video URL.", gr.update(visible=False)
    start_time = time.time()
    retriever = load_vector_store_from_youtube_url(video_url)
    chain = build_chain(retriever)
    elapsed_time = time.time() - start_time
    return f"✅ Video processed in {elapsed_time:.2f} seconds. You can now ask questions.", gr.update(visible=True)

def ask_question(query):
    global chain
    if not chain:
        return "Please process a video first."
    start_time = time.time()
    response = chain.invoke(query)
    elapsed_time = time.time() - start_time
    return f"💬 Answer (generated in {elapsed_time:.2f} seconds):\n\n{response}"

# Gradio Interface
with gr.Blocks(title="Chat with YouTube Video") as demo:
    gr.Markdown("# 🎥 Chat with YouTube Video")
    
    with gr.Row():
        video_url = gr.Textbox(label="Enter YouTube Video URL")
        process_button = gr.Button("Load Video")
    
    status = gr.Markdown()
    question_input = gr.Textbox(label="Ask a question based on the video")
    ask_button = gr.Button("Ask")
    answer_output = gr.Markdown()
    
    # Hide question UI until video is processed
    question_input.visible = False
    ask_button.visible = False

    process_button.click(fn=process_video, inputs=video_url, outputs=[status, question_input])
    process_button.click(fn=process_video, inputs=video_url, outputs=[status, ask_button])
    ask_button.click(fn=ask_question, inputs=question_input, outputs=answer_output)

# Launch app
if __name__ == "__main__":
    demo.launch()
