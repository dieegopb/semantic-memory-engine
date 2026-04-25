from app.services.search_service import SearchService

def search_node(state):
    service = SearchService()

    results = service.search(state["question"])

    return {
        **state,
        "web_results": results
    }