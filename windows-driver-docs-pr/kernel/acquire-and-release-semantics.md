---
title: Acquire and Release Semantics
description: Acquire and Release Semantics
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

For example, the [**InterlockedIncrementAcquire**](/previous-versions/windows/hardware/drivers/ff547916(v=vs.85)) routine uses acquire semantics to increment a variable. If you rewrote the preceding code example as follows:

```cpp
 InterlockedIncrementAcquire(&a);
 b++;
 c++;
```

other processors would always see the increment of `a` before the increments of `b` and `c`.

Likewise, the [**InterlockedIncrementRelease**](/previous-versions/windows/hardware/drivers/ff547919(v=vs.85)) routine uses release semantics to increment a variable. If you rewrote the code example once again, as follows:

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
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-interlockedincrement" data-raw-source="[&lt;strong&gt;InterlockedIncrement&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-interlockedincrement)"><strong>InterlockedIncrement</strong></a></p></td>
<td><p><a href="/previous-versions/windows/hardware/drivers/ff547916(v=vs.85)" data-raw-source="[&lt;strong&gt;InterlockedIncrementAcquire&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff547916(v=vs.85))"><strong>InterlockedIncrementAcquire</strong></a></p></td>
<td><p><a href="/previous-versions/windows/hardware/drivers/ff547919(v=vs.85)" data-raw-source="[&lt;strong&gt;InterlockedIncrementRelease&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff547919(v=vs.85))"><strong>InterlockedIncrementRelease</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-interlockeddecrement" data-raw-source="[&lt;strong&gt;InterlockedDecrement&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-interlockeddecrement)"><strong>InterlockedDecrement</strong></a></p></td>
<td><p><a href="/previous-versions/windows/hardware/drivers/ff547875(v=vs.85)" data-raw-source="[&lt;strong&gt;InterlockedDecrementAcquire&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff547875(v=vs.85))"><strong>InterlockedDecrementAcquire</strong></a></p></td>
<td><p><a href="/previous-versions/windows/hardware/drivers/ff547883(v=vs.85)" data-raw-source="[&lt;strong&gt;InterlockedDecrementRelease&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff547883(v=vs.85))"><strong>InterlockedDecrementRelease</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-interlockedcompareexchange" data-raw-source="[&lt;strong&gt;InterlockedCompareExchange&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-interlockedcompareexchange)"><strong>InterlockedCompareExchange</strong></a></p></td>
<td><p><a href="/previous-versions/windows/hardware/drivers/ff547857(v=vs.85)" data-raw-source="[&lt;strong&gt;InterlockedCompareExchangeAcquire&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff547857(v=vs.85))"><strong>InterlockedCompareExchangeAcquire</strong></a></p></td>
<td><p><a href="/previous-versions/windows/hardware/drivers/ff547867(v=vs.85)" data-raw-source="[&lt;strong&gt;InterlockedCompareExchangeRelease&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff547867(v=vs.85))"><strong>InterlockedCompareExchangeRelease</strong></a></p></td>
</tr>
</tbody>
</table>

 

