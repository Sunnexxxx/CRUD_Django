from django.shortcuts import render
from .models import Burger


def create_new_dict(local_data):
    insert_data = {}
    names = ['meat', 'chicken', 'cheese', 'tomato']
    for i in names:
        try:
            if local_data[i] == 'on':
                insert_data[i] = True
        except:
            insert_data[i] = False
    insert_data['name'] = local_data['name'] if local_data['name'] else False
    insert_data['price'] = int(local_data['price']) if local_data['price'] else False
    return insert_data


def insert_values(local_data):
    Burger.objects.create(
        name=local_data['name'],
        meat=local_data['meat'],
        chicken=local_data['chicken'],
        cheese=local_data['cheese'],
        tomato=local_data['tomato'],
        price=local_data['price']
    )


def update_page(request):
    local_data = request.GET
    if local_data:
        object = Burger.objects.get(id=local_data['update'])
        data = {'name': object.name, 'meat': object.meat, 'chicken': object.chicken, 'cheese': object.cheese,
                'tomato': object.tomato, 'price': object.price, 'id': local_data['update']}

    return render(request, 'main/index_dump.html', {'data': data})


def main_page(request):
    return render(request, 'main/index_main.html')


def side_page(request):
    if request.GET:
        try:
            local_data = create_new_dict(request.GET)
        except:
            pass
        else:
            if local_data['name'] and local_data['price']:
                insert_values(local_data)

        try:
            Burger.objects.filter(id=request.GET['delete']).delete()
        except:
            pass

        if 're_name' in request.GET:
            update_data = request.GET
            new_update_data = {}
            names = ['re_meat', 're_chicken', 're_cheese', 're_tomato']
            for i in names:
                if i in update_data:
                    new_update_data[i] = True
                else:
                    new_update_data[i] = False
            new_update_data['re_name'] = update_data['re_name']
            new_update_data['re_price'] = update_data['re_price']

            print(12312313, new_update_data)

            Burger.objects.filter(id=request.GET['id']).update(name=new_update_data['re_name'],
                                                               meat=new_update_data['re_meat'],
                                                               chicken=new_update_data['re_chicken'],
                                                               cheese=new_update_data['re_cheese'],
                                                               tomato=new_update_data['re_tomato'],
                                                               price=new_update_data['re_price'])

    data = Burger.objects.all()

    return render(request, 'main/index_side.html', {'data': data})
