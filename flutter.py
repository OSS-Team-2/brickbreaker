import 'dart:ui';
import 'package:flame/flame.dart';
import 'package:flame/game.dart';
import 'package:flutter/material.dart';
import 'package:flutter/gestures.dart';

void main() {
  runApp(GameWidget());
}

class GameWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: SafeArea(
          child: Game(),
        ),
      ),
    );
  }
}

class Ball {
  static const double radius = 10;
  Rect rect;
  Paint paint;

  double speedX;
  double speedY;

  Ball() {
    rect = Rect.fromLTWH(0, 0, radius * 2, radius * 2);
    paint = Paint()..color = Colors.white;
    speedX = 2;
    speedY = -2;
  }

  void render(Canvas canvas) {
    canvas.drawCircle(Offset(rect.center.dx, rect.center.dy), radius, paint);
  }

  void update() {
    rect = rect.translate(speedX, speedY);

    if (rect.left <= 0 || rect.right >= screenSize.width) {
      speedX *= -1;
    }
    if (rect.top <= 0) {
      speedY *= -1;
    }
  }
}

class Paddle {
  static const double width = 100;
  static const double height = 20;
  Rect rect;
  Paint paint;

  Paddle() {
    rect = Rect.fromLTWH((screenSize.width - width) / 2, screenSize.height - height * 2, width, height);
    paint = Paint()..color = Colors.blue;
  }

  void render(Canvas canvas) {
    canvas.drawRect(rect, paint);
  }

  void update(double x) {
    rect = rect.translate(x - rect.center.dx, 0);

    if (rect.left <= 0) {
      rect = rect.translate(-rect.left, 0);
    }
    if (rect.right >= screenSize.width) {
      rect = rect.translate(screenSize.width - rect.right, 0);
    }
  }
}

class Brick {
  static const double width = 50;
  static const double height = 20;
  Rect rect;
  Paint paint;

  Brick(double x, double y) {
    rect = Rect.fromLTWH(x, y, width, height);
    paint = Paint()..color = Colors.red;
  }

  void render(Canvas canvas) {
    canvas.drawRect(rect, paint);
  }
}

class Game extends BaseGame {
  Size screenSize;
  Ball ball;
  Paddle paddle;
  List<Brick> bricks = [];

  Game() {
    initialize();
  }

  void initialize() async {
    screenSize = await Flame.util.initialDimensions();

    ball = Ball();
    paddle = Paddle();

    double brickWidth = Brick.width;
    double brickHeight = Brick.height;
    int numBricks = (screenSize.width / brickWidth).floor();
    int numRows = 5;

    for (int row = 0; row < numRows; row++) {
      for (int col = 0; col < numBricks; col++) {
        double x = col * brickWidth;
        double y = row * brickHeight + 50;
        bricks.add(Brick(x, y));
      }
    }
  }

  @override
  void render(Canvas canvas) {
    canvas.drawRect(Rect.fromLTWH(0, 0, screenSize.width, screenSize.height), Paint()..color = Colors.black);

    ball.render(canvas);
    paddle.render(canvas);
    bricks.forEach((brick) => brick.render(canvas));
  }

  @override
  void update(double t) {
    ball.update();
  }

  @override
  void resize(Size size) {
    screenSize = size;
    super.resize(size);
  }

  @override
  void onTapDown(TapDownDetails details) {
    super.onTapDown(details);
    double x = details.globalPosition.dx;
    paddle.update(x);
  }
}
