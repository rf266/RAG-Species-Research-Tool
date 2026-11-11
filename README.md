# RAG Powered Species Conservation Research Tool 

This system aims to provide researchers with the ability to develop a preliminary understanding of species conservation techniques using a RAG pipeline backed by a corpus of 100+ research articles and agency/government department brochures on species research conservation. 

## Current Tech Stack (In Progress)

- LlamaCloud + LlamaIndex RAG pipeline (including Groq and HuggingFace local and API integrations)
- Vue.js frontend
- Pickle used for nodes/embeddings/document saving
- GPU utilisation on Colab and LightningAI during semantic chunking and embedding + Kaggle
- Pinecone vector DB integration
- Arxiv data extraction
- Model quantization through Transfomers


*AI tools were also used for debugging/ideation, pathway illustration, guidance, strategies etc. This was especially helpful as a knowledgeable assistant to help with a full-scale RAG project of this size, integral in filling gaps in technical understanding.*


## Data Sourcing 
Research papers were found from online, with regards to research on species extinction. Arxiv was used as a primary resource due to its ability to allow mass paper download, proving convenient in creating a knowledge base. Other platforms were attempted such as OpenAlex, CORE, PubMed and Europe PMC, however, it was not feasible to mass-download these papers at once, considering the large scale required. Arxiv mainly focuses on technical exploration, hence the nature of its downloaded papers are based on the technological aspect of species extinction research and prevention, which caused me to pivot the true nature of the RAG pipeline to allow researchers to look into technical strategies they may use. Additionally, individual papers/brochures/documents were researched into on the internet, with many of these added to the corpus. In total, around 150-160+ papers were downloaded. 

## Data Preprocessing
- The data was ingested using LlamaParse for further processing. 
- For the final version, Kaggle was used for its GPU. In previous iterations, Colab and LightningAI were also used. 

## Problem Faced 
- One problem faced was the RAG pipeline returning chunks, which, apon inspection, were taken from the documents' reference/bibliography page. Due to the titles of the works in the bibliography, the model understood these as to be part of answering the query, due to the cosine similarity between the query and the words in the references. This provided false context for answers, which were based on the model's interpretation and knowledge rather than solely what the corpus says. After research/AI, I found that rechunking the entire corpus was the best action, where the chunks would be classified as either reference/bibliography or paper_body. I also took this opportunity to employ hybrid embeddings, which would be useful as in a scientific context, both semantic meaning and specific keywords are essential in correctly formulating an answer. 




## Sources (non exhaustive)

Arxiv docs
OpenAlex/CORE/PubMed/Europe PMC etc docs
LLamaIndex framework/Llamaparse docs
OpenAI docs
Gemini API docs
HuggingFace models
OpenRouter docs
Requests docs
HuggingFace docs
Pinecone docs
Vue.js docs
Various pages on W3 schools and GeeksForGeeks - Vue and CSS

- Papers/documents from various online sources including government/research organisations


- https://www.llamaindex.ai/blog/pdf-parsing-llamaparse - Documentation parsing

- https://medium.com/kx-systems/rag-llamaparse-advanced-pdf-parsing-for-retrieval-c393ab29891b - Llamaindex parsing

- https://llamaindexxx.readthedocs.io/en/latest/api/llama_index.core.node_parser.SemanticSplitterNodeParser.html - Semantic Splitter

- https://github.com/orgs/community/discussions/118713 - Keras and TF dependency error


- https://www.youtube.com/watch?v=yzPQaNhuVGU - RAG and LLamaindex


- https://huggingface.co/docs/transformers/en/quantization/bitsandbytes - Model quantization


- https://developers.llamaindex.ai/python/framework-api-reference/llms/huggingface/ - HF 


- https://stackoverflow.com/questions/58608425/how-to-append-new-data-to-pickle-file-using-python - Pickle


- https://stackoverflow.com/questions/2104080/how-do-i-check-file-size-in-python - file sizes;


- https://www.youtube.com/watch?v=zwvUAh91itA - Vue 


- https://medium.com/@myscale/advanced-rag-optimization-smarter-queries-superior-insights-d020a66a8fac - Query optimization stratgies


- https://shweta-lodha.medium.com/using-pinecone-with-openai-and-llamaindex-a-complete-solution-c596d0963e3d - basic strategies


- https://medium.com/@visrow/rag-pipeline-best-practices-10-critical-engineering-decisions-for-production-systems-937a6f8d141c - RAG optimization strategies


- https://medium.com/hackernoon/front-end-refactored-components-with-vue-907a08a3630 - Vue components


- https://www.reddit.com/r/vuejs/comments/1eg27rm/how_to_change_background_color_for_the_whole/ - Vue styling


- https://stackoverflow.com/questions/69287834/search-bar-vue-js - Search bar in Vue


- https://www.geeksforgeeks.org/python/introduction-to-fastapi/ - Fastapi


- https://medium.com/@abheshith7/mastering-reranking-in-rag-from-basic-retrieval-to-advanced-methods-db297530361a  - Reranking


- https://medium.com/@visrow/rag-pipeline-best-practices-10-critical-engineering-decisions-for-production-systems-937a6f8d141c - RAG strategies


 - https://kajetan.io/articles/search-bar-vue -navigation Vue


 - https://www.youtube.com/watch?v=LW-cQN0_1R4&t=52s 


 - https://stackoverflow.com/questions/77444025/how-can-i-manage-vue-routes-inside-fastapi


-  https://www.youtube.com/watch?v=7UKOCrUjAY8


- https://www.youtube.com/watch?v=YLFOynY72sE