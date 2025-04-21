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

        # Prepare payload from parameters
        payload = {
            "search_id": tool_parameters.get("search_id", ""),
            "response_mode": tool_parameters.get("response_mode", "COMPLETE"),
            "language": tool_parameters.get("language", "en")
        }

        # Remove None values
        payload = {k: v for k, v in payload.items() if v is not None}

        try:
            # Make the API request
            response = requests.post(
                url=api_url,
                json=payload,
                headers=headers,
                timeout=60  # Longer timeout as explanation might take more time
            )
            response.raise_for_status()

            # Parse and return the response
            result = response.json()
            yield self.create_json_message(result)

        except requests.exceptions.RequestException as e:
            # Handle request errors
            error_message = f"Error making request to TXYZ Explain API: {str(e)}"
            yield self.create_text_message(error_message)
