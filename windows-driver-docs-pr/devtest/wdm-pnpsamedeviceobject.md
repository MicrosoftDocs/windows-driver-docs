---
title: PnpSameDeviceObject rule (wdm)
description: The PnpSameDeviceObject rule specifies that the driver calls IoAttachDeviceToDeviceStack with a pointer to a valid target device object.
ms.assetid: 9430962c-7430-445b-b598-57ce7f34cd45
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["PnpSameDeviceObject rule (wdm)"]
topic_type:
- apiref
api_name:
- PnpSameDeviceObject
api_type:
- NA
ms.localizationpriority: medium
---

# PnpSameDeviceObject rule (wdm)


The **PnpSameDeviceObject** rule specifies that the driver calls [**IoAttachDeviceToDeviceStack**](https://msdn.microsoft.com/library/windows/hardware/ff548300) with a pointer to a valid target device object.

If the pointed-to device object is not standard, the driver violates this rule. This rule ensures that the driver correctly attaches to the device stack.

This rule does not verify the validity of the pointer to the source object.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>PnpSameDeviceObject</strong> rule.</p>
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

[**IoAttachDeviceToDeviceStack**](https://msdn.microsoft.com/library/windows/hardware/ff548300)
 

 





