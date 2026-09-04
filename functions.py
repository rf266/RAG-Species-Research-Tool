from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core import get_response_synthesizer
from llama_index.core import Settings
from llama_index.llms.groq import Groq
from dotenv import load_dotenv
import os 
from pinecone.grpc import PineconeGRPC
from llama_index.vector_stores.pinecone import PineconeVectorStore
load_dotenv()
from llama_index.embeddings.huggingface_api import HuggingFaceInferenceAPIEmbedding
import nest_asyncio
nest_asyncio.apply()
from llama_index.core import VectorStoreIndex

def pipeline():
    api = os.getenv("PINECONE_API_KEY")
    pine = PineconeGRPC(api_key=api)
    index = pine.Index("embeddings")
    vectorstore = PineconeVectorStore(pinecone_index=index)
    api = os.getenv("GROQ_API_KEY")
    llm = Groq(model="openai/gpt-oss-120b", api=api)   
    Settings.llm = llm 
    embed_model = HuggingFaceInferenceAPIEmbedding(
    model_name="BAAI/bge-m3",
    token=os.getenv("HF_API_KEY"))
    Settings.embed_model=embed_model
    vectorindex = VectorStoreIndex.from_vector_store(vector_store=vectorstore, llm=llm)
    retriver = VectorIndexRetriever(index=vectorindex,verbose=True, top_k=20)
    synth = get_response_synthesizer()
    from llama_index.core.postprocessor import SentenceTransformerRerank

    rerank = SentenceTransformerRerank(model="cross-encoder/ms-marco-MiniLM-L4-v2", top_n=7)

    query = input("Enter your query: ")

    prompt_instructions = f'You are a part of a conservation research RAG assistant - improve the prompt for the LLM to yield better results. The user has entered the prompt below:\n {query} \n The prompt could have limitations such as being too specific where the corpus may not have information on the exact species or too generalised for a corpus detailing technical insights into species conservation. It may also not provide constraints and rules to the LLM \n Your job is to enhance the query so that RAG retrieval returns interesting points of discussion. Ensure you mention that all information must be backed by citations sourced only from the actual RAG vector database, tell it to recognise levels of uncertainty of information due to the corpus and a breakdown of information reasoning which does not go beyond species conservation. \n in Ensure the new prompt is between 50-60 words max. \nOnly return the prompt text.'

    new_prompt = llm.complete(prompt_instructions).text
    print(new_prompt)

    query_engine = RetrieverQueryEngine(retriever=retriver, response_synthesizer=synth, node_postprocessors=[rerank])
    response = query_engine.query(new_prompt)
    nodes = response.source_nodes

    print([node.score for node in nodes])
    print([node.text for node in nodes])
    print(response)
    return response


pipeline()

