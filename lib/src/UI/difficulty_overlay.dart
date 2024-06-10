import 'package:flutter/material.dart';
import '../brickbreakergame.dart';

class DifficultyOverlay extends StatelessWidget {
  final BrickBreaker game;

  const DifficultyOverlay({required this.game, super.key});

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Padding(
        padding: const EdgeInsets.all(20.0), // 패딩을 추가하여 전체 여백 설정
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            const Text(
              'Select difficulty',
              style: TextStyle(fontSize: 35, color: Colors.black),
            ),
            const SizedBox(height: 100), // 간격 설정
            SizedBox(
              width: 220, // 버튼의 너비 설정
              child: ElevatedButton(
                onPressed: () {
                  game.startGame(difficulty: 1.0); // Easy
                },
                child: const Text(
                  'Easy',
                  style: TextStyle(fontSize: 24), // 폰트 크기 설정
                ),
              ),
            ),
            const SizedBox(height: 40), // 간격 설정
            SizedBox(
              width: 220, // 버튼의 너비 설정
              child: ElevatedButton(
                onPressed: () {
                  game.startGame(difficulty: 1.1); // Medium
                },
                child: const Text(
                  'Medium',
                  style: TextStyle(fontSize: 24), // 폰트 크기 설정
                ),
              ),
            ),
            const SizedBox(height: 40), // 간격 설정
            SizedBox(
              width: 220, // 버튼의 너비 설정
              child: ElevatedButton(
                onPressed: () {
                  game.startGame(difficulty: 1.2); // Hard
                },
                child: const Text(
                  'Hard',
                  style: TextStyle(fontSize: 24), // 폰트 크기 설정
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

