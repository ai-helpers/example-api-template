import fastapi

from api_example import __version__
from api_example.endpoints import root, health, info, test, predict

#
app = fastapi.FastAPI(
    title="API",
    description="My project description",
    version=__version__,
)

# Register the endpoints. See the endpoints/ directory
# for the corresponding source code.
app.include_router(root.router)
app.include_router(health.router)
app.include_router(info.router)
app.include_router(test.router)
app.include_router(predict.router)
