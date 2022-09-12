
//Principios de creaciòn sonora procedural. Edmar Soria
//Ejemplo de sistemas dinàmicos
//Instalar la clase Map_Chaos.

//Definir un objeto del tipo Map_Chaos
//https://mathworld.wolfram.com/HenonMap.html

~source = Map_Chaos.new;

//Sobre este objeto se pueden calcular las òrbitas que se deseen para diversos tipos de sistemas dinàmicos simples que exhiben propiedas caòticas bajo ciertas condiciones iniciales.

//Calcular òrbitas distintas para distintas condiciones iniciales del mapeo logìstico.
//Tres paràmetros: punto inicial (x_0), paràmetro de control (r), no. de iteraciones.
(
~x_0 = [0.5,0.75,0.8,0.7,0.6];
~r_param = Array.fill(5,{arg i; 3.7+(i/15)});
~logistic_fam = {arg i; ~source.logistic(~x_0[i],~r_param[i],200)}!5;
{arg i; ~logistic_fam[i].plot}!5
)

//Calcular òrbitas distintas para distintas condiciones iniciales del mapeo Henon.
//Cinco paràmetros: paràmetros de control a y b, puntos iniciales x/y, iteraciones.
Supercollider

(
~a_H = [0.2,0.2,0.25,1.29,1.3];
~b_H = [0.9,-0.9,0.9,0.29,0.3,0.3];
~x_H = [0,0.001,0.1,0.01,0.4,0.5];
~y_H = [0.001,0.1,0.3,-0.5,-0.45];
~henon = {arg i; ~source.henon(~a_H[i],~b_H[i],~x_H[i],~y_H[i],200)}!(~a_H.size);
{arg i; ~henon[i][0].plot}!(~a_H.size)
)

//Càlculo de otros sistemas dinàmicos. Paràmetros seteados por default para comportamiento caòtico
(
~sine = ~source.sine(it:250);
~cubic = ~source.cubic(it:250);
~tent = ~source.tent(it:250);
~duff = ~source.duff(it:250);
)


//Hibridaciòn de envolventes. Combinar envolventes para los paràmetros de data, tiempo y curvatura. Aplicar normalizaciòn para establecer escalamiento para transudcciòn de paràmetros sonoros
//Serie muestra
a = (~duff*~sine).normalize(0,0.91);
a.plot
a.reverse
(
z = Env.new(a,~duff.normalize(5,7),~tent.normalize(-4,4.0));
x = Env.new(a.normalize(20,30,7),~sine.normalize(20,30),~sine.normalize(-1.0,1.0));
y = Env.new(~sine.normalize(5,7), a.normalize(0,10),~tent.normalize(-2.0,0.01));
w = Env.new(~cubic.normalize(100,300),~cubic.normalize(100,300), ~tent.normalize(-6.1,0.5));
v = Env.new((a.reverse).normalize(1,3),~cubic.normalize(1,3));
t = Env.new((~tent*~cubic).normalize(0,1),~cubic.normalize(10,30));
p = Env.new((a.reverse*~cubic).normalize(1000,3000),~cubic.normalize(1000,3000));
)

[x,y,z,w,v,t,p].plot