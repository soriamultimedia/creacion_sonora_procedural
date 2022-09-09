
//Principios de creación sonora procedural. Edmar Soria
//Conjuntos y permutaciones en SC.


//Definir conjuntos. Un conjunto no tiene duplicaciones y sus elementos no están ordenados.
a = 1.seriesIter.nextN(5).asSet;
b = Array.series(10,-5,2).asSet;
c = Array.series(10,1,3)
d = [0,0,1,2,3,4,5,5].asSet;

//operaciones básicas
union(a,b)
union(a,c)
difference(b,a)
symmetricDifference(a, b);

a.isSubsetOf(b)

//Conjunto potencia
x = a.powerset;
y = b.powerset

//Conjuntos con símbolos
a = Set["ajsjhs","bhh","csk","dajs","euis","foa"]

//ejemplo con texto
(
~text = "Y la muerte perderá su dominio. Los muertos desnudos serán un solo muerto."
)

//split en array distintos niveles
~level1 = ~text.split($ )
~level2 = ~level1.collect({arg i; i.split($ )})

//conjunto potencia 2**n
~set = ~level1.as(Set)
z = ~set.powerset
z.size
.choose

//función para generar permutaciones del texto
(
~pwr = {
	arg in_array;
	var set, s_pwr;
	set = in_array.as(Set);
	s_pwr = set.powerset;
	s_pwr.asArray
};

~permut = {
	arg in_set, deep;
	var set, permut;

	set = List[];
	in_set.do({arg i; if(i.size==deep,{set.add(i)})});
	//set.postln;

	permut = (set.choose.asArray).scramble;
	//permut = permut.join(" ") ; para texto,

}
)

//obtener el cojnuto potencia
x = ~pwr.(~level1)

//permutaciones de distintos tamaños
~permut.(x,3)
~permut.(x,5)

//rutina simple sobre la permutación, con serie geométrica
~serie = Array.geom(10,1,1.5).floor.asInteger;


(
~task = {
	arg input_data, source;
	var pwr_set;

	pwr_set = ~pwr.(source);
	{
	(input_data.maxItem.floor.asInteger).do({
		arg i;
		var indx, time;

		indx = input_data.choose;
		time = input_data.choose.reciprocal;
		if(indx  > source.size, {indx = input_data.choose;});
		~permut.(pwr_set,indx).postln;
		time.wait;

	})
}.fork
}
)

~task.(~serie, ~level1)


//Ejemplos con conjuntos de elementos sonoros
(
~nat = ['C','D','E','F','G','A','B'];
~shrp = ['C#','D#','E#','F#','G#','A#','B#'];
~bml = ['Cb','Db','Eb','Fb','Gb','Ab','Bb'];

~nat_pwr = ~pwr.(~nat);
~shrp_pwr = ~pwr.(~shrp);
~bml_pwr = ~pwr.(~bml);
)


~permut.(~nat_pwr,3)
~permut.(~shrp_pwr,5)

~task.(~serie, ~nat)
~task.(~serie, ~bml)

//serie cromática
(
~chrm = List[];
7.do({arg i; ~chrm.add(~nat[i]); ~chrm.add(~shrp[i]);});
~chrm.removeAt(5);
~chrm.removeAt(~chrm.size-1);
~chrm;
)

~task.(~serie, ~chrm)

//dinámica

~din = ['ppp','pp','p','mp','mf','f','ff','fff','sf'];
~din_pwr = ~pwr.(~din);

~permut.(~din_pwr,5)


//Mapeo a valores MIDI
//construcción de diccionario
(
~symbl2MIDI = Dictionary.new;
(~chrm.size).do({arg i; ~symbl2MIDI.put(~chrm[i],i)});
)

~symbl2MIDI.keys;
~symbl2MIDI.at('D');
(
~s2MIDI = {
	arg note, octave;

	~symbl2MIDI.at(note.asSymbol)+(12*octave);
};

)
~s2MIDI.('D',4)
~s2MIDI.('A#',7)



//notas midi 0-120, octavas 0-10
~serie = Array.series(120,0,1).floor.asInteger;
~oct = Array.series(10,0,1).floor.asInteger;


~time = {rrand(0.1,2)}!100
~task_M.(~serie, ~time, ~chrm)

