import 'package:flutter/material.dart';
import 'package:audioplayers/audioplayers.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatefulWidget {
  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  late AudioCache _audioCache;
  AudioPlayer? _audioPlayer;
  bool _isPlaying = false;

  @override
  void initState() {
    super.initState();
    _audioCache = AudioCache(prefix: 'assets/audio/');
  }

  Future<void> _playMusic() async {
    _audioPlayer = await _audioCache.loop('background.mp3');
    setState(() {
      _isPlaying = true;
    });
  }

  Future<void> _stopMusic() async {
    if (_audioPlayer != null) {
      await _audioPlayer!.stop();
      setState(() {
        _isPlaying = false;
      });
    }
  }

  @override
  void dispose() {
    _audioPlayer?.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Game Background Music'),
        ),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              ElevatedButton(
                onPressed: _isPlaying ? _stopMusic : _playMusic,
                child: Text(_isPlaying ? 'Stop Music' : 'Play Music'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
