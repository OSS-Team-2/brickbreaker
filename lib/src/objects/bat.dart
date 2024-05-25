import 'package:flame/collisions.dart';
import 'package:flame/components.dart';
import 'package:flame/effects.dart';
import 'package:flame/events.dart';
import 'package:flutter/material.dart';

import '../brickbreakergame.dart';

class Bat extends PositionComponent 
  with HasGameRef<BrickBreaker>,DragCallbacks{
  // Add your custom properties and methods here
  Bat({
    required this.cornerRadius,
    required super.position,
    required super.size,
  }) : super(
    anchor: Anchor.center,
    children: [RectangleHitbox()],
    );

    final Radius cornerRadius;

    final _paint = Paint()
      ..color = const Color(0xFFFFFFFF)
      ..style = PaintingStyle.fill;
  
  @override
  void render(Canvas canvas) {
    // Implement the rendering logic for the bat
    super.render(canvas);
    canvas.drawRRect(
      RRect.fromRectAndRadius(
        Offset.zero & size.toSize(),
        cornerRadius),
      _paint,
    );
  }
  
  @override
  void onDragUpdate(DragUpdateEvent event) {
    // Implement the drag update logic for the bat
    super.onDragUpdate(event);
    position.x = (position.x + event.localDelta.x).clamp(0, game.width);
  }

  void moveBy(double dx){
    add(MoveToEffect(
      Vector2((position.x + dx).clamp(0, game.width), position.y),
      EffectController(duration: 0.1),
      ));
  }


  @override
  void update(double dt) {
    // Implement the update logic for the bat
  }
}