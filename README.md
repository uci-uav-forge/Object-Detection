# Object-Detection


Current State - Able to remove small markings from an image with a shape. (isolates the shape). Stil having some trouble with identiying larged bodies since they are disconnected pixels.

How it Works - uses morphology lib to filter the uneccessary pixels but is unable to detect larger bodies. This is why we are utilizing a dictionary to check the quanitity of each pixels based on RGB. Beyond 200-500 pixels is the allowable range and anything beyond will be deleted.

Future: Refine the range to be more accurate, and hopefully use Keras to make image cleaning more accurate.
