import 'package:flame/collisions.dart';
import 'package:flame/components.dart';
import 'package:flutter/material.dart';
import 'dart:math';

import '../brickbreakergame.dart';
import '../config.dart';
import 'ball.dart';
import 'bat.dart';

class Brick extends RectangleComponent 
  with HasGameRef<BrickBreaker>, CollisionCallbacks{
    
  int colorIndex;
  // Add your custom properties and methods here
  Brick({
    required super.position,
    required Color color,
  }) : colorIndex = Random().nextInt(brickColors.length), super(
    size: Vector2(brickWidth, brickHeight),
    anchor: Anchor.center,
    paint: Paint()
      ..color = color
      ..style = PaintingStyle.fill,
    children: [RectangleHitbox()],
    );

  // Method to handle brick hit
  void hit() {
    if (colorIndex < brickColors.length - 1) {
      colorIndex++;
      paint.color = brickColors[colorIndex];
    } else {
      // Brick is red and will be removed
      removeFromParent();
    }
  }

  @override
  void onCollisionStart(
    Set<Vector2> intersectionPoints, PositionComponent other) {
    // Implement the collision logic for the brick
    hit();
    super.onCollisionStart(intersectionPoints, other);
    removeFromParent();
    if (game.streak.value == 0) { // when streak is 0 add 1 to score
      game.score.value += 1;
    } else {
      game.score.value += game.streak.value;
    }

    if(game.world.children.query<Brick>().length == 1){
      game.playState = PlayState.gameWon;
      game.world.removeAll(game.world.children.query<Ball>());
      game.world.removeAll(game.world.children.query<Bat>());
    }
  }
}