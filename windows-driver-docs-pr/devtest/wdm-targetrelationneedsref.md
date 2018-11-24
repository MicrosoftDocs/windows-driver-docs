---
title: TargetRelationNeedsRef rule (wdm)
description: The TargetRelationNeedsRef rule specifies that when processing a TargetDeviceRelation query, the driver's DispatchPnP routine calls one of the following functions to reference the child device's PDO ObReferenceObjectObReferenceObjectByHandleObReferenceObjectByPointer.
ms.assetid: a341ff7a-1b36-4dfc-9e73-8268ed5b9a78
ms.date: 05/21/2018
keywords: ["TargetRelationNeedsRef rule (wdm)"]
topic_type:
- apiref
api_name:
- TargetRelationNeedsRef
api_type:
- NA
ms.localizationpriority: medium
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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>TargetRelationNeedsRef</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code" data-raw-source="[Prepare your code (use role type declarations).](https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code)">Prepare your code (use role type declarations).</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier" data-raw-source="[Run Static Driver Verifier.](https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier)">Run Static Driver Verifier.</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results" data-raw-source="[View and analyze the results.](https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results)">View and analyze the results.</a></li>
</ol>
<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh454281" data-raw-source="[Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281)">Using Static Driver Verifier to Find Defects in Drivers</a>.</p></td>
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
 

 





