"""Apply the profile's existing terminal palette to gh-space-shooter 2.0.5."""
from gh_space_shooter.game.render_context import RenderContext
from gh_space_shooter.cli import app


def terminal_theme():
    return RenderContext(
        cell_size=12, cell_spacing=3, padding=40,
        background_color=(8, 8, 16), grid_color=(28, 20, 40),
        enemy_colors={
            1: (168, 85, 247), 2: (236, 72, 153),
            3: (249, 115, 22), 4: (250, 204, 21),
        },
        ship_color=(192, 132, 252), bullet_color=(250, 204, 21),
    )


RenderContext.darkmode = staticmethod(terminal_theme)
if __name__ == '__main__':
    app()
