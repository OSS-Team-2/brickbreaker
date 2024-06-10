dependencies:
  flutter:
    sdk: flutter
  flame: ^1.0.0

import 'dart:ui';
import 'package:flutter/material.dart';
import 'package:flame/game.dart';
import 'package:flame/flame.dart';
import 'package:flame/components/component.dart';
import 'package:flame/components/mixins/resizable.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  runApp(GameWidget());
}

class Brick extends PositionComponent with Resizable {
  static const double width = 40;
  static const double height = 20;
  static const double padding = 5;

  Brick(double x, double y) {
    this.x = x;
    this.y = y;
    this.width = Brick.width;
    this.height = Brick.height;
  }

  @override
  void render(Canvas c) {
    c.drawRect(toRect(), Paint()..color = Colors.blue);
  }
}

class Ball extends PositionComponent with Resizable {
  static const double radius = 10;
  static const double speed = 200;

  Offset velocity = Offset(speed, speed);

  @override
  void update(double t) {
    super.update(t);
    x += velocity.dx * t;
    y += velocity.dy * t;

    // Collision detection with walls
    if (x <= 0 || x + width >= size.width) {
      velocity = Offset(-velocity.dx, velocity.dy);
    }
    if (y <= 0 || y + height >= size.height) {
      velocity = Offset(velocity.dx, -velocity.dy);
    }
  }

  @override
  void render(Canvas c) {
    c.drawCircle(Offset(x + radius, y + radius), radius, Paint()..color = Colors.red);
  }
}

class Game extends BaseGame with Resizable {
  late Ball ball;
  late List<Brick> bricks;

  @override
  Future<void> onLoad() async {
    ball = Ball();
    bricks = List.generate(5, (index) {
      return Brick(
        index * (Brick.width + Brick.padding),
        Brick.height * 2 + Brick.padding * 2,
      );
    });
  }

  @override
  void update(double t) {
    super.update(t);
    ball.update(t);
  }

  @override
  void render(Canvas c) {
    super.render(c);
    ball.render(c);
    bricks.forEach((brick) => brick.render(c));
  }
}

class GameWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: Container(
          decoration: BoxDecoration(color: Colors.white),
          child: Game().widget,
        ),
      ),
    );
  }
}
