import 'package:flutter/material.dart';


class RainDrop extends StatefulWidget {
  // returns a raindrop of given color, size is fixed

  // NB: This widget can be made dynamic based on size, when required!!!!!!!
  final Color color;
  const RainDrop ({ Key key, this.color }): super(key: key);
  _RainDropState createState() => _RainDropState();
}


class _RainDropState extends State<RainDrop> with TickerProviderStateMixin {
  Widget build(BuildContext context) {
    // main widget
    return Container(
      padding: EdgeInsets.all(6),
      height: 25,
      width: 25,
      decoration: BoxDecoration(
        shape: BoxShape.circle,
        color: widget.color.withOpacity(0.30),
      ),
      child: Container(
        decoration: BoxDecoration(
          shape: BoxShape.circle,
          color: widget.color,
        ),
      ),
    );
  }
}
