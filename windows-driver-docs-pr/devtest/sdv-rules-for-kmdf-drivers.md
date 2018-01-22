---
title: Rules for KMDF Drivers
description: Rules for KMDF Drivers
ms.assetid: 63ac4df5-b2dc-43da-abaa-49c5de036d79
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
<td align="left"><p>[Default rule set (KMDF)](default-rule-set--kmdf-.md)</p></td>
<td align="left"><p>The Default rule set (Default.sdv) specifies the recommended sets of rules to use when you analyze your driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[DDI usage rule set (KMDF)](ddi-usage-rule-set--kmdf-.md)</p></td>
<td align="left"><p>Use these rules to verify that your driver correctly uses KMDF DDIs correctly.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[IrpProcessing rule set (KMDF)](irpprocessing-rule-set--kmdf-.md)</p></td>
<td align="left"><p>Use these rules to verify that your driver correctly processes I/O request packets (IRP).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Irql rule set (KMDF)](irql-rule-set--kmdf-.md)</p></td>
<td align="left"><p>Use these rules to verify that your driver makes DDI calls at the required IRQL.</p>
<p>A driver that does not follow the IRQL rules can cause serious problems during operation that can lead to deadlock conditions or computer crashes.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Locking rule set (KMDF)](locking-rule-set--kmdf-.md)</p></td>
<td align="left"><p>Use these rules to verify that your driver correctly manages shared resources.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Miscellaneous rule set (KMDF)](miscellaneous-rule-set--kmdf-.md)</p></td>
<td align="left"><p>Use these rules to verify that your driver correctly follows a general set of requirements for the proper handling of device objects, keys, and that the driver does not makes calls to DDIs that are not appropriate for a non-PnP driver or for a non-FDO driver that is not a power policy owner.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[RequestProcessing rule set (KMDF)](requestprocessing-rule-set--kmdf-.md)</p></td>
<td align="left"><p>Use these rules to verify that your driver correctly completes or cancels I/O request packets (IRP).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Usb rule set (KMDF)](usb-rule-set--kmdf-.md)</p></td>
<td align="left"><p>Use these rules to verify that your driver correctly handles some specialized KMDF methods for USB devices.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Warning rule set (KMDF)](warning-rule-set--kmdf-.md)</p></td>
<td align="left"><p>Use these rules to verify that your driver can correctly processes IRPs in various contexts and follows Microsoft recommended best practices.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20Rules%20for%20KMDF%20Drivers%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




