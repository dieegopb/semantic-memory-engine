from app.services.qa_service import QAService

def main():
    service = QAService()

    user_id = "123"

    print("\n🧠 Semantic Memory Engine (CLI)")
    print("Digite sua pergunta (ou 'exit' para sair)\n")

    while True:
        question = input("Você: ")

        if question.lower() in ["exit", "quit", "sair"]:
            print("👋 Encerrando...")
            break

        result = service.ask(user_id, question)

        print("\n🤖 Resposta:")
        print(result["answer"])
        print("-" * 50)

if __name__ == "__main__":
    main()