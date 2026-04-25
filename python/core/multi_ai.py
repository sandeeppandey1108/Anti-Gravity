def route_task(task_type, payload):
    if task_type == "research":
        return "Gemini"
    if task_type == "script":
        return "Claude"
    if task_type == "review":
        return "GPT-OSS 120B"
    return "Python"
