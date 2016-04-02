#
## python --version -> Python 2.7.10
#

road_start_points = []
road_end_points = []



tmp = int(raw_input().strip())

while tmp >= 0:
  line = raw_input().strip().split(' ')
  road_start_points.append(int(line[0]))
  road_end_points.append(int(line[1]))

  tmp -= 1

counter = 0
last_direction = ''
for idx, val in enumerate(road_start_points):

  direction = ''

  if idx != len(road_start_points) - 1:
    if val == road_start_points[idx + 1]:
      if road_end_points[idx] > road_end_points[idx + 1]:
        direction = 'down'
      else:
        direction = 'up'
    else:
      if val > road_start_points[idx + 1]:
        direction = 'left'
      else:
        direction = 'right'

  if not last_direction:
    last_direction = direction
    continue

  if last_direction and direction:
    if direction is 'up':
      if last_direction is 'right':
        counter += 1

    elif direction is 'down':
      if last_direction is 'left':
        counter += 1

    elif direction is 'left':
      if last_direction is 'up':
        counter += 1

    elif direction is 'right':
      if last_direction is 'down':
        counter += 1

    last_direction = direction

print counter


