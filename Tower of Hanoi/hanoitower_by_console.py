

def moveDisk(diskIndex, fromPole, toPole):
	print_str = 'Move disk %s form %s to %s' % (diskIndex, fromPole, toPole)
	print(print_str)


def moveTower(height, fromPole, withPole, toPole):
	if height == 1 :
		moveDisk(1, fromPole, toPole)
	else:
		moveTower(height-1, fromPole, toPole, withPole)
		moveDisk(height, fromPole, toPole)
		moveTower(height-1, withPole, fromPole, toPole)


if __name__ == '__main__':
	moveTower(3, "A", "B", "C")
