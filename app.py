from Attrition_App import logger
from Attrition_App.pipline.training_pipeline import TraningPipeline

try:
    logger.info('*'*100)
    logger.info('Initiating traning pipeline')
    pipe = TraningPipeline()
    pipe.main()
    logger.info('Traning pipeline completed succesfully')
    logger.info('*'*100)
except Exception as e:
    logger.exception(e)
    
    