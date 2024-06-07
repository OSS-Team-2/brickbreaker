import 'package:flame/collisions.dart';
import 'package:flame/components.dart';
import 'package:flutter/material.dart';
import '../brickbreakergame.dart';

const double brickWidth = 50;
const double brickHeight = 20;

class Brick extends RectangleComponent with HasGameReference<BrickBreaker>, CollisionCallbacks {
  Brick({
    required super.position,
    required Color color,
  }) : super(
          size: Vector2(brickWidth, brickHeight),
          anchor: Anchor.center,
          paint: Paint()
            ..color = color
            ..style = PaintingStyle.fill,
          children: [RectangleHitbox()],
        );

  @override
  void onCollisionStart(Set<Vector2> intersectionPoints, PositionComponent other) {
    super.onCollisionStart(intersectionPoints, other);
    removeFromParent();
    gameRef.score.value += streak;

    if (gameRef.world.children.whereType<Brick>().length == 1) {
      gameRef.playState = PlayState.gameWon;
      gameRef.world.removeAll(gameRef.world.children.whereType<Ball>());
      gameRef.world.removeAll(gameRef.world.children.whereType<Bat>());
    }
  }
}