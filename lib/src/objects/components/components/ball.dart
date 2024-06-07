import 'package:flame/collisions.dart';
import 'package:flame/components.dart';
import 'package:flame/effects.dart';
import 'package:flutter/material.dart';
import '../brickbreakergame.dart';
import 'bat.dart';
import 'brick.dart';
import 'game_area.dart';

int streak = 1;

class Ball extends CircleComponent with HasGameReference<BrickBreaker>, CollisionCallbacks {
  Ball({
    required this.velocity,
    required super.position,
    required double radius,
    required this.difficultyModifier,
  }) : super(
          anchor: Anchor.center,
          radius: radius,
          paint: Paint()
            ..color = Color.fromARGB(255, 255, 0, 0)
            ..style = PaintingStyle.fill,
          children: [CircleHitbox()],
        );

  final Vector2 velocity;
  final double difficultyModifier;

  @override
  void update(double dt) {
    super.update(dt);
    position += velocity * dt;
  }

  @override
  void onCollisionStart(Set<Vector2> intersectionPoints, PositionComponent other) {
    super.onCollisionStart(intersectionPoints, other);
    if (other is GameArea) {
      if (intersectionPoints.first.y <= 0) {
        velocity.y *= -1;
      } else if (intersectionPoints.first.x <= 0) {
        velocity.x *= -1;
      } else if (intersectionPoints.first.x >= gameRef.size.x) {
        velocity.x *= -1;
      } else if (intersectionPoints.first.y >= gameRef.size.y) {
        gameRef.removeBall(this);
      }
    } else if (other is Bat) {
      velocity.y *= -1;
      velocity.x += (position.x - other.position.x) / other.size.x * gameRef.size.x * 0.3;
      streak = 1;
    } else if (other is Brick) {
      if (position.y < other.position.y - other.size.y / 2) {
        velocity.y *= -1;
      } else if (position.y > other.position.y + other.size.y / 2) {
        velocity.y *= -1;
      } else if (position.x < other.position.x) {
        velocity.x *= -1;
      } else if (position.x > other.position.x) {
        velocity.x *= -1;
      }
      velocity.setFrom(velocity * difficultyModifier);
      streak += 1;
    }
  }
}