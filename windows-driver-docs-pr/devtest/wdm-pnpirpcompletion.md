---
title: PnpIrpCompletion rule (wdm)
description: The PnpIrpCompletion rule verifies that an FDO driver passes PnP IRPs to the lower driver.
ms.assetid: 32b2ed2c-4222-4d93-8323-3ad442a14d9d
ms.date: 05/21/2018
keywords: ["PnpIrpCompletion rule (wdm)"]
topic_type:
- apiref
api_name:
- PnpIrpCompletion
api_type:
- NA
ms.localizationpriority: medium
---

# PnpIrpCompletion rule (wdm)


The **PnpIrpCompletion** rule verifies that an FDO driver passes PnP IRPs to the lower driver.

This rule does not apply to bus drivers.

The following PnP IRPs are excluded from this rule:

-   IRP\_MN\_QUERY\_INTERFACE
-   IRP\_MN\_QUERY\_STOP\_DEVICE
-   IRP\_MN\_QUERY\_REMOVE\_DEVICE

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>PnpIrpCompletion</strong> rule.</p>
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
[**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343)
[**IoForwardIrpSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff549100)
[**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654)
 

 





