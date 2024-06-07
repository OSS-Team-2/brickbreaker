import 'package:flame/game.dart';
import 'package:flame/components.dart';
import 'package:flame/events.dart';
import 'package:flame/collisions.dart';
import 'components/ball.dart';
import 'components/bat.dart';
import 'components/brick.dart';
import 'components/game_area.dart';

enum PlayState {
  playing,
  paused,
  gameOver,
  gameWon,
}

class BrickBreaker extends FlameGame with HasCollisionDetection {
  List<Ball> balls = [];
  PlayState playState = PlayState.playing;

  @override
  Future<void> onLoad() async {
    super.onLoad();
    // 게임 영역과 첫 공을 생성
    add(GameArea());
    add(Bat(
      cornerRadius: Radius.circular(10),
      position: Vector2(size.x / 2, size.y - 50),
      size: Vector2(100, 20),
    ));
    spawnBall();
  }

  void spawnBall() {
    if (playState == PlayState.playing) {
      final ball = Ball(
        velocity: Vector2(200, -200),
        position: Vector2(size.x / 2, size.y / 2),
        radius: 10,
        difficultyModifier: 1.1,
      );
      balls.add(ball);
      add(ball);
    }
  }

  void removeBall(Ball ball) {
    balls.remove(ball);
    ball.removeFromParent();
    if (balls.isEmpty) {
      playState = PlayState.gameOver;
    }
  }

  void addBall() {
    spawnBall();
  }

  int getBallCount() {
    return balls.length;
  }

  void resetGame() {
    playState = PlayState.playing;
    removeAll(balls);
    balls.clear();
    spawnBall();
  }
}