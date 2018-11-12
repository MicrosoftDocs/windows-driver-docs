---
title: DanglingDeviceObjectReference rule (wdm)
description: The DanglingDeviceObjectReference rule specifies that the driver calls ObDereferenceObject with the same device object pointer that IoGetAttachedDeviceReference returned.
ms.assetid: b2aeaa16-f246-48c7-9e80-719d441a44ef
ms.date: 05/21/2018
keywords: ["DanglingDeviceObjectReference rule (wdm)"]
topic_type:
- apiref
api_name:
- DanglingDeviceObjectReference
api_type:
- NA
ms.localizationpriority: medium
---

# DanglingDeviceObjectReference rule (wdm)


The **DanglingDeviceObjectReference** rule specifies that the driver calls [**ObDereferenceObject**](https://msdn.microsoft.com/library/windows/hardware/ff557724) with the same device object pointer that [**IoGetAttachedDeviceReference**](https://msdn.microsoft.com/library/windows/hardware/ff549145) returned.

This rule also specifies that all device object pointers that the driver referenced by calling **IoGetAttachedDeviceReference** are dereferenced by calling **ObDereferenceObject** before the driver exits. ObfDereferenceObject

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>DanglingDeviceObjectReference</strong> rule.</p>
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

[**IoGetAttachedDeviceReference**](https://msdn.microsoft.com/library/windows/hardware/ff549145)
 

 





