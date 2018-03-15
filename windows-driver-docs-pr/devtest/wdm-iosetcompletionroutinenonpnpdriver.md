---
title: IoSetCompletionRoutineNonPnpDriver rule (wdm)
description: The IoSetCompletionRoutineNonPnpDriver rule specifies that drivers that are not PnP drivers should use IoSetCompletionRoutineEx not IoSetCompletionRoutine.
ms.assetid: E4C6415B-DCB5-4AE2-9112-BC314D443C73
keywords: ["IoSetCompletionRoutineNonPnpDriver rule (wdm)"]
topic_type:
- apiref
api_name:
- IoSetCompletionRoutineNonPnpDriver
api_type:
- NA
---

# IoSetCompletionRoutineNonPnpDriver rule (wdm)


The **IoSetCompletionRoutineNonPnpDriver** rule specifies that drivers that are not PnP drivers should use [**IoSetCompletionRoutineEx**](https://msdn.microsoft.com/library/windows/hardware/ff549686) not [**IoSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549679).

The [**IoSetCompletionRoutineEx**](https://msdn.microsoft.com/library/windows/hardware/ff549686) routine avoids the actual driver image unloading after the driver has been marked for unload. This applies to non-PnP drivers since they are not notified by the PnP manager when a remove or unload is happening.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IoSetCompletionRoutineNonPnpDriver</strong> rule.</p>
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

[**IoSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549679)
 

 





