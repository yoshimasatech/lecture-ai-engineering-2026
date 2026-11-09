from adk_app.agent import root_agent


def test_adk_agent_registers_the_same_learning_tools():
    assert root_agent.name == "aie_learning_agent"
    assert {tool.__name__ for tool in root_agent.tools} == {
        "search_glossary",
        "get_lecture_summary",
    }