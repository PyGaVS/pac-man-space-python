class Animation():
    def __init__(self, frames):
        # Index de la texture actuelle
        self.current = 0

        # Temps écoulé depuis le dernier changement de frame
        self.last = 0.0

        # Durée entre les frames (en secondes)
        self.frame_duration = 0.1  # 10 FPS

        self.frames = frames

    def update(self, dt: float):
        self.last += dt
        
        if self.last >= self.frame_duration:
            self.last = 0.0
            self.current = (self.current + 1) % len(self.frames)

            return self.frames[self.current]
        else:
            return False
