---
title: IoBuildFsdComplete rule (wdm)
description: The IoBuildFsdComplete rule specifies that a driver should not call IoCompleteRequest if the IRP was created with IoBuildAsynchronousFsdRequest.
ms.assetid: 51F3411F-0D59-4341-94C3-8FAF4B98BB3E
keywords: ["IoBuildFsdComplete rule (wdm)"]
topic_type:
- apiref
api_name:
- IoBuildFsdComplete
api_type:
- NA
---

# IoBuildFsdComplete rule (wdm)


The **IoBuildFsdComplete** rule specifies that a driver should not call [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) if the IRP was created with [**IoBuildAsynchronousFsdRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548310).

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IoBuildFsdComplete</strong> rule.</p>
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

[**IoBuildAsynchronousFsdRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548310)
[**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343)
 

 





