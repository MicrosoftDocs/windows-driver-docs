---
title: Rules for Storport Drivers
description: Rules for Storport Drivers
ms.assetid: C880A30B-8629-4648-B2E3-7AC8F1A9059D
---

# Rules for Storport Drivers


This section lists and describes the [DDI compliance rules](https://msdn.microsoft.com/library/windows/hardware/ff552839) for Storport drivers that you can include in a verification of your driver.

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
<td align="left"><p>[Default rule set (Storport)](default-rule-set--storport-.md)</p></td>
<td align="left"><p>The Default rule set (Default.sdv) specifies the recommended sets of rules to use when you analyze your driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[DDI usage rule set (Storport)](ddi-usage-rule-set--storport-.md)</p></td>
<td align="left"><p>Use these rules to verify that your driver correctly uses Storport DDIs correctly.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Irql rule set (Storport)](irql-rule-set--storport-.md)</p></td>
<td align="left"><p>Use these rules to verify that your driver makes DDI calls at the required IRQL.</p>
<p>A driver that does not follow the IRQL rules can cause serious problems during operation that can lead to deadlock conditions or computer crashes.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Locking rule set (Storport)](locking-rule-set--storport-.md)</p></td>
<td align="left"><p>Use these rules to verify that your driver correctly manages shared resources.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[SrbProcessing rule set (Storport)](srbprocessing-rule-set--storport-.md)</p></td>
<td align="left"><p>Use these rules to verify that your driver correctly processes SRB requests.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[VirtualStorport rule set (Storport)](virtualstorport-rule-set--storport-.md)</p></td>
<td align="left"><p>Use these rules to verify that your driver correctly calls DDIs that are of particular interest to Storport virtual miniport (VMiniport) drivers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Warning rule set (Storport)](warning-rule-set--storport-.md)</p></td>
<td align="left"><p>Use these rules to verify that your driver can correctly processes IRPs in various contexts and follows Microsoft recommended best practices.</p></td>
</tr>
</tbody>
</table>

 

 

 





