import 'package:flutter/material.dart';

void main() => runApp(BrickBreakerGame());

class BrickBreakerGame extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Brick Breaker',
      home: Scaffold(
        appBar: AppBar(
          title: Text('Brick Breaker'),
        ),
        body: BrickBreaker(),
      ),
    );
  }
}

class BrickBreaker extends StatefulWidget {
  @override
  _BrickBreakerState createState() => _BrickBreakerState();
}

class _BrickBreakerState extends State<BrickBreaker> {
  int rows = 5;
  int columns = 10;
  List<List<int>> bricks;
  double brickWidth;
  double brickHeight;
  double paddleWidth = 100.0;
  double paddleHeight = 20.0;
  double paddlePosition = 0.0;
  double ballRadius = 10.0;
  Offset ballPosition = Offset(0.0, 0.0);
  Offset ballVelocity = Offset(2.0, 5.0);
  int score = 0;

  @override
  void initState() {
    super.initState();
    initializeBricks();
    startGame();
  }

  void initializeBricks() {
    bricks = List<List<int>>.generate(rows, (row) => List<int>.filled(columns, 1));
    brickWidth = MediaQuery.of(context).size.width / columns;
    brickHeight = 20.0;
  }

  void startGame() {
    setState(() {
      ballPosition = Offset(0.0, 0.0);
      ballVelocity = Offset(2.0, 5.0);
      score = 0;
    });
  }

  void movePaddle(double dx) {
    setState(() {
      paddlePosition += dx;
    });
  }

  void moveBall() {
    setState(() {
      ballPosition += ballVelocity;
      // Check for collisions with walls
      if (ballPosition.dx <= -1 * ballRadius ||
          ballPosition.dx >= MediaQuery.of(context).size.width - ballRadius) {
        ballVelocity = Offset(-1 * ballVelocity.dx, ballVelocity.dy);
      }
      if (ballPosition.dy <= -1 * ballRadius) {
        ballVelocity = Offset(ballVelocity.dx, -1 * ballVelocity.dy);
      }
      // Check for collisions with paddle
      if (ballPosition.dy >= MediaQuery.of(context).size.height - paddleHeight - ballRadius &&
          ballPosition.dx >= paddlePosition &&
          ballPosition.dx <= paddlePosition + paddleWidth) {
        ballVelocity = Offset(ballVelocity.dx, -1 * ballVelocity.dy);
      }
      // Check for collisions with bricks
      for (int i = 0; i < rows; i++) {
        for (int j = 0; j < columns; j++) {
          if (bricks[i][j] == 1) {
            double brickLeft = j * brickWidth;
            double brickTop = i * brickHeight;
            if (ballPosition.dx >= brickLeft &&
                ballPosition.dx <= brickLeft + brickWidth &&
                ballPosition.dy >= brickTop &&
                ballPosition.dy <= brickTop + brickHeight) {
              ballVelocity = Offset(ballVelocity.dx, -1 * ballVelocity.dy);
              bricks[i][j] = 0;
              score++;
              if (score == rows * columns) {
                startGame();
              }
            }
          }
        }
      }
      // Check for game over
      if (ballPosition.dy >= MediaQuery.of(context).size.height) {
        startGame();
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onHorizontalDragUpdate: (details) {
        movePaddle(details.delta.dx);
      },
      child: Container(
        color: Colors.black,
        child: Stack(
          children: <Widget>[
            Positioned(
              left: paddlePosition,
              bottom: 0,
              child: Container(
                width: paddleWidth,
                height: paddleHeight,
                color: Colors.white,
              ),
            ),
            for (int i = 0; i < rows; i++)
              for (int j = 0; j < columns; j++)
                if (bricks[i][j] == 1)
                  Positioned(
                    left: j * brickWidth,
                    top: i * brickHeight,
                    child: Container(
                      width: brickWidth,
                      height: brickHeight,
                      color: Colors.blue,
                    ),
                  ),
            Positioned(
              left: ballPosition.dx - ballRadius,
              top: ballPosition.dy - ballRadius,
              child: Container(
                width: ballRadius * 2,
                height: ballRadius * 2,
                decoration: BoxDecoration(
                  color: Colors.red,
                  shape: BoxShape.circle,
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  @override
  void dispose() {
    super.dispose();
  }
}
