# TXYZ API 工具集

这个Dify插件提供了与TXYZ API集成的工具，帮助用户通过AI应用进行智能搜索和学术研究。

## 功能

插件包含以下四个工具：

1. **智能搜索 (Smart Search)** - 使用TXYZ API进行智能网络搜索，返回相关结果。
   - 参数：查询语句(query)、最大结果数量(max_num_results)、超时时间(timeout)
   - API端点：https://api.txyz.ai/v1/search/smart

2. **学术搜索 (Scholar Search)** - 搜索学术论文和研究资料。
   - 参数：查询语句(query)、最大结果数量(max_num_results)、超时时间(timeout)
   - API端点：https://api.txyz.ai/v1/search/scholar

3. **网页搜索 (Web Search)** - 搜索网页上的一般性信息。
   - 参数：查询语句(query)、最大结果数量(max_num_results)、超时时间(timeout)
   - API端点：https://api.txyz.ai/v1/search/web

4. **搜索结果解释 (Explain Search Results)** - 提供对搜索结果的解释和总结。
   - 参数：搜索ID(search_id)、响应模式(response_mode)、语言(language)、超时时间(timeout)
   - API端点：https://api.txyz.ai/v1/search/explain
   - 支持多种语言和响应模式

## 公共参数

- **超时时间 (timeout)** - 所有工具都支持自定义请求超时时间，默认为120秒，可根据需要自行调整。

## 使用方法

1. 安装该插件到您的Dify工作区。
2. 配置TXYZ API密钥。
3. 在您的AI应用中启用这些工具。

## 凭证配置

- **API密钥** - 您的TXYZ API密钥，可从[TXYZ平台](https://platform.txyz.ai)获取。

## 开发者信息

- 作者: sakura4036
- 版本: 0.0.1
