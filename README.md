# Debate Crew

Welcome to the Debate Crew project, powered by [crewAI](https://crewai.com). This project sets up a multi-agent AI system that simulates a formal debate. It features a proponent, an opponent, and a judge who oversees a 5-round debate on a given topic.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/first_crew/config/agents.yaml` to define your agents
- Modify `src/first_crew/config/tasks.yaml` to define your tasks
- Modify `src/first_crew/crew.py` to add your own logic, tools and specific args
- Modify `src/first_crew/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the Debate Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run a debate on "Pineapple on pizza" and create a `debate_verdict.md` file with the judge's final decision in the root folder.

## Understanding Your Crew

The Debate Crew is composed of three AI agents:

-   **Proponent**: Argues in favor of the debate topic.
-   **Opponent**: Argues against the debate topic.
-   **Judge**: Objectively evaluates the arguments from both sides and declares a winner.

The debate follows a 5-round structure, including opening statements, three rounds of rebuttals, and closing statements. The tasks for each round are defined in `config/tasks.yaml`, and the agent configurations are in `config/agents.yaml`.

## Support

For support, questions, or feedback regarding the FirstCrew Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
