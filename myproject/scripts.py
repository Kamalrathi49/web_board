from boards.models import Board, Topic
from django.contrib.auth.models import User

board_list = [{
  "name": "Mitsubishi",
  "description": "Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec pharetra, magna vestibulum aliquet ultrices, erat tortor sollicitudin mi, sit amet lobortis sapien sapien non mi. Integer ac neque."
}, {
  "name": "Pontiacw",
  "description": "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Proin risus. Praesent lectus."
}, {
  "name": "Pontiac",
  "description": "Proin eu mi. Nulla ac enim. In tempor, turpis nec euismod scelerisque, quam turpis adipiscing lorem, vitae mattis nibh ligula nec sem."
}, {
  "name": "Lexus",
  "description": "Pellentesque at nulla. Suspendisse potenti. Cras in purus eu magna vulputate luctus."
}, {
  "name": "Dodge",
  "description": "Cras non velit nec nisi vulputate nonummy. Maecenas tincidunt lacus at velit. Vivamus vel nulla eget eros elementum pellentesque."
}]


for item in board_list:
    board = Board.objects.create(
      name=item['name'], 
      description=item['description']
    )
    board.save()

#python manage.py shell