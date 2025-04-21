from typing import Any
import requests
from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError


class TxyzProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        # 验证API密钥是否有效
        try:
            api_key = credentials.get("api_key")
            
            # 检查API密钥是否存在
            if not api_key:
                raise ToolProviderCredentialValidationError("API密钥不能为空")
            
            # 使用Smart Search工具尝试一个简单查询来验证API密钥
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            
            # 使用TXYZ API验证密钥
            response = requests.post(
                url="https://api.txyz.ai/v1/search/web",
                json={"query": "test", "max_num_results": 1},
                headers=headers,
                timeout=10
            )
            print(response.status_code, response.text)  # Debugging line to check the response status and text
            
            # 检查响应状态
            if response.status_code == 401:
                raise ToolProviderCredentialValidationError("无效的API密钥")
            elif response.status_code != 200:
                raise ToolProviderCredentialValidationError(f"API验证失败: HTTP {response.status_code}")
            
            # 尝试解析响应以确保返回有效数据
            response.json()
            
        except requests.exceptions.RequestException as e:
            # 处理请求错误
            raise ToolProviderCredentialValidationError(f"无法连接到TXYZ API: {str(e)}")
        except ValueError as e:
            # 处理JSON解析错误
            raise ToolProviderCredentialValidationError(f"API返回了无效的响应: {str(e)}")
        except Exception as e:
            # 处理其他所有错误
            raise ToolProviderCredentialValidationError(f"验证过程中出现错误: {str(e)}")
