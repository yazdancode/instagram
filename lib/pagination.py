from rest_framework.pagination import PageNumberPagination, CursorPagination

# A pagination class for small sets of results
class SmallPageNumberPagination(PageNumberPagination):
    # Default number of items per page is 5
    page_size = 5
    # Clients can set a custom page size using this query parameter (?page_size=10)
    page_size_query_param = 'page_size'
    # Maximum number of items allowed per page is 7
    max_page_size = 7

# A pagination class using cursor pagination for better performance with large datasets
class StandardPageNumberPagination(CursorPagination):
    # Items will be ordered by 'created_time' in descending order
    ordering = '-created_time'

# A pagination class for large sets of results
class LargePageNumberPagination(PageNumberPagination):
    # Default number of items per page is 20
    page_size = 20
    # Clients can set a custom page size using this query parameter (?page_size=20)
    page_size_query_param = 'page_size'
    # Maximum number of items allowed per page is 40
    max_page_size = 40
