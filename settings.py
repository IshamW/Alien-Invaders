class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship Settings
        self.ship_speed = 2
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 3
        self.bullet_width = 20000
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Alien Settings
        self.fleet_drop_speed = 50

        # How quickly the game speeds up
        self.speedup_scale = 1

        # How quickly the alien point values increase
        self.score_scale = 2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_limit = 3
        self.bullet_speed = 3
        self.alien_speed = 1

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
