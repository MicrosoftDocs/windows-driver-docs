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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20OidProcessing%20rule%20set%20%28NDIS%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




