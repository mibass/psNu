functions {
    real OscProb(real L, real Elo, real Eup, real theta, real dm){
        real Ec=(Eup+Elo)/2;
        return 1-pow(sin(2*theta),2)*pow(sin(1.27*dm*L/Ec),2);
    }
}
