from google.adk.agents import LlmAgent


def _make_sub_agents():
    selector = LlmAgent(
        name="bp_selector",
        model="gemini-2.5-flash",
        description="Identifies if the query concerns big purchases and classifies the purchase type.",
        instruction=(
            "You detect if a user is asking about large purchases (cars, appliances, home upgrades, tuition)."
            " If yes, classify the purchase type and surface key factors (budget, financing, timeline)."
        ),
    )

    advisor = LlmAgent(
        name="bp_advisor",
        model="gemini-2.5-flash",
        description="Provides guidance on budgeting, financing, and timing for big purchases.",
        instruction=(
            "Provide concise advice on budgeting, saving strategies, financing options, and timing for large purchases."
            " Use clear bullet points and short guidance."
        ),
    )

    return selector, advisor


_sub_selector, _sub_advisor = _make_sub_agents()

root_agent = LlmAgent(
    name="big_purchases_agent",
    model="gemini-2.5-flash",
    description="Coordinates sub-agents to help plan and evaluate big purchases.",
    instruction=(
        "You orchestrate big purchase planning."
        " First, use 'bp_selector' to determine relevance and purchase type."
        " Then, use 'bp_advisor' to provide budgeting and financing guidance."
        " Keep responses concise and actionable."
    ),
    sub_agents=[_sub_selector, _sub_advisor],
)


