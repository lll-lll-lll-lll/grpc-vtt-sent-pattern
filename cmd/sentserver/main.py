import api.api_pb2_grpc as api_pb2_grpc
import api.api_pb2 as pb2
from concurrent.futures import ThreadPoolExecutor
import grpc
import asyncio
import spacy
import logging
from grpc_reflection.v1alpha import reflection
from sent_pattern import tags
nlp = spacy.load("en_core_web_md")


class Server(api_pb2_grpc.VTTSentPatternServiceServicer):
    def Hello(self, request:pb2.HelloRequest, context:grpc.aio.ServicerContext) -> pb2.HelloResponse:
        print("Hello method start!")
        res = pb2.HelloResponse(message=request.name)
        print("Hello method done!")
        return res
    
    def GetPattern(self, request: pb2.GetPatternRequest, context:grpc.aio.ServicerContext) -> pb2.GetPatternResponse:
        print("GetPattern start")
        text = request.text
        doc = nlp(text)
        dep_list = tags.create_dep_list(doc)
        elements = tags.create_elements(dep_list)
        pattern = tags.create_sent_pattern(elements)
        res = pb2.GetPatternResponse(text=pattern.type.__class__.__name__)
        print("GetPattern Done")
        return res

def setRefrection(server):
    SERVICE_NAMES = (
        pb2.DESCRIPTOR.services_by_name['VTTSentPatternService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    
    
async def serve()-> None:
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    setRefrection(server)
    api_pb2_grpc.add_VTTSentPatternServiceServicer_to_server(
        Server(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("start server!")
    server.wait_for_termination()

def main()->None :
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())

if __name__ == '__main__':
    main()