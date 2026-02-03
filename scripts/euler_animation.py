from manim import *
import numpy as np

class EulerMethod(Scene):
    def construct(self):
        # 1. Setup Axes - Numbers removed for a cleaner look
        axes = Axes(
            x_range=[0, 2.5, 0.5],
            y_range=[0, 6, 1],
            x_length=9,
            y_length=6,
            axis_config={"include_ticks": False} # Ticks remain, but numbers are gone
        )
        labels = axes.get_axis_labels(x_label="t", y_label="X_t")
        
        self.play(Create(axes), Write(labels))

        # 2. The True Curve
        graph = axes.plot(lambda t: np.exp(t), color=BLUE, x_range=[0, 1.8], stroke_opacity=0.4)
        graph_label = MathTex("X_t", color=BLUE).next_to(graph, UR, buff=0.1)
        self.play(Create(graph), Write(graph_label))

        # 3. Euler Parameters
        t_val, x_val = 0, 1
        h = 0.7 
        steps = 2

        for i in range(steps):
            slope = x_val
            next_t, next_x = t_val + h, x_val + h * slope
            
            curr_dot = Dot(axes.c2p(t_val, x_val), color=YELLOW)
            curr_lbl = MathTex("X_t").next_to(curr_dot, UL, buff=0.15)
            
            # Guide line (tangent)
            guide_line = Line(
                axes.c2p(t_val - 0.1, x_val - 0.1 * slope),
                axes.c2p(next_t + 0.3, x_val + (h + 0.3) * slope),
                color=WHITE, stroke_opacity=0.2
            )
            
            # Label u_t(X_t) at the Top-Right of the tangent guide
            slope_lbl = MathTex("u_t(X_t)", color=WHITE, font_size=36).next_to(guide_line.get_end(), UR, buff=0.1)

            step_path = Line(
                axes.c2p(t_val, x_val), 
                axes.c2p(next_t, next_x), 
                color=RED, stroke_width=6
            )

            next_dot = Dot(axes.c2p(next_t, next_x), color=RED)
            next_lbl = MathTex("X_{t+h}").next_to(next_dot, DR, buff=0.15)

            brace_h = BraceBetweenPoints(axes.c2p(t_val, x_val), axes.c2p(next_t, x_val), DOWN)
            label_h = brace_h.get_text("$h$")

            # Animation Sequence
            self.play(FadeIn(curr_dot), Write(curr_lbl))
            self.play(Create(guide_line), Write(slope_lbl))
            self.play(Create(step_path), Create(brace_h), Write(label_h), run_time=1.2)
            self.play(FadeIn(next_dot), Write(next_lbl))
            self.wait(1)

            # Cleanup
            self.play(
                FadeOut(curr_lbl, next_lbl, guide_line, slope_lbl, brace_h, label_h),
                curr_dot.animate.set_opacity(0.5)
            )

            t_val, x_val = next_t, next_x

        # 4. Final Error Visualization
        actual_x = np.exp(t_val)
        actual_point = axes.c2p(t_val, actual_x)
        estimated_point = axes.c2p(t_val, x_val)

        error_line = DashedLine(estimated_point, actual_point, color=YELLOW)
        error_label = Tex("error", color=WHITE, font_size=36).next_to(error_line, RIGHT, buff=0.2)
        true_dot_final = Dot(actual_point, color=BLUE)

        # Immediate appearance and quick exit
        self.add(error_line, true_dot_final, error_label)
        self.wait(1.5)