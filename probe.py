# -*- coding: utf-8 -*-

# pip install -r requirements.txt
from astrobox.space_field import SpaceField
from astrobox.guns import Gun, Projectile, PlasmaProjectile
from stage_03_harvesters.driller import DrillerDrone
from surkova import SurkovaDrone
from robogame_engine.theme import Theme

NUMBER_OF_DRONES = 5

if __name__ == '__main__':
    scene = SpaceField(
        speed=5,
        field=(1200, 600),
        asteroids_count=20,
        can_fight=True,
    )
    team_1 = [SurkovaDrone() for _ in range(NUMBER_OF_DRONES)]
    # TODO и побороть противников!
    team_2 = [DrillerDrone() for _ in range(NUMBER_OF_DRONES)]
    for teamer in team_1:
        shell = Projectile(owner=teamer, coord=teamer.coord, speed=5, ttl=100)
        shell.on_born()
        gunny = Gun(owner=teamer)
        gunny.projectile = shell
        print(type(gunny.projectile))
        for enemy in team_2:
            gunny.shot(target=enemy)
    scene.go()



