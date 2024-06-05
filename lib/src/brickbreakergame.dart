import 'dart:async';
import 'dart:math' as math;

import 'package:flame/components.dart';
import 'package:flame/events.dart';
import 'package:flame/game.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';


import 'objects/obj.dart';
import 'config.dart';

enum PlayState { welcome, playing, gameOver, gameWon }

class BrickBreaker extends FlameGame with HasCollisionDetection, KeyboardEvents, TapDetector {
  final ValueNotifier<int> score = ValueNotifier(0);
  final rand = math.Random();
  double get width => size.x;
  double get height => size.y;

  late PlayState _playState;
  PlayState get playState => _playState;
  set playState(PlayState playState) {
    _playState = playState;
    switch (playState) {
      case PlayState.welcome:
      case PlayState.gameOver:
      case PlayState.gameWon:
        overlays.add(playState.name);
        break;
      case PlayState.playing:
        overlays.remove(PlayState.welcome.name);
        overlays.remove(PlayState.gameWon.name);
        overlays.remove(PlayState.gameOver.name);
        break;
    }
  }

  @override
  Future<void> onLoad() async {
    super.onLoad();
    camera.viewfinder.anchor = Anchor.topLeft;
    world.add(GameArea());
    playState = PlayState.welcome;
  }

  void startGame({required double difficulty}) {
    if (playState == PlayState.playing) {
      return;
    }

    world.removeAll(world.children.query<Ball>());
    world.removeAll(world.children.query<Brick>());
    world.removeAll(world.children.query<Bat>());

    playState = PlayState.playing;
    score.value = 0;
    
    world.add(Ball(
      difficultyModifier: difficultyModifier * difficulty,
      radius: ballRadius,
      position: size / 2,
      velocity: Vector2((rand.nextDouble() - 0.5) * width, height * 0.2).normalized()..scale(height / 4),
    ));

    world.add(Bat(
      cornerRadius: const Radius.circular(ballRadius / 2),
      position: Vector2(width / 2, height * 0.95),
      size: Vector2(batWidth, batHeight),
    ));

    int rows = (4 * difficulty).round();

    world.addAll([
      for (var i = 0; i < brickColors.length; i++)
        for (var j = 1; j <= rows; j++)
          Brick(
            position: Vector2(
              (i + 0.5) * brickWidth + (i + 1) * brickGutter,
              (j + 2.0) * brickHeight + j * brickGutter,
            ),
            color: brickColors[i],
          ),
    ]);
  }

  @override
  void onTap() {
    super.onTap();
    playState = PlayState.welcome;
  }

  @override
  KeyEventResult onKeyEvent(KeyEvent event, Set<LogicalKeyboardKey> keysPressed) {
    super.onKeyEvent(event, keysPressed);
    switch (event.logicalKey) {
      case LogicalKeyboardKey.arrowLeft:
        world.children.query<Bat>().first.moveBy(-batStep);
        break;
      case LogicalKeyboardKey.arrowRight:
        world.children.query<Bat>().first.moveBy(batStep);
        break;
      case LogicalKeyboardKey.space:
      case LogicalKeyboardKey.enter:
        startGame(difficulty: 1.0); // 기본 난이도로 게임 시작
        break;
    }

    return KeyEventResult.handled;
  }

  @override
  Color backgroundColor() => const Color(0xffa9d6e5);
}
