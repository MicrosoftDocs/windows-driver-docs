---
title: Converting an Ordinary DPC to a Threaded DPC
description: Converting an Ordinary DPC to a Threaded DPC
ms.assetid: 89a7a408-e01b-4543-9775-5ef542d05b75
keywords: ["threaded DPCs WDK kernel", "converting DPCs"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Converting an Ordinary DPC to a Threaded DPC





Converting an ordinary DPC to a threaded DPC is straightforward. Simply replace the call to [**KeInitializeDpc**](https://msdn.microsoft.com/library/windows/hardware/ff552130) (which initializes the DPC) with one to [**KeInitializeThreadedDpc**](https://msdn.microsoft.com/library/windows/hardware/ff552166), and refer to the following table to replace the calls inside the DPC routine that acquire and release spin locks.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Ordinary DPC call</th>
<th>Corresponding threaded DPC call</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551921" data-raw-source="[&lt;strong&gt;KeAcquireSpinLockAtDpcLevel&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551921)"><strong>KeAcquireSpinLockAtDpcLevel</strong></a></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551923" data-raw-source="[&lt;strong&gt;KeAcquireSpinLockForDpc&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551923)"><strong>KeAcquireSpinLockForDpc</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553150" data-raw-source="[&lt;strong&gt;KeReleaseSpinLockFromDpcLevel&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553150)"><strong>KeReleaseSpinLockFromDpcLevel</strong></a></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553148" data-raw-source="[&lt;strong&gt;KeReleaseSpinLockForDpc&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553148)"><strong>KeReleaseSpinLockForDpc</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551908" data-raw-source="[&lt;strong&gt;KeAcquireInStackQueuedSpinLockAtDpcLevel&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551908)"><strong>KeAcquireInStackQueuedSpinLockAtDpcLevel</strong></a></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551912" data-raw-source="[&lt;strong&gt;KeAcquireInStackQueuedSpinLockForDpc&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551912)"><strong>KeAcquireInStackQueuedSpinLockForDpc</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553137" data-raw-source="[&lt;strong&gt;KeReleaseInStackQueuedSpinLockFromDpcLevel&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553137)"><strong>KeReleaseInStackQueuedSpinLockFromDpcLevel</strong></a></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553133" data-raw-source="[&lt;strong&gt;KeReleaseInStackQueuedSpinLockForDpc&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553133)"><strong>KeReleaseInStackQueuedSpinLockForDpc</strong></a></p></td>
</tr>
</tbody>
</table>

 

You do not need to change calls to other spin lock routines, such as [**KeAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551917) or [**KeAcquireInStackQueuedSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551899).

 

 




