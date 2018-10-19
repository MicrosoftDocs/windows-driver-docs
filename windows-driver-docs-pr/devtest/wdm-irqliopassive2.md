---
title: IrqlIoPassive2 rule (wdm)
ms.assetid: 36e449c2-9b24-4309-a4ac-af496cdc7b4f
ms.date: 05/21/2018
description: 
keywords: ["IrqlIoPassive2 rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlIoPassive2
api_type:
- NA
ms.localizationpriority: medium
---

# IrqlIoPassive2 rule (wdm)


The **IrqlIoPassive2** rule specifies that the driver calls the following I/O Manager routines only at IRQL = PASSIVE\_LEVEL:

-   [**IoCheckShareAccess**](https://msdn.microsoft.com/library/windows/hardware/ff548341)

-   [**IoConnectInterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff548371)

-   [**IoCreateController**](https://msdn.microsoft.com/library/windows/hardware/ff548395)

|              |     |
|--------------|-----|
| Driver model | WDM |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x0002000B) |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IrqlIoPassive2</strong> rule.</p>
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

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At run time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Run [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448) and select the [DDI compliance checking](https://msdn.microsoft.com/library/windows/hardware/hh454208) option.</p></td>
</tr>
</tbody>
</table>

 

Applies to
----------

[**IoCheckShareAccess**](https://msdn.microsoft.com/library/windows/hardware/ff548341)
[**IoConnectInterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff548371)
[**IoCreateController**](https://msdn.microsoft.com/library/windows/hardware/ff548395)
 

 





