from manim import *


class LinearTransformation2D(Scene):
    def construct(self):
        grid = NumberPlane(
            x_range=(-15, 15, 1),
            y_range=(-10, 10, 1),
            background_line_style={'stroke_opacity': 0.4}
        )
        self.add(grid)
        self.wait(1)

        transformation_matrix = [
            [1, 1],
            [0, 1]
        ]
        self.play(ApplyMatrix(transformation_matrix, grid))
        self.wait(2)


class FunctionsOnAxes(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-3, 3],
            y_range=[-3, 3],
            axis_config={'include_tip': True, 'include_numbers': True}
        )
        self.add(axes)

        func = axes.plot(lambda x: x ** 2, color=BLUE)
        self.play(Create(func))
        self.wait(2)

        func2 = axes.plot(lambda x: x ** 3, color=RED)
        self.play(ReplacementTransform(func, func2))
        self.wait(2)


class CameraRotation3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)

        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(5)
        self.stop_ambient_camera_rotation()


class LinearTransformation3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)

        grid_lines = VGroup()
        for x in np.linspace(-2, 2, 9):
            for y in np.linspace(-2, 2, 3):
                grid_lines.add(Line([x, y, -2], [x, y, 2], color=BLUE, stroke_opacity=0.2))
            for z in np.linspace(-2, 2, 9):
                grid_lines.add(Line([x, -2, z], [x, 2, z], color=BLUE, stroke_opacity=0.2))
        for y in np.linspace(-2, 2, 9):
            for z in np.linspace(-2, 2, 9):
                grid_lines.add(Line([-2, y, z], [2, y, z], color=BLUE, stroke_opacity=0.2))

        self.add(grid_lines)

        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        transformation_matrix = np.array([
            [1, 0, 0],
            [0, 2, 0],
            [0, 0, 3]
        ])

        self.begin_ambient_camera_rotation(rate=0.2)
        self.play(ApplyPointwiseFunction(lambda point: transformation_matrix @ point, grid_lines))
        self.wait(5)

        self.stop_ambient_camera_rotation()
