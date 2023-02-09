from rest_framework import viewsets

class ProductViewSet(viewsetsViewSet):
	"""This view class implements the crud operations"""
	def list(self, request): #api/products
		pass

	def create(self, request): #api/products
		pass

	def retrieve(self, request, pk=None): #api/products/<str:id>
		pass

	def update(self, request, pk=None): #api/products/<str:id>
		pass

	def delete(self, request, pk=None): #api/products/<str:id>
		pass


