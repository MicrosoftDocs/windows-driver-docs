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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20Rules%20for%20NDIS%20Drivers%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




