from django.conf.urls import include, url

from store import views


urlpatterns = [
    #url(r'^createproduct/$', views.ProductCreate.as_view(), name="createproduct"),

    #PRODUCT URL
    url(r'^add/product$', views.ProductAddSet.as_view(), name="add_product"),
    url(r'^products/(?P<product_number>[\w-]+)/get$', views.ProductGet.as_view(), name='product_view_api'),

    #CUSTOMER URL'S
    url(r'^add_customer/$', views.CustomerCreate.as_view(), name="add_customer"),
    url(r'^customer/(?P<customer_number>[\w-]+)/get$', views.GetCustomerDetails.as_view(), name="get_customer_api"),


    url(r'^products/get$', views.ProductGet.as_view(), name="get_product"),
    url(r'^order/add$', views.OrderCreate.as_view(), name="create_order"),

    url(r'^remove/customer/(?P<customer_number>[\w-]+)', views.DeleteCustomer.as_view(), name="delete_customer"),

    # url(r'^orderd_details/get$', views.GetOrderedDetails.as_view(), name="get_all_data"),)
    url(r'^orderd_details/(?P<query_type>\w+)$',views.GetOrderedDetailsCsv.as_view(), name="json_csv_report"),

    #Get Order Details By Id
    url(r'^orderd_details/(?P<order_id>[\w-]+)/get$',views.GetOrderedDetails.as_view(), name="get orderd details by id"),

    #Get By Id
    #url(r'^orderd_details/(?P<query_type>\w+)$',views.GetOrderedDetailsById.as_view()),

    #Min & Max url
    url(r'^orderd_details/aggregate/(?P<query_type>\w+)$',views.AggregateView.as_view(), name="get_Min&Max_price"),

    #summary by date
    url(r'^ordered_summary/get$', views.SummaryReportView.as_view(), name="get_order_summary"),

    #summary csv url
    url(r'^order/summary/csv/report$', views.OrderSummaryReportCsv.as_view(), name="get_order_summary"),

    #Get last 10 orders
    url(r'^last/orders/get$', views.GetLastOrderDetails.as_view(), name="get latest orders"),

    #Vendor
    url(r'^vendor/add$', views.VendorAdd.as_view(), name="create_vendor_data"),
    url(r'^vendor/update/(?P<id>[\w-]+)$', views.VendorUpdate.as_view(), name="update vendors"),

    #vendor details by id
    url(r'^vendor_details/(?P<id>[\w-]+)/get$',views.GetVendorDetails.as_view(), name="get_vendor_details"),

]