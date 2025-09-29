[](https://www.zhihu.com)
  * [首页](https://www.zhihu.com/)
  * [焕新](https://www.zhihu.com/zhida)
  * [知乎知学堂](https://www.zhihu.com/education/learning)
  * [等你来答](https://www.zhihu.com/question/waiting)


​
切换模式
登录/注册
# 告别手动：N8N + Crawl4ai + MCP 自动化网页数据抓取与 RAG 知识库构建实战（本地部署教程）
[![AI解码师](https://pica.zhimg.com/v2-fdac6de0add53a6c59762650c399ff7e_l.jpg?source=172ae18b)](https://www.zhihu.com/people/ferrarizrw)
[AI解码师](https://www.zhihu.com/people/ferrarizrw)[​![](https://pic1.zhimg.com/v2-2ddc5cc683982648f6f123616fb4ec09_l.png?source=32738c0c)](https://www.zhihu.com/question/48510028)
互联网行业 技术专家
[收录于 · AI技术赋能地图：行业应用指南](https://www.zhihu.com/column/c_1895939310890497087)
在人工智能的众多应用领域中，**检索增强生成（Retrieval-Augmented Generation, RAG）** 是一项非常重要的技术。简单来说，RAG 是一种巧妙地将信息检索与文本生成相结合的 AI 解决方案。它的核心工作流程是这样的：当我们向 AI 提出问题时，RAG 系统会首先在预先构建的知识库中快速检索出与我们问题相关的资料。然后，它会将这些检索到的信息作为额外的上下文，连同我们的原始问题一起，发送给强大的语言模型（Large Language Model, LLM）。最终，大模型会综合我们提出的问题以及检索到的相关知识，生成更准确、更具时效性的答案。这与普通的大模型相比，由于参考了外部的知识库，其回答的质量往往会更高。
而在 RAG 流程中，一个至关重要的环节便是知识库中所使用的数据。那么，今天这篇文章，我就来和大家分享一下如何利用强大的自动化工作流平台 **N8N** ，以及专为 AI 应用设计的开源爬虫工具 **crawl4ai** ，搭建一个自动化数据抓取的工作流，从而轻松地从网站上获取所需的数据。更进一步，我们还将介绍如何利用抓取到的数据构建一个属于我们自己的知识库，最终实现一套完整的 RAG 解决方案。
![](https://pic3.zhimg.com/v2-a7c2f7e31bce6d01ea3708254a792b64_1440w.jpg)
**一、自动化数据抓取工作流概览**
先给大家展示一下我们最终搭建完成的数据抓取工作流。它的操作非常简单，你只需要输入一个想要抓取的网站网址，工作流就能自动地完成以下任务：
  * 抓取该网站的所有网页。
  * 将抓取到的网页内容转换为 Markdown 文件。
  * 将这些 Markdown 文件保存到你的电脑本地。


有了这些 Markdown 文件，我们就可以轻松地将它们加载到知识库中，从而使用 RAG 技术进行高效的问题查询。
![](https://picx.zhimg.com/v2-faed3d9c5b44bbf51e1eaa56daa2f1f5_1440w.jpg)
**二、N8N 工作流的本地部署**
好了，接下来我们就一步步地来搭建这个 N8N 工作流。
首先，我们需要部署 N8N 服务。打开 N8N 的 官方页面，你会发现它为个人用户提供了 14 天的在线免费试用。不过，为了更灵活地使用，我们这里选择本地部署的方式。打开git地址，向下滚动页面，在 "Quick Start" 部分，N8N 提供了两种本地部署方法：
**1. 使用 Node.js 部署**
如果你选择这种方式，需要先安装 Node.js。访问 Node.js 的官方网站，下载并安装适合你操作系统的版本。安装完成后，打开命令行窗口（终端），分别执行以下两条命令来检查 Node.js 和 npm 是否安装成功：
```
node -v
npm -v
```

如果能够输出对应的版本号，就说明 Node.js 已经成功安装了。
接下来，复制 N8N GitHub 页面上提供的 Node.js 部署命令，粘贴到命令行窗口中并执行：
```
npx n8n
```

等待命令执行成功后，命令行会输出 N8N 的本地网址。按下键盘上的 "O" 键，它会自动在你的浏览器中打开 N8N 的 Web 界面。至此，基于 Node.js 部署的 N8N 服务就搭建完成了。
![](https://pic2.zhimg.com/v2-71f35ae61570f13c7971f1499f3d73a7_1440w.jpg)
**2. 使用 Docker 部署**
除了 Node.js，我们还可以使用 Docker 来部署 N8N。如果你还没有安装 Docker，可以在 Docker 的官方网站下载并安装。安装完成后，记得将 Docker 的镜像源配置为国内的镜像源，以加快镜像下载速度。
复制 N8N GitHub 页面上提供的第一个 Docker 命令并执行，这条命令会创建一个名为 `n8n_data` 的 Docker 数据卷。它的作用是用来存储和持久化 N8N 容器的数据。这样，即使 Docker 容器重启或者被删除，数据也不会丢失。而且这个操作是幂等的，重复执行也不会有问题。然后，执行第二条命令来运行 N8N 容器：
```
docker volume create n8n_data
docker run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```

这个命令中用到了一些参数，我们稍后会详细介绍这些参数的作用。
服务启动成功后，打开浏览器，访问 `http://localhost:5678`（或者你 Docker 配置的端口），就可以开始使用 N8N 了。
![](https://pic3.zhimg.com/v2-739bf21ada69431da739203aedccfc7a_1440w.jpg)
**三、Crawl4AI 服务的本地部署**
接下来，我们再来部署 crawl4ai 服务。**crawl4ai** 是一款专门为大模型和 AI 应用设计的开源爬虫工具。它能够自动抓取网页，并提取结构化的数据，比如 JSON、Markdown 等。我们的工作流将使用它来抓取网站数据。
我们同样使用 Docker 的方式来部署 crawl4ai。打开你的 Docker 软件，在左侧点击 "Docker Hub"，然后在搜索框中输入 "crawl4ai"。选择第一个搜索结果，然后点击 "Tags" 选项卡。在这里，你会看到提供了很多不同版本的镜像。你可以根据自己电脑的芯片架构（AMD 或 ARM）选择合适的镜像。
![](https://pic1.zhimg.com/v2-b65057590deb6daff8f81a18a0eef4ba_1440w.jpg)
例如，如果你的电脑是 AMD64 架构的，可以选择带有 `-amd64` 标签的镜像。回到命令行，执行以下命令来拉取镜像（请根据你的芯片架构替换冒号后面的标签）：
![](https://pic1.zhimg.com/v2-32ad9d4bb4d2afc83a0b49e4906c976e_1440w.jpg)![](https://pic1.zhimg.com/v2-59f041ebf10b9dc46139e21cfef9bec8_1440w.jpg)
如果你的芯片是 ARM 架构的，可以将命令中的 `amd64` 替换为 `arm64`。你也可以直接在 Docker 软件中搜索并拉取镜像。
镜像拉取完成后，你会在 Docker 镜像列表中看到两个镜像：一个是 N8N 的，另一个是 crawl4ai 的。
![](https://pic1.zhimg.com/v2-99378dc2bd456e512c32cca33bb0240c_1440w.jpg)
现在，我们来启动 crawl4ai 容器，执行以下命令：
![](https://pic3.zhimg.com/v2-fc42950965e39e5c3e6a4cdcbfbf6e7e_1440w.jpg)
启动成功后。点击打开它的地址，如果看到的是 crawl4ai 的操作文档，就说明服务已经成功启动了。
**四、获取网站的 Sitemap 和 Robots.txt**
要使用 crawl4ai 来抓取一个网站的所有网页，我们通常需要先获取该网站的 **Sitemap** 文件（通常命名为 `sitemap.xml`）。Sitemap 文件列出了网站的所有网页链接，方便爬虫进行抓取。
例如，以crawl4ai 的操作文档网站为例，可以在其网址后面添加 `/sitemap.xml` 来访问它的 Sitemap 文件。你会看到一个包含许多 `<`url`>` 标签的 XML 文件，每个标签都对应着网站的一个网页链接。
对于大多数现代网站来说，它们都会配置自己的 Sitemap 文件，你可以直接使用。但是，仍然有一些网站可能没有配置 Sitemap，打开其根目录下的 `sitemap.xml`，你会发现并没有对应的内容。
对于这种情况，我们可以使用在线工具来生成 Sitemap。只需将网站的网址输入到工具中，然后点击开始执行，工具就会自动抓取网站并生成 Sitemap 文件。完成后，你可以点击查看按钮，获取生成的 Sitemap 文件内容，并直接使用它。
![](https://pica.zhimg.com/v2-a3f5eb808cedde4581605e41c10c6b74_1440w.jpg)
另外，在抓取数据的时候，我们还需要参考网站的 **robots.txt** 文件。这个文件告诉爬虫哪些内容是允许抓取的，哪些是被禁止的。你只需要在网站网址后面加上 `/robots.txt` 就可以打开它。例如，crawl4ai 的网站就没有配置 `robots.txt` 文件。我们打开 Google 的 `robots.txt` 文件可以看到，里面列出了允许和不允许爬虫访问的路径。在抓取数据时，最好遵守这些规范。
**五、在 N8N 中搭建数据抓取工作流**
现在，我们已经成功搭建了 N8N 和 crawl4ai 服务，下面就可以开始搭建数据抓取的工作流了。
  1. **添加启动节点：** 在 N8N 工作流界面，点击 "添加触发器"（Add Trigger），选择 "聊天消息"（Chat Message），然后点击 "打开聊天"（Open Chat）。之后，我们只需要在这里发送一条消息，就可以启动这个工作流。  

  2. **添加 HTTP 请求节点（获取 Sitemap）：** 在启动节点后面添加一个 "HTTP 请求"（HTTP Request）节点。将 "请求方法"（Request Method）设置为 "GET"。在 "URL" 字段，直接将左侧 "启动节点"（Chat Input）的输出拖拽过来。这意味着我们将通过聊天消息发送要抓取的网站的 Sitemap XML 文件对应的网址。点击 "测试"（Execute Node），你应该能成功获取到 Sitemap XML 文件的内容。  

  3. **添加 XML 节点（XML 转 JSON）：** 为了方便处理 Sitemap 数据，我们需要将其从 XML 格式转换为 JSON 格式。添加一个 "XML" 节点，选择 "XML to JSON" 转换类型。点击 "测试"，你会看到 XML 内容已经成功转换为 JSON 格式。  

  4. **添加 Split Out 节点（分割 URL）：** 在转换后的 JSON 数据中，包含着多个网页的 URL。我们需要将这些 URL 分割成单独的项进行处理。添加一个 "Split Out" 节点，在 "字段"（Fields）中，直接将左侧包含 URL 的字段拖拽过来。点击 "测试"，你会看到 URL 已经被分割成一个个独立的项。  

  5. **添加 Limit 节点（限制抓取数量）：** 为了方便调试和避免对目标网站造成过大的压力，我们可以添加一个 "Limit" 节点来限制每次抓取的 URL 数量。例如，我们可以设置为只抓取前 2 个 URL。在需要抓取整个网站时，再将这个值调大即可。点击 "测试"，你会看到只有指定数量的 URL 被保留下来。  

  6. **添加 Looping 节点（循环处理每个 URL）：** 接下来，我们需要循环处理每个 URL。添加一个 "Looping" 节点，选择 "每次处理一个项"（Process One Item at a Time）。点击 "测试" 确保没有问题。  

  7. **添加 HTTP 请求节点（POST 请求到 Cross for AI）：** 将上一步的 Looping 节点替换为一个新的 "HTTP 请求" 节点。将 "请求方法" 设置为 "POST"。在 "URL" 字段，粘贴上 Cross for AI 提供的抓取数据的 API 地址。由于我们是使用 Docker 部署的 Cross for AI，这里的域名需要使用 `host.docker.internal` 来替换 `127.0.0.1`。当然，你也可以使用反向代理进行配置。将 "认证方式"（Authentication）设置为 "普通认证"（Basic Auth），然后选择 "请求头认证"（Header Auth），点击 "添加信任凭证"（Add New Credential）。  

  8. **配置 Cross for AI API 认证：** 回忆一下我们在部署 Cross for AI 服务时使用的 Docker 命令，其中通过 `-e` 参数设置了 `CROWN_API_TOKEN` 环境变量。我们需要在这里使用这个 Token 进行认证。在 "信任凭证" 对话框中，将 "名称"（Name）设置为 "Authorization"，将 "值"（Value）设置为 `Bearer 你的Token值`（例如：`Bearer 12345`，将 `12345` 替换为你自己设置的 Token）。点击 "保存"（Save）。  

  9. **配置 HTTP 请求体：** 打开 HTTP 请求节点的 "发送数据"（Send Data）选项卡，选择 "Body" 类型为 "JSON/Raw Parameters"。我们需要添加两个消息体字段：`url` 和 `priority`。这两个字段可以参考 Cross for AI 的官方文档。`url` 的值直接从上一步的 Looping 节点拖拽包含 URL 的字段过来。`priority` 设置为一个默认值，例如 `10`。点击 "测试"，你应该能看到执行成功，并且返回一个 `task_id`。  

  10. **添加 Wait 节点（等待）：** 为了避免抓取频率过快，触发目标网站的反爬策略，我们在每次抓取数据之前添加一个 "Wait" 节点，设置等待几秒钟。这个数值可以根据你的需求进行调整。点击 "测试" 确保没有问题。  

  11. **添加 HTTP 请求节点（GET 请求获取抓取结果）：** 接着，我们再添加一个 "HTTP 请求" 节点，用于执行抓取任务，即 Cross for AI 提供的第二个 API。将 "请求方法" 设置为 "GET"。在 "URL" 字段，粘贴上 Cross for AI 获取抓取结果的 API 地址，并在后面拼接上上一步返回的 `task_id`。同样，认证方式选择 "Header Auth"，并使用之前创建的信任凭证。点击 "测试"，你应该能看到执行成功，并且返回了抓取到的网页内容。注意，成功返回的 JSON 数据中，通常会包含一个 `status` 字段，其值为 `completed` 表示抓取任务已完成。  

  12. **添加 If 节点（判断任务状态）：** 为了判断抓取任务是否成功，我们添加一个 "If" 节点。在 "条件"（Conditions）中，判断上一步返回的 JSON 数据中 `status` 字段的值是否等于 `completed`。点击 "测试" 确保没有问题。这个 If 节点有两个输出分支：True（任务成功）和 False（任务失败）。  

  13. **添加 AI Agent 节点（数据处理）：** 在 True 分支后面添加一个 "AI Agent" 节点。选择 "自定义"（Custom），然后粘贴上你的 AI 提示词（Prompt）。这个提示词的作用是让 AI 将抓取到的数据整理成适合大模型驱动的 RAG 知识库的结构化、易读的格式。例如，你可以要求 AI 进行内容解析、结构化整理、创建 FAQ、提升可读性、优化输出等。在左侧的输入字段中，找到包含抓取到的 Markdown 内容的字段（通常是 `markdown`），将其拖拽到 AI Agent 节点的输入端。在右侧，点击左下角的加号，添加一个 AI 模型。这里我们选择 DeepSeek，然后添加你的 DeepSeek API Key。模型选择 `chat`，对应 DeepSeek 的 V3 模型。点击 "测试"，你应该能在右侧看到经过 AI 整理后的内容。  

  14. **处理抓取失败的情况：** 点击 If 节点的 False 分支，添加一个 "字段编辑"（Set）节点。在这里，添加一个名为 `task_id` 的字段，其值与之前创建抓取任务时返回的 `task_id` 相同。然后，将这个字段编辑节点的输出连接到之前的 Wait 节点。这样，当抓取任务失败时，它会重新创建一个相同的抓取任务并再次执行。  

  15. **添加 Convert to File 节点（转换为文件）：** 在 AI Agent 节点后面添加一个 "Convert to File" 节点。将左侧 AI Agent 节点的输出中包含 Markdown 内容的字段拖拽到 "输入字段"（Input Data）中。在 "文件名"（Filename）这里，可以使用输出内容的第一行作为文件名。点击 "测试"，你应该能看到生成了一个文件，点击下载即可查看。  

  16. **添加 Write File to Disk 节点（保存到本地）：** 最后，添加一个 "Write File to Disk" 节点。在 "操作"（Operation）中选择 "写入文件到磁盘"（Write File to Disk）。在 "文件路径"（File Path）这里，你可以设置一个固定的路径，例如你本地磁盘的某个文件夹。在 "文件名" 这里，同样可以使用上一步输出内容的第一行，或者使用当前时间作为文件名。  
**注意：** 回忆一下我们在启动 N8N 服务时，可能使用了 `-v` 参数进行路径映射。这是因为 N8N 服务运行在 Docker 容器中，默认情况下生成的文件会保存在容器内部，而不是你的本地磁盘上。通过路径映射，可以将容器内的指定路径（例如 `/home/node/.n8n`）下的文件映射到你本地磁盘的某个路径下（例如 `~/Downloads/markdown`）。你需要根据你的实际 Docker 配置来设置文件路径。

![](https://pic1.zhimg.com/v2-ea596e2972c76c1a633bafedcc465e50_1440w.jpg)
至此，我们的自动化数据抓取工作流就搭建完成了！
**六、测试工作流**
现在，我们来测试一下这个工作流。在 N8N 的聊天对话框中，发送一个你想要抓取的网站的 Sitemap XML 文件对应的 URL。工作流就会开始执行，你可以在 N8N 的界面上看到任务的执行进度。执行完成后，你会在之前设置的本地磁盘路径下看到生成的 Markdown 文件。打开文件查看，内容应该是没有问题的。
为了测试抓取整个网站的能力，我们可以将 Limit 节点的限制调大（例如 20），然后输入一个大型网站的 Sitemap URL（例如 DeepSeek API 文档的网站）。点击发送，等待任务执行完成，你会看到在本地生成了多个对应的 Markdown 文件，里面包含了 DeepSeek API 的文档内容。
![](https://pica.zhimg.com/v2-f92ebc785155a62b0133cd4e6abc6340_1440w.jpg)
**七、使用抓取到的数据搭建知识库**
接下来，我们可以使用抓取到的数据搭建一个知识库。这里我们使用 **Cherry Studio** 这款免费软件来搭建知识库。关于 Cherry Studio 的使用，以及如何搭配本地 AI 和配置知识库，作者之前做过专门的一期，感兴趣的可以去看一下。
在 Cherry Studio 中，创建一个新的知识库，选择你想要使用的本地 AI 模型。然后，将之前抓取到的所有 Markdown 文件加载到这个知识库中。数据加载完成后，你就可以在 Cherry Studio 中直接进行检索，测试知识库是否能够正常工作。
最后，在 Cherry Studio 的 AI 对话页面，关联上你刚刚创建的知识库，然后向 AI 提问一些与你抓取的网站内容相关的问题。你会发现，AI 能够参考你上传到知识库中的内容以及它自身的知识，给出更准确、更全面的回答。
![](https://pic2.zhimg.com/v2-ed37554ef58150ac4e860b7185f7eecb_1440w.jpg)
**八、一些需要注意的问题**
  * 在抓取数据后，我们使用了在线的 DeepSeek 模型进行了数据整理。如果需要抓取的网页数量非常多，需要关注一下 API 的使用成本。如果想要使用本地的 AI 模型进行数据处理，只需要将 N8N 工作流中的 AI Agent 节点替换为你本地部署的 AI 模型即可。但是，由于网页数据量可能较大，使用本地 AI 进行处理时，最好搭配性能较好的显卡，否则处理速度可能会比较慢。
  * 在抓取数据时，务必注意控制好抓取频率，避免对目标网站造成过大的压力，从而被网站的反爬策略限制。可以在 N8N 的 Wait 节点中调整等待时间。


**九、分享和导入 N8N 工作流**
为了方便分享和复用，你可以将你创建的 N8N 工作流导出为配置文件。在 N8N 工作流界面，点击右上角的三个点，选择 "Download"，即可将工作流配置下载到本地。要导入一个已有的工作流，只需在 N8N 中新建一个工作流，然后点击右上角的三个点，选择 "Import from File"，选择你下载的配置文件即可导入。
需要注意的是，在分享工作流之前，务必删除配置文件中包含的敏感信息，例如 API Key 等。导入别人的工作流后，也需要将这些参数配置为你自己的参数才能正常使用。
![](https://pic1.zhimg.com/v2-450f1ea05d09d806b9b19272faf48d92_1440w.jpg)
**十、N8N 的 MCP 功能（进阶）**
N8N 提供了一个名为 **MCP（Managed Code Plugin）** 的功能，它允许你在 N8N 中运行自定义的代码片段，以实现更复杂的功能。我们在部署 N8N 服务时，如果使用了 `-e` 参数配置了 `N8N_COMMUNITY PACKAGES_ALLOW TOOL_USAGE=true`，就开启了 MCP 功能。
![](https://pic1.zhimg.com/v2-dee8614110adcb89c08ad3438824d72a_1440w.jpg)
要使用 MCP 功能，你需要先安装相关的社区节点。在 N8N 界面，点击左下角的 "设置"（Settings），在左侧选择 "社区节点"（Community Nodes），点击 "安装节点"（Install Node），然后输入 `n8n-nodes-mcp` 并点击安装。
安装完成后，你就可以在 N8N 中使用 MCP 节点了。例如，你可以使用 MCP 节点来实现将文件保存到本地的功能，从而替换掉之前的 "Convert to File" 和 "Write File to Disk" 节点。
![](https://pic4.zhimg.com/v2-d01366f213ef4c27eaaeb22b08058473_1440w.jpg)
**总结**
通过本文的介绍，相信你已经了解了如何使用 N8N 和 crawl4ai 搭建一个自动化抓取网站数据的工作流，并利用抓取到的数据构建知识库，最终实现 RAG 方案。这个工作流可以帮助你自动化地获取网络上的信息，为你的 AI 应用提供强大的数据支持。
发布于 2025-04-08 12:28・北京
[AI工作流](https://www.zhihu.com/topic/27732938)
[Mcp](https://www.zhihu.com/topic/20661231)
[国产大模型DeepSeek](https://www.zhihu.com/topic/1862547279613046600)
​赞同 32​​5 条评论
​分享
​喜欢​收藏​申请转载
​
关于作者
[![AI解码师](https://pica.zhimg.com/v2-fdac6de0add53a6c59762650c399ff7e_l.jpg?source=172ae18b)](https://www.zhihu.com/people/ferrarizrw)
[AI解码师](https://www.zhihu.com/people/ferrarizrw)
xx-ferrari787381610
[​](https://zhuanlan.zhihu.com/p/96956163)
互联网行业 技术专家
[回答](https://www.zhihu.com/people/ferrarizrw/answers)[文章](https://www.zhihu.com/people/ferrarizrw/posts)[关注者](https://www.zhihu.com/people/ferrarizrw/followers)
​关注​发私信
