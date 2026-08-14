from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import CollaborationRequest
from .serializer import CollaborationRequestSerializer


class CollaborationRequestListCreateView(ListCreateAPIView):
    queryset = CollaborationRequest.objects.all()
    serializer_class = CollaborationRequestSerializer
        
class CollaborationRequestDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = CollaborationRequest.objects.all()
    serializer_class = CollaborationRequestSerializer











# from rest_framework.decorators import APIView
# from rest_framework.response import Response
# from rest_framework import status

# from .models import CollaborationRequest
# from .serializer import CollaborationRequestSerializer

# class CollaborationRequestListCreateView(APIView):
#     def get(self, request):
#         collaboration = CollaborationRequest.objects.all()
#         serializer = CollaborationRequestSerializer(collaboration, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = CollaborationRequestSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        

        

# class CollaborationRequestDetailsView(APIView):
#     def try_except_collaboration(self, request, pk):
#         try:
#             return CollaborationRequest.objects.get(id = pk)
#         except CollaborationRequest.DoesNotExist:
#             return None

#     def get(self, request, pk):
#         collaboration = self.try_except_collaboration(pk)

#         if not collaboration:
#             return Response({'error':'collaboration does not exist.'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = CollaborationRequestSerializer(collaboration, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, pk):
#         collaboration = self.try_except_collaboration(pk)

#         if not collaboration:
#             return Response({'error':'collaboration does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = CollaborationRequestSerializer(collaboration, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         collaboration = self.try_except_collaboration(pk)

#         if not collaboration:
#             return Response({'error':'collaboration does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        
#         collaboration.delete()
#         return Response({'massage':'collaboration delete successfully.'}, status=status.HTTP_404_NOT_FOUND)

