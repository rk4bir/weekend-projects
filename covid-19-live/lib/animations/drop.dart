import 'package:flutter/material.dart';
import 'package:flutter/animation.dart';
import '../widgets/drop.dart';

class AnimatedRainDrop extends StatefulWidget {
  /*
  * Rain drop animation: color (Colors object) and size (integer) is required!
  */
  final Color color;
  final double size;
  const AnimatedRainDrop ({ Key key, this.color, this.size }): super(key: key);
  _AnimatedRainDropState createState() => _AnimatedRainDropState();
}

class _AnimatedRainDropState extends State<AnimatedRainDrop> with TickerProviderStateMixin {
  AnimationController _controller;
  Animation<double> _animation;

  initState() {
    super.initState();
    _controller = AnimationController(duration: const Duration(milliseconds: 400), vsync: this, value: 0.1);
    _animation = CurvedAnimation(parent: _controller, curve: Curves.bounceInOut);
    _controller.repeat();
  }

  @override
  dispose() {
    _controller.dispose();
    super.dispose();
  }

  Widget build(BuildContext context) {
    /* Main widget is defined here */
    return ScaleTransition(
      scale: _animation,
      alignment: Alignment.center,
      child: Container(
        // drop's outer padding
        padding: EdgeInsets.all(widget.size/5 + 1),
        // margin: EdgeInsets.only(right: 5, left: 5),
        height: widget.size,
        width: widget.size,
        decoration: BoxDecoration(
          shape: BoxShape.circle,
          color: widget.color.withOpacity(0.30),
        ),
        // drop itself
        child: Container(
          decoration: BoxDecoration(
            shape: BoxShape.circle,
            color: widget.color,
          ),
        ),
      ),
    );
  }
}
