# -*- coding: utf-8 -*-

# pip install -r requirements.txt
from astrobox.space_field import SpaceField
from stage_03_harvesters.driller import DrillerDrone
from stage_03_harvesters.reaper import ReaperDrone
from devastator import DevastatorDrone
from surkova import SurkovaDrone

NUMBER_OF_DRONES = 5


class Dev2(DevastatorDrone):
    pass


class Dev3(DevastatorDrone):
    pass


if __name__ == '__main__':
    scene = SpaceField(
        field=(1200, 600),
        speed=3,
        asteroids_count=15,
        can_fight=True,
    )
    team_1 = [SurkovaDrone() for _ in range(NUMBER_OF_DRONES)]
    team_2 = [Dev3() for _ in range(NUMBER_OF_DRONES)]
    # team_3 = [Dev2() for _ in range(NUMBER_OF_DRONES)]
    team_4 = [DevastatorDrone() for _ in range(NUMBER_OF_DRONES)]

    scene.go()
