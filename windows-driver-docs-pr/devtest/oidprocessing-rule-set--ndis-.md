---
title: OidProcessing rule set (NDIS)
description: Use these rules to verify that your driver correctly processes OID requests.
ms.assetid: 0E12778B-BB86-4387-9B8A-19E3876D6F8C
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
<td align="left"><p>[<strong>DoubleComplete</strong>](ndis-doublecomplete.md)</p></td>
<td align="left"><p>The [DoubleComplete](ndis-doublecomplete.md) rule specifies that NDIS drivers must not complete an object identifier (OID) request multiple times.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DoubleCompleteWorkItem</strong>](ndis-doublecompleteworkitem.md)</p></td>
<td align="left"><p>The DoubleCompleteWorkItem rule specifies that NDIS drivers must not complete an OID request multiple times when the completion is deferred in a work item.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NdisMNetPnPEventInOIDRequest</strong>](ndis-ndismnetpnpeventinoidrequest.md)</p></td>
<td align="left"><p>This rule checks that [<strong>NdisMNetPnPEvent</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563616) is not called in the context of an OID request.</p></td>
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

 

 





