import 'package:flame/game.dart';
import 'package:flutter/material.dart';
import 'package:flame/components.dart';
import 'package:flame/input.dart';

void main() {
  runApp(GameWidget(game: BrickBreakerGame()));
}

class BrickBreakerGame extends FlameGame with HasCollidables, HasDraggables {
  late Paddle playerPaddle;
  late Paddle aiPaddle;
  late Ball ball;

  @override
  Future<void> onLoad() async {
    super.onLoad();

    // 플레이어 패들
    playerPaddle = Paddle(Vector2(size.x / 2 - 50, size.y - 30), isAI: false);
    add(playerPaddle);

    // AI 패들
    aiPaddle = Paddle(Vector2(size.x / 2 - 50, 10), isAI: true);
    add(aiPaddle);

    // 공
    ball = Ball(Vector2(size.x / 2, size.y / 2));
    add(ball);
  }

  @override
  void update(double dt) {
    super.update(dt);
    aiPaddle.aiMove(ball);
  }
}

class Paddle extends SpriteComponent with Draggable {
  bool isAI;
  Paddle(Vector2 position, {required this.isAI}) : super(position: position, size: Vector2(100, 20));

  @override
  bool onDragUpdate(int pointerId, DragUpdateInfo event) {
    if (!isAI) {
      position.add(event.delta);
      position.x = position.x.clamp(0, gameRef.size.x - size.x);
    }
    return true;
  }

  void aiMove(Ball ball) {
    if (isAI) {
      // AI 패들 움직임 로직
      if (ball.position.x > position.x + size.x / 2) {
        position.x += 200 * gameRef.dt;
      } else if (ball.position.x < position.x + size.x / 2) {
        position.x -= 200 * gameRef.dt;
      }
      position.x = position.x.clamp(0, gameRef.size.x - size.x);
    }
  }
}

class Ball extends SpriteComponent {
  Vector2 velocity = Vector2(150, 150);

  Ball(Vector2 position) : super(position: position, size: Vector2(20, 20));

  @override
  void update(double dt) {
    super.update(dt);
    position += velocity * dt;

    // 화면 가장자리 충돌
    if (position.x <= 0 || position.x + size.x >= gameRef.size.x) {
      velocity.x = -velocity.x;
    }

    // 위 아래 충돌
    if (position.y <= 0 || position.y + size.y >= gameRef.size.y) {
      velocity.y = -velocity.y;
    }

    // 패들과 충돌
    gameRef.children.whereType<Paddle>().forEach((paddle) {
      if (paddle.toRect().overlaps(toRect())) {
        velocity.y = -velocity.y;
      }
    });
  }
}
