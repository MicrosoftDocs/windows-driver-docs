---
title: WmiForward rule (wdm)
description: The WmiForward rule specifies that the driver must forward WMI minor IRPs when forwarding is required.
ms.assetid: c62f37d2-ebd5-4705-9590-d1bf17137802
ms.date: 05/21/2018
keywords: ["WmiForward rule (wdm)"]
topic_type:
- apiref
api_name:
- WmiForward
api_type:
- NA
ms.localizationpriority: medium
---

# WmiForward rule (wdm)


The **WmiForward** rule specifies that the driver must forward [**WMI minor IRPs**](https://msdn.microsoft.com/library/windows/hardware/ff566361) when forwarding is required.

Specifically, when the driver calls [**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834) and the value of the *IrpDisposition* parameter is **IrpForward**, the driver must call [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) or [**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654) to forward the IRP before returning from the dispatch routine.

This rule does not apply to bus drivers.

A *WMI minor IRP* is an [**IRP\_MJ\_SYSTEM\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550813) request with a WMI minor function code.

For more information about processing WMI minor IRPs, see [**WMI Requirements for WDM Drivers**](https://msdn.microsoft.com/library/windows/hardware/ff566370), [**Handling WMI Requests**](https://msdn.microsoft.com/library/windows/hardware/ff546968), [**Windows Management Instrumentation Routines**](https://msdn.microsoft.com/library/windows/hardware/ff565794), and [**WMI Library Support Routines**](https://msdn.microsoft.com/library/windows/hardware/ff566359).

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>WmiForward</strong> rule.</p>
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

Applies to
----------

[**IoAcquireRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff548204)
[**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336)
[**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654)
See also
--------

[**WMI Requirements for WDM Drivers**](https://msdn.microsoft.com/library/windows/hardware/ff566370)
[**Handling WMI Requests**](https://msdn.microsoft.com/library/windows/hardware/ff546968)
[**WMI Library Support Routines**](https://msdn.microsoft.com/library/windows/hardware/ff566359)
 

 





