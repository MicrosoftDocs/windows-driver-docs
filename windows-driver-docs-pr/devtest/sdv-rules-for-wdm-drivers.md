---
title: Rules for WDM Drivers
description: Rules for WDM Drivers
ms.assetid: 4e8bc895-4f36-450c-8017-996df482b90d
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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20Rules%20for%20WDM%20Drivers%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




