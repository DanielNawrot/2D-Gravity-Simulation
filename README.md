# 2D Gravity Simulation

In this project I challenged myself with programming a large body gravity simulation. Although simple and unrefined, I learned many things through this project. 

The simulation uses Newton's Gravity Equations: 

![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/png.image?\inline&space;\dpi{200}\bg{black}\overrightarrow{F}_{g}=\frac{GM_{1}M_{2}}{r^{2}})

Then we find acceleration using Newton's Second Law:

![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/png.image?\inline&space;\dpi{200}\bg{black}F=ma)

![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/png.image?\inline&space;\dpi{200}\bg{black}a=\frac{F}{m})

Finally, we break down the acceleration vector into its x & y components, which are usable in our simulation. First we normalize the distance between the two objects, by dividing the components of the distance vector by its magnitude.

![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/png.image?\inline&space;\dpi{200}\bg{black}\left\|r\right\|=\sqrt{(x_{2}-x_{1})^{2}&plus;(y_{2}-y_{1})^{2}})

![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/png.image?\inline&space;\dpi{200}\bg{black}(x_{r},y_{r})=(x_{2}-x_{1},y_{2}-y_{1}))

![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/png.image?\inline&space;\dpi{200}\bg{black}\hat{r}=(\frac{x_{r}}{\left\|r\right\|},\frac{y_{r}}{\left\|r\right\|}))

![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/png.image?\inline&space;\dpi{200}\bg{black}(a_{x},a_{y})=(\hat{r}_{x}\times\left\|a\right\|,\hat{r}_{y}\times\left\|a\right\|))

One problem with my approach is that it does not consider optimising the program, meaning that processing speeds increase dramatically with increasing amounts of bodies. My program loops through each body, and calculates the attraction towards each other body.

Here are some images of the simulation:

![alt text](https://github.com/DanielNawrot/2D-Gravity-Simulation/blob/main/GravitySimScreenshot1.png)

![alt text](https://github.com/DanielNawrot/2D-Gravity-Simulation/blob/main/GravitySimScrrenshot2.png)
