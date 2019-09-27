from products.models import TransactionHeader, TransactionDetail
import datetime

def run():
    # Fetch all questions
    
    #TransactionDetail.objects.all().delete()
    TransactionHeader.objects.all().delete()
    # Delete one product from databaset
    ths = TransactionHeader.objects.all()
    #tds = TransactionDetail.objects.all()
    
    # creating headers 
    ths.create(transac_header_date = datetime.date(year=2020, month=9, day=11), transac_header_name = "automated transaction header 1", transac_header_total_amount = 123.23)
    ths.create(transac_header_date = datetime.date(year=2021, month=10, day=12), transac_header_name = "automated transaction header 2", transac_header_total_amount = 123.23)
    ths.create(transac_header_date = datetime.date(year=2022, month=11, day=14), transac_header_name = "automated transaction header 3", transac_header_total_amount = 123.23)
    ths.create(transac_header_date = datetime.date(year=2019, month=12, day=15), transac_header_name = "automated transaction header 4", transac_header_total_amount = 123.23)

    for item in ths:
        item.save()

    # # creating details
    # tds.create(title = "automated test case 1", description = "test case added from created_transactions_dataset script", price = 123.23, summary = "avoiding leaving this field blank")
    # tds.create(title = "automated test case 2", description = "test case added from created_transactions_dataset script", price = 124.23, summary = "avoiding leaving this field blank")
    # tds.create(title = "automated test case 3", description = "test case added from created_transactions_dataset script", price = 125.23, summary = "avoiding leaving this field blank")
    # tds.create(title = "automated test case 4", description = "test case added from created_transactions_dataset script", price = 126.23, summary = "avoiding leaving this field blank")
    # for item2 in ths:
    #     item2.save()

    