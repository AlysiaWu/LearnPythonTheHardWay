'''
Author: Zhu Xiuwei
Date: 2014-4-22
'''

class Scene(object):
	def enter(self):
		pass
		
class Engine(object):
	def __init__(self, scene_map):
		self.scene_map = scene_map
	
	def play(self):
		self.scene_map.opening_scene()
		
class Death(Scene):
	def enter(self):
		pass

class CentralCorridor(Scene):
	def enter(self):
		print "You are at central_corridor now."
		return "next"
		
class LaserWeaponArmory(Scene):
	def enter(self):
		print "You are at laser_weapon_armory now."
		return "next"

class TheBridge(Scene):
	def enter(self):
		print "You are at the_bridge now."
		return "next"
		
class EscapePod(Scene):
	def enter(self):
		print "You are at escape_pod now. Congratulations!"
		return "done"
		
class Map(object):
	def __init__(self, start_scene):
		self.sceneMap = {
			'CentralCorridor': CentralCorridor,
			'LaserWeaponArmory': LaserWeaponArmory,
			'TheBridge': TheBridge,
			'EscapePod': EscapePod
		}
		self.next_scene_map = {
			'CentralCorridor': LaserWeaponArmory,
			'LaserWeaponArmory': TheBridge,
			'TheBridge': EscapePod
		}
		self.sceneName = start_scene
		self.scene = self.sceneMap.get(start_scene)()
	
	def next_scene(self, scene_name):
		nextScene = self.next_scene_map.get(scene_name)()
		
		#Update sceneName attribute.
		nextSceneName = nextScene.__class__.__name__
		
		print "Player go to next scene. Current scene: ", scene_name, ', Next scene: ', nextSceneName
		result = nextScene.enter()
		if(result == 'next'):
			self.next_scene(nextSceneName)
		elif(result == 'done'):
			print('you pass the game!')
			exit(0)
		
	def opening_scene(self):
		result = self.scene.enter()	
		if(result == 'next'):
			self.next_scene(self.sceneName)
		else:
			pass
		
a_map = Map('CentralCorridor')
a_game = Engine(a_map)
a_game.play()