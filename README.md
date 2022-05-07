# 4 Credit MP: Ray Tracing

Ray Tracing MP using Python.

This work is based off **[Ray Tracing in One Weekend](https://raytracing.github.io/books/RayTracingInOneWeekend.html)** and **[Ray Tracing: The Next Week](https://raytracing.github.io/books/RayTracingTheNextWeek.html)** by Peter Shirley but ported to Python. **[PyTrace_Next_Week](https://github.com/Arjun-Arora/PyTrace_Next_Week)** by Arjun-Arora also helped me a lot on finishing this MP.

dependencies include: 
1. pypy3 (note all other dependencies must be installed within pypy3)
2. numpy 
3. matplotlib
4. tqdm

## Quickstart guide: 
1. Install Anaconda
2. conda create -n rayTrace pypy
3. conda activate rayTrace
4. pypy3 -m ensurepip
5. **if on mac you may need to fake a linked library described [here](https://bitbucket.org/pypy/pypy/issues/2942/unable-to-install-numpy-with-pypy3-on)**
6. pypy3 -m pip install -r requirements.txt
7. pypy3 main.py

Can run without pypy3 installed but will run very slow.

## Output Image: 
![image2](./output.png)

The formate of my output image is png, with resolution being 875x500.

### Image Concepts
A pinky room with a bouncing glass sphere, some small candies(diffuse), marbles(metal), and glasses scattering next to the glass ball. A mirror is leaning on a box. These items are all lying on a wooden desk. The light direction is from the top to the desk.
