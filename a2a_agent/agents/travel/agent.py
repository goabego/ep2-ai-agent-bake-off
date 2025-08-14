from google.adk.agents import LlmAgent


def _make_sub_agents():
    planner = LlmAgent(
        name="travel_planner",
        model="gemini-2.5-flash",
        description="Creates itineraries and suggests destinations based on budget and preferences.",
        instruction=(
            "Draft a simple itinerary with destinations, dates, and activities."
            " Ask for missing constraints (budget, dates, origin) when needed."
        ),
    )

    saver = LlmAgent(
        name="travel_saver",
        model="gemini-2.5-flash",
        description="Finds cost-saving tactics for travel (timing, routes, accommodations).",
        instruction=(
            "Provide cost-saving suggestions (off-peak travel, nearby airports, bundles, loyalty points)."
            " Keep the list short and prioritized."
        ),
    )

    return planner, saver


_sub_planner, _sub_saver = _make_sub_agents()

root_agent = LlmAgent(
    name="travel_agent",
    model="gemini-2.5-flash",
    description="Helps plan trips and optimize for savings using specialized sub-agents.",
    instruction=(
        "You orchestrate travel planning."
        " First, use 'travel_planner' to build or refine an itinerary."
        " Then, use 'travel_saver' to propose key savings."
    ),
    sub_agents=[_sub_planner, _sub_saver],
)


