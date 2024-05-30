import logging
import pydantic

import pandas as pd


from api_example.errors import APIModelNotFoundError, APIModelNotLoadableError
from api_example.settings.app_settings import Settings, get_settings
from api_example.endpoints.router import router
from api_example.load_model import load_model


#
class InputData(pydantic.BaseModel):
    feature_1: float = 10.0


endpoint_description = "My project description."


@router.post("/predict", description=endpoint_description)
def predict(request_data: InputData) -> dict:
    """Predict the output based on the input data.

    Args:
        request_data (InputData): The input data for the prediction.

    Returns:
        dict: The output of the prediction.
    """
    settings: Settings = get_settings()

    logger = logging.getLogger(__name__)
    logger.setLevel(settings.log_level)

    logger.info(f"[API::predict] Request data: {request_data}")

    input_data = request_data.dict()
    logger.info(f"[API::predict] Input data: {input_data}")

    # Read the Pickled model from the file-system
    model = load_model(settings=settings)

    # Prepare the data for the model
    data = pd.DataFrame.from_records([input_data])

    # Make the prediction
    predictions = model.predict(data)

    # Basic example of how to return the predictions
    output = {}
    output["predictions"] = predictions[0]

    logger.info(f"[API::predict] Prediction made: {output}")

    #
    return output
