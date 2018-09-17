---
title: DanglingDeviceObjectReference rule (wdm)
description: The DanglingDeviceObjectReference rule specifies that the driver calls ObDereferenceObject with the same device object pointer that IoGetAttachedDeviceReference returned.
ms.assetid: b2aeaa16-f246-48c7-9e80-719d441a44ef
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>DanglingDeviceObjectReference</strong> rule.</p>
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

[**IoGetAttachedDeviceReference**](https://msdn.microsoft.com/library/windows/hardware/ff549145)
 

 





