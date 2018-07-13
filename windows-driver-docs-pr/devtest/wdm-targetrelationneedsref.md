---
title: TargetRelationNeedsRef rule (wdm)
description: The TargetRelationNeedsRef rule specifies that when processing a TargetDeviceRelation query, the driver's DispatchPnP routine calls one of the following functions to reference the child device's PDO ObReferenceObjectObReferenceObjectByHandleObReferenceObjectByPointer.
ms.assetid: a341ff7a-1b36-4dfc-9e73-8268ed5b9a78
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
 

 





