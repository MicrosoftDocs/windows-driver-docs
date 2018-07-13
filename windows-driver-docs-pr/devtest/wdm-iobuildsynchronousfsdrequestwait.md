---
title: IoBuildSynchronousFsdRequestWait rule (wdm)
description: The IoBuildSynchronousFsdRequestWait rule specifies that KeWaitForSingleObject should be called in the case that IoCallDriver or PoCallDriver returns STATUS\_PENDING.
ms.assetid: 99C717B3-1125-4DD9-81A8-1DC4F506B719
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["IoBuildSynchronousFsdRequestWait rule (wdm)"]
topic_type:
- apiref
api_name:
- IoBuildSynchronousFsdRequestWait
api_type:
- NA
---

# IoBuildSynchronousFsdRequestWait rule (wdm)


The **IoBuildSynchronousFsdRequestWait** rule specifies that [**KeWaitForSingleObject**](https://msdn.microsoft.com/library/windows/hardware/ff553350) should be called in the case that [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) or [**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654) returns STATUS\_PENDING.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IoBuildSynchronousFsdRequestWait</strong> rule.</p>
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

[**IoBuildSynchronousFsdRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548330)
[**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336)
[**KeInitializeEvent**](https://msdn.microsoft.com/library/windows/hardware/ff552137)
[**KeWaitForSingleObject**](https://msdn.microsoft.com/library/windows/hardware/ff553350)
[**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654)
 

 





