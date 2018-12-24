# ASCII Art
<br>
A python script that converts an **image** to **ascii art**.

### The scripts uses the following libraries:
1. **Python Image Library (PIL)**
2. **Numpy**

### How it works:

The script reads the image using PIL and loads it. This is then first converted to a thumbnail of size (128, 128), which is then loaded into a numpy array. This numpy array has the dimensions: **(height x width x 3)**. This is the array representation of each pixel in the image. This pixel is now operated upon to give a single value between 0-64.
<br>The steps involved are:
1. Getting **RBG** values of every pixel.
2. Performing **mathematical operations**. eg: average on the RBG values.
3. Scaling the condensed value from range **0-255** to **0-64**.
4. Using the scaled value to lookup and get the corresponding ASCII value from a **custom ASCII table** consisting of 65 characters.

Once the ASCII values for every pixel are obtained, they are stored in a new **2-D list**, and printed onto the terminal.

### Future changes:

1. Current ASCII image that is printout onto the terminal is squashed. This will be changed to display the art to the correct scale.
2. Color options to the ASCII art.
3. More RBG to ASCII functions.
4. Option to save the ASCII art as an image.
5. Filters for the pinted ASCII art.

### Authors:

**Naren Surampudi**

### Credits:

**Robert Heaton**
