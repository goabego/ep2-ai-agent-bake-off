
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from api.endpoints import users, accounts, goals, transactions, financials, partners, schedule, meeting
from core.config import API_PREFIX
import requests
import os

app = FastAPI(
    title="Cymbal Bank API",
    description="API for the Cymbal Bank, providing access to financial data.",
    version="0.1.0",
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include routers
app.include_router(users.router, prefix=API_PREFIX, tags=["Users"])
app.include_router(accounts.router, prefix=API_PREFIX, tags=["Accounts"])
app.include_router(goals.router, prefix=API_PREFIX, tags=["Goals"])
app.include_router(transactions.router, prefix=API_PREFIX, tags=["Transactions"])
app.include_router(financials.router, prefix=API_PREFIX, tags=["Financials"])
app.include_router(partners.router, prefix=API_PREFIX, tags=["Partners"])
app.include_router(schedule.router, prefix=API_PREFIX, tags=["Schedule"])
app.include_router(meeting.router, prefix=API_PREFIX, tags=["Meeting"])

@app.get("/", tags=["Root"])
def read_root():
    """
    Root endpoint for health checks.
    """
    return {"status": "ok", "message": "Welcome to the AI Financial Steward API"}

A2A_AGENT_URL = os.environ.get("A2A_AGENT_URL", "https://a2a-bfpwtp2iiq-uc.a.run.app")


@app.get("/token", tags=["Authentication"])
def get_auth_token():
    """
    Get Google Cloud ID token for A2A service authentication.
    This endpoint fetches the token from the metadata server and returns it to the frontend.
    """
    try:
        # Fetch ID token from Google Cloud metadata server
        metadata_url = "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/identity"
        params = {"audience": A2A_AGENT_URL}
        headers = {"Metadata-Flavor": "Google"}

        response = requests.get(metadata_url, params=params, headers=headers, timeout=10)

        if response.status_code == 200:
            return {"token": response.text, "status": "success"}
        else:
            raise HTTPException(status_code=500, detail=f"Failed to fetch token: {response.status_code}")

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching token: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")


@app.post("/proxy/a2a", tags=["Proxy"])
async def proxy_a2a_request(request: dict):
    """
    Proxy requests to the A2A service with proper authentication.
    This eliminates CORS issues by handling all communication server-side.
    """
    try:
        # Get authentication token
        metadata_url = "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/identity"
        params = {"audience": A2A_AGENT_URL}
        headers = {"Metadata-Flavor": "Google"}

        token_response = requests.get(metadata_url, params=params, headers=headers, timeout=10)

        if token_response.status_code != 200:
            raise HTTPException(status_code=500, detail="Failed to get authentication token")

        auth_token = token_response.text

        # Forward request to A2A service
        a2a_url = f"{A2A_AGENT_URL}/"
        a2a_headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {auth_token}"
        }

        a2a_response = requests.post(a2a_url, json=request, headers=a2a_headers, timeout=30)

        if a2a_response.status_code == 200:
            return a2a_response.json()
        else:
            raise HTTPException(status_code=a2a_response.status_code, detail=f"A2A service error: {a2a_response.text}")

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Proxy error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

