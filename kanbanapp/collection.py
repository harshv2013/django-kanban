from .models import Collection

def creat_collection(res_obj):
    id = res_obj.id
    owner_id = res_obj.owner_id
    Collection.objects.create(**{"name":"BACKLOG","board_id":id, "owner_id":owner_id})
    Collection.objects.create(**{"name":"TODO","board_id":id, "owner_id":owner_id})
    Collection.objects.create(**{"name":"DOING","board_id":id, "owner_id":owner_id})
    Collection.objects.create(**{"name":"TESTING","board_id":id, "owner_id":owner_id})
    Collection.objects.create(**{"name":"DONE","board_id":id, "owner_id":owner_id})
    
    return {"message":"Collections created successfully"}

