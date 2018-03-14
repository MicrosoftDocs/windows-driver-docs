---
title: Rules for NDIS Drivers
description: Rules for NDIS Drivers
ms.assetid: fd31b797-1175-4f65-8fa0-a50acd01f446
---

# Rules for NDIS Drivers


This section lists and describes the [Static Driver Verifier rules](https://msdn.microsoft.com/library/windows/hardware/ff552839) for NDIS drivers that you can include in a verification of your driver.

## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[Default rule set (NDIS)](default-rule-set--ndis-.md)</p></td>
<td align="left"><p>The Default rule set (Default.sdv) specifies the recommended sets of rules to use when you analyze your driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[DDI usage rule set (NDIS)](ddi-usage-rule-set--ndis-.md)</p></td>
<td align="left"><p>Use these rules to verify that your driver correctly uses NDIS DDIs correctly.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[IRQL rule set (NDIS)](irql-rule-set--ndis-.md)</p></td>
<td align="left"><p>Use these rules to verify that your driver makes DDI calls at the required IRQL.</p>
<p>A driver that does not follow the IRQL rules can cause serious problems during operation that can lead to deadlock conditions or computer crashes.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Locking rule set (NDIS)](locking-rule-set--ndis-.md)</p></td>
<td align="left"><p>Use these rules to verify that your driver correctly manages shared resources.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Memory usage rule set (NDIS)](memory-usage-rule-set--ndis-.md)</p></td>
<td align="left"><p>Use these rules to verify that your driver correctly calls NDIS functions to allocate and free memory.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Miscellaneous rule set (NDIS)](miscellaneous-rule-set--ndis-.md)</p></td>
<td align="left"><p>Use these rules to verify that your driver correctly follows a general set of requirements for the proper handling of timers, pause operations, keys, strings and bindings.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OidProcessing rule set (NDIS)](oidprocessing-rule-set--ndis-.md)</p></td>
<td align="left"><p>Use these rules to verify that your driver correctly processes OID requests.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Warning rule set (NDIS)](warning-rule-set--ndis-.md)</p></td>
<td align="left"><p>Use these rules to verify that your driver can correctly processes IRPs in various contexts and follows Microsoft recommended best practices.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[NDIS/WIFI verification rule set](ndis-wifi-verification-rule-set.md)</p></td>
<td align="left"><blockquote>
[!Note]<br />
You can test NDIS/WIFI drivers with these rules starting with Windows 8.1.
</blockquote>
 </td>
</tr>
</tbody>
</table>

 

 

 





