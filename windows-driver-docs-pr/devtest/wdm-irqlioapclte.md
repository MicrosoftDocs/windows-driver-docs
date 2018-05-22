---
title: IrqlIoApcLte rule (wdm)
description: The IrqlIoApcLte rule specifies that the driver calls the following I/O manager routines only when it is executing at IRQL�  APC\_LEVEL IoDeleteDeviceIoGetInitialStackIoRaiseHardErrorIoRaiseInformationalHardError.
ms.assetid: 1f0b2b9c-f67c-4e34-b079-6a2769f62879
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["IrqlIoApcLte rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlIoApcLte
api_type:
- NA
---

# IrqlIoApcLte rule (wdm)


The **IrqlIoApcLte** rule specifies that the driver calls the following I/O manager routines only when it is executing at IRQL &lt;= APC\_LEVEL:

-   [**IoDeleteDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549083)

-   [**IoGetInitialStack**](https://msdn.microsoft.com/library/windows/hardware/ff549247)

-   [**IoRaiseHardError**](https://msdn.microsoft.com/library/windows/hardware/ff549482)

-   [**IoRaiseInformationalHardError**](https://msdn.microsoft.com/library/windows/hardware/ff549488)

|              |     |
|--------------|-----|
| Driver model | WDM |

|                                   |                                                                                                                                                                                                                                        |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x00020009), [**Bug Check 0xA: IRQL\_NOT\_LESS\_OR\_EQUAL**](https://msdn.microsoft.com/library/windows/hardware/ff560129) |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IrqlIoApcLte</strong> rule.</p>
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

[**IoDeleteDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549083)
[**IoGetInitialStack**](https://msdn.microsoft.com/library/windows/hardware/ff549247)
[**IoRaiseHardError**](https://msdn.microsoft.com/library/windows/hardware/ff549482)
[**IoRaiseInformationalHardError**](https://msdn.microsoft.com/library/windows/hardware/ff549488)
See also
--------

[**Managing Hardware Priorities**](https://msdn.microsoft.com/library/windows/hardware/ff554368)
[**Preventing Errors and Deadlocks While Using Spin Locks**](https://msdn.microsoft.com/library/windows/hardware/ff559854)
 

 





