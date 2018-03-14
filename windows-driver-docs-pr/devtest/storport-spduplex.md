---
title: SpDuplex rule (storport)
description: This rule verifies that this miniport is in Full Duplex mode. Any driver built according to the StorPort-miniport model must be in Full Duplex mode. Half Duplex should only be used when porting an existing SCSI driver to StorPort.
ms.assetid: 07B331B4-F0D6-48C4-BEEC-166D43F60E41
keywords: ["SpDuplex rule (storport)"]
topic_type:
- apiref
api_name:
- SpDuplex
api_type:
- NA
---

# SpDuplex rule (storport)


This rule verifies that this miniport is in **Full Duplex** mode. Any driver built according to the StorPort-miniport model must be in **Full Duplex** mode. **Half Duplex** should only be used when porting an existing SCSI driver to StorPort.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>SpDuplex</strong> rule.</p>
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

 

 





