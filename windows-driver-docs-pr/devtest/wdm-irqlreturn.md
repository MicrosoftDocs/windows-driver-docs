---
title: IrqlReturn rule (wdm)
description: The IrqlReturn rule specifies that the driver's dispatch routines return at the same IRQL at which they were called.
ms.assetid: 1b2ef432-e3ba-4a01-b3df-839ff13b03f6
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["IrqlReturn rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlReturn
api_type:
- NA
ms.localizationpriority: medium
---

# IrqlReturn rule (wdm)


The **IrqlReturn** rule specifies that the driver's dispatch routines return at the same IRQL at which they were called. For more information about the IRQLs at which dispatch routines are properly called, see [**Dispatch Routines and IRQLs.**](https://msdn.microsoft.com/library/windows/hardware/ff544039)

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IrqlReturn</strong> rule.</p>
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

See also
--------

[**Dispatch Routines and IRQLs**](https://msdn.microsoft.com/library/windows/hardware/ff544039)
 

 





