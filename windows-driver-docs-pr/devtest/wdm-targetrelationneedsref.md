---
title: TargetRelationNeedsRef rule (wdm)
description: The TargetRelationNeedsRef rule specifies that when processing a TargetDeviceRelation query, the driver's DispatchPnP routine calls one of the following functions to reference the child device's PDO ObReferenceObjectObReferenceObjectByHandleObReferenceObjectByPointer.
ms.assetid: a341ff7a-1b36-4dfc-9e73-8268ed5b9a78
keywords: ["TargetRelationNeedsRef rule (wdm)"]
topic_type:
- apiref
api_name:
- TargetRelationNeedsRef
api_type:
- NA
---

# TargetRelationNeedsRef rule (wdm)


The **TargetRelationNeedsRef** rule specifies that when processing a *TargetDeviceRelation* query, the driver's [**DispatchPnP**](https://msdn.microsoft.com/library/windows/hardware/ff543341) routine calls one of the following functions to reference the child device's PDO:

-   [**ObReferenceObject**](https://msdn.microsoft.com/library/windows/hardware/ff558678)

-   [**ObReferenceObjectByHandle**](https://msdn.microsoft.com/library/windows/hardware/ff558679)

-   [**ObReferenceObjectByPointer**](https://msdn.microsoft.com/library/windows/hardware/ff558686)

This rule applies only when the driver completes the IRP by setting the `Irp->IoStatus.Information` pointer to a new, non-**NULL** value. It is not applied when the driver passes the IRP to a lower driver.

This rule does not specify what qualifies as a valid value for `Irp->IoStatus.Information`. This rule applies only when the driver changes the value and the new value is not **NULL**. A valid value is a pointer to a DEVICE\_RELATIONS structure that contains the requested relations information.

This rule only applies to bus drivers.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>TargetRelationNeedsRef</strong> rule.</p>
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

[**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336)
[**ObReferenceObjectByHandle**](https://msdn.microsoft.com/library/windows/hardware/ff558679)
[**ObReferenceObjectByPointer**](https://msdn.microsoft.com/library/windows/hardware/ff558686)
[**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654)
See also
--------

[**DanglingDeviceObjectReference**](wdm-danglingdeviceobjectreference.md)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20TargetRelationNeedsRef%20rule%20%28wdm%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




