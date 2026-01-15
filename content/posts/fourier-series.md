---
title: "Fourier Series"
date: 2026-01-13
draft: false
tags: ["Analysis", "Fourier Series"]
summary: "How far can we get with trigonometric functions?"
showToc: false
weight: 1
---


### The Motivating Problem
Here's a bold claim that Fourier made in the 19th century:

> **Fourier's Claim**
>  
> Every **reasonable** periodic function $f$ can be expressed as an infinite linear combination of sines and cosines. That is, for some $a_n, b_n$,
> $$f(x) = a_0 + \sum_{n=1}^{\infty} (a_n\cos nx + b_n\sin nx)$$


**Reasonable** allows sharp corners and jumps (discontinuities)—but wait, is that really possible? Can an infinite sum of *smooth* functions (sines/cosines) converge to sharp corners or jumps? 

Thus follows the central question of this post: 

> If we treat sine and cosine as a **basis** for a function space $X$, what exactly is $X$, and how do we prove it spans the space?



### Notation
To get started, using the exponential form via Euler's formula keeps things tidy:

$$a_0 + \sum_{n=1}^{N} (a_n\cos nx + b_n\sin nx) = \sum_{n=-N}^{N}c_ne^{inx}, $$

where $a_n, b_n, c_n \in \mathbb{C}$. Finding the expression of $c_n$ in terms of $a_n, b_n$ is left as an exercise. Letting $u_n(x)=e^{inx}$ and $\mathcal{B}=\lbrace u_n : n \in \mathbb{Z} \rbrace$ turns our question into
 > Which function space $X$ is $\mathcal{B}$ a basis of?


<details>
  <summary style="cursor: pointer; color: #007bff; font-weight: bold;">
    Exercise Answer
  </summary>

  <div style="padding: 10px; border-left: 2px solid #007bff; margin-top: 10px;">

  $$c_n = \frac{a_n-ib_n}{2}, \quad c_{-n} = \frac{a_n + ib_n}{2}, \quad c_0=a_0$$

  </div>
</details>

### The Function Space $\mathcal{R}^2$
To talk about convergence, distance must be defined in $X$. As an extension of dot products, it is natural to define the inner product of $X$ as:

$$\langle f, g\rangle = \frac{1}{2\pi}\int_{I}f\bar{g}$$

Since we deal with periodic functions, we set $I=[-\pi, \pi]$. The distance (norm) is then:

$$||f||^2 = \langle f, f \rangle = \cfrac{1}{2\pi} \int_{-\pi}^{\pi} |f|^2 $$

The coefficient $\frac{1}{2\pi}$ will be justified soon. For this norm to be well-defined, we must limit our function space $X$ such that its functions satisfy $\int |f|^2 < \infty$. We give the name $\mathcal{R}^2[-\pi, \pi]$, or simply $\mathcal{R}^2$, to this space.


### Orthogonality
The set $\mathcal{B} = \lbrace e^{inx}: n\in \mathbb{Z} \rbrace$ is **orthonormal**, which is easy to see via direct algebra. If $n\neq m,$

$$
\begin{aligned}
    \langle u_n, u_m \rangle &= \frac{1}{2\pi} \int_{-\pi}^{\pi} e^{inx} e^{-imx} dx \\\\
                             &= \frac{1}{2\pi} \int_{-\pi}^{\pi} e^{i(n-m)x} dx     \\\\
                             &= 0  \\\\
\end{aligned}
$$

since integration of sines and cosines over their full period is zero. When $n=m$, $\langle u_n, u_m \rangle = 1$, which justifies the mysterious $\frac{1}{2\pi}$ in our inner product.


### Basis of a Function Space
While $\mathcal{B}$ is orthonormal, does it span the whole space $\mathcal{R}^2$? In function spaces (which are infinite dimensional), a **basis** must satisfy the following condition:

> **Basis Condition** 
> 
> $\forall f\in X$, we can get arbitrarily close to $f$ with a finite linear combination of basis vectors. Let such linear combination, with $n$ terms, be $s_n$; then the condition is
> $$ \lim_{n \rightarrow \infty} ||f - s_n|| = 0$$

Then given $f$, how do we find the "best" coefficients $\lbrace c_k \rbrace$ for approximating $f$ with a finite sum $s_n = \sum^{n}_{k=-n} c_k u_k$?


### The Dirichlet Kernel
Linear algebra tells us the answer:  **projection**. Project the given function $f$ onto the span of $\mathcal{B}$, and look for the coefficients.

> **Proposition 1.**
>  
> $c_n = \langle f, u_n\rangle$ minimizes the distance $||f - s_n||$. For other arbitrary coefficients $\lbrace z_n \rbrace$,
> $$\left\lVert f - \sum_{n=-N}^{N} c_n u_n \right\rVert \leq \left\lVert f - \sum_{n=-N}^{N} z_n u_n \right\rVert, \quad {\small N=1,2,\dots} $$


<details>
  <summary style="cursor: pointer; color: #007bff; font-weight: bold;">
    Proof
  </summary>

  <div style="padding: 10px; border-left: 2px solid #007bff; margin-top: 10px;">

  We first compute the following inner product:

  $$ \left\langle f - \sum_{k=-n}^{n} c_k u_k , \sum_{k=-n}^{n} (c_k-z_k)u_k \right\rangle $$
  $$ = \sum_{k=-n}^{n} (\bar{c_k} - \bar{z_k}) \langle f, u_k \rangle - \sum_{ \substack{m, \\ k=-n} }^{n} c_m (\bar{c_k} - \bar{z_k}) \langle u_m, u_n \rangle $$
  $$ = \sum_{k=-n}^{n} (\bar{c_k} - \bar{z_k})c_k - \sum_{k=-n}^{n} c_k(\bar{c_k} - \bar{z_k}) = 0$$

  Therefore the two vectors are orthogonal. Then the pythagorean theorem yields:

  $$ \left\lVert f - \sum_{k=-n}^{n} c_k u_k  \right\rVert^2 + \left\lVert \sum_{k=-n}^{n} (c_k - z_k)u_k \right\rVert^2 = \left\lVert f - \sum_{k=-n}^{n} z_k u_k \right\rVert^2 $$

  The proposition follows.
  </div>
</details>

By substituting the definition of $c_n$, we find:

$$
\begin{aligned}
    s_n(f,x) &= \sum_{k=-n}^{n} c_n u_n(x) \\\\
             &= \sum_{k=-n}^{n} [\cfrac{1}{2\pi} \int_{-\pi}^{\pi}f(t)e^{-ikt} dt] e^{ikx}  \\\\
             &= \cfrac{1}{2\pi} \int_{-\pi}^{\pi} f(t) [\sum_{k=-n}^{n} e^{ik(x-t)}] dt
\end{aligned}
$$

The term inside brackets is known as the **Dirichlet Kernel**:

$$
    D_n(x) = \sum_{k=-n}^n e^{ikx} 
           = \cfrac{\sin(n+\frac{1}{2})x}{\sin\frac{x}{2}}.
$$

<div id="proof-dirichlet"></div> <details> 
  <summary style="cursor: pointer; color: #007bff; font-weight: bold;">
    Proof 
  </summary>

  <div style="padding: 10px; border-left: 2px solid #007bff; margin-top: 10px;">

  Using the geometric series formula:
  
  $$
  \begin{aligned}
    \sum_{k=1}^{n} e^{ikx} &= e^{ix}\frac{1 - e^{inx}}{1 - e^{ix}} \\
                           &= \frac{e^{inx/2} - e^{-inx/2}}{e^{ix/2} - e^{-ix/2}} e^{i(n+1)x/2} \\
                           &= \frac{\sin \frac{nx}{2}}{\sin \frac{x}{2}} e^{i(n+1)x/2}
  \end{aligned}
  $$

  Taking the real part:

  $$
  \begin{aligned}
    \sum_{k=1}^{n} \cos kx &= \frac{\sin\frac{nx}{2} \cos\frac{(n+1)x}{2}}{\sin\frac{x}{2}} \\
                           &= -\frac{1}{2} + \frac{1}{2} \frac{\sin(n+\frac{1}{2})x}{\sin\frac{x}{2}}
  \end{aligned}
  $$

  Since $D_n(x) = 1 + 2\sum_{k=1}^{n} \cos kx$, the result follows. It is noteworthy that
  
  $$\int_{-\pi}^{\pi} D_n(x)  dx = 2\pi.$$

  </div>
</details>

For later use, we further expand $s_n$ as follows.

$$
\begin{aligned}
s_n(f,x) &= \cfrac{1}{2\pi} \int_{-\pi}^{\pi} f(t)D_n(x-t) dt \\\\
         &= \cfrac{1}{2\pi} \int_{x+\pi}^{x-\pi} f(x-u)D_n(u) (-du) \qquad ({\small u=x-t})\\\\
         &= \cfrac{1}{2\pi} \int_{-\pi}^{\pi} f(x-t)D_n(t) dt \qquad (\text{\small integration over full period}) \\\\
         &= \cfrac{1}{\pi} \int_{\color{red}{0}}^{\color{red}{\pi}} \cfrac{f(x+t)+f(x-t)}{2}D_n(t) (dt) \qquad ({\small D_n \text{ is even}})
\end{aligned}
$$


### End of the Story?
Not quite. So far, we have showed that $s_n(f)$ is the best approximation of $f$ with respect to the norm $||\cdot||$. However, does it satisfy the **basis condition**? We must show that
$$\int_{-\pi}^{\pi} | f(x) - \frac{1}{2\pi}(\int_{-\pi}^{\pi} f(t)D_n(x-t) dt) |^2 dx$$ 
will get arbitrarily small, which turns out to be surprisingly hard. The main problem is that it is hard to bound integrals involving $|D_n|$, since the integral $\int |D_n|$ is unbounded. 

Let's look for an alternative. 


### The Fejér Sum
We define the **Fejér sum** $\sigma_n(f)$ as

$$ 
\begin{aligned}
    \sigma_n(f) &= \cfrac{1}{n} [s_0(f) + s_1(f) + ... + s_{n-1}(f)] \\\\
                &= \cfrac{1}{n\pi} \int_0^{\pi} \cfrac{f(x+t)+f(x-t)}{2} [\sum_{k=0}^{n-1} D_k(t)] dt \\\\
                &= \cfrac{1}{n\pi} \int_0^{\pi} \cfrac{f(x+t)+f(x-t)}{2} K_n(t) dt 
\end{aligned}
$$

where $K_n(t)$ is known as the Fejér kernel -- the **average** of Dirichlet kernels, which provides a smoothing effect. Since $\sigma_n$ is simply an average of $s_n$, it is still in the span of $\mathcal{B}$. Also,
$$
    K_n(t) = \sum_{k=0}^{n-1} D_k(t) 
           = \frac{1}{n} \frac{\sin^2(\frac{nt}{2})}{\sin^2(\frac{t}{2})}
           \geq 0
$$

<details>
  <summary style="cursor: pointer; color: #007bff; font-weight: bold;">
    Proof
  </summary>

  <div style="padding: 10px; border-left: 2px solid #007bff; margin-top: 10px;">

  $$
  \begin{aligned}
    K_n(t) &= \frac{1}{n}[D_0(t) + D_1(t) + ... D_{n-1}(t)] \\\\
           &= \frac{1}{n} \frac{1}{\sin\frac{t}{2}}[\sin\frac{t}{2} + \dots + \sin (n-\frac{1}{2})t]
  \end{aligned}
  $$

  Now recall that (see proof for the Dirichlet kernel)

  $$ \sum_{k=1}^{n} e^{ikx} = \frac{ \sin \frac{nx}{2}}{ \sin \frac{x}{2}} e^{i(n+1)x/2} $$

  It follows that

  $$ \sum_{k=1}^{n} e^{i(k-1/2)t} =  \frac{ \sin (\frac{nt}{2})}{ \sin (\frac{t}{2})} e^{int/2} $$

  Now taking the imaginary part of both sides yields:

  $$\sum_{k=1}^{n} \sin (k - \frac{1}{2})t = \frac{\sin^2 (\frac{nt}{2})}{\sin (\frac{t}{2})}$$

  The statement follows.

  </div>
</details>

What useful properties does $K_n$ have that $D_n$ doesn't? Well first, $K_n(t)$ is **positive**. More distinctly, for fixed $\delta \in (0, \pi)$,

$$0 \leq K_n(t) \leq  \frac{1}{n\sin^2(\frac{\delta}{2})}, \qquad {\small t\in[\delta, \pi], n=1,2,\dots}$$

$K_n$ is bounded, but so is $D_n$ on $[\delta, \pi]$. The important distinction is that $K_n$ (uniformly) converges to zero. This is what makes the Fejér kernel *nicer* than Dirichlet's.


### Fejér's Theorem
With the better tool on our hand, can we finally prove the basis condition? Not yet, but we're very close. Let us detour a little bit and prove the following proposition.

> **Proposition 2.**
> If $f$ is a **continuous** (periodic) function, then $$\lim_{n\rightarrow \infty} ||\sigma_n(f) - f|| = 0 $$
> That is, $\mathcal{B}$ is a basis of $\mathcal{C} \subsetneq \mathcal{R}^2$.

We used $\mathcal{C}$ to denote the set of continuous functions, which is (obviously) a strict subset of $\mathcal{R}^2$. In the proof below, look for parts where the Dirichlet kernel would fail.


### Proof
Let $\epsilon > 0, x\in I$ be given. Our goal is to bound $|\sigma_n(f, x) - f(x)|$. By definition,

$$
\begin{aligned}
    |\sigma_n(f,x) - f(x) | &= |\cfrac{1}{\pi}\int_0^{\pi} (\cfrac{f(x+t)+f(x-t)}{2}-f(x))K_n(t) dt| \\\\
                            &= |\cfrac{1}{\pi}\int_0^{\pi} g_x(t)K_n(t) dt|
\end{aligned}
$$

We used the fact that $\int_0^{\pi} K_n = \pi$ above (see the proof [here](#proof-dirichlet) if confused), and also defined $$g_x(t) = \cfrac{f(x+t)+f(x-t)}{2}-f(x).$$

Notice that $$\lim_{t\rightarrow 0^+} g_x(t) = 0,$$ 

<details>
  <summary style="cursor: pointer; color: #007bff; font-weight: bold;">
    Why?
  </summary>

  <div style="padding: 10px; border-left: 2px solid #007bff; margin-top: 10px;">

  Since $f$ is continuous, $\forall \epsilon>0, \enspace \exists \delta > 0 $ such that 

  $$|t| < \delta \implies |f(x+t)-f(x)| < \epsilon $$  

  Hence if $0 < t < \delta$,

  $$|f(x\pm t)-f(x)| < \epsilon $$

  Then 

  $$  |g_x(t)| \leq \frac{1}{2}( |f(x+t)-f(x)| + |f(x-t)-f(x)|) \leq \epsilon  $$


  </div>
</details>

so our strategy becomes **divide and conquer**; $g_x$ is tiny on $(0, \delta)$, and $K_n$ is tiny on $(\delta, \pi)$ for sufficiently large n.

Hence, we first take $\delta\in (0, \pi)$ such that

$$0<t<\delta \implies |g_x(t)|<\epsilon.$$

It follows that

$$
\begin{aligned}
    |\sigma_n(f,x) - f(x) | &\leq |\cfrac{1}{\pi}\int_{\color{red}{0}}^{\color{red}{\delta}} g_x(t)K_n(t) dt| + |\cfrac{1}{\pi}\int_{\color{red}{\delta}}^{\color{red}{\pi}} g_x(t)K_n(t) dt| \\\\
                            &\leq |\cfrac{\epsilon}{\pi}\int_0^{\delta}K_n(t)dt| + |\frac{1}{n\pi\sin^2(\frac{\delta}{2})}\int_{\delta}^{\pi}|g_x(t)|dt| \\\\
                            &\leq \epsilon + \frac{M}{n}
\end{aligned}
$$
where $|\frac{1}{n\pi\sin^2(\delta/2)}\int_{\delta}^{\pi}|g_x(t)|dt| \leq M$ ($g$ is continuous and thus bounded). Then taking $N$ such that
$$n\geq N \implies \frac{M}{n} \leq \epsilon$$

leads to the conclusion that

$$
\begin{aligned}
n \geq N, x\in I &\implies |\sigma_n(f,x) - f(x) | < 2\epsilon \\\\
                          &\implies \lim_{n\rightarrow \infty} ||f - \sigma_n(f)|| = 0. 
\end{aligned}
$$


### Beyond $\mathcal{C}$
We have shown that $\mathcal{B}$ is a basis of $\mathcal{C}$. This is impressive, but also quite reasonable from our intuitions. But what about $\mathcal{R}^2$? Actually, $\mathcal{C}$ is **dense** in $\mathcal{R}^2$; that is, to formally put,

> **Proposition 3.**
>
> Given $\epsilon > 0$ and $f \in \mathcal{R}^2$, there exists $g\in\mathcal{C}$ such that
> $$ || f - g || < \epsilon $$

This just means that any *weird* function in $\mathcal{R}^2$ can be expressed as a limit of functions in $\mathcal{C}$, just like irrational numbers can be too with rational numbers. For now, we take this for granted, without proof.


### The End
We have everything on our hands now. Given any $\epsilon>0$ and $f \in \mathcal{R}^2$, we can first take a continuous function $g\in\mathcal{C}$ such that

$$|| f - g|| < \epsilon. $$

But proposition 2 claims the existence of a Fejér sum $\sigma_n(g)$ and $N$ such that

$$n \geq N \implies || g - \sigma_n(g) || < \epsilon $$

Therefore, 

$$n \geq N \implies || f - \sigma_n(g) || \leq || f  - g || + || g - \sigma_n(g)|| < 2\epsilon,$$

while $\sigma_n$ is a (finite) linear combination of basis vectors of $\mathcal{B}$. Finally, we have the answer.

> **The Answer**
>
> $\mathcal{B}$ is a basis of $X = \mathcal{R}^2$.

### Remarks & Bibligraphy
This post is largely based on the notation and framework of *Introduction to Mathematical Analysis* (Kim, Kim & Kyhe, 2011, Korean title: *해석개론*). For the scope of this post, the space of Riemann-integrable functions $\mathcal{R}^2$ and the Lebesgue space $L^2$ may be used interchangeably without loss of generality.