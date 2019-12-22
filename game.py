# -*- coding: utf-8 -*-

# pip install -r requirements.txt
from astrobox.space_field import SpaceField
from astrobox.guns import Projectile
from stage_03_harvesters.driller import DrillerDrone
from stage_03_harvesters.reaper import ReaperDrone
from surkova import SurkovaDrone

NUMBER_OF_DRONES = 5

if __name__ == '__main__':
    scene = SpaceField(
        speed=5,
        field=(1200, 900),
        asteroids_count=20,
    )
    team_1 = [SurkovaDrone() for _ in range(NUMBER_OF_DRONES)]
    team_2 = [DrillerDrone() for _ in range(NUMBER_OF_DRONES)]
    team_3 = [ReaperDrone() for _ in range(NUMBER_OF_DRONES)]

    # TODO - Это зачем здесь?
    # for teamer in team_1:
    #     gunny = Projectile(owner=teamer, speed=5, ttl=100)
    #     for enemy in team_2:
    #         gunny.on_overlap_with(obj_status=enemy)

    scene.go()

# Третий этап: зачёт!
