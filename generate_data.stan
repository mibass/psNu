//generate far detector (oscillated) event spectrum
transformed data {
  int<lower=1> N = 10000;

  //flux distribution (DUNE numu CC FD), modeled as gamma
  real f_alpha=3.01;
  real f_shift=0.33;
  real f_beta=0.75;

  //true oscillation parameters
  real ttheta=0.7854; //rad
  real tdelta=2.4e-3; //eV^2
}

generated quantities {
  real E_meas[N];

  for (i in 1:N) {
    E_meas[i]=gamma_rng(f_alpha, f_beta)+f_shift;
  }
}
