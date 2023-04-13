import pygame as py
py.init()
font = py.font.Font(None,30)

def debug(info,y = 10, x = 10):
	display_surface = py.display.get_surface()
	debug_surf = font.render(str(info),True,'White')
	debug_rect = debug_surf.get_rect(topleft = (x,y))
	py.draw.rect(display_surface,'Black',debug_rect)
	display_surface.blit(debug_surf,debug_rect)
