class Dragon(MovingCameraScene):
    CONFIG = {
        "iterations":14,
    }
    def construct(self):
        path = VGroup()
        first_line = Line(ORIGIN,UP/5)
        self.camera_frame.set_height(first_line.get_height()*1.2)
        self.camera_frame.move_to(first_line)
        self.play(ShowCreation(first_line))
        path.add(first_line)

        self.target_path,self.target_points = self.get_all_paths(path,self.iterations)

        for i in range(self.iterations):
            self.duplicate_path(path,i)
        self.wait()

    def duplicate_path(self,path,i):
        height = self.target_path[:2**(i+1)].get_height()*1.1
        new_path = path.copy()
        self.add(new_path)
        if len(path)>1:
            point = 0
        else: 
            point = -1
        self.play(
            Rotating(new_path,radians=PI/2,about_point=path[-1].points[point]
                ),
            self.camera_frame.move_to,self.target_points[i],
            self.camera_frame.set_height,height,
            run_time=1,rate_func=linear
            )
        post_path = reversed([*new_path])
        path.add(*post_path)

    def get_all_paths(self,path,iterations):
        target_path = path.copy()
        fractal = []
        points = []
        for _ in range(iterations):
            new_path = target_path.copy()
            if len(target_path)>1:
                point = 0
            else: 
                point = -1
            new_path.rotate(PI/2,about_point=target_path[-1].points[point],
                about_edge=target_path[-1].points[point])
            post_path = reversed([*new_path])
            target_path.add(*post_path)
            points.append(target_path.get_center())

        return target_path,points
