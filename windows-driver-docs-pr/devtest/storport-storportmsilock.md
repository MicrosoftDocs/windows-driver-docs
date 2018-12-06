---
title: StorPortMSILock rule (storport)
description: Miniport drivers are required to acquire the MSI spin lock for a message if, and only if, the InterruptSynchronizationMode member of the PORT\_CONFIGURATION\_INFORMATION (Storport) structure is set to InterruptSynchronizePerMessage.
ms.assetid: 99C45ADB-AFCC-4B9E-8EB9-DBD7C7F6D800
ms.date: 05/21/2018
keywords: ["StorPortMSILock rule (storport)"]
topic_type:
- apiref
api_name:
- StorPortMSILock
api_type:
- NA
ms.localizationpriority: medium
---

# StorPortMSILock rule (storport)


Miniport drivers are required to acquire the MSI spin lock for a message if, and only if, the **InterruptSynchronizationMode** member of the [**PORT\_CONFIGURATION\_INFORMATION (Storport)**](https://msdn.microsoft.com/library/windows/hardware/ff563901) structure is set to **InterruptSynchronizePerMessage**. This rule verifies that calls to [**StorPortAcquireMSISpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff567023) are only made if the synchronization mode is **InterruptSynchronizePerMessage**.

|              |          |
|--------------|----------|
| Driver model | Storport |

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>StorPortMSILock</strong> rule.</p>
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

 

 





