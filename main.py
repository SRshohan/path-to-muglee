import os
import sys
import constants
import openai

from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import TextLoader
from langchain.vectorstores import Chroma
from langchain.indexes.vectorstore import VectorStoreIndexWrapper, VectorstoreIndexCreator
from langchain.chains import ConversationalRetrievalChain, RetrievalQA, ConversationChain




os.environ["OPENAI_API_KEY"] = constants.APIKEY

PERSIST = False

query = None

if len(sys.argv) > 1:
    query = sys.argv[1]

if PERSIST and os.path.exists("persist"):
    print("Reusing index...\n")
    vectorstore = Chroma(persist_directory="persist")
    index = VectorStoreIndexWrapper(vectorstore=vectorstore)
else:
    loader =TextLoader('demo.txt')
    inde = VectorstoreIndexCreator().from_loaders([loader])

chain = ConversationalRetrievalChain.from_llm(
    llm=ChatOpenAI(model="gpt-3.5-turbo"),
    retriever=inde.vectorstore.as_retriever(search_kwargs={"k": 1}),

)




chat_history = []
while True:
    if not query:
        query = input("Prompt: ")
    if query in ['quit', 'q', 'exit']:
        sys.exit()
    result = chain({
        'question': query,
        'chat_history': chat_history
    })
    print(result['answer'])
    chat_history.append((query, result['answer']))
    query = None
