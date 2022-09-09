
//Principios de creación sonora procedural. Edmar Soria.
//Series geométricas y aritméticas en SC.



(
~serie = {
	arg a, r, it;
	var box;

	box = List[];

	it.do({
		arg i;
		var temp_;

		temp_ = a*r**(i);
		box.add(temp_);
			});
	box = box.asArray;
};

//Calcular serie con a=1, r=1/2, iteraciones = 100
a = ~serie.(1,1/2,100);
//Subdivisiones y escalamiento de intervalos

~div = {
	arg input,factor;
	var split = List[];

	((input.size/factor).floor.asInteger).do({
		arg i;
		var c_ , d_;

		c_ = factor*i;
		d_ = c_+(factor-1);

		split.add(input[c_..d_]);
	});
	split;

	};


~scal = {
	arg input, thr=1;
	var box;
		box = input.collect({arg i;while({i<thr},{i=i*10;}); i});

}
)

//Split del array original en el factor dado; factor=5 --> 20 subarrays.
z = ~div.(a,10);

//escalamiento proporcional al número de 0´s de cada elemento individual para un sub array.
x = z[0];
w = ~scal.(x,1);

//escalamiento proporcional al número de 0´s de cada elemento individual para todos los subarrays.
~s_total = z.collect({arg i; ~scal.(i,1);})

//un threshold distinto
~s_total = z.collect({arg i; ~scal.(i,0.1);})

//un thresold distinto para cada subarray

~thr = ({arg i; (10**(i)).reciprocal})!4
~sel_t = Prand(~thr, inf);
~sel_t = ~sel_t.asStream;
~s_total = z.collect({arg i; ~scal.(i,~sel_t.next);})


//La forma directa
Array.geom(100,1,1/2)
Array.fib(100)









