import gradio as gr
from .RomanDictionary.Seacher import Searcher

searcher = Searcher()

app = gr.Interface(
    fn=searcher.search,
    inputs=["text", gr.Radio(["Eng", "Romanized", "Th"])],
    outputs="text"
)