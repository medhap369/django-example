from django.conf.urls import url
from views.product import add, list, edit, del_product, index

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^add', add),
    url(r'^', list),
    url(r'^edit', edit),
    url(r'^del', del_product),
]