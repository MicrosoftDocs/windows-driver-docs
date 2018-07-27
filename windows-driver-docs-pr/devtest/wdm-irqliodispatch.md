---
title: IrqlIoDispatch rule (wdm)
description: The IrqlIoDispatch rule specifies that the driver calls the following I/O Manager routines only when it is executing at IRQL DISPATCH\_LEVEL IoGetDeviceToVerify, IoSetDeviceToVerify.
ms.assetid: 4794123F-EB8E-4B3D-A7DE-8E6B145AE816
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["IrqlIoDispatch rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlIoDispatch
api_type:
- NA
ms.localizationpriority: medium
---

# IrqlIoDispatch rule (wdm)


The **IrqlIoDispatch** rule specifies that the driver calls the following I/O Manager routines only when it is executing at IRQL &lt;= DISPATCH\_LEVEL: [**IoGetDeviceToVerify**](https://msdn.microsoft.com/library/windows/hardware/ff549212), [**IoSetDeviceToVerify**](https://msdn.microsoft.com/library/windows/hardware/ff548529).

|              |     |
|--------------|-----|
| Driver model | WDM |

|                                   |                                                                                                                                        |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x 0x20022 ) |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IrqlIoDispatch</strong> rule.</p>
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

[Managing Hardware Priorities](https://msdn.microsoft.com/library/windows/hardware/ff554368)
 

 





