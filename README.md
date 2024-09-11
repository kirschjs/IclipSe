# IclipSe
Simulation of Eclipses in few-body systems

```Python
define global simulation parameters:
dimension of space     d=3
total simulation time  T
time increment         dt

define class stelar object(s):
emission spectrum      Intensity(wavelength)
orbit/trajectory       r(t)
size                   R

main simulation for 2 objects:

for t=1:T:dt

    for i=1:No(jects)

            calcDistancefromCentre = dd(i) = abs[r(t,i)]

    obtain distance-ordered object list at t:
        1,2,...,No -> closest, 2nd closest,...,most distant = [3,2,6,1,...] = D

    initialize attenuation-factor array A(i)

    A(D[0]) = 1 // as nothing shields the closest objects

    for j:1:No

        for k in D[j:]

            R := R(D[k])

            project size R(D[j]) from dd(D[j]) to dd(D[k]) -> Rp

            calc distance between projected, inner object and potential shadowed object:
            1) normalize r(D[j]) to the same length as r(D[k]):
                rp = r(D[j]) * dd(D[k])/dd(D[k])
            2) distance between centers:
                dc = | rp-r(D[k]) |
            if R+Rp>dc:
                calc overlap area:
                Ao = r^2 ArcCos( (dc^2 + R^2 - Rp^2)/(2*d*R) + (R<->Rp) 
                     - (1/2)*((-R+Rp+d)(R-Rp+d)(R+Rp-d)(R+Rp+d))^-(1/2)
            else:
                Ao = 0

            if A(D[k]) = 1:
                A(D[k]) = 1 - Ao/(pi*R^2)
            else: (i.e., the object is already partially shielded)
                let us not get too fancy here, yet, and just assume that the shaddows add up
                A(D[k]) -= Ao/(pi*R^2)

    calculate intensity at the detector:
    for i:1:No
        I0[lambda,t] += A(i)*I(i,lambda)/dd(i)^2
```
