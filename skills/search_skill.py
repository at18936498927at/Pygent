from base_skill import BaseSkill

from duckduckgo_search import DDGS


class SearchSkill(BaseSkill):
    name = "search"
    description = "A tool that uses to search for information."

    def run(self, query: str, max_results: int = 10) -> str:  # type: ignore
        """
        A Tool that uses DuckDuckGo to search for information.

        Args:
            query: The search query string.
            max_results: The maximum number of search results to return (default is 10). 
        
        Returns:
            A string containing the search results or a message indicating no results were found.
        """
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=max_results)
            if results:
                return "\n".join([f"{result['title']}: {result['href']}" for result in results])
            else:
                return "No results found."
        return f"Search results for: {query}"
