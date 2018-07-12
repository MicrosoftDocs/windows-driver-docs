---
title: ChildListConfiguration rule (kmdf)
description: The ChildListConfiguration rule specifies that drivers that support Dynamic Enumeration must call WdfFdoInitSetDefaultChildListConfig before calling the WdfDeviceCreate function.
ms.assetid: B6A6A775-F2FC-4E73-9B4A-D29BF8CCB649
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["ChildListConfiguration rule (kmdf)"]
topic_type:
- apiref
api_name:
- ChildListConfiguration
api_type:
- NA
---

# ChildListConfiguration rule (kmdf)


The **ChildListConfiguration** rule specifies that drivers that support [Dynamic Enumeration](https://msdn.microsoft.com/library/windows/hardware/ff540812) must call [**WdfFdoInitSetDefaultChildListConfig**](https://msdn.microsoft.com/library/windows/hardware/ff547258) before calling the [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926) function.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>ChildListConfiguration</strong> rule.</p>
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

[**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926)
[**WdfFdoInitSetDefaultChildListConfig**](https://msdn.microsoft.com/library/windows/hardware/ff547258)
 

 





