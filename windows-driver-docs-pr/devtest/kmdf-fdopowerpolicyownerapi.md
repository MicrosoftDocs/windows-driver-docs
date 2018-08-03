---
title: FDOPowerPolicyOwnerAPI rule (kmdf)
description: The FDOPowerPolicyOwnerAPI rule specifies that if an FDO driver relinquishes power policy ownership, the methods WdfDeviceInitSetPowerPolicyEventCallbacks, WdfDeviceAssignS0IdleSettings, and WdfDeviceAssignSxWakeSettings can only be called on the execution paths where the driver is a power policy owner. SDV issues a warning for this rule.
ms.assetid: b0695dff-070c-4c55-a71d-a78fc45eb805
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["FDOPowerPolicyOwnerAPI rule (kmdf)"]
topic_type:
- apiref
api_name:
- FDOPowerPolicyOwnerAPI
api_type:
- NA
ms.localizationpriority: medium
---

# FDOPowerPolicyOwnerAPI rule (kmdf)


The **FDOPowerPolicyOwnerAPI** rule specifies that if an FDO driver relinquishes power policy ownership, the methods [**WdfDeviceInitSetPowerPolicyEventCallbacks**](https://msdn.microsoft.com/library/windows/hardware/ff546774), [**WdfDeviceAssignS0IdleSettings**](https://msdn.microsoft.com/library/windows/hardware/ff545903), and [**WdfDeviceAssignSxWakeSettings**](https://msdn.microsoft.com/library/windows/hardware/ff545909) can only be called on the execution paths where the driver is a power policy owner. SDV issues a warning for this rule.

If an FDO driver calls the [**WdfDeviceInitSetPowerPolicyOwnership**](https://msdn.microsoft.com/library/windows/hardware/ff546776) method with **FALSE** as the value of the second parameter, any subsequent calls to [**WdfDeviceInitSetPowerPolicyEventCallbacks**](https://msdn.microsoft.com/library/windows/hardware/ff546774), **WdfDeviceAssignS0IdleSettings**, and **WdfDeviceAssignSxWakeSettings** by that driver will cause a rule violation and a warning message.

|              |      |
|--------------|------|
| Driver model | KMDF |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>FDOPowerPolicyOwnerAPI</strong> rule.</p>
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

[**WdfDeviceAssignS0IdleSettings**](https://msdn.microsoft.com/library/windows/hardware/ff545903)
[**WdfDeviceAssignSxWakeSettings**](https://msdn.microsoft.com/library/windows/hardware/ff545909)
[**WdfDeviceInitSetPowerPolicyEventCallbacks**](https://msdn.microsoft.com/library/windows/hardware/ff546774)
[**WdfDeviceInitSetPowerPolicyOwnership**](https://msdn.microsoft.com/library/windows/hardware/ff546776)
 

 





