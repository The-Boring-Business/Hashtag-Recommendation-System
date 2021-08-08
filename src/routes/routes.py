from src.api.visiontag import ImageApi
from src.api.docs import Home

 

def initialize_routes(Api):
    #Get: check to see if APi is running 
    #POST: send image for prediction 
    Api.add_resource(ImageApi,'/api/image')
    Api.add_resource(Home,'/')
