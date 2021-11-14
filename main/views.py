from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Stat
from .serializers import StatSerializer, GetStatSerializer


class SaveStatView(APIView):
    serializer_class = StatSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class GetStatView(APIView):
    serializer_class = GetStatSerializer

    def post(self, request, order_by):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        if order_by == 'cost':
            queryset = Stat.objects.filter(date__range=[serializer.data['start'], serializer.data['end']]).order_by('-cost')
        elif order_by == 'clicks':
            queryset = Stat.objects.filter(date__range=[serializer.data['start'], serializer.data['end']]).order_by('-clicks')
        elif order_by == 'views':
            queryset = Stat.objects.filter(date__range=[serializer.data['start'], serializer.data['end']]).order_by('-views')
        else:
            queryset = Stat.objects.filter(date__range=[serializer.data['start'], serializer.data['end']])
        serializer = StatSerializer(queryset, many=True)
        for x in serializer.data:
            try:
                x['cpc'] = round((x['cost'] / x['clicks']), 2)
            except:
                x['Cpc Error'] = 'Недостаточно данных для расчетов.'
            try:
                x['cpm'] = round((x["cost"] / x["views"] * 1000), 2)
            except:
                x['Cpm Error'] = 'Недостаточно данных для расчетов.'
        return Response(serializer.data)


class DeleteStatView(APIView):
    serializer_class = StatSerializer

    def post(self, request):
        Stat.objects.all().delete()
        return Response({"success": "delete"})