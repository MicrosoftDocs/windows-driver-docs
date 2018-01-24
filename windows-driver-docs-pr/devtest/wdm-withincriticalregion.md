---
title: WithinCriticalRegion rule (wdm)
description: The WithinCriticalRegion rule specifies that the driver's calls to particular synchronization functions appear only after calling KeEnterCriticalRegion and before calling KeLeaveCriticalRegion.
ms.assetid: 9b74b868-6025-4e81-b5ba-21e0da734cd9
keywords: ["WithinCriticalRegion rule (wdm)"]
topic_type:
- apiref
api_name:
- WithinCriticalRegion
api_type:
- NA
---

# WithinCriticalRegion rule (wdm)


The **WithinCriticalRegion** rule specifies that the driver's calls to particular synchronization functions appear only after calling [**KeEnterCriticalRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552021) and before calling [**KeLeaveCriticalRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552964).

The affected synchronization functions are the following:

-   [**ExAcquireResourceSharedLite**](https://msdn.microsoft.com/library/windows/hardware/ff544363)

-   [**ExAcquireResourceExclusiveLite**](https://msdn.microsoft.com/library/windows/hardware/ff544351)

-   [**ExAcquireSharedStarveExclusive**](https://msdn.microsoft.com/library/windows/hardware/ff544367)

-   [**ExAcquireSharedWaitForExclusive**](https://msdn.microsoft.com/library/windows/hardware/ff544370)

-   [**ExReleaseResourceLite**](https://msdn.microsoft.com/library/windows/hardware/ff545597)

-   [**ExReleaseResourceForThreadLite**](https://msdn.microsoft.com/library/windows/hardware/ff545585)

This rule does not recognize other methods of disabling normal APC delivery. For more information, see [**Disabling APCs**](https://msdn.microsoft.com/library/windows/hardware/ff543219).

|              |     |
|--------------|-----|
| Driver model | WDM |

How to test
-----------

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At compile time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>WithinCriticalRegion</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li>[Prepare your code (use role type declarations).](https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code)</li>
<li>[Run Static Driver Verifier.](https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier)</li>
<li>[View and analyze the results.](https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results)</li>
</ol>
<p>For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281).</p></td>
</tr>
</tbody>
</table>

Applies to
----------

[**ExAcquireResourceExclusiveLite**](https://msdn.microsoft.com/library/windows/hardware/ff544351)
[**ExAcquireResourceSharedLite**](https://msdn.microsoft.com/library/windows/hardware/ff544363)
[**ExAcquireSharedStarveExclusive**](https://msdn.microsoft.com/library/windows/hardware/ff544367)
[**ExAcquireSharedWaitForExclusive**](https://msdn.microsoft.com/library/windows/hardware/ff544370)
[**ExReleaseResourceForThreadLite**](https://msdn.microsoft.com/library/windows/hardware/ff545585)
[**ExReleaseResourceLite**](https://msdn.microsoft.com/library/windows/hardware/ff545597)
[**KeEnterCriticalRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552021)
[**KeEnterGuardedRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552028)
[**KeLeaveCriticalRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552964)
[**KeLeaveGuardedRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552967)
See also
--------

[**Managing Hardware Priorities**](https://msdn.microsoft.com/library/windows/hardware/ff554368)
[**Preventing Errors and Deadlocks While Using Spin Locks**](https://msdn.microsoft.com/library/windows/hardware/ff559854)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20WithinCriticalRegion%20rule%20%28wdm%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




