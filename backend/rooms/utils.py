from rooms.models import Room, User


def create_room(name: str, password: str, slots: int, host: User) -> Room:
    Room.objects.create(name=name, password=password, slots=slots, host=host)
