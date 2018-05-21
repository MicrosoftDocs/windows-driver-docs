---
title: WmiForward rule (wdm)
description: The WmiForward rule specifies that the driver must forward WMI minor IRPs when forwarding is required.
ms.assetid: c62f37d2-ebd5-4705-9590-d1bf17137802
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["WmiForward rule (wdm)"]
topic_type:
- apiref
api_name:
- WmiForward
api_type:
- NA
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>WmiForward</strong> rule.</p>
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

[**IoAcquireRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff548204)
[**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336)
[**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654)
See also
--------

[**WMI Requirements for WDM Drivers**](https://msdn.microsoft.com/library/windows/hardware/ff566370)
[**Handling WMI Requests**](https://msdn.microsoft.com/library/windows/hardware/ff546968)
[**WMI Library Support Routines**](https://msdn.microsoft.com/library/windows/hardware/ff566359)
 

 





