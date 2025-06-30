import time
import yaml
from julep import Julep
from config import JULEP_API_KEY

# Initialize client
client = Julep(api_key=JULEP_API_KEY)

# Create an agent (only needs to be created once—ideally you cache this ID)
agent = client.agents.create(
    name="Indian Foodie Tour Guide",
    model="claude-3.5-sonnet",
    about="An expert Indian food travel guide who creates delightful one-day foodie tour itineraries."
)

# Define the task template
task_definition = yaml.safe_load("""
name: Foodie Tour Generator
description: Generate a one-day foodie tour for a given city in India.
main:
- prompt:
  - role: system
    content: You are an expert Indian food and travel guide.
  - role: user
    content: |
      $ f"Create a one-day foodie tour itinerary for {steps[0].input.city}, India.

      Include:
      - The current weather (invent something realistic).
      - Whether to recommend indoor or outdoor dining.
      - 3 iconic local dishes for breakfast, lunch, dinner.
      - 3 restaurants with names and addresses.
      - A warm, descriptive narrative of the day's journey.

      Format it nicely."
""")


# Create the task
task = client.tasks.create(
    agent_id=agent.id,
    **task_definition
)

class FoodieTour:
    def __init__(self, cities):
        self.cities = cities

    def generate_tour(self, city):
        print(f"\nProcessing: {city}")

        # Start execution
        execution = client.executions.create(
            task_id=task.id,
            input={"city": city}
        )

        # Poll for completion
        while True:
            result = client.executions.get(execution.id)
            if result.status in ["succeeded", "failed"]:
                break
            print(f"Status: {result.status}")
            time.sleep(1)

        if result.status == "succeeded":
            return result.output
        else:
            return f"Error: {result.error}"

    def run(self):
        for city in self.cities:
            narrative = self.generate_tour(city)
            print("\n" + narrative)
            print("-" * 80)


if __name__ == "__main__":
    cities = ["Mumbai", "Delhi", "Kolkata"]
    planner = FoodieTour(cities)
    planner.run()

