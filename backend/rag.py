from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from vectorstore import load_vectorstore
from llm import get_llm


def get_retriever():

    vectorstore = load_vectorstore()

    return vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 4})


def format_documents(docs):

    return "\n\n".join(doc.page_content for doc in docs)


def ask(query: str):

    retriever = get_retriever()

    parser = StrOutputParser()

    model = get_llm()

    # transcript content chain
    content_chain = retriever | format_documents

    # return query unchanged
    query_chain = RunnablePassthrough()

    # parallel chain 
    parallel_chain = RunnableParallel({
        "content": content_chain,
        "query": query_chain
    })

    prompt = PromptTemplate(
        template="""
You are a helpful assistant answering question from a Youtube transcript.

Use only the provided transcript content.

If the answer is not available in the content, say you do not know.

Transcript content: {content}

User Question: {query}

Answer:

"""
    )

    final_chain = parallel_chain | prompt | model | parser

    return final_chain.invoke(query)
