import pygame
import sys

# 게임 설정
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 120, 20
BALL_RADIUS = 10
BRICK_WIDTH, BRICK_HEIGHT = 80, 30
PADDLE_SPEED = 10
BALL_SPEED_X, BALL_SPEED_Y = 7, 7

# 색깔
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 벽돌 클래스
class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((BRICK_WIDTH, BRICK_HEIGHT))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(topleft=(x, y))

# 공 클래스
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((BALL_RADIUS*2, BALL_RADIUS*2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, RED, (BALL_RADIUS, BALL_RADIUS), BALL_RADIUS)
        self.rect = self.image.get_rect(center=(WIDTH//2, HEIGHT//2))
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # 화면 경계 충돌 체크
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed_x *= -1
        if self.rect.top <= 0:
            self.speed_y *= -1

# 패들 클래스
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(topleft=(WIDTH//2 - PADDLE_WIDTH//2, HEIGHT - 50))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= PADDLE_SPEED
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += PADDLE_SPEED

# 게임 초기화
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("벽돌깨기 게임")
clock = pygame.time.Clock()

# 스프라이트 그룹 설정
all_sprites = pygame.sprite.Group()
bricks = pygame.sprite.Group()

# 벽돌 생성
for row in range(5):
    for column in range(10):
        brick = Brick(column * (BRICK_WIDTH + 2) + 30, row * (BRICK_HEIGHT + 2) + 50)
        bricks.add(brick)
        all_sprites.add(brick)

# 공과 패들 생성
ball = Ball()
paddle = Paddle()
all_sprites.add(ball, paddle)

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 충돌 체크
    hits = pygame.sprite.spritecollide(ball, bricks, True)
    if hits:
        ball.speed_y *= -1

    if pygame.sprite.collide_rect(ball, paddle):
        ball.speed_y *= -1

    # 게임 로직 업데이트
    all_sprites.update()

    # 화면 그리기
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()