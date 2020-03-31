from direct.showbase import DirectObject
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import LineSegs, NodePath
from numpy import append
from math import pi, sin, cos



class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.disableMouse()
        self.scene = self.loader.loadModel("models/zup-axis")
        #self.scene = self.loader.loadModel("models/environment")
        self.scene.reparentTo(self.render)
        self.scene.setScale(0.1)
        self.scene.setPos(0, 0, 0)
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

    def spinCameraTask(self, task):
        angleDegrees = task.time * 26.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0,0)
        #print(self.camera.getHpr())
        return Task.cont






class Hello(DirectObject.DirectObject):
    def __init__(self):
        self.accept("mouse1", self.printHello)

    def printHello(self):
        x = base.mouseWatcherNode.getMouseX()
        y = base.mouseWatcherNode.getMouseY()
        # lines = LineSegs()
        # lines.moveTo(x/0.1, 0, y/0.1)
        # lines.drawTo(x/0.1, -4, y/0.1)
        # lines.setThickness(4)
        # node = lines.create()
        # np = NodePath(node)
        # np.reparentTo(render)
        print(append(x/0.1, y/0.1))

app = MyApp()
h = Hello()
app.run()
