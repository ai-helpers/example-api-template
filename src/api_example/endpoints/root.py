import fastapi

from api_example.endpoints.router import router

endpoint_description = """
Returns the description of the project.
"""


@router.get("/", description=endpoint_description, status_code=fastapi.status.HTTP_200_OK)
async def default() -> str:
    return "API - Powered by AI Helpers github organization"
