from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def hi(request):
    logger.debug('page hi ok')
    return HttpResponse('hi')


def about(request):
    logger.debug('page about ok')
    return HttpResponse('about')

