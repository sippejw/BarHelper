import 'dart:async';
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';

void main() {
  runApp(BarHelper());
}

class BarHelper extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Bar Helper',
      home: HomePage(),
    );
  }
}

class HomePage extends StatefulWidget {
  @override
  HomePageState createState() => new HomePageState();
}

class HomePageState extends State<HomePage> {
  File image;
  Future getImage() async {
    File picture = await ImagePicker.pickImage(
      source: ImageSource.camera,
      maxWidth: 300.0,
      maxHeight: 500.0
    );
    setState(() {
      image = picture;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Take a picture')
      ),
      body: Center(
        child: image == null
          ? Text('Take a picture')
          : Image.file(image)
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: getImage,
        tooltip: 'Pick image',
        child: Icon(Icons.add_a_photo)
      ),
    );
  }
}



/* import 'dart:async';
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:camera/camera.dart';
import 'package:path_provider/path_provider.dart';

List<CameraDescription> cameras;

Future<void> main() async {
  cameras = await availableCameras();
  runApp(CameraApp());
}

class CameraApp extends StatefulWidget {
  @override
  _CameraAppState createState() => _CameraAppState();
}

class _CameraAppState extends State<CameraApp> {
  CameraController controller;

  @override
  void initState() {
    super.initState();
    controller = CameraController(cameras[0], ResolutionPreset.medium);
    controller.initialize().then((_) {
      if (!mounted) {
        return;
      }
      setState(() {});
    });
  }

  @override
  void dispose() {
    controller?.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    if (!controller.value.isInitialized) {
      return Container();
    }

    return MaterialApp(
      title: 'BarHelper',
      home: Scaffold(
        appBar: AppBar(
          title: Text("Bar Helper")
        ),
        body: Stack(
          alignment: FractionalOffset.center,
          children: <Widget>[
            Positioned.fill(
              child: AspectRatio(
                aspectRatio:controller.value.aspectRatio,
                child: CameraPreview(controller)
              ),
            ),
            RaisedButton(
              padding: const EdgeInsets.all(8.0),
              textColor: Colors.white,
              color: Colors.blue,
              onPressed: () async {
                
                // Directory dir = await getApplicationDocumentsDirectory();
                // controller.takePicture('/storage/emulated/0/Pictures/BarHelper/0.jpg');
                // print(dir.path);

                
              }
            )
          ]
        )
      )
    );
  }
} */