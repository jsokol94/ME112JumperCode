# ME112JumperCode

This contains all of the python programs we have written as a team to design our final project.

Written by:
_Jean-Christophe Perrin, Alejandro Ballestros, Jan Sokol, and Frederick Tan_

____
## Project Overview
From the project description:

> Design, prototype and test a small robot that jumps upwards using legs that move like those of a mynock (or an Earth frog) and sticks to the underside of a spaceship.

* Your bio-inspired jumping robot should leap upwards, preferably at least one meter (a typical hull height), and stick to the underside of the faux Falcon (provided). The final product will use adhesion of some kind, but at this prototyping stage we’ll use Velcro. The hull will be covered with the loop side and you will be provided with strips of the hook side.
* The robot should jump within 5 seconds of being activated, preventing a first-strike by wild mynocks.
* After the robot is turned on, it should operate autonomously, including initiating the jump. It is allowed to continue to try to jump, periodically, once it has attached to the ship, if desired. (In practice we’ll detach it before the next 5 seconds is up.)
* The robot will be powered by batteries. There are no constraints on electrical energy use, per se.
* The external appearance of the robot, and particularly the motions of its legs, should resemble
those of a mynock, approximated by those of an Earth frog such as  Rana temporaria .

____
## Included Scripts

### LinkageUtilities.py
This is a set of python functions written by our professor (Dr. Mark Cutkosky)
to help compute the geometry of a linkage as it moves through space.

Contents:
* arcpoints(): Compute points in an arc.
* coupler(): Given 2 points and an angle and distance, compute the third point.
* circcirc(): Compute intersection of two circles.
* grashof(): Check if 4-bar linkage satisfies Grashof criterion (continuous rotation)
* joints2links(): Given a sequence of joint locations, return array of Link lengths

Created Sep  8 2015.
@author: markcutkosky
