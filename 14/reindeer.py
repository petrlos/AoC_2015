class Reindeer:

    def __init__(self, name, speed, time, rest):
        self.name = name
        self.speed = int(speed)
        self.time = int(time)
        self.rest = int(rest)
        self.distance = 0
        self.points = 0

    def __str__(self):
        return "{0}: {1}km, {2} points".format(self.name, self.position, self.points)

    def getDistanceInTime(self, time):
        completeCycles = int (time / (self.time + self.rest))
        restTime = time % (self.time + self.rest)
        if self.time < restTime:
            restTimeFlying = self.time
        else:
            restTimeFlying = restTime
        return completeCycles * self.time * self.speed + restTimeFlying * self.speed