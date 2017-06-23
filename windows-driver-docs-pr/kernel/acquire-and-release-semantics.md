---
title: Acquire and Release Semantics
author: windows-driver-content
description: Acquire and Release Semantics
ms.assetid: a0852881-c33f-427a-be8a-5b9edac81f9a
keywords: ["synchronization WDK kernel , acquire semantics", "synchronization WDK kernel , release semantics", "acquire semantics WDK kernel", "release semantics WDK kernel", "semantics WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Acquire and Release Semantics


## <a href="" id="ddk-acquire-and-release-semantics-kg"></a>


An operation has *acquire semantics* if other processors will always see its effect before any subsequent operation's effect. An operation has *release semantics* if other processors will see every preceding operation's effect before the effect of the operation itself.

Consider the following code example:

```
 a++;
 b++;
 c++;
```

From another processor's point of view, the preceding operations can appear to occur in any order. For example, the other processor might see the increment of `b` before the increment of `a`.

Atomic operations, such as those that the **Interlocked*Xxx*** routines perform, have both acquire and release semantics by default. However, Itanium-based processors execute operations that have only acquire or only release semantics faster than those that have both. Therefore, the system provides **Interlocked*Xxx*Acquire** and **Interlocked*Xxx*Release** versions of some of the **Interlocked*Xxx*** routines.

For example, the [**InterlockedIncrementAcquire**](https://msdn.microsoft.com/library/windows/hardware/ff547916) routine uses acquire semantics to increment a variable. If you rewrote the preceding code example as follows:

```
 InterlockedIncrementAcquire(&amp;a);
 b++;
 c++;
```

other processors would always see the increment of `a` before the increments of `b` and `c`.

Likewise, the [**InterlockedIncrementRelease**](https://msdn.microsoft.com/library/windows/hardware/ff547919) routine uses release semantics to increment a variable. If you rewrote the code example once again, as follows:

```
 a++;
 b++;
 InterlockedIncrementRelease(&amp;c);
```

other processors would always see the increments of `a` and `b` before the increment of `c`.

If the processor does not provide instructions that have only acquire or only release semantics, the system will use the corresponding routine that provides both types of semantics. For example, on x86 processors both **InterlockedIncrementAcquire** and **InterlockedIncrementRelease** are equivalent to **InterlockedIncrement**.

The following table lists the routines that have acquire-only and release-only variants.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Interlocked<em>Xxx</em> Routine</th>
<th>Acquire-Semantics-Only Version</th>
<th>Release-Semantics-Only Version</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>InterlockedIncrement</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547910)</p></td>
<td><p>[<strong>InterlockedIncrementAcquire</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547916)</p></td>
<td><p>[<strong>InterlockedIncrementRelease</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547919)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>InterlockedDecrement</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547871)</p></td>
<td><p>[<strong>InterlockedDecrementAcquire</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547875)</p></td>
<td><p>[<strong>InterlockedDecrementRelease</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547883)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>InterlockedCompareExchange</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547853)</p></td>
<td><p>[<strong>InterlockedCompareExchangeAcquire</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547857)</p></td>
<td><p>[<strong>InterlockedCompareExchangeRelease</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547867)</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Acquire%20and%20Release%20Semantics%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


