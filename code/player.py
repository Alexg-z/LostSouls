import pygame as py
from settings import *
from support import import_folder
from entity import Entity

class Player(Entity):
    def __init__(self,pos,groups,obstacle_sprites,create_attack,destroy_attack,create_magic):
        super().__init__(groups)
        self.image = py.image.load('./graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-26)

        # graphics set up
        self.import_player_assets()
        self.status = 'down'

        self.attaking = False
        self.attack_cooldown = 400
        self.attack_time = None

        self.obstacle_sprites = obstacle_sprites

        # weapon
        self.create_attack = create_attack
        self.destroy_attack = destroy_attack
        self.weapon_index = 0
        self.weapon = list(weapon_data.keys())[self.weapon_index]
        self.can_switch_weapon = True
        self.weapon_switch_time = None
        self.switch_duration_cooldown = 200

        # magic
        self.create_magic = create_magic
        self.magic_index = 0
        self.magic = list(magic_data.keys())[self.magic_index]
        self.can_switch_magic = True
        self.magic_Switch_time = None

        # player stats
        self.stats = {'health': 100,'energy': 60,'attack': 10,'magic': 4,'speed':6}
        self.health = self.stats['health']
        self.energy = self.stats['energy']
        self.exp = 123
        self.speed = self.stats['speed']

    def import_player_assets(self):
        character_path = './graphics/player/'
        self.animations = {'up': [],'down': [],'left': [],'right': [],
            'right_idle': [],'left_idle': [],'up_idle': [],'down_idle': [],
            'right_attack': [],'left_attack': [],'up_attack': [],'down_attack': []}
        
        for animation in self.animations.keys():
            full_path =  character_path + animation
            self.animations[animation] = import_folder(full_path)
        
        # print(self.animations)
    
    def input(self):
        if not self.attaking:
            keys = py.key.get_pressed()

            # Movement input
            if keys[py.K_w]:
                self.direction.y = -1
                self.status = 'up'
            elif keys[py.K_s]:
                self.direction.y = 1
                self.status = 'down'
            else:
                self.direction.y = 0
            if keys[py.K_d]:
                self.direction.x = 1
                self.status = 'right'
            elif keys[py.K_a]:
                self.direction.x = -1
                self.status = 'left'
            else:
                self.direction.x = 0

            # Attack input
            if keys[py.K_SPACE]:
                self.attaking = True
                self.attack_time = py.time.get_ticks()
                self.create_attack()

            # Magic input
            if keys[py.K_LCTRL]:
                self.attaking =  True
                self.attack_time = py.time.get_ticks()
                style = list(magic_data.keys())[self.magic_index]
                strength = list(magic_data.values())[self.magic_index]['strength'] + self.stats['magic']
                cost = list(magic_data.values())[self.magic_index]['cost']
                self.create_magic(style,strength,cost)

            # change weapon
            if keys[py.K_q] and self.can_switch_weapon:
                self.can_switch_weapon = False
                self.weapon_switch_time = py.time.get_ticks()
                if self.weapon_index < len(list(weapon_data.keys())) - 1:
                    self.weapon_index += 1
                else:
                    self.weapon_index = 0

                self.weapon = list(weapon_data.keys())[self.weapon_index]

            # change magic
            if keys[py.K_e] and self.can_switch_magic:
                self.can_switch_magic = False
                self.magic_switch_time = py.time.get_ticks()
                if self.magic_index < len(list(magic_data.keys())) - 1:
                    self.magic_index += 1
                else:
                    self.magic_index = 0

                self.magic = list(weapon_data.keys())[self.magic_index]

    def get_status(self):
        # idle status
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status + '_idle'

        if self.attaking:
            self.direction.x = 0
            self.direction.y = 0
            if not 'attack' in self.status:
                if 'idle' in self.status:
                    #overwrite idle
                    self.status = self.status.replace('_idle','_attack')
                else:
                    self.status = self.status + '_attack'
        else:
            if 'attack' in self.status:
                self.status = self.status.replace('_attack','')
    
    def cooldowns(self):
        current_time = py.time.get_ticks()
        if self.attaking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attaking = False
                self.destroy_attack()

        if not self.can_switch_weapon:
            if current_time - self.weapon_switch_time >= self.switch_duration_cooldown:
                self.can_switch_weapon = True

        if not self.can_switch_magic:
            if current_time - self.magic_switch_time >= self.switch_duration_cooldown:
                self.can_switch_magic = True

    def animate(self):
        animation = self.animations[self.status]

        # lopp the frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        # set image
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def update(self):
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.move(self.speed)