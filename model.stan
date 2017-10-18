#include func.stan

data {
    real L; //baseline [km]
    int<lower=0> Nbins;
    real Ebins[Nbins+1]; //Energy bin boundaries [GeV]
    vector[Nbins] ynd; //number of events measured at ND
    real ttheta; //true value of theta
    real tdm; //true value of dm^2
    matrix[Nbins,Nbins] Sa; //true to reco energy smearing
    matrix[Nbins,Nbins] Sb; //true to reco energy smearing
}

transformed data {
    int y[Nbins]; //number of events measured at FD
    vector[Nbins] ty; //vector version to be converted to int at the end
    real gqoscprobs[Nbins];

    //apply oscillation to true spectrum
    for (j in 1:Nbins){
        ty[j]=OscProb(L,Ebins[j],Ebins[j+1],ttheta,tdm) * ynd[j];
    }

    //apply smearing
    print(ty);
    ty=Sa*ty;
    print(ty);

    //convert vector to int array
    for (j in 1:Nbins){
        int i=0;
        while (i<ty[j]) i=i+1;
        y[j] = i;
    }

    for (j in 1:Nbins){
        gqoscprobs[j]=OscProb(L,Ebins[j],Ebins[j+1],ttheta,tdm);
    }
}

parameters {
    real<lower=0,upper=1.57> theta;
    real<lower=2e-3,upper=4e-3> dm;
}

transformed parameters {
    vector[Nbins] pyfd; //predicted flux at FD
    for (j in 1:Nbins)
        pyfd[j] = OscProb(L,Ebins[j],Ebins[j+1],theta,dm) * ynd[j];

    pyfd=Sb*pyfd;
}

model {
    y ~ poisson(pyfd);
}
