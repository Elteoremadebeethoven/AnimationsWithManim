class Dragon(MovingCameraScene):
    CONFIG = {
        "iterations":10,
    }
    def construct(self):
        path = VGroup()
        first_line = Line(ORIGIN,UP / 5)
        path.add(first_line)

        self.camera_frame.set_height(first_line.get_height() * 1.2)
        self.camera_frame.move_to(first_line)
        self.play(ShowCreation(first_line))

        self.target_path = self.get_all_paths(path,self.iterations)
        for i in range(self.iterations):
            self.duplicate_path(path,i)
        self.wait()

    def duplicate_path(self,path,i):
        set_paths = self.target_path[:2**(i + 1)]
        height = set_paths.get_height() * 1.1
        new_path = path.copy()
        self.add(new_path)
        point = self.get_last_point(path)
        self.play(
            Rotating(
                new_path,
                radians=PI/2,
                about_point=path[-1].points[point],
                rate_func=linear
                ),
            self.camera_frame.move_to,set_paths,
            self.camera_frame.set_height,height,
            run_time=1, rate_func=smooth
            )
        post_path = reversed([*new_path])
        path.add(*post_path)

    def get_all_paths(self, path, iterations):
        target_path = path.copy()
        for _ in range(iterations):
            new_path = target_path.copy()
            point = self.get_last_point(new_path)
            new_path.rotate(
                        PI/2, 
                        about_point=target_path[-1].points[point],
                    )
            post_path = reversed([*new_path])
            target_path.add(*post_path)

        return target_path

    def get_last_point(self, path):
        return 0 if len(path) > 1 else -1
