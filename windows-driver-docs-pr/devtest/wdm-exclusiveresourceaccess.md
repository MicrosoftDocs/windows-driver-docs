---
title: ExclusiveResourceAccess rule (wdm)
description: The ExclusiveResourceAccess rule specifies that the driver calls ExAcquireResourceExclusiveLite before calling ExReleaseResourceLite or ExReleaseResourceForThreadLite and specifies that the driver calls ExReleaseResourceLite or ExReleaseResourceForThreadLite before any subsequent calls to ExAcquireResourceExclusiveLite.
ms.assetid: 3de539c0-5af2-4ced-8111-44918f4effc4
keywords: ["ExclusiveResourceAccess rule (wdm)"]
topic_type:
- apiref
api_name:
- ExclusiveResourceAccess
api_type:
- NA
---

# ExclusiveResourceAccess rule (wdm)


The **ExclusiveResourceAccess** rule specifies that the driver calls [**ExAcquireResourceExclusiveLite**](https://msdn.microsoft.com/library/windows/hardware/ff544351) before calling [**ExReleaseResourceLite**](https://msdn.microsoft.com/library/windows/hardware/ff545597) or [**ExReleaseResourceForThreadLite**](https://msdn.microsoft.com/library/windows/hardware/ff545585) and specifies that the driver calls **ExReleaseResourceLite** or **ExReleaseResourceForThreadLite** before any subsequent calls to **ExAcquireResourceExclusiveLite**.

Nested calls are permitted if they are acquiring and releasing different resources. Nested calls to acquire or release the same resources violate this rule.

This rule also states that when the routine ends, the driver must not have exclusive access to the resource. Static Driver Verifier monitors the end of the **DriverEntry**, **AddDevice**, **StartIo**, **StartDevice**, **DpcForIsr**, **Cancel**, **Dispatch**, **RemoveDevice**, and **Unload** routines.

|              |     |
|--------------|-----|
| Driver model | WDM |

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">Bug check(s) found with this rule</td>
<td align="left"></td>
</tr>
</tbody>
</table>

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>ExclusiveResourceAccess</strong> rule.</p>
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
[**ExReleaseResourceForThreadLite**](https://msdn.microsoft.com/library/windows/hardware/ff545585)
[**ExReleaseResourceLite**](https://msdn.microsoft.com/library/windows/hardware/ff545597)
See also
--------

[**Preventing Errors and Deadlocks While Using Spin Locks**](https://msdn.microsoft.com/library/windows/hardware/ff559854)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20ExclusiveResourceAccess%20rule%20%28wdm%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




