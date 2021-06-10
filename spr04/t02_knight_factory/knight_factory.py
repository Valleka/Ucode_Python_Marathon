import generator as g

g.logger.info("Package __init__ executed.")

if __name__ == '__main__':
    for i in range(1, 6):
        g.logger.info("[Name chosen.]")
        g.logger.info("[Title chosen.]")
        g.logger.info("Sir " + g.names() + " the " + g.titles())
