---
title: WmiComplete rule (wdm)
description: The WmiComplete rule specifies that when processing a WMI minor IRP, the driver calls IoCompleteRequest before returning from the DispatchSystemControl routine.
ms.assetid: 3908da96-beb1-4651-b41b-06f849b72000
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["WmiComplete rule (wdm)"]
topic_type:
- apiref
api_name:
- WmiComplete
api_type:
- NA
---

# WmiComplete rule (wdm)


The **WmiComplete** rule specifies that when processing a [**WMI minor IRP**](https://msdn.microsoft.com/library/windows/hardware/ff566361), the driver calls [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) before returning from the [**DispatchSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff543412) routine.

A *WMI minor IRP* is an [**IRP\_MJ\_SYSTEM\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550813) request with a WMI minor function code.

For more information about processing WMI minor IRPs, see [**WMI Requirements for WDM Drivers**](https://msdn.microsoft.com/library/windows/hardware/ff566370), [**Handling WMI Requests**](https://msdn.microsoft.com/library/windows/hardware/ff546968), [**Windows Management Instrumentation Routines**](https://msdn.microsoft.com/library/windows/hardware/ff565794), and [**WMI Library Support Routines**](https://msdn.microsoft.com/library/windows/hardware/ff566359).

Drivers that are not registered as WMI data providers must forward the WMI request to the next lower driver. To verify this action, use the [**WmiForward**](wdm-wmiforward.md) rule.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>WmiComplete</strong> rule.</p>
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

[**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343)
[**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834)
See also
--------

[**WmiForward**](wdm-wmiforward.md)
[**WMI Requirements for WDM Drivers**](https://msdn.microsoft.com/library/windows/hardware/ff566370)
[**Handling WMI Requests**](https://msdn.microsoft.com/library/windows/hardware/ff546968)
[**WMI Library Support Routines**](https://msdn.microsoft.com/library/windows/hardware/ff566359)
 

 





