from django.shortcuts import render
from dashboard.models import Orders, LegalEntities, Bids, Runs, Users, Comments
import datetime
from calendar import monthrange

# Create your views here.
def index(request):
    month = 7
    year = 2019

    destination_list = [['Жлобин', 'Всеволожск', 166, 27],
                        ['Жлобин', 'Воронеж', 166, 51],
                        ['Жлобин', 'Киров', 166, 26],
                        ['Жлобин', 'Ярославль', 166, 58],
                        ['Воронеж', 'Жлобин', 51, 166],
                        ['Киров', 'Жлобин', 166, 26]
                        ]
    destinations_output = []
    for destination_item in destination_list:

        destination = [destination_item[0], destination_item[1], []]
        (monthrange(year, month))
        num_days = monthrange(year, month)[1]
        for day in range(1, num_days + 1):
            orders = Orders.objects.filter(date_from__year=year, date_from__month=month, date_from__day=day, customer_legal_entity_id=309,
                                           sender_region_id = destination_item[2], recipient_region_id = destination_item[3])
            destination[2].append([])
            for order in orders:
                destination[2][day-1].append(order)


        destinations_output.append(destination)


    return render(request, 'dashboard/index.html', {'destinations': destinations_output})
