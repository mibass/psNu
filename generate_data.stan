//generate far detector (oscillated) event spectrum
functions {
    real OscProb(real L, real Elo, real Eup, real theta, real dm){
        real Ec=(Eup+Elo)/2;
        return 1-pow(sin(2*theta),2)*pow(sin(1.27*dm*L/Ec),2);
    }
}

data {
  int<lower=1> N;
  //true oscillation parameters
  real ttheta; //rad
  real tdelta; //eV^2
  real<lower=0> L; //km

  //flux distribution (DUNE numu CC FD), modeled as gamma
  real f_alpha;//=3.01;
  real f_shift;//=0.33;
  real f_beta;//=0.75;
}



generated quantities {
  real E_true[N];
  real E_meas[N];

  for (i in 1:N) {
    E_true[i]=gamma_rng(f_alpha, f_beta)+f_shift;
    if (uniform_rng(0,1)>OscProb(L, E_true[i], E_true[i], ttheta, tdelta))
      E_meas[i]=0.0;
    else
      E_meas[i]=E_true[i];
  }
}
