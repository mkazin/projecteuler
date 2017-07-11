- Problem 1: Classic FizBuzz. I decided to solve this the right way (rather than brute-force it), meaning manually using sums of series (and a calculator). So independently sum the 3s, the 5s and the 15s. Then add the 3s and 5s and subtract the 15s (because they get double-counted, being in both the 3s and 5s sets). In other words: ![Prob2BigIdea][Prob2BigIdea] , then pull the multipliers out of the Sigmas, after which you can use the simple series formula: ![SimpleSeriesSum][SimpleSeriesSum]

[SimpleSeriesSum]: https://latex.codecogs.com/png.latex?{\sum_{i=0}^{n}i%20=%20\frac{n*(n+1)}{2}}
[Prob2BigIdea]: https://latex.codecogs.com/png.latex?{\sum_{i=0}^{\lfloor999/3\rfloor}3*i%20+%20\sum_{i=0}^{\lfloor\999/5\rfloor}5*i%20-%20\sum_{i=0}^{\lfloor\999/15\rfloor}15*i}



PS- hat tip to CogeCogs.com - check out their awesome [latex editor](https://www.codecogs.com/eqnedit.php) and image-generation service.
