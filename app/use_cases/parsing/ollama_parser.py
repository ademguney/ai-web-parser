from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from config.settings import OLLAMA_MODEL


template = (
    "Aşağıdaki metin parçasından şu bilgiyi çıkarman gerekiyor: {parse_instruction}\n\n"
    "Metin:\n{chunk}\n\n"
    "Sadece doğrudan eşleşen bilgileri çıkar. Ek açıklama yapma. "
    "Eğer bilgi yoksa boş string ('') döndür."
)


model = OllamaLLM(model = OLLAMA_MODEL)


def parse_with_ollama(chunks: list[str], parse_instruction: str) -> str:
    """
    Cleans and parses each DOM chunk using the local Ollama LLM based on the given instruction.
    """
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    results = []

    for i, chunk in enumerate(chunks, 1):
        print(f"[OllamaParser] Parsing chunk {i} of {len(chunks)}")
        response = chain.invoke({
            "chunk": chunk,
            "parse_instruction": parse_instruction
        })
        results.append(response.strip())

    return "\n".join(results)