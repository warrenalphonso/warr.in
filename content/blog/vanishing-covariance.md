Title: What’s So Bad About a Vanishing Covariance?
Date: 2023-07-06

# Context

Consider a fully-connected network:

-   linear activation
-   $L$ layers
-   each layer has $n$ neurons
-   biases are all initialized to 0
-   weights are initialized with a Gaussian with mean 0 and variance $\frac{C_W}{n_{l-1}}$
    for some $C_W$. We choose this variance because [variance of a Gaussian sum is
    sum of Gaussian variances](https://en.wikipedia.org/wiki/Sum_of_normally_distributed_random_variables).
    We choose a Gaussian distribution because practical networks are very wide, and
    the [CLT](https://en.wikipedia.org/wiki/Central_limit_theorem) tells us that
    only up to the second cumulant is preserved so we might as well use a Gaussian.
-   we won't train the network. That makes things more complicated because weights
    wouldn't be independent anymore.

Let's consider the covariances between activations in the same layer. For the first
layer,

$$\begin{aligned}E[z_{i_1; \alpha_1}^{(1)} z_{i_2 \alpha_2}^{(1)}] &= \sum_{j_1, j_2=1}^{n_0} E[ W_{i_1 j_1}^{(1)} x_{j_1; \alpha_1} W_{i_2 j_2}^{(1)} x_{j_2 ; \alpha_2} ] = \sum E[W_{i_1 j_1}^{(1)} W_{i_2 j_2}^{(1)}] x_{j_1; \alpha_1} x_{j_2 ; \alpha_2}\\\\ &= \sum_{j_0, j_1=1}^{n_0} \frac{C_W}{n_0} \delta_{i_1 i_2} \delta_{j_1 j_2} x_{j_1; \alpha_1} x_{j_2; \alpha_2} \\\\ &= \delta_{i_1 i_2} \frac{C_W}{n_0} \sum_{j=1}^{n_0} x_{j; \alpha_1} x_{j; \alpha_2} \\\\ &= \delta_{i_1 i_2} C_W G_{\alpha_1 \alpha_2}^{(0)} \end{aligned}$$
where $G_{\alpha_1 \alpha_2}^{(0)}$ is a new variable for this inner product between
samples.

For later layers,
$$ E[z_{i_1; \alpha_1}^{(l+1)} z_{i_2; \alpha_2}^{(l+1)}] = \delta_{i_1 i_2} C_W \frac{1}{n_l} \sum_{j=1}^{n_l} E[z_{j; \alpha_1}^{(l)} z_{j; \alpha_2}^{(l)}] = \delta_{i_1 i_2} C_W G_{\alpha_1 \alpha_2}^{(l)}$$
where we introduce a generalized $G_{\alpha_1 \alpha_2}^{(l)}$. Notice that since
$G$ is inner product of two inputs divided by number, it's basically expectation
with $i_1 = i_2$. Thus,
$$G_{\alpha_1 \alpha_2}^{(l+1)} = \frac{1}{n_{l+1}} \sum_{j=1}^{n_{l+1}} E[z_{j; \alpha_1}^{(l+1)} z_{j; \alpha_2}^{(l+1)}] = \frac{1}{n_{l+1}} \sum^{n_{l+1}} C_W G_{\alpha_1 \alpha_2}^{(l)} = C_W G^{(l)}_{\alpha_1 \alpha_2}$$

And so we find that **the covariance matrix for layer $l$ is:**

-   0 if $i_1 \neq i_2$
-   $G_{\alpha_1 \alpha_2}^{(l)} = (C_W)^l G_{\alpha_1 \alpha_2}^{(0)}$ if $i_1 = i_2$

**It looks like we have a vanishing or exploding covariance unless we set $C_W=1$!**

(This derivation is from Chapter 3 of
[_Principles of Deep Learning Theory_](https://deeplearningtheory.com/). Fantastic
book so far, by the way.)

# Interpretations

Glorot and He initialization are derived by keeping the covariance stable, but I
think the motivation there is to make gradients behave nicely.
Here I just want to consider the forward-pass of a randomly initialized network.
Is there any reason we'd want the covariances to not explode or vanish?

## What Even Is Covariance?

Positive covariance means if one variable deviates from its mean, the other one
linearly deviates from its mean in the same direction. Negative means there's an
inverse linear relationship. If it's zero, there's no linear relationship between
deviations.

We've calculated covariance of preactivations at each layer. So instantiation to
instantiation, how does preactivation of neuron $i$ in layer $l$ deviate from 0
for input $\alpha$ versus input $\beta$? Let's think about magnitude for now.

If covariance for a preactivation is 0 between two different inputs, then the
preactivation cannot distinguish between the inputs. There's no data dependence.
That's no bueno.

If covariance for a preactivation is $\pm \infty$ between two different inputs,
there's too much data dependence. If $Cov(X, Y) = E[(X-E[X])(Y-E[Y])]=\infty$ then,
on an average instantiation, if $X$ is above its average $Y$ is infinitely above
its average. That seems bad. Consider the preactivations in the output layer;
they're hugely different in each instantiation.

## This $G_{\alpha_1 \alpha_2}^{(0)}$ Thing Should Probably Be Meaningful

If we set $C_W=1$, then $G_{\alpha_1 \alpha_2}^{(l)} = G_{\alpha_1 \alpha_2}^{(0)}$.

If $\alpha_1 = \alpha_2$, this becomes squared norm divided by length. That's fine,
it's just some constant.

Some alarm bells started going off when I considered different inputs though.
If $\alpha_1 \neq \alpha_2$ the covariance
at later layers is proportional to the dot product of the two inputs. That's
typically a meaningless quantity unless we normalize the inputs! We probably want
two very similar vectors to have positive covariance and two nearly orthogonal
vectors to have zero covariance, but if the two nearly orthogonal vectors have
huge magnitude they might have same covariance as two smaller vectors with similar
direction.

Should we always rescale inputs so they've got the same norm? Well, this makes
the inner product capture how similar two directions are but it's throwing away the
magnitude of the vectors, so I don't think this generally works. We probably don't
want to consider a $24 \times 24$ white image with only a tiny amount of gray in
the first pixel equivalent to a white image with a very black first pixel.
So really the point is that you should be paying attention to the scale of the
components of your input vectors. You might want to normalize or center them.
