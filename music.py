import pygame

# Initialize pygame
pygame.init()

# Create a window (not necessary for a basic music player)
# pygame.display.set_mode((800, 600))

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Create a mixer object for audio playback
pygame.mixer.init()

# Load your music file
music_file = "[iSongs.info] 03 - Kushi Title Song (1).mp3"
pygame.mixer.music.load(music_file)
# Play the music
pygame.mixer.music.play()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # You can add controls here, such as pausing, stopping, or changing the volume.

    # Control the frame rate (optional)
    clock.tick(60)

# Quit pygame
pygame.quit()
