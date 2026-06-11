from agents.desktop_agent import run_agent

print("\nREAD FILE")
print(run_agent(
    r"Read file D:\AI_AGENT_TEST\TestFolder\notes.txt"
))

print("\nOPEN FILE")
print(run_agent(
    r"Open file D:\AI_AGENT_TEST\TestFolder\notes.txt"
))

print("\nDELETE FILE")
print(run_agent(
    r"Delete file D:\AI_AGENT_TEST\TestFolder\notes.txt"
))