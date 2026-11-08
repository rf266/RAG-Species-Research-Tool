from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core import get_response_synthesizer
from llama_index.core import Settings
from llama_index.llms.groq import Groq
from dotenv import load_dotenv
import os 
from llama_index.sparse_embeddings.fastembed import FastEmbedSparseEmbedding

from pinecone.grpc import PineconeGRPC
from llama_index.vector_stores.pinecone import PineconeVectorStore
load_dotenv()
from llama_index.embeddings.huggingface_api import HuggingFaceInferenceAPIEmbedding
import nest_asyncio
nest_asyncio.apply()
from llama_index.core import VectorStoreIndex
from llama_index.core.postprocessor import SentenceTransformerRerank
from llama_index.core.vector_stores import MetadataFilters, ExactMatchFilter
from llama_index.embeddings.cloudflare_workersai import CloudflareEmbedding
def pipeline():
    api = os.getenv("PINECONE_API_KEY")
    pine = PineconeGRPC(api_key=api)
    sparse_model = FastEmbedSparseEmbedding(model_name="prithivida/Splade_PP_en_v1")

    index = pine.Index("embeddings2")
    vectorstore = PineconeVectorStore(pinecone_index=index,add_sparse_vector=True,sparse_embedding_model=sparse_model)


    api = os.getenv("GROQ_API_KEY")
    llm = Groq(model="openai/gpt-oss-120b", api=api)   
    Settings.llm = llm 

    filter = MetadataFilters( filters=[ExactMatchFilter(key="classification", value="paper_body")])
 

    embed_model = CloudflareEmbedding(
        account_id = os.getenv("CF_ACCOUNT_ID"), 
        auth_token = os.getenv("CF_API_KEY"),
        model="@cf/baai/bge-m3",
    )

    Settings.embed_model=embed_model
    vectorindex = VectorStoreIndex.from_vector_store(vector_store=vectorstore, llm=llm)


    filter = MetadataFilters(filters=[ExactMatchFilter(key="classification", value="paper_body")])

    retriver = VectorIndexRetriever( index=vectorindex,verbose=True,similarity_top_k=20,vector_store_query_mode="hybrid",filters=filter)
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

