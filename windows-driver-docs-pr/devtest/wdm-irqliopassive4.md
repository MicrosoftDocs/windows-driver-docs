---
title: IrqlIoPassive4 rule (wdm)
ms.assetid: 2bdfa09d-0777-4eaf-85ff-d5accc0f31de
ms.date: 05/21/2018
description: 
keywords: ["IrqlIoPassive4 rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlIoPassive4
api_type:
- NA
ms.localizationpriority: medium
---

# IrqlIoPassive4 rule (wdm)


The **IrqlIoPassive4** rule specifies that the driver calls the following routines only when it is executing at IRQL = PASSIVE\_LEVEL:

-   [**IoCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff548418)

-   [**IoCreateNotificationEvent**](https://msdn.microsoft.com/library/windows/hardware/ff549039)

-   [**IoCreateSymbolicLink**](https://msdn.microsoft.com/library/windows/hardware/ff549043)

-   [**IoCreateSynchronizationEvent**](https://msdn.microsoft.com/library/windows/hardware/ff549045)

-   [**IoCreateUnprotectedSymbolicLink**](https://msdn.microsoft.com/library/windows/hardware/ff549050)

-   [**IoDeassignArcName**](https://msdn.microsoft.com/library/windows/hardware/ff549076)

-   [**IoDeleteController**](https://msdn.microsoft.com/library/windows/hardware/ff549078)

-   [**IoDeleteSymbolicLink**](https://msdn.microsoft.com/library/windows/hardware/ff549085)

-   [**IoDisconnectInterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff549089)

|              |     |
|--------------|-----|
| Driver model | WDM |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x0002000D) |

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>IrqlIoPassive4</strong> rule.</p>
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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff545448" data-raw-source="[Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448)">Driver Verifier</a> and select the <a href="https://msdn.microsoft.com/library/windows/hardware/hh454208" data-raw-source="[DDI compliance checking](https://msdn.microsoft.com/library/windows/hardware/hh454208)">DDI compliance checking</a> option.</p></td>
</tr>
</tbody>
</table>

 

Applies to
----------

[**IoCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff548418)
[**IoCreateNotificationEvent**](https://msdn.microsoft.com/library/windows/hardware/ff549039)
[**IoCreateSynchronizationEvent**](https://msdn.microsoft.com/library/windows/hardware/ff549045)
[**IoCreateUnprotectedSymbolicLink**](https://msdn.microsoft.com/library/windows/hardware/ff549050)
[**IoDeleteController**](https://msdn.microsoft.com/library/windows/hardware/ff549078)
[**IoDeleteSymbolicLink**](https://msdn.microsoft.com/library/windows/hardware/ff549085)
[**IoDisconnectInterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff549089)
 

 





