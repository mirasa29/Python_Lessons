from os import walk
from me import life, know, be
from recover import dust_off, reflect

class LiveError(Exception):
	"""
	Life goes on. Pick yourself up!
	"""

def run_life(myself, not_me, direction="forward"):
	
	all_paths = walk(life.paths)

	for path in all_paths:
		if not_me:
			if path.attributes in not_me:
			continue
			
		try:
			be.always(myself, mode="strict")
		except be.RuntimeError:
			dust_off.lick_wounds(mode="all")
			reflect(scope="all") 
			raise LiveError()
			
			
if __name__ == "__main__":

	myself = know.who(True)
	not_me = know.who(False)
	
	for moment in len(life.all):
		run_life(myself, not_me)
		
	