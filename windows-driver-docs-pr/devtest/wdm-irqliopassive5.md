---
title: IrqlIoPassive5 rule (wdm)
description: The IrqlIoPassive5 rule specifies that the driver calls specific I/O Manager routines only when it is executing at IRQL�  PASSIVE\_LEVEL.
ms.assetid: 07037cf2-37eb-4045-9588-ac10e79b9c5c
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["IrqlIoPassive5 rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlIoPassive5
api_type:
- NA
---

# IrqlIoPassive5 rule (wdm)


The **IrqlIoPassive5** rule specifies that the driver calls specific I/O Manager routines only when it is executing at IRQL = PASSIVE\_LEVEL.

|              |     |
|--------------|-----|
| Driver model | WDM |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x0002000E) |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IrqlIoPassive5</strong> rule.</p>
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

[**IoGetConfigurationInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549157)
[**IoGetDeviceObjectPointer**](https://msdn.microsoft.com/library/windows/hardware/ff549198)
[**IoGetDmaAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff549220)
[**IoGetFileObjectGenericMapping**](https://msdn.microsoft.com/library/windows/hardware/ff549231)
[**IoInitializeTimer**](https://msdn.microsoft.com/library/windows/hardware/ff549344)
[**IoIsWdmVersionAvailable**](https://msdn.microsoft.com/library/windows/hardware/ff549382)
[**IoRegisterDriverReinitialization**](https://msdn.microsoft.com/library/windows/hardware/ff549511)
[**IoRegisterShutdownNotification**](https://msdn.microsoft.com/library/windows/hardware/ff549541)
[**IoRemoveShareAccess**](https://msdn.microsoft.com/library/windows/hardware/ff549587)
[**IoSetShareAccess**](https://msdn.microsoft.com/library/windows/hardware/ff550324)
[**IoUnregisterShutdownNotification**](https://msdn.microsoft.com/library/windows/hardware/ff550409)
[**IoUpdateShareAccess**](https://msdn.microsoft.com/library/windows/hardware/ff550412)
[**IoWMIAllocateInstanceIds**](https://msdn.microsoft.com/library/windows/hardware/ff550429)
[**IoWMIRegistrationControl**](https://msdn.microsoft.com/library/windows/hardware/ff550480)
 

 





