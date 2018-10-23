---
title: IrqlIoPassive1 rule (wdm)
ms.assetid: c8960015-3b7c-4827-82dc-fd1225a376ea
ms.date: 05/21/2018
description: 
keywords: ["IrqlIoPassive1 rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlIoPassive1
api_type:
- NA
ms.localizationpriority: medium
---

# IrqlIoPassive1 rule (wdm)


The **IrqlIoPassive1** rule specifies that the driver calls the following routines only when it is executing at IRQL = PASSIVE\_LEVEL:

-   [**IoAttachDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548294)

-   [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397)

-   [**IoSetDeviceInterfaceState**](https://msdn.microsoft.com/library/windows/hardware/ff549700)

The rule also specifies that the driver calls the following routine only when it is executing at IRQL = PASSIVE\_LEVEL or IRQL = APC\_LEVEL:

-   [**IoBuildDeviceIoControlRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548318)

|              |     |
|--------------|-----|
| Driver model | WDM |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x0002000A) |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IrqlIoPassive1</strong> rule.</p>
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

[**IoAttachDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548294)
[**IoBuildDeviceIoControlRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548318)
[**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397)
[**IoSetDeviceInterfaceState**](https://msdn.microsoft.com/library/windows/hardware/ff549700)
 

 





