
from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='hz1gsy$i$tvn2=e$5$!qi2qfkdqvne#4b85-b#qe$f(&a)pnpo')

DEBUG = env.bool('DJANGO_DEBUG', default=True)
