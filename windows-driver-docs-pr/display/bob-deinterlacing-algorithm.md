---
title: Bob Deinterlacing Algorithm
description: Bob Deinterlacing Algorithm
ms.assetid: ef3220bd-841d-4187-bc86-11b999eae2bd
keywords:
- bob deinterlacing WDK DirectX VA , algorithm
- deinterlacing WDK DirectX VA , bob, algorithm
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Bob Deinterlacing Algorithm


## <span id="ddk_bob_deinterlacing_algorithm_gg"></span><span id="DDK_BOB_DEINTERLACING_ALGORITHM_GG"></span>


If your display driver implements the DXVA [deinterlacing DDI](https://msdn.microsoft.com/library/windows/hardware/ff552701), it must support the bob-style deinterlacing algorithm in addition to any proprietary deinterlacing algorithms. Following is a description of the bob-style deinterlacing algorithm:

Input is a field F<sub>in</sub>(i,j) of size MxN such that 0 &lt;= i &lt;= Mâˆ’1 and 0 &lt;= j &lt;=Nâˆ’1, where i and j are row and column indices, respectively.

Output is a frame F<sub>out</sub>(i,j) of size 2xMxN such that 0 &lt;= i &lt;= 2Mâˆ’1 and 0 &lt;= j &lt;=Nâˆ’1, where i and j are row and column indices, respectively.

If F<sub>in</sub>(i,j) is a top field:

![calculation illustrating a bob deinterlacing algorithm when fin(i,j) is a top field](images/bobtop.png)

If F<sub>in</sub>(i,j) is a bottom field:

![calculation illustrating a bob deinterlacing algorithm when fin(i,j) is a bottom field](images/bobbotom.png)

Each definition uses a finite impulse response (FIR) filter with an impulse response h of length 2K. Impulse response h is symmetric about its midpoint, such that h₋₍ₖ₊₁₎ = hₖ for k=0 to Kâˆ’1 and

![calculation illustrating a filter algorithm](images/firfiltr.png)

The preferred form of bob-style deinterlacing uses K=2 and h₀ = 9/16 (so h₁ = âˆ’1/16). This filter should be implemented as (9\*(b+c)âˆ’(a+d)+8)&gt;&gt;4, where a, b, c, and d are the four input samples used to produce one output sample.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Bob%20Deinterlacing%20Algorithm%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




