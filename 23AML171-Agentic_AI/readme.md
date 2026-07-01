# AGENTIC ARTIFICIAL INTELLIGENCE [23AML171]

## EXPERIMENTS

- **Introduction**

    1. A 'hello world' agent that responds to generic question in non-streaming and streaming mode.

    2. A simple agent handing customer service request

- **Tools Use**

    3. An agent capable of calling local and API-based tools

    4. MCP server as a tool for an agent to connect

- **Memory & Knowledge**

    5. An agent with short-term memory

    6. An agent to query a knowledge graph

- **Multi-agent Systems**

    7. Multi-agent Personal Assistant System Built on Supervisor Pattern

    8. Multi-agent Knowledge Base System Built on Router Pattern

- **Evaluation & Monitoring**

    9. Evaluating agent performance assessing its trajectory using trajectory match and LLM-as-Judge approaches
    
_Remaining ones coming soon..._


## CONDA ENVIRONMENT
Python 3.12.13


## SELF-HOSTED MODELS & PROVIDERS
Majority of the experiments use self-hosted models using provider _Ollama_. Ollama service must be running to serve the models to the experiments. Refer to the installation section for additional instructions.

List of few of popular selft-hosted models are provided below.

| MODEL	| Intelligence on Artificial Analysis (https://artificialanalysis.ai/) | SIZE | CONTEXT WINDOW | INPUT | OUTPUT SPEED (tokens/second)| CAPABILITIES |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| **qwen3.5:9b**    |	32  |	6.6 GB |	256K |	Text, Image, Audio |	59      | Reasoning and Non-Reasoning, Tools, Coding |
| **gemma4:12b**  |  29   | 7.6 GB	|256K	| Text, Image, Audio, Video | -- | Automatic speech recognition, Agentic reasoning, Diarization, Video understanding, Coding, and more |
| **gemma4:e4b**  |  19   | 9.6 GB	|128K	| Text, Image, Audio | -- | Vision, Tools, Multi-modal Reasoning, Coding, Audio |
| **llama3.1:8b**  | 12    | 4.9 GB	|128K	| Text | 155 | Mathematics, Tools, Reasoning, Multilingual translation, Summarization, Coding |
| **granite4.1:3b**  | 9    | 2.1 GB	|128K	| Text | -- | Summarization, Text classification, Text extraction, Question-answering, Retrieval Augmented Generation (RAG), Coding, Tools, Multilingual dialog use cases, Fill-In-the-Middle (FIM) |
| **granite4.1:8b**	| 12    | 5.3 GB    |	128K | Text | 111 | Summarization, Text classification, Text extraction, Question-answering, Retrieval Augmented Generation (RAG), Coding, Tools, Multilingual dialog use cases, Fill-In-the-Middle (FIM) |
| **gemma4:e2b**    | 15    |	7.2 GB | 128K |	Text, Image, Audio | - | Multi-Turn Conversations, Reasoning and Non-Reasoning, Coding, Native function-calling |
| **gemma4:e4b**    | 15    |	9.6 GB | 128K |	Text, Image, Audio | 42/50 | Multi-Turn Conversations, Reasoning and Non-Reasoning, Coding, Native function-calling |
| **qwen3.5:2b**    |	16  |	2.7 GB |	256K |	Text, Image, Audio |	340     | Reasoning and Non-Reasoning, Tools, Coding |
| **qwen3.5:4b** |	27  |	3.4 GB |	256K |	Text, Image, Audio |	177/199 | Reasoning and Non-Reasoning, Tools, Coding |
| **ministral-3:3b** |	11  |	3.0 GB |	256K |	Text, Image |	282 | Reasoning, Multilingual, Tools, Coding, Document analysis [This model requires Ollama 0.13.1, which is currently in pre-release.] |
| **ministral-3:8b** |	15  |	6.0 GB |	256K |	Text, Image |	158 | Reasoning, Multilingual, Tools, Coding, Document analysis [This model requires Ollama 0.13.1, which is currently in pre-release.] |
| **deepseek-r1:8b** (DeepSeek-R1-0528 upgrade) | - |	5.2 GB |	128K |	Text |	- |	Reasoning, Coding, Mathematics |
| **llama3.2:3b** |	-   | 2.0 GB |	128K |	Text |	- |	Multilingual dialog use cases, Tools, Summarization, Prompt rewriting |
| **nemotron-3-nano:4b** |	15 |	2.8 GB |	256K |	Text | - |		Reasoning, Multilingual, Tools |
| **Mistral 7B**        | - | 4.4 GB |	32K |	Text | - | - |

## INSTALLATION

**Anaconda Datascience Platform:**

Ensure Anaconda datascience platform is already installed in your computer. Then follow the instruction below to complete required installation to perform all the above listed experiments.

**Specific Environment to Run Experiments:**

For Windows, run the following commands in **Anaconda Prompt**.

```
conda create -n agentic_ai python=3.12.13     # Creates a new conda environment named "agentic_ai".

conda activate agentic_ai                     # Activates the newly created environment.

```

**Ollama:**

Ollama installation for Windows:

1. Download installation file `OllamaSetup.exe` from
https://github.com/ollama/ollama/releases/tag/v0.24.0 and install following online instructions.

2. During Ollama installation, if it asks permission to install `Visual C++ Redistributables`, provide consent to install the same.

Ollama installation for Linux:

```
curl -fsSL https://github.com/ollama/ollama/releases/download/v0.24.0/install.sh | sh     # Installs a specific version of Ollama
```

Checking Ollama installation:

- To make the command 'ollama' avilable in the terminal, exit from the current terminal and re-open once again.

- Ollama listens at `127.0.0.1:11434`. Open the link in any web browser (alternatively, running command `curl http://localhost:11434` at the terminal) and check if response `Ollama is running` is received. 

If no response is received, then consider starting Ollama using the below mentioned command in the terminal.

```
ollama serve
```

Downlading specific models:

Run the following command to download the mentioned model(s).

```
ollama pull llama3.2:3b     # Downloads Llama 3.2 3B model

ollama pull qwen3.5:2b      # Downloads Qwen 3.5 2B model

ollama pull granite4.1:3b   # Downloads Granite 4.1 3B model
```

Similarly, other models can also be downloaded as required.

Checking downloaded model(s):

For a quick check if the downloaded models works, run the following command in the terminal and engage with a short conversation with it. To quit from the model prompt, type `/bye` and press enter to return to terminal prompt.

```
ollama run llama3.2:3b --think=false        # Setting --think=false will switch off model reason resulting faster responses from the model
```

**Packages:**

Install the required packages by running the following commands in the terminal with environment `agentic_ai` active.

```
pip install agent-framework                 # Installs v1.2.0

pip install ollama                          # Installs ollama v0.5.3

pip install agent-framework-ollama --pre	# Installs agent-framework-ollama v1.0.0b260424 [requires ollama<0.5.4,>=0.5.3]

pip install agent-framework-openai          # OpenAI compatible Ollama chat client

pip install langchain                       # Installs Lanchain framework

pip install langchain-ollama                # An integration package connecting Ollama and LangChain   

pip install langchain-community             # Installs packages for 3rd-party integrations

pip install langchain-mcp-adapters          # Library provides a lightweight wrapper that makes Anthropic Model Context Protocol (MCP) tools compatible with LangChain and LangGraph

pip install wikipedia                       # Makes it easy to access and parse data from Wikipedia

pip install langchain-experimental          # Holds experimental LangChain code, intended for research and experimental uses

pip install langchain-neo4j                 # Package contains the LangChain integration with Neo4j.

pip install langgraph-checkpoint-sqlite     # Contains implementation of LangGraph `CheckpointSaver` that uses SQLite DB (both sync and async, via aiosqlite)

pip install neo4j-mcp-server                # A bridge between an MCP client and Neo4j instance providing direct and structured access to graph database.

pip install agentevals                      # Provides prebuilt evaluators based on trajectory match or by LLM-as-judge

```

**Workflow Visualization:**

Installs visualization support for workflows. For Windows, refer https://graphviz.org/download/ and follow the installation instructions. For Linux, run the following command in the terminal.

```
sudo apt install graphviz
```

**Neo4j Desktop:**

 Neo4j Desktop Installation on Windows:

Open Neo4j [Deployment Center](https://neo4j.com/deployment-center/?desktop-gdb), go to section `https://neo4j.com/deployment-center/?desktop-gdb`, select operating system from the dropdown and click on `Download`. Then run the installation file and follow online instructions.

Neo4j Desktop Installation on Linux:

- Download AppImage for Neo4j Desktop from https://neo4j.com/download/ by filling an online form.
- Move the downloaded AppImage file to an appropriate folder.
- Open terminal and change the current directory to the one that contains the AppImage.
- Run command `chmod +x <appimage file name>` to make the AppImage executable.
- Double-click the AppImage file to launch the Neo4j Desktop app.
- Creating a local instance
    - Click on "Local instances" menu option
    - Click "Create instance" button
    - Provide details such as name of local instance such as "local", select "2026.05.0" as instance version, database password as "neo4jneo4j" (recommended only in academic settings).
    - Click on "Create" button.
    - Start the newly created instance by clicking on "Start" icon.
    - Once instance gets started, click on 3-dots button in the same pane and select "Plugins".
    - Locate for "APOC" and install it by clickin on its "Install" button. If prompted for restarting the instance, do so by clicking on "Restart" button.

After the installation, check if Neo4j can then be accessed over a web browser at http://localhost:7474.

The default password of neo4j database is is 'neo4j'. When prompted to change the default password at first login, it is suggested to be changed to 'neo4jneo4j' in academic settings for the same database to be accessible to all.

The following commands could be handy at times.

```
sudo neo4j start    # Starts Neo4j daemon.

sudo neo4j stop     # Stops Neo4j daemon.

sudo neo4j restart  # Restarts Neo4j daemon.

MATCH (n)-[r]->(m) RETURN n, r, m       # Returns all nodes and their connecting relationships. 

MATCH (n) DETACH DELETE n                Execute this at neo4j$ prompt in Neo4j UI to delete all the nodes and relationships from the database
```

## RUNNING EXPERIMENTS 

It is recommended to use an IDE (Integrated Development Environment) to carry out the experiments. Visual Studio Code (VS Code) and `Jupyter Lab` (successor of `Jupyter Notebook`) are very popular development environments. Refer IDE specific instructions below.

### Visual Studio Code

Following instructions below to configure VS Code.

1. Get VS Code updated to the latest version.

2. Install extension `Python` and `Jupyter`, if not already installed.

3. Restart extension that show their restart are pending.

4. For every experiments, set kernel to `agentic_ai` from `Select kernel` window located bottom-right corner of the IDE.

### Jupyter Lab

1. Execute the following command in the **Anaconda Prompt** terminal ensuring active environment is `agentic_ai`.

```
pip install jupyterlab
```

2. `[Optional]` Change the working directory to the one of preference.

3. Execute the following command to open Jupyter Lab interface. Kernel will be set to appropriate one automatically, if Jupyter Lab was opened keeping the 'agentic_ai` environment active.

```
jupyter lab
```
4. Enable code completion by checking `Enable autocompletion` in `Settings` > `Code Completion`. This also enables the 
    - auto-complete menu to appear with `Tab` key press and 
    - show of function signature, parameters, and documentation tooltip with `Shift + Tab` key press.
