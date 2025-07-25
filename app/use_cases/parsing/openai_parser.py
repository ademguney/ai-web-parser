from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from config.settings import OPENAI_MODEL

llm = ChatOpenAI(model= OPENAI_MODEL)

template = (
    "Aşağıdaki metin parçasından şu bilgiyi çıkarman gerekiyor: {parse_instruction}\n\n"
    "Metin:\n{chunk}\n\n"
    "Sadece doğrudan eşleşen bilgileri çıkar. Ek açıklama yapma. "
    "Eğer bilgi yoksa boş string ('') döndür."
)

def parse_with_openai(chunks: list[str], parse_instruction: str) -> str:
    """
    Parses DOM chunks using OpenAI GPT model based on user instruction.
    """
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | llm

    results = []

    for i, chunk in enumerate(chunks, 1):
        print(f"[OpenAIParser] Parsing chunk {i} of {len(chunks)}")
        response = chain.invoke({
            "chunk": chunk,
            "parse_instruction": parse_instruction
        })
        results.append(response.content.strip())

    return "\n".join(results)
    