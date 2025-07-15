from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableLambda, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from model.llm import llm


def build_chain(retriever):
    prompt = PromptTemplate(
        template="""
        You are a helpful assistant.
        Answer only from the provided transcript context.
        If the context is insufficient, just say you don't know.
        
        Context:
        {context}
        
        Question: {question}
        """,
        input_variables=["context", "question"]
    )

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    parallel_chain = RunnableParallel({
        "context": retriever | RunnableLambda(format_docs),
        "question": RunnablePassthrough()
    })

    generate_prompt = RunnableLambda(lambda input: prompt.invoke(input))
    get_text = RunnableLambda(lambda prompt_value: prompt_value.text)
    parser = StrOutputParser()

    chain = parallel_chain | generate_prompt | get_text | llm | parser
    return chain


if __name__ == '__main__':
    print("chain working..")