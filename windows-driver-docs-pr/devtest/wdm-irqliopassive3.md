---
title: IrqlIoPassive3 rule (wdm)
ms.assetid: 84e45026-7535-4e72-afc8-19b6a7e43bd7
description: 
keywords: ["IrqlIoPassive3 rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlIoPassive3
api_type:
- NA
---

# IrqlIoPassive3 rule (wdm)


The IrqlIoPassive3 rule specifies that the driver calls the following routines only when it is executing at IRQL = PASSIVE\_LEVEL:

-   [**IoDetachDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549087)

-   [**IoAssignArcName**](https://msdn.microsoft.com/library/windows/hardware/ff548282)

-   [**IoRegisterDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff549506)

|              |     |
|--------------|-----|
| Driver model | WDM |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x0002000C) |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IrqlIoPassive3</strong> rule.</p>
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

[**IoCreateSymbolicLink**](https://msdn.microsoft.com/library/windows/hardware/ff549043)
[**IoDetachDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549087)
[**IoRegisterDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff549506)
 

 





