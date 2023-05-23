import 'package:flutter/material.dart';
import 'package:flutter/animation.dart';

class TitleBarIconTransition extends StatefulWidget {
  /* App's title bar's rotating icon animator */
  _TitleBarIconTransitionState createState() => _TitleBarIconTransitionState();
}

class _TitleBarIconTransitionState extends State<TitleBarIconTransition> with TickerProviderStateMixin {
  AnimationController _controller;
  Animation<double> _animation;
  
  // stages of rotation
  final Tween<double> turnsTween = Tween<double>(
    begin: 1,
    end: 4,
  );

  final Color color = Colors.red;

  initState() {
    super.initState();
    _controller = AnimationController(duration: const Duration(milliseconds: 6000), vsync: this, value: 0.1);
    _animation = CurvedAnimation(parent: _controller, curve: Curves.bounceInOut);
    _controller.repeat();
  }

  @override
  dispose() {
    _controller.dispose();
    super.dispose();
  }

  Widget build(BuildContext context) {
    // main widget 
    return Container(
      padding: EdgeInsets.only(left: 5),
      child: RotationTransition(
        turns: turnsTween.animate(_controller),
        child: Icon(Icons.autorenew, size: 38, color: Colors.white),
      ),
    );
  }
}