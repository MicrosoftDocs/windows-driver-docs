---
title: DoubleDeviceInitFree rule (kmdf)
description: The DoubleDeviceInitFree rule specifies that drivers should not free device initialization structure twice.
ms.assetid: C48FB426-C958-4F4A-A1F0-C91A603DC1FD
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["DoubleDeviceInitFree rule (kmdf)"]
topic_type:
- apiref
api_name:
- DoubleDeviceInitFree
api_type:
- NA
---

# DoubleDeviceInitFree rule (kmdf)


The **DoubleDeviceInitFree** rule specifies that drivers should not free device initialization structure twice.

The [**WdfDeviceInitFree**](https://msdn.microsoft.com/library/windows/hardware/ff546050) method should not be called twice for the same device initialization structure.

|              |      |
|--------------|------|
| Driver model | KMDF |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>DoubleDeviceInitFree</strong> rule.</p>
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

[**WdfDeviceInitFree**](https://msdn.microsoft.com/library/windows/hardware/ff546050)
 

 





