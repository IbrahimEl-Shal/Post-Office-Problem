### Post-Office-Problem

![](Output Images/Capture.PNG)

We have n villages {V0, V1, V2, V3, … ,Vn-1} which have two dimensional coordinates denoted by integer xi
and yi. A post office needs to be built in one of these villages. All villages are well connected with almost a
straight-line road.

* Using brute-force approach, design an algorithm to find the post-office location minimizing the average
distance between the villages and the post office.
* Using brute-force approach, design an algorithm to find the post-office location minimizing the
maximum distance from a village to the post office.
* Support your design by tricks to run those algorithms efficiently.
* Analyze your designed algorithms mathematically and empirically.
* Which minimization is more suitable for this application, average or maximum distance and why? And
which is faster to execute?

![](Output Images/Order of Growth[Max Case][Old].jpg)
![](Output Images/Order of Growth[Avg Case][Old].jpg)

![](Output Images/Order of Growth[Avg Case][Enhanced].jpg)
![](Output Images/Order of Growth[Max Case][Enhanced].jpg)


<figure>
 <img src="Output Images/Order of Growth[Max Case][Old]_.jpg" width="380" alt="Combined Image" />
 <figcaption>
 <p></p> 
 <p style="text-align: center;"> First output after detecting line segments </p> 
 </figcaption>
</figure>
 <p></p> 
<figure>
 <img src="Output Images/Order of Growth[Avg Case][Old]_.jpg" width="380" alt="Combined Image" />
 <figcaption>
 <p></p> 
 <p style="text-align: center;"> Our enhancement after connect and average line segments to get output like this</p> 
 </figcaption>
</figure>
