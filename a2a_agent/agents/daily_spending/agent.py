from google.adk.agents import LlmAgent


def _make_sub_agents():
    categorizer = LlmAgent(
        name="ds_categorizer",
        model="gemini-2.5-flash",
        description="Classifies daily transactions into categories and flags anomalies.",
        instruction=(
            "Classify spending by category (groceries, dining, transport, utilities, shopping, other)"
            " and flag unusual spikes relative to recent patterns."
        ),
    )

    coach = LlmAgent(
        name="ds_coach",
        model="gemini-2.5-flash",
        description="Provides short coaching tips to reduce daily spending.",
        instruction=(
            "Provide 2-4 concise tips tailored to the spending categories with the highest impact."
            " Keep tone supportive and practical."
        ),
    )

    return categorizer, coach


_sub_categorizer, _sub_coach = _make_sub_agents()

root_agent = LlmAgent(
    name="daily_spending_agent",
    model="gemini-2.5-flash",
    description="Analyzes daily spending and offers coaching suggestions.",
    instruction=(
        "You orchestrate daily spending analysis."
        " First, use 'ds_categorizer' to categorize and detect spikes."
        " Then, use 'ds_coach' to provide concise coaching tips."
    ),
    sub_agents=[_sub_categorizer, _sub_coach],
)


