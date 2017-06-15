---
title: Converting an Ordinary DPC to a Threaded DPC
author: windows-driver-content
description: Converting an Ordinary DPC to a Threaded DPC
MS-HAID:
- 'Intrupts\_46578055-a4e0-4c22-9bc5-419d4a6b9e7c.xml'
- 'kernel.converting\_an\_ordinary\_dpc\_to\_a\_threaded\_dpc'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 89a7a408-e01b-4543-9775-5ef542d05b75
keywords: ["threaded DPCs WDK kernel", "converting DPCs"]
---

# Converting an Ordinary DPC to a Threaded DPC


## <a href="" id="ddk-converting-an-ordinary-dpc-to-a-threaded-dpc-kg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Converting%20an%20Ordinary%20DPC%20to%20a%20Threaded%20DPC%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


