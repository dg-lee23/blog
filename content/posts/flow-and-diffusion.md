---
title: "What Actually \"Flows\" in Flow Models?"
date: 2026-02-01
draft: false
tags: ["Generative AI", "Diffusion", "Flow"]
summary: "How to transport noise into data using ODEs"
showToc: false
weight: 1
---

### Motivation
Generative models aim to find the link between the latent distribution $p_\text{init}$ (noise) and the data distribution $p_\text{data}$. Let us frame this as a **transportation** problem:

> **Generation as Transport**
> 
> Generation is *transporting* samples from $p_\text{init}$ to the $p_\text{data}$ manifold by following a "flow".

Think of *flow* as a time-dependent vector field that represents velocity. Then, generation is as simple as:

> 1. Sample from $p_\text{init}$.
> 2. Follow the velocity lines.
> 3. We end up in the data manifold, $p_\text{data}$.

Let us formulate this more cleanly in the language of Ordinary Differential Equations (ODEs).


### The ODE Framework
Suppose we start at an initial position $X_0\sim p_\text{init}$ and move along a **path** $X_t$ dictated by a (time-varying) **vector field** $u_t$. In ODE-terms,

<div id="eq.1">
$$\frac{d}{dt} X_t = u_t(X_t), \quad t\in[0,1] \tag{1}$$
</div>

Simply, $u_t$ is the velocity at each position. 

<mark>**Flow models** parameterize this vector field with a neural network $u_t^{\theta}$ </mark>. Once learning is done, we can sample any $X_0 \sim p_{\text{init}}$ and use numerical methods to solve the ODE above for generation. Euler's method is a solid choice:


<div id="eq.2">
$$X_{t+h} \approx X_t + h\cdot u_t(X_t) \tag{2}.$$
</div>

> **Flow Models**
>
> Flow models aim to train $u_t^{\theta}$ such that it will transport any $X_0 \sim p_{\text{init}}$ to $X_1\sim p_{\text{data}}$.

But how do we construct such vector fields? What is our training target?


### Probability Paths
We need to construct $u_t$, but all we have is samples from $p_{\text{data}}$. Therefore, let us simplify the problem by fixing *one* specific data point $z$. Our simplified goal becomes finding a **conditional vector field** $u_t(\cdot|z)$ that forces the transport:

$$p_{\text{init}} \rightarrow \delta_z $$

where $\delta_z$ is a Dirac-delta distribution. It is natural to consider what happens **between** these boundaries; thus, we define a **conditional probability path**  $\lbrace p_t(x|z) \rbrace_t$ that anchors the flow:

<div id="eq.3">
$$p_0(\cdot | z) = p_{\text{init}} \qquad p_1(\cdot | z) = \delta_z  \tag{3}$$
</div>

Among various possible paths, we present the simplest example below.

<details>
  <summary style="cursor: pointer; color: #007bff; font-weight: bold;">
    Example: Gaussian Probability Paths
  </summary>

  <div style="padding: 10px; border-left: 2px solid #007bff; margin-top: 10px;">

  A common choice is the **Gaussian Probability Path.** To satisfy the boundary condition in [Eq. 3](#eq.3), a natural construction would be:

  $$p_t(\cdot | z) = \mathcal{N}(\alpha_tz, \beta_t^2I_d)$$

  where $\alpha_t, \beta_t$ are *noise schedulers*. To satisfy the boundary conditions, we need 

  $$\alpha_0=\beta_1=0 \quad \text{\small (making $p_0=\mathcal{N}(0, I_d)$)}$$
  
  $$\alpha_1=\beta_0=1 \quad \text{\small (making $p_1=\delta_z$)}$$
  </div>
</details>

In most cases, the **conditional vector field** that induces the transport $p_{\text{init}} \rightarrow \delta_z $ is easy to find (by hand). Again, we continue the example with Gaussian probability paths.

<details>
  <summary style="cursor: pointer; color: #007bff; font-weight: bold;">
    Example: Deriving Conditional Target Vector Fields
  </summary>

  <div style="padding: 10px; border-left: 2px solid #007bff; margin-top: 10px;">

  The problem becomes trivial once it is nicely stated (try it yourself!).

  <div style="background-color: #f4f4f459; padding: 15px; border-left: 5px solid #ccc;">
    <b>Problem.</b>
    <br>
    Find the vector field $u_t(x|z)$ that induces the flow for the Gaussian path
    $$x_t \sim p_t(x|z) = \mathcal{N}(\alpha_tz, \beta_t^2I_d)$$
    <br>
    according to the ODE $\frac{dx_t}{dt} = u_t(x_t|z).$
  </div>

  <div><br></div>
  
  **Solution.**

  All we have to do is calculate the time derivative of $x_t$. We thus use the **reparameterization trick** and write:
  
  $$x_t = \alpha_t z + \beta_t \epsilon, \qquad \epsilon\sim\mathcal{N}(0,I)$$

  Then,

  $$\frac{dx_t}{dt}=\dot{\alpha}_t z + \dot{\beta}_t \epsilon = u_t(x_t | z)$$

  where ${\small \dot{\alpha}_t = \partial_t \alpha_t, \dot{\beta}_t = \partial_t \beta_t}$ denote the time derivatives. 
  
  Eliminating $\epsilon$ and fixing the notation with ($x_t \rightarrow x$) gives:

  $$
  \begin{aligned}
      u_t( x | z)  &= \dot{\alpha}_t z + \dot{\beta}_t (\frac{x_t - \alpha_tz}{\beta_t}) \\\\
                   &= (\dot{\alpha_t} - \frac{\dot{\beta_t}}{\beta_t}\alpha_t)z + \frac{\dot{\beta_t}}{\beta_t}x
  \end{aligned}
  $$


  </div>
</details>


### The Continuity Equation
We showed that the conditional vector fields $u_t(x|z)$ are easy to find, but what we need is the **marginal vector field** $u_t(x)$, which works for the entire dataset. 

To derive $u_t(x)$, we must first introduce the **continuity equation**.

> **The Continuity Equation** 
>
> $$\underbrace{\frac{\partial}{\partial t} p_t}_{\text{net inflow}} + \underbrace{\nabla \cdot (p_tu_t)}_{\text{net outflow}}=0$$

Intuitively, the equation states that **<span style="color:#007bff;">probability mass is conserved</span>**. This is a necessary condition that our vector fields must satisfy; otherwise, probability *leaks* during the transport process.


### The Marginalization Trick
Suppose we are given $z$. We can construct a probability path $p_t(x|z)$ (e.g. Gaussian) and analytically find the corresponding vector field $u_t(x|z)$. That is, we have a "local" solution: a pair $(p_t(x|z), u_t(x|z))$, that should satisfy the continuity equation:

$$\frac{\partial}{\partial t}p_t(x|z) + \nabla \cdot (p_t(x|z)u_t(x|z)) = 0$$

Our goal is to find a "global" vector field that works for the entire dataset—we need to eliminate $z$, by averaging over it.

We multiply both sides by $p_\text{data}(z)$ and integrate to get

$$\int \frac{\partial}{\partial t}p_t(x|z) {\color{red}{p_\text{data}(z)}} dz + \int \nabla \cdot (p_t(x|z)u_t(x|z)) {\color{red}{p_\text{data}(z)}} dz = 0$$

Since the derivatives are w.r.t. $t$ and $x$, and the integral is over $z$, we can swap orders:

$$\frac{\partial}{\partial t} \int {p_t(x|z) p_\text{data}(z)} dz + \nabla \cdot ( \int p_t(x|z)u_t(x|z) {p_\text{data}(z)} dz ) = 0$$

The first term is the **marginal distributuion** $p_t(x)$, defined as

$$p_t(x) = \int p_t(x|z)p_{\text{data}}(z) dz$$

We then have:

$$\frac{\partial}{\partial t} p_t(x) + \nabla \cdot ( \int p_t(x|z)u_t(x|z) {p_\text{data}(z)} dz ) = 0$$

To make the second term match the form of the continuity equation, we define the **marginal vector field** $u_t(x)$ such that:

<div id="eq.6">
$$u_t(x) = \int u_t(x|z) \frac{p_t(x|z) p_{\text{data}}(z)}{p_t(x)} dz \tag{6} $$
</div>

Note the trick here—we have defined $u_t(x)$ such that the marginal pair $(p_t(x), u_t(x))$ also satisfies the continuity equation.

While we are fortunate to have $u_t(x)$ in closed form, it remains **intractable** (we cannot integrate over all $z$). Nevertheless, we actually don't need to compute this integral, as we will see in the next section.


### The Flow Matching Loss
With the marginal vector field $u_t(x)$ defined in [Eq. 6](#eq.6), the target for our neural network $u_t^{\theta}$ is clear. The definition of **flow matching loss** comes naturally:

<div id="eq.7">
$$\mathcal{L}_{\text{FM}}(\theta) = \mathbb{E}_{t \sim U, x \sim p_t} [|| u_t^{\theta}(x) - u_t(x)  ||^2] \tag{7}$$
</div>

where $U$ is a uniform distribution over $[0,1]$. Since $u_t(x)$ is intractable whatsoever, we consider its "local" counterpart: the conditional vector field $u_t(x|z)$. The **conditional flow matching loss** is defined as:

<div id="eq.8">
$$\mathcal{L}_{\text{CFM}}(\theta) = \mathbb{E}_{t \sim U, z \sim p_{\text{data}}, x \sim p_t(\cdot|z)} [|| u_t^{\theta}(x) - u_t(x | z) ||^2] \tag{8}$$
</div>

The essential idea is: since we average over all data points $z$ anyways, wouldn't minimizing the "local" loss $\mathcal{L}_{\text{CFM}}$ also minimize the "global" loss $\mathcal{L}_{\text{FM}}$?

> **Theorem.**
>
> The losses $\mathcal{L}_{\text{FM}}(\theta)$ and $\mathcal{L}_{\text{CFM}}(\theta)$ are equivalent (up to a constant). Specifically, they share the same gradients:
> $$\nabla_{\theta} \mathcal{L}_{\text{FM}}(\theta) = \nabla_{\theta} \mathcal{L}_{\text{CFM}}(\theta)  $$

### Proof
We first expand $\mathcal{L}_{\text{FM}}$ and $\mathcal{L}_{\text{CFM}}$ respectively. Note that the terms $||u_t(x)||^2$ and $||u_t(x|z)||^2$ do not depend on our parameter $\theta$, so we can treat them as constants $C_1, C_2$.

$$
\begin{aligned}
    \mathcal{L}_{\text{FM}} &= \mathbb{E}_{t \sim U, x \sim p_t} [|| u_t^{\theta}(x) ||^2] - 2 \mathbb{E}_{t \sim U, x \sim p_t} [u_t^{\theta}(x)^T {\color{blue}{u_t(x)}}] + C_1 \\\\
\end{aligned}
$$

$$
\begin{aligned}
    \mathcal{L}_{\text{CFM}} &= \mathbb{E}_{t \sim U, z \sim p_{\text{data}}, x \sim p_t(\cdot|z)} [|| u_t^{\theta}(x) ||^2] - 2 \mathbb{E}_{t \sim U, z \sim p_{\text{data}}, x \sim p_t(\cdot|z)} [u_t^{\theta}(x)^T {\color{red}{u_t(x|z)}}] + C_2 \\\\
\end{aligned}
$$

The first terms are identical since $\mathbb{E}_{t,z,x}[f(x)] = \mathbb{E}_{t,x}[f(x)]$. It remains to compare the inner product terms. By substituting our definition of the marginal vector field $u_t(x)$ from [Eq. 6](#eq.6):

$$
\begin{aligned}
    \mathbb{E}_{t \sim U, x \sim p_t} [u_t^{\theta}(x)^T {\color{blue}{u_t(x)}}] &= \int \int p_t(x) u_t^{\theta}(x)^T \left[ \int u_t(x|z) \frac{p_t(x|z) p_{\text{data}}(z)}{p_t(x)} dz \right] dx dt \\\\
    &= \int \int \int u_t^{\theta}(x)^T u_t(x|z) p_t(x|z) p_{\text{data}}(z) dz dx dt \\\\
    &= \mathbb{E}_{t \sim U, z \sim p_{\text{data}}, x \sim p_t(\cdot|z)} [u_t^{\theta}(x)^T {\color{red}{u_t(x|z)}}]
\end{aligned}
$$

Since the inner products (and thus the gradients) are identical, the theorem follows. 

The key takeaway is that:
> By simply training our network to point toward individual data points $z$, it **automatically** learns to follow the complex, marginal flow of the entire distribution.

We end the post with an example of explicitly calculating $\mathcal{L}_{\text{CFM}}$.

<details>
  <summary style="cursor: pointer; color: #007bff; font-weight: bold;">
    Example: $\mathcal{L}_{\text{CFM}}$ for Gaussian Paths
  </summary>

  <div style="padding: 10px; border-left: 2px solid #007bff; margin-top: 10px;">

  Let us explicitly compute $\mathcal{L}_{\text{CFM}}$ in the case of Gaussian probability paths, 
  
  $$p_t(x|z) = \mathcal{N}(\alpha_tz, \beta_t^2I_d) $$
  
  In this case, $x_t \sim p_t(\cdot | z)$ implies:

  $$x_t = \alpha_tz + \beta_t\epsilon$$

  where $\epsilon \sim \mathcal{N}(0, I_d)$.
  
  Recall from [Eq. 5](#eq.5) that the conditional vector field was found to be:

  $$u_t( x | z) =  (\dot{\alpha_t} - \frac{\dot{\beta_t}}{\beta_t}\alpha_t)z + \frac{\dot{\beta_t}}{\beta_t}x$$

  Then, by [Eq. 8](#eq.8),

  $$
  \begin{aligned}
      \mathcal{L}_{\text{CFM}} &= \mathbb{E}_{t \sim U, z\sim p_{\text{data}}, x \sim p_t} [|| u_t^{\theta}(x) - (\dot{\alpha_t} - \frac{\dot{\beta_t}}{\beta_t}\alpha_t)z - \frac{\dot{\beta_t}}{\beta_t}x ||^2] \\\\
                               &= \mathbb{E}_{t \sim U, z\sim p_{\text{data}}, \epsilon \sim \mathcal{N}(0, I_d)} [ || u_t^{\theta}(\alpha_tz + \beta_t\epsilon) - (\dot{\alpha}_tz + \dot{\beta}_t\epsilon)||^2]
  \end{aligned}
  $$

  The expression above can be further simplified if we explicitly set $\alpha_t=t, \beta_t=1-t$. We obtain:

  $$\mathcal{L}_{\text{CFM}} = \mathbb{E}_{t \sim U, z\sim p_{\text{data}}, \epsilon \sim \mathcal{N}(0, I_d)} [ || u_t^{\theta}(tz + (1-t)\epsilon) - (z-\epsilon)||^2] $$

  Note that both the sampling procedure (of $t, z, \epsilon$) and the computation of each term is incredibly simple.

  </div>
</details>

### Remarks & Bibligraphy
This post presents my understanding of the MIT course *Introduction to Flow Matching and Diffusion Models* (Holderrieth & Erives, 2025). Refer to the [original source](https://diffusion.csail.mit.edu/) for further details and explanations.