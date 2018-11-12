---
title: Rules for KMDF Drivers
description: Rules for KMDF Drivers
ms.assetid: 63ac4df5-b2dc-43da-abaa-49c5de036d79
ms.date: 05/21/2018
ms.localizationpriority: medium
---

# Rules for KMDF Drivers


This section lists and describes the [DDI Compliance Rules](static-driver-verifier-rules.md) for Kernel Mode Driver Framework (KMDF) drivers that you can include in a verification.

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
<td align="left"><p><a href="default-rule-set--kmdf-.md" data-raw-source="[Default rule set (KMDF)](default-rule-set--kmdf-.md)">Default rule set (KMDF)</a></p></td>
<td align="left"><p>The Default rule set (Default.sdv) specifies the recommended sets of rules to use when you analyze your driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ddi-usage-rule-set--kmdf-.md" data-raw-source="[DDI usage rule set (KMDF)](ddi-usage-rule-set--kmdf-.md)">DDI usage rule set (KMDF)</a></p></td>
<td align="left"><p>Use these rules to verify that your driver correctly uses KMDF DDIs correctly.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="irpprocessing-rule-set--kmdf-.md" data-raw-source="[IrpProcessing rule set (KMDF)](irpprocessing-rule-set--kmdf-.md)">IrpProcessing rule set (KMDF)</a></p></td>
<td align="left"><p>Use these rules to verify that your driver correctly processes I/O request packets (IRP).</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="irql-rule-set--kmdf-.md" data-raw-source="[Irql rule set (KMDF)](irql-rule-set--kmdf-.md)">Irql rule set (KMDF)</a></p></td>
<td align="left"><p>Use these rules to verify that your driver makes DDI calls at the required IRQL.</p>
<p>A driver that does not follow the IRQL rules can cause serious problems during operation that can lead to deadlock conditions or computer crashes.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="locking-rule-set--kmdf-.md" data-raw-source="[Locking rule set (KMDF)](locking-rule-set--kmdf-.md)">Locking rule set (KMDF)</a></p></td>
<td align="left"><p>Use these rules to verify that your driver correctly manages shared resources.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="miscellaneous-rule-set--kmdf-.md" data-raw-source="[Miscellaneous rule set (KMDF)](miscellaneous-rule-set--kmdf-.md)">Miscellaneous rule set (KMDF)</a></p></td>
<td align="left"><p>Use these rules to verify that your driver correctly follows a general set of requirements for the proper handling of device objects, keys, and that the driver does not makes calls to DDIs that are not appropriate for a non-PnP driver or for a non-FDO driver that is not a power policy owner.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="requestprocessing-rule-set--kmdf-.md" data-raw-source="[RequestProcessing rule set (KMDF)](requestprocessing-rule-set--kmdf-.md)">RequestProcessing rule set (KMDF)</a></p></td>
<td align="left"><p>Use these rules to verify that your driver correctly completes or cancels I/O request packets (IRP).</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="usb-rule-set--kmdf-.md" data-raw-source="[Usb rule set (KMDF)](usb-rule-set--kmdf-.md)">Usb rule set (KMDF)</a></p></td>
<td align="left"><p>Use these rules to verify that your driver correctly handles some specialized KMDF methods for USB devices.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="warning-rule-set--kmdf-.md" data-raw-source="[Warning rule set (KMDF)](warning-rule-set--kmdf-.md)">Warning rule set (KMDF)</a></p></td>
<td align="left"><p>Use these rules to verify that your driver can correctly processes IRPs in various contexts and follows Microsoft recommended best practices.</p></td>
</tr>
</tbody>
</table>

 

 

 





