---
title: Assigning Precedence to Protection Levels
description: Assigning Precedence to Protection Levels
ms.assetid: 87a63d30-4aa2-4835-87bc-1acb062bde26
keywords:
- protection levels WDK display , assigning precedence
- protection levels WDK display , ACP precedence
- protection levels WDK display , CGMS-A precedence
- protection levels WDK display , HDCP precedence
- protection levels WDK display , DPCP precedence
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Assigning Precedence to Protection Levels


A precedence value is assigned to each protection level for each protection type. This way, a physical output can determine which protection level to use if two or more protected outputs are associated with the physical output and each protected output has a different protection level.

The Microsoft DirectX graphics kernel subsystem (*Dxgkrnl.sys*) can make more than one call to a display miniport driver's [**DxgkDdiOPMCreateProtectedOutput**](https://msdn.microsoft.com/library/windows/hardware/ff559705) function to create more than one protected output for a particular physical output. Furthermore, each of these protected outputs can have a different protection level for the same output protection type.

For example, suppose that a graphics adapter has one composite output that has the CGMS-A protection type, and that protected outputs A and B are both associated with that composite output. Next, suppose that protected output A's [**CGMS-A protection level**](https://msdn.microsoft.com/library/windows/hardware/ff560846) is set to DXGKMDT\_OPM\_CGMSA\_COPY\_NO\_MORE while protected output B's CGMS-A protection level is set to DXGKMDT\_OPM\_CGMSA\_COPY\_ONE\_GENERATION. In this situation, the physical output cannot use both protection levels. Therefore, because the physical output can output only one CGMS-A protection level at a time, the physical output must use the CGMS-A protection level with the higher precedence.

The following sections show which protection level a physical output should use (from highest to lowest precedence) when different protected outputs instruct the physical output to use different protection levels. Note that these tables apply to protected outputs with COPP or OPM semantics.

### <span id="acp_protection_level_precedence"></span><span id="ACP_PROTECTION_LEVEL_PRECEDENCE"></span>ACP Protection Level Precedence

When different protected outputs instruct the physical output to use different ACP protection levels, the physical output should use the protection level with the higher precedence as shown in the following table. Note that this table applies to protected outputs with COPP semantics.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">ACP protection level value</th>
<th align="left">Precedence</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>DXGKMDT_OPM_ACP_OFF (0)</p></td>
<td align="left"><p>Lowest precedence (0)</p></td>
</tr>
<tr class="even">
<td align="left"><p>DXGKMDT_OPM_ACP_LEVEL_ONE (1)</p></td>
<td align="left"><p>1</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DXGKMDT_OPM_ACP_LEVEL_THREE (3)</p></td>
<td align="left"><p>2</p></td>
</tr>
<tr class="even">
<td align="left"><p>DXGKMDT_OPM_ACP_LEVEL_TWO (2)</p></td>
<td align="left"><p>Highest precedence (3)</p></td>
</tr>
</tbody>
</table>

 

### <span id="cgms_a_protection_level_precedence"></span><span id="CGMS_A_PROTECTION_LEVEL_PRECEDENCE"></span>CGMS-A Protection Level Precedence

When different protected outputs instruct the physical output to use different CGMS-A protection levels, the physical output should use the protection level with the higher precedence as shown in the following table. Note that this table applies to protected outputs with COPP semantics.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">CGMS-A protection level value</th>
<th align="left">Precedence</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>DXGKMDT_OPM_CGMSA_OFF (0)</p></td>
<td align="left"><p>Lowest precedence (0)</p></td>
</tr>
<tr class="even">
<td align="left"><p>DXGKMDT_OPM_CGMSA_COPY_FREELY (1)</p></td>
<td align="left"><p>1</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DXGKMDT_OPM_CGMSA_COPY_ONE_GENERATION (3)</p></td>
<td align="left"><p>2</p></td>
</tr>
<tr class="even">
<td align="left"><p>DXGKMDT_OPM_CGMSA_COPY_NO_MORE (2)</p></td>
<td align="left"><p>3</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DXGKMDT_OPM_CGMSA_COPY_NEVER (4)</p></td>
<td align="left"><p>Highest precedence (4)</p></td>
</tr>
</tbody>
</table>

 

**Note**   The redistribution control flag (DXGKMDT\_OPM\_REDISTRIBUTION\_CONTROL\_REQUIRED) does not affect the CGMS-A precedence value. For example, (DXGKMDT\_OPM\_CGMSA\_COPY\_ONE\_GENERATION | DXGKMDT\_OPM\_REDISTRIBUTION\_CONTROL\_REQUIRED) has the same precedence value as DXGKMDT\_OPM\_CGMSA\_COPY\_ONE\_GENERATION.

 

### <span id="hdcp_protection_level_precedence"></span><span id="HDCP_PROTECTION_LEVEL_PRECEDENCE"></span>HDCP Protection Level Precedence

When different protected outputs instruct the physical output to use different HDCP protection levels, the physical output should use the protection level with the higher precedence as shown in the following table. Note that this table applies to protected outputs with COPP or OPM semantics.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">HDCP protection level value</th>
<th align="left">Precedence</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>DXGKMDT_OPM_HDCP_OFF (0)</p></td>
<td align="left"><p>Lowest precedence (0)</p></td>
</tr>
<tr class="even">
<td align="left"><p>DXGKMDT_OPM_HDCP_ON (1)</p></td>
<td align="left"><p>Highest precedence (1)</p></td>
</tr>
</tbody>
</table>

 

### <span id="dpcp_protection_level_precedence"></span><span id="DPCP_PROTECTION_LEVEL_PRECEDENCE"></span>DPCP Protection Level Precedence

When different protected outputs instruct the physical output to use different DPCP protection levels, the physical output should use the protection level with the higher precedence as shown in the following table. Note that this table applies to protected outputs with OPM semantics.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">DPCP protection level value</th>
<th align="left">Precedence</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>DXGKMDT_OPM_DPCP_OFF (0)</p></td>
<td align="left"><p>Lowest precedence (0)</p></td>
</tr>
<tr class="even">
<td align="left"><p>DXGKMDT_OPM_DPCP_ON (1)</p></td>
<td align="left"><p>Highest precedence (1)</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Assigning%20Precedence%20to%20Protection%20Levels%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




