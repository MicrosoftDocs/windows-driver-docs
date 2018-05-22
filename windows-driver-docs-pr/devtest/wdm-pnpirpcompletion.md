---
title: PnpIrpCompletion rule (wdm)
description: The PnpIrpCompletion rule verifies that an FDO driver passes PnP IRPs to the lower driver.
ms.assetid: 32b2ed2c-4222-4d93-8323-3ad442a14d9d
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["PnpIrpCompletion rule (wdm)"]
topic_type:
- apiref
api_name:
- PnpIrpCompletion
api_type:
- NA
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>PnpIrpCompletion</strong> rule.</p>
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
[**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343)
[**IoForwardIrpSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff549100)
[**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654)
 

 





