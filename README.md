# AI Marketing Team Automation Project

![AI Marketing Team Automation](https://raw.githubusercontent.com/othmansamih/AI-Marketing-Team-Automation/main/assets/AI-Marketing-Team-Automation.png)

This project automates the process of researching, planning, and creating Instagram content using CrewAI. It leverages agent-based architecture and predefined tasks to streamline content creation for Instagram pages.

## Features

- **Market Research**: Automatically identify Instagram trends, hashtags, and audience insights.
- **Content Strategy**: Create a structured 7-day content calendar based on research.
- **Copywriting**: Generate SEO-optimized and engaging captions tailored to the content strategy.
- **Image Descriptions**: Produce vivid descriptions for visuals to inspire or directly use with AI image generation tools.
- **Automation Pipeline**: Compile all outputs into a cohesive weekly content plan.



## Project Structure
```markdown
src/
├── instagram/
│ ├── config/
│ │ ├── agents.yaml # Configuration for agents
│ │ ├── tasks.yaml # Configuration for tasks
│ ├── tools/
│ │ └── search_tools.py # Tools for web and Instagram searches
│ ├── crew.py # Core CrewAI logic
│ └── main.py # Entry point for running, training, and testing the crew
├── tasks/ # Directory for task outputs
├── .env # Environment variables
├── .gitignore # Git ignore file
├── pyproject.toml # Python project configuration
```


## Getting Started

### Prerequisites

- Python ">=3.10,<=3.13"
- An OpenAI API key
- A Serper API key for Google Search integration

### Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd instagram
   ```

1. Install dependencies:
    
    ```bash
    pip install -r requirements.txt
    ```
    
2. Create a `.env` file and add your API keys:
    
    ```
    SERPER_API_KEY=<your-serper-api-key>
    OPENAI_API_KEY=<your-openai-api-key>
    
    # use the config below if you want to trace the llm calls
    LANGCHAIN_TRACING_V2=true
    LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
    LANGCHAIN_API_KEY=<your-langchain-api-key>
    LANGCHAIN_PROJECT="project-name"
    ```
    

### Run the Crew

To execute the workflow:

```bash
crewai run
```

You'll be prompted to provide:

- Instagram page description
- Topic of the week

## Configuration

### Agents

Defined in `src/instagram/config/agents.yaml`, agents represent the roles in the workflow:

- **Market Researcher**: Conducts Instagram market research.
- **Content Strategist**: Plans the weekly content calendar.
- **Copywriter**: Writes captions for posts.
- **Visual Artist**: Describes visuals for posts.

### Tasks

Defined in `src/instagram/config/tasks.yaml`, tasks represent the actions taken by agents:

- `market_research_task`
- `content_calendar_task`
- `copy_writing_task`
- `image_description_task`
- `compile_weekly_content_task`

## Tools

Custom tools in `src/instagram/tools/search_tools.py` allow agents to:

- Search the internet or Instagram.
- Open and extract content from web pages.

## Output

Task results are saved in the `tasks/` directory as markdown files:

- `1_market_research_task.md`
- `2_content_calendar_task.md`
- `3_copy_writing_task.md`
- `4_image_description_task.md`
- `5_compile_weekly_content_task.md`

## Dependencies

- CrewAI (`crewai[tools]>=0.86.0`)
- Python libraries as specified in `pyproject.toml`
