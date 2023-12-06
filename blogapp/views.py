from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import BlogModel
from .serializers import BlogSerializer
from django.db.models import Q
# Create your views here.

class BlogApiView(APIView):

    def post(self,request):
        try:
            data = request.data
            serializer = BlogSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                error = False
                status = 200
                msg = "Blog Saved Successfully."
                data = serializer.data
            
            else:
                error = True
                status = 400
                msg = serializer.errors
                data = None
        except Exception as e:
            error = True
            status = 400
            msg = e.args[0]
            data = None

        return Response({
            "error" : error,
            "status" : status,
            "message" : msg,
            "data" : data
            })
    

    def get(self,request):
        
        try:
            id = request.GET.get("id")
            blogObj = BlogModel.objects.filter(is_deleted=False).order_by("-created_at")
            if id:
                blogObj = blogObj.filter(id=id)
            serilizer = BlogSerializer(blogObj,many=True)
            if len(blogObj) == 0:
                mes = "Blog Does Not Exists."
                blog_data = None
            else:
                mes = "Blog Fetch Successfully."
                blog_data = serilizer.data

            error = False
            status = 200
            msg = mes
            data = blog_data
        except Exception as e:
            error = True
            status = 400
            msg = e.args[0]
            data = None
        return Response({
            "error" : error,
            "status" : status,
            "message" : msg,
            "data" : data
        })
    
    def patch(self,request):
        try:
            id = request.GET.get("id")
            blogObj = BlogModel.objects.get(Q(id=id) & Q(is_deleted=False))
            serializer = BlogSerializer(blogObj,data=request.data,partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                error = False
                status = 200
                msg = "Blog Updated Successfully."
                data = serializer.data
            
            else:
                error = True
                status = 400
                msg = serializer.errors
                data = None
        except Exception as e:
            error = True
            status = 400
            msg = e.args[0]
            data = None

        return Response({
            "error" : error,
            "status" : status,
            "message" : msg,
            "data" : data
            })

    def delete(self,request):
        try:
            id = request.GET.get("id")
            blogObj = BlogModel.objects.get(Q(id=id) & Q(is_deleted=False))
            if blogObj:
                blogObj.is_deleted = True
                blogObj.save()
                error = False
                status = 200
                msg = "Blog Deleted Successfully."

            else:
                error = False
                status = 200
                msg = "Blog Doesn't Exist."
        except Exception as e:
            error = True
            status = 400
            msg = e.args[0]

        return Response({
            "error" : error,
            "status" : status,
            "message" : msg,
            "data" : None
            })