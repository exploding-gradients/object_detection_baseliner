import os

ms_api_key = os.getenv('MS_SUBSCRIPTION_KEY', '')
ms_api_reg = os.getenv('MS_REGION', 'southcentralus')
ms_obj_detection_url = 'https://{}.api.cognitive.microsoft.com/vision/v2.0/analyze'.format(ms_api_reg)
