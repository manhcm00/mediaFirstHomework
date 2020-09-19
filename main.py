import binomial
import geometric
import negbinomial

print(geometric.prob(100, 0.3))
print(geometric.infoMeasure(100, 0.3))
print(geometric.sumProb(100, 0.3))
print(geometric.approxEntropy(100, 0.3))

print(binomial.prob(10, 0.3, 100))
print(binomial.infoMeasure(10, 0.3, 100))
print(binomial.sumProb(100, 0.3))
print(binomial.approxEntropy(100, 0.3))

print(negbinomial.prob(100, 0.3, 10))
print(negbinomial.infoMeasure(100, 0.3, 10))
print(negbinomial.sumProb(100, 0.3, 10))
print(negbinomial.approxEntropy(100, 0.3, 10))