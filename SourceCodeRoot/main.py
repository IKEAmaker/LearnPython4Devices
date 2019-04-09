#################################################################################
#                                                                               #
# Select which project to load by setting project to a number between 3 and 10 #
#                                                                               #
#################################################################################

project = 6

#################################################################################
#
#  Nothing to see below :-)
#

import sys

loadingSource = "/solutions"
sys.path.insert(0, loadingSource)
print('loading project')
print(project)

if project < 4:
    import kit

elif project < 5:
    import Blink_4

elif project < 6:
    import LightsOn_5

elif project < 7:
    import ScrollSomeText_6

elif project < 8:
    import ControlTheScroll_7

elif project < 9:
    import MoveTheDotAround_8

elif project < 10:
    import LimitTheMovement_9

elif project < 11:
    import PaintSomeYellow_10