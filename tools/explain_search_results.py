from collections.abc import Generator
from typing import Any

import requests

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage


class ExplainSearchResultsTool(Tool):
    """
    Explain Search Results tool for TXYZ API
    """

    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        # Get API credentials from runtime
        api_key = self.runtime.credentials.get("api_key")

        # Set API endpoint
        api_url = "https://api.txyz.ai/v1/search/explain"

        # Prepare headers
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        # Prepare params from parameters
        params = {
            "search_id": tool_parameters.get("search_id", ""),
            "response_mode": tool_parameters.get("response_mode", "COMPLETE"),
            "language": tool_parameters.get("language", "en")
        }

        # Get timeout parameter
        timeout = tool_parameters.get("timeout", 120)

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        try:
            # Make the API request
            response = requests.post(
                url=api_url,
                params=params,
                headers=headers,
                timeout=timeout  # Use the configured timeout
            )
            response.raise_for_status()

            # Parse and return the response
            result = response.json()
            yield self.create_json_message(result)

        except requests.exceptions.RequestException as e:
            # Handle request errors
            error_message = f"Error making request to TXYZ Explain API: {str(e)}"
            yield self.create_text_message(error_message)
