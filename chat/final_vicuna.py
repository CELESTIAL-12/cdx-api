import logging
#import click
import torch
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.llms import HuggingFacePipeline

# from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.vectorstores import Chroma
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    GenerationConfig,
    pipeline,
)


# Default Instructor Model
def embeddings(search_type, search_kwargs):
    EMBEDDING_MODEL_NAME = "hkunlp/instructor-large"
    embeddings = HuggingFaceInstructEmbeddings(model_name=EMBEDDING_MODEL_NAME, model_kwargs={"device": 'cuda'})

    db = Chroma(
            persist_directory='DB/',
            embedding_function=embeddings,
        )
    retriever = db.as_retriever(search_type, search_kwargs)
    return retriever

def load_model():
    tokenizer = AutoTokenizer.from_pretrained("saved_tokenizer/", use_fast=True)
    
    model = AutoModelForCausalLM.from_pretrained(
        "saved_model/",
        device_map="auto",
        torch_dtype=torch.float16,
        low_cpu_mem_usage=True,
        trust_remote_code=True,
        #max_memory={0: "15GB"},
        ).half()
    model.tie_weights()
    
    generation_config = GenerationConfig.from_pretrained("TheBloke/vicuna-7B-1.1-HF")
    
    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        torch_dtype=torch.float16,
        max_length=2048,
        temperature=0.2,
        top_p=0.95,
        repetition_penalty=1.15,
        #device=0,
        generation_config=generation_config,
    )

    local_llm = HuggingFacePipeline(pipeline=pipe)
    
    return local_llm


def generate_text():
     
    llm = load_model()

    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=embeddings('similarity',{"k": 3}))

    while True:
            query = input("\nEnter a query: ")
            if query == "exit":
                break
            # Get the answer from the chain
            res = qa(query)
            answer, docs = res["result"], res["source_documents"]

            # Print the result
            print("\n\n> Question:")
            print(query)
            print("\n> Answer:")
            print(answer)
            return(answer)
