from langchain.memory import ConversationBuffer


def get_memory():
    """Simple conversation memory."""
    
    return ConversationBuffer(
        memory_key="chat_history",
        return_messages=True
    )