import 'dart:async';
import 'package:flame/collisions.dart';
import 'package:flame/components.dart';
import '../brickbreakergame.dart';

class GameArea extends RectangleComponent with HasGameReference<BrickBreaker> {
  GameArea()
      : super(
          paint: Paint()..color = const Color(0xFFFFFFFF),
          children: [RectangleHitbox()],
        );

  @override
  FutureOr<void> onLoad() async {
    super.onLoad();
    size = Vector2(gameRef.size.x, gameRef.size.y);
  }
}