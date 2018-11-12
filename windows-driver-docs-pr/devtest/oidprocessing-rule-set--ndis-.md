---
title: OidProcessing rule set (NDIS)
description: Use these rules to verify that your driver correctly processes OID requests.
ms.assetid: 0E12778B-BB86-4387-9B8A-19E3876D6F8C
ms.date: 05/21/2018
ms.localizationpriority: medium
---

# OidProcessing rule set (NDIS)


Use these rules to verify that your driver correctly processes OID requests.

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
<td align="left"><p><a href="ndis-doublecomplete.md" data-raw-source="[&lt;strong&gt;DoubleComplete&lt;/strong&gt;](ndis-doublecomplete.md)"><strong>DoubleComplete</strong></a></p></td>
<td align="left"><p>The <a href="ndis-doublecomplete.md" data-raw-source="[DoubleComplete](ndis-doublecomplete.md)">DoubleComplete</a> rule specifies that NDIS drivers must not complete an object identifier (OID) request multiple times.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ndis-doublecompleteworkitem.md" data-raw-source="[&lt;strong&gt;DoubleCompleteWorkItem&lt;/strong&gt;](ndis-doublecompleteworkitem.md)"><strong>DoubleCompleteWorkItem</strong></a></p></td>
<td align="left"><p>The DoubleCompleteWorkItem rule specifies that NDIS drivers must not complete an OID request multiple times when the completion is deferred in a work item.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ndis-ndismnetpnpeventinoidrequest.md" data-raw-source="[&lt;strong&gt;NdisMNetPnPEventInOIDRequest&lt;/strong&gt;](ndis-ndismnetpnpeventinoidrequest.md)"><strong>NdisMNetPnPEventInOIDRequest</strong></a></p></td>
<td align="left"><p>This rule checks that <a href="https://msdn.microsoft.com/library/windows/hardware/ff563616" data-raw-source="[&lt;strong&gt;NdisMNetPnPEvent&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563616)"><strong>NdisMNetPnPEvent</strong></a> is not called in the context of an OID request.</p></td>
</tr>
</tbody>
</table>

 

**To select the OidProcessing rule set**

1.  Select your driver project (.vcxProj) in Microsoft Visual Studio. From the **Driver** menu, click **Launch Static Driver Verifier…**.

2.  Click the **Rules** tab. Under **Rule Sets**, select **OidProcessing**.

    To select the default rule set from a Visual Studio developer command prompt window, specify **OidProcessing.sdv** with the **/check** option. For example:

    ```
    msbuild /t:sdv /p:Inputs="/check:OidProcessing.sdv" mydriver.VcxProj /p:Configuration="Win8 Release" /p:Platform=Win32
    ```

    For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281) and [Static Driver Verifier commands (MSBuild)](https://msdn.microsoft.com/library/windows/hardware/hh466459).

 

 





