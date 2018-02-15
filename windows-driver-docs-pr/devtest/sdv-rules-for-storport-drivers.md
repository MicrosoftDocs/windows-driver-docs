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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20Rules%20for%20Storport%20Drivers%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




