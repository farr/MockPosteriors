import jax.numpy as jnp
import numpyro
import numpyro.distributions as dist

def normal_normal_model(x_obs, sigma_obs):
    n = x_obs.shape[0]

    mu = numpyro.sample('mu', dist.Normal(0, 1))
    sigma = numpyro.sample('sigma', dist.HalfNormal(1))

    sigma_full = jnp.sqrt(sigma*sigma + sigma_obs*sigma_obs)

    _ = numpyro.sample('xobs', dist.Normal(mu, sigma_full), obs=x_obs)
