from dotenv import load_dotenv
from swarm import Swarm, Agent

# Load environment variables from .env file
load_dotenv()

mock_jira_ticket= f"""
Ticket Id: 1234
Issue Type: Story
Priority: High
Status: To Do
Summary: Implement User Authentication System

Description:
We need to implement a user authentication system that allows users to securely register, log in, and log out of the platform. This feature should also support password recovery and include basic security measures such as account lockout after multiple failed login attempts.

Acceptance Criteria:

Users should be able to register using an email and password.
Users should receive a confirmation email after registration.
Implement secure login functionality.
Users should be able to recover their password via email.
After 5 failed login attempts, the account should be temporarily locked for 30 minutes.
Ensure all sensitive data is encrypted.
Technical Notes:

Use JWT for handling session management.
Passwords should be stored with hashing (use bcrypt).
Email service can use SendGrid for sending registration and recovery emails.
Assignee: John Smith
Reporter: Jane Doe
Labels: Authentication, Backend, Security
Story Points: 5
Sprint: Sprint 3
Component/s: Backend, Authentication
"""

client = Swarm()

# Mock get Jira ticket API call
def get_jira_ticket(ticket_id):
   print(f"fetching ticket {ticket_id}")
   return mock_jira_ticket

def transfer_to_agent_b():
    return agent_b


agent_a = Agent(
    name="Agent A",
    instructions="You are a helpful agent interfacing between users and the team.",
    functions=[transfer_to_agent_b],
)

agent_b = Agent(
    name="Agent B",
    instructions="You are a helpful product manager",
    functions=[get_jira_ticket]
)

response = client.run(
    agent=agent_a,
    messages=[{"role": "user", "content": "Is the ticket with id 1234 complete?"}],
    debug=True,
)

print(response.messages[-1]["content"])
