# MockPosteriors
Showing a common error in mocking up posteriors.  If the measurement error
(observational uncertainty) is made to depend on the *latent*, *true* parameters
of each observation, but this is not accounted for in the analysis (usually we
assume that the measurement uncertainty is known and fixed), then one obtains
biased results from population analyses.

In my own work, I have sometimes **incorrectly** assumed, for example, that the
uncertainty in our measurements of some binary coalescence from gravitaitonal
waves scales inversely with the ideal S/N of the waveform, often written
`sqrt(<h|h>)`.  Such an assumption will introduce bias, because the uncertainty
depends on the latent parameters in the fit.  Instead, one should imagine that
the uncertainty depends on the matched filter S/N in some mock data (one does
not need actual mock data to draw a random matched-filter S/N if one assumes
that the data consist of Gaussian noise), `<d|h>/sqrt(<h|h>)`, that is, on the
actual observed data, which is conditioned on in the analysis and therefore
fixed indpendent of the values of the latent parameters explored.
