from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PagePageListPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'limit'

    def get_paginated_response(self, data):

        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'result': data,
            'status': True,
            'pages_count': self.page.paginator.num_pages,
            'objects_count': len(data)
        })
