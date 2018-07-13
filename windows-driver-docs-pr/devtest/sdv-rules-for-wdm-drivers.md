---
title: Rules for WDM Drivers
description: Rules for WDM Drivers
ms.assetid: 4e8bc895-4f36-450c-8017-996df482b90d
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["Static Driver Verifier WDK , rules", "StaticDV WDK , rules", "SDV WDK , rules", "rules WDK Static Driver Verifier"]
---

# Rules for WDM Drivers


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
<td align="left"><p>[Default rule set (WDM)](default-rule-set--wdm-.md)</p></td>
<td align="left"><p>The Default rule set (Default.sdv) specifies the recommended sets of rules to use when you analyze your driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[DDI usage rule set (WDM)](ddi-usage-rule-set--wdm-.md)</p></td>
<td align="left"><p>Use these rules to verify that your driver correctly uses WDM DDIs correctly.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[IrpPending rule set (WDM)](irppending-rule-set--wdm-.md)</p></td>
<td align="left"><p>Use these rules to verify that your driver correctly pends I/O request packets (IRP).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[IrpProcessing rule set (WDM)](irpprocessing-rule-set--wdm-.md)</p></td>
<td align="left"><p>Use these rules to verify that your driver correctly processes I/O request packets (IRP).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[IrpTracking rule set (WDM)](irptracking-rule-set--wdm-.md)</p></td>
<td align="left"><p>Use these rules to verify that your driver correctly tracks I/O request packets (IRP) so that the device is not removed while IRPs are outstanding.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Irql rule set (WDM)](irql-rule-set--wdm-.md)</p></td>
<td align="left"><p>Use these rules to verify that your driver makes DDI calls at the required IRQL.</p>
<p>A driver that does not follow the IRQL rules can cause serious problems during operation that can lead to deadlock conditions or computer crashes.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[LocalIrpProcessing rule set (WDM)](localirpprocessing-rule-set--wdm-.md)</p></td>
<td align="left"><p>Use these rules to verify that your driver correctly handles I/O request packets (IRP) that are created by the driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Locking rule set (WDM)](locking-rule-set--wdm-.md)</p></td>
<td align="left"><p>Use these rules to verify that your driver correctly manages shared resources.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Miscellaneous rule set (WDM)](miscellaneous-rule-set--wdm-.md)</p></td>
<td align="left"><p>Use these rules to verify that your driver correctly follows a general set of requirements for the proper handling of registry keys, strings and device object pointers.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Warning rule set (WDM)](warning-rule-set--wdm-.md)</p></td>
<td align="left"><p>Use these rules to verify that your driver can correctly processes IRPs in various contexts and follows Microsoft recommended best practices.</p></td>
</tr>
</tbody>
</table>

 

 

 





