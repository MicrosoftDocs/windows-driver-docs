---
title: Acquire and Release Semantics
description: Acquire and Release Semantics
ms.assetid: a0852881-c33f-427a-be8a-5b9edac81f9a
keywords: ["synchronization WDK kernel , acquire semantics", "synchronization WDK kernel , release semantics", "acquire semantics WDK kernel", "release semantics WDK kernel", "semantics WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Acquire and Release Semantics





An operation has *acquire semantics* if other processors will always see its effect before any subsequent operation's effect. An operation has *release semantics* if other processors will see every preceding operation's effect before the effect of the operation itself.

Consider the following code example:

```cpp
 a++;
 b++;
 c++;
```

From another processor's point of view, the preceding operations can appear to occur in any order. For example, the other processor might see the increment of `b` before the increment of `a`.

Atomic operations, such as those that the **Interlocked*Xxx*** routines perform, have both acquire and release semantics by default. However, Itanium-based processors execute operations that have only acquire or only release semantics faster than those that have both. Therefore, the system provides **Interlocked*Xxx*Acquire** and **Interlocked*Xxx*Release** versions of some of the **Interlocked*Xxx*** routines.

For example, the [**InterlockedIncrementAcquire**](https://msdn.microsoft.com/library/windows/hardware/ff547916) routine uses acquire semantics to increment a variable. If you rewrote the preceding code example as follows:

```cpp
 InterlockedIncrementAcquire(&a);
 b++;
 c++;
```

other processors would always see the increment of `a` before the increments of `b` and `c`.

Likewise, the [**InterlockedIncrementRelease**](https://msdn.microsoft.com/library/windows/hardware/ff547919) routine uses release semantics to increment a variable. If you rewrote the code example once again, as follows:

```cpp
 a++;
 b++;
 InterlockedIncrementRelease(&c);
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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff547910" data-raw-source="[&lt;strong&gt;InterlockedIncrement&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547910)"><strong>InterlockedIncrement</strong></a></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff547916" data-raw-source="[&lt;strong&gt;InterlockedIncrementAcquire&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547916)"><strong>InterlockedIncrementAcquire</strong></a></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff547919" data-raw-source="[&lt;strong&gt;InterlockedIncrementRelease&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547919)"><strong>InterlockedIncrementRelease</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff547871" data-raw-source="[&lt;strong&gt;InterlockedDecrement&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547871)"><strong>InterlockedDecrement</strong></a></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff547875" data-raw-source="[&lt;strong&gt;InterlockedDecrementAcquire&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547875)"><strong>InterlockedDecrementAcquire</strong></a></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff547883" data-raw-source="[&lt;strong&gt;InterlockedDecrementRelease&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547883)"><strong>InterlockedDecrementRelease</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff547853" data-raw-source="[&lt;strong&gt;InterlockedCompareExchange&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547853)"><strong>InterlockedCompareExchange</strong></a></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff547857" data-raw-source="[&lt;strong&gt;InterlockedCompareExchangeAcquire&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547857)"><strong>InterlockedCompareExchangeAcquire</strong></a></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff547867" data-raw-source="[&lt;strong&gt;InterlockedCompareExchangeRelease&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547867)"><strong>InterlockedCompareExchangeRelease</strong></a></p></td>
</tr>
</tbody>
</table>

 

 

 




