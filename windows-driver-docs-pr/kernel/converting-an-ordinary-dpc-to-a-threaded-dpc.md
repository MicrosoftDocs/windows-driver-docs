---
title: Converting an Ordinary DPC to a Threaded DPC
author: windows-driver-content
description: Converting an Ordinary DPC to a Threaded DPC
ms.assetid: 89a7a408-e01b-4543-9775-5ef542d05b75
keywords: ["threaded DPCs WDK kernel", "converting DPCs"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td><p>[<strong>KeAcquireSpinLockAtDpcLevel</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551921)</p></td>
<td><p>[<strong>KeAcquireSpinLockForDpc</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551923)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KeReleaseSpinLockFromDpcLevel</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553150)</p></td>
<td><p>[<strong>KeReleaseSpinLockForDpc</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553148)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KeAcquireInStackQueuedSpinLockAtDpcLevel</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551908)</p></td>
<td><p>[<strong>KeAcquireInStackQueuedSpinLockForDpc</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551912)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KeReleaseInStackQueuedSpinLockFromDpcLevel</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553137)</p></td>
<td><p>[<strong>KeReleaseInStackQueuedSpinLockForDpc</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553133)</p></td>
</tr>
</tbody>
</table>

 

You do not need to change calls to other spin lock routines, such as [**KeAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551917) or [**KeAcquireInStackQueuedSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551899).

 

 




