---
title: ObsoleteDDIs rule (wdm)
description: The ObsoleteDDIs rule specifies that drivers should not call FsRtlPrivateLock. This function is obsolete. Use FsRtlFastLock instead.
ms.assetid: 5C49270A-7AD1-4762-921E-7925006D0400
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["ObsoleteDDIs rule (wdm)"]
topic_type:
- apiref
api_name:
- ObsoleteDDIs
api_type:
- NA
---

# ObsoleteDDIs rule (wdm)


The **ObsoleteDDIs** rule specifies that drivers should not call [**FsRtlPrivateLock**](https://msdn.microsoft.com/library/windows/hardware/ff547164). This function is obsolete. Use [**FsRtlFastLock**](https://msdn.microsoft.com/library/windows/hardware/ff545940) instead.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>ObsoleteDDIs</strong> rule.</p>
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

 

 





