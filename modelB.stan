functions {
    real OscProb(real L, real Elo, real Eup, real theta, real dm){
        real Ec=(Eup+Elo)/2;
        return 1-pow(sin(2*theta),2)*pow(sin(1.27*dm*L/Ec),2);
    }
}

data {
    int<lower=1> N;
    real L; //baseline [km]
    real y[N]; //measured event energies at FD

    //flux distribution (DUNE numu CC FD), modeled as gamma
    real f_alpha;//=3.01;
    real f_shift;//=0.33;
    real f_beta;//=0.75;
}


parameters {
    real<lower=0,upper=1.57> theta;
    real<lower=2e-3,upper=4e-3> dm;

    real<lower=0> yf[N];
    real osc[N];
}


model {

  osc ~ uniform(0,1);
  yf ~ gamma(f_alpha, f_beta);
  print(yf);
  //for (i in 1:N) {
  //  if (osc[i]>OscProb(L, yf[i], yf[i], theta, dm))
  //    yf[i]=0.0;
  //}
  y ~ gamma(yf,1);
}
