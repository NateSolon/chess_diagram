## Chess Diagram Recognizer

Recognize the position from an image of a chess diagram and export it as a FEN that can be used with chess apps. Check out the app deployed at https://chessdiagram923489.herokuapp.com/.

[![Demo of app](http://img.youtube.com/vi/QrEialnghho/0.jpg)](http://www.youtube.com/watch?v=QrEialnghho "Demo")

The image must be cropped to the board only and from white's point of view (first rank at the bottom). It's been tested with the standard sets from lichess, chess.com, and ChessBase.

The code for the app as deployed at https://chessdiagram923489.herokuapp.com/ is in the `app` directory. The web code is mostly copied from this project: https://github.com/rouenlee29/cat-detector.

The rest of the repo consists of notebooks, experiments, etc. that were used in developing this project. Some are aborted attempts. I hope you will find something useful!

## Next Steps

* **Lighter Weight Model**: The current model architecture is Resnet18. This is the smallest vision model included in fastai. However, even this is probably overkill for the task at hand. I'd like to see what is the minimum architecture required to successfully accomplish the task. In fact, the piece images are similar to MNIST in terms of scale and detail. Maybe pretraining on MNIST would be a good idea.

* **Object Detection**: That is, finding a chessboard in a larger (uncropped) image. Here again, the usual models seem like massive overkill, because standard object detection models are capable of detecting many categories of objects, as well as multiple objects in a single image; whereas I am looking for exactly one object of exactly one type, a chessboard. I would like to add a widget to the web app to crop the image directly on the app. This would make the app more convenient to use, especially on mobile, and the cropped images, if saved, could become the training data for an object detection model.
