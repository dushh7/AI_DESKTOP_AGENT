from agents.desktop_agent import run_agent

print(run_agent(
    r"Create folder D:\AI_AGENT_TEST\TestFolder"
))

print(run_agent(
    r"Create file D:\AI_AGENT_TEST\TestFolder\notes.txt"
))

print(run_agent(
    r"Search file notes.txt"
))