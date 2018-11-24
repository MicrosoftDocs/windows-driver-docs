---
title: Using Aspect Ratio and Custom Scaling Modes
description: Using Aspect Ratio and Custom Scaling Modes
ms.assetid: cafb6597-64a2-4d0f-bf7b-ab37f9a53bdc
keywords:
- aspect ratio scaling WDK display
- custom scaling WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Aspect Ratio and Custom Scaling Modes


To support aspect-ratio-preserving stretched scaling and custom scaling modes available beginning with Windows 7 (where **DXGKDDI\_INTERFACE\_VERSION** &gt;= **DXGKDDI\_INTERFACE\_VERSION\_WIN7**), the following capabilities are added to VidPN present path data used by display miniport drivers:

-   [**D3DKMDT\_VIDPN\_PRESENT\_PATH\_SCALING\_SUPPORT**](https://msdn.microsoft.com/library/windows/hardware/ff546712) structure:

    **AspectRatioCenteredMax** and **Custom** members

-   [**D3DKMDT\_VIDPN\_PRESENT\_PATH\_SCALING**](https://msdn.microsoft.com/library/windows/hardware/ff546706) enumeration:

    **D3DKMDT\_VPPS\_ASPECTRATIOCENTEREDMAX** and **D3DKMDT\_VPPS\_CUSTOM** values

### <span id="specifying_scaling_modes"></span><span id="SPECIFYING_SCALING_MODES"></span> Specifying Scaling Modes

The behavior and appearance of the desktop on the monitor using these scaling modes is described in [Scaling the Desktop Image](scaling-the-desktop-image.md). When the display mode manager (DMM) calls the [*DxgkDdiEnumVidPnCofuncModality*](https://msdn.microsoft.com/library/windows/hardware/ff559649) function, the driver must set the members of [**D3DKMDT\_VIDPN\_PRESENT\_PATH\_SCALING\_SUPPORT**](https://msdn.microsoft.com/library/windows/hardware/ff546712) according to the types of scaling that the VidPN present path supports, as follows:

<span id="________Identity_Scaling_______"></span><span id="________identity_scaling_______"></span><span id="________IDENTITY_SCALING_______"></span> Identity Scaling   
If the path can display content with no transformation, set the **Identity** member of [**D3DKMDT\_VIDPN\_PRESENT\_PATH\_SCALING\_SUPPORT**](https://msdn.microsoft.com/library/windows/hardware/ff546712) to a nonzero value. When [*DxgkDdiEnumVidPnCofuncModality*](https://msdn.microsoft.com/library/windows/hardware/ff559649) is called, set the **Scaling** member of the [**D3DKMDT\_VIDPN\_PRESENT\_PATH\_TRANSFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff546719) structure to **D3DKMDT\_VPPS\_IDENTITY**.

<span id="________Centered_Scaling_______"></span><span id="________centered_scaling_______"></span><span id="________CENTERED_SCALING_______"></span> Centered Scaling   
If the path can display content unscaled and centered on the target, set **D3DKMDT\_VIDPN\_PRESENT\_PATH\_SCALING\_SUPPORT.Centered**. When [*DxgkDdiEnumVidPnCofuncModality*](https://msdn.microsoft.com/library/windows/hardware/ff559649) is called, set **D3DKMDT\_VIDPN\_PRESENT\_PATH\_TRANSFORMATION.Scaling** to **D3DKMDT\_VPPS\_CENTERED**.

<span id="________Stretched_Scaling_______"></span><span id="________stretched_scaling_______"></span><span id="________STRETCHED_SCALING_______"></span> Stretched Scaling   
If the path can display content that is scaled to fit the target while not preserving the aspect ratio of the source, set **D3DKMDT\_VIDPN\_PRESENT\_PATH\_SCALING\_SUPPORT.Stretched**. When [*DxgkDdiEnumVidPnCofuncModality*](https://msdn.microsoft.com/library/windows/hardware/ff559649) is called, set **D3DKMDT\_VIDPN\_PRESENT\_PATH\_TRANSFORMATION.Scaling** to **D3DKMDT\_VPPS\_STRETCHED**.

<span id="________Aspect-Ratio-Preserving_Stretched_Scaling_______"></span><span id="________aspect-ratio-preserving_stretched_scaling_______"></span><span id="________ASPECT-RATIO-PRESERVING_STRETCHED_SCALING_______"></span> Aspect-Ratio-Preserving Stretched Scaling   
If the path can scale source content to fit the target while preserving the aspect ratio of the source, set **D3DKMDT\_VIDPN\_PRESENT\_PATH\_SCALING\_SUPPORT.AspectRatioCenteredMax**. When [*DxgkDdiEnumVidPnCofuncModality*](https://msdn.microsoft.com/library/windows/hardware/ff559649) is called, set **D3DKMDT\_VIDPN\_PRESENT\_PATH\_TRANSFORMATION.Scaling** to **D3DKMDT\_VPPS\_ASPECTRATIOCENTEREDMAX**.

<span id="________Custom_Scaling_______"></span><span id="________custom_scaling_______"></span><span id="________CUSTOM_SCALING_______"></span> Custom Scaling   
If the path can display one or more scaling modes that are not described by the other [**D3DKMDT\_VIDPN\_PRESENT\_PATH\_SCALING\_SUPPORT**](https://msdn.microsoft.com/library/windows/hardware/ff546712) structure members, set **D3DKMDT\_VIDPN\_PRESENT\_PATH\_SCALING\_SUPPORT.Custom**. When [*DxgkDdiEnumVidPnCofuncModality*](https://msdn.microsoft.com/library/windows/hardware/ff559649) is called, set **D3DKMDT\_VIDPN\_PRESENT\_PATH\_TRANSFORMATION.Scaling** to **D3DKMDT\_VPPS\_CUSTOM**. Independent hardware vendors (IHVs) can use private escape values to inform the driver how to interpret custom scaling on a given target.

If the current pinned target and source modes have the same aspect ratio but are different sizes, the display miniport driver should set only the **Stretched** and **Centered** members. In this case DMM will clear any nonzero value of the **AspectRatioCenteredMax** member.

### <span id="api_to_ddi_scaling"></span><span id="API_TO_DDI_SCALING"></span> API to DDI Scaling

The correspondence of user-mode API scaling values to the display miniport driver DDI scaling values in the [**D3DKMDT\_VIDPN\_PRESENT\_PATH\_SCALING**](https://msdn.microsoft.com/library/windows/hardware/ff546706) enumeration is shown in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff569533" data-raw-source="[&lt;strong&gt;SetDisplayConfig&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff569533)"><strong>SetDisplayConfig</strong></a> API Scaling Value</th>
<th align="left">DDI Scaling Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>DC_IDENTITY</p></td>
<td align="left"><p>D3DKMDT_VPPS_IDENTITY</p></td>
</tr>
<tr class="even">
<td align="left"><p>DC_CENTERED</p></td>
<td align="left"><p>D3DKMDT_VPPS_CENTERED</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DC_STRETCHED</p></td>
<td align="left"><p>D3DKMDT_VPPS_STRETCHED</p></td>
</tr>
<tr class="even">
<td align="left"><p>DC_ASPRATIOMAX</p></td>
<td align="left"><p>D3DKMDT_VPPS_ASPECTRATIOCENTEREDMAX</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DC_CUSTOM</p></td>
<td align="left"><p>D3DKMDT_VPPS_CUSTOM</p></td>
</tr>
<tr class="even">
<td align="left"><p>DC_PREFERRED</p></td>
<td align="left"><p>D3DKMDT_VPPS_PREFERRED</p></td>
</tr>
</tbody>
</table>

 

This mapping can be used with the tables in [Scaling the Desktop Image](scaling-the-desktop-image.md) to understand how user-mode scaling types are translated into DDI scaling types that are sent to the display miniport driver.

### <span id="scaling_and_driver_versions"></span><span id="SCALING_AND_DRIVER_VERSIONS"></span> Scaling and Driver Versions

The behavior of different display miniport driver versions running on different versions of the operating system are shown in the following table.

Driver Version
Operating System Version

**DXGKDDI\_INTERFACE\_VERSION** &lt; **DXGKDDI\_INTERFACE\_VERSION\_WIN7**

and

&gt;= **DXGKDDI\_INTERFACE\_VERSION\_VISTA**

**DXGKDDI\_INTERFACE\_VERSION** &gt;= **DXGKDDI\_INTERFACE\_VERSION\_WIN7**

Windows Vista

The driver has Windows Vista behavior.

The driver must check the operating system version during initialization and should never expose or use the **AspectRatioCenteredMax** and **Custom** members of **D3DKMDT\_VIDPN\_PRESENT\_PATH\_SCALING\_SUPPORT**. If the driver violates this requirement, DMM will ignore **AspectRatioCenteredMax** and **Custom** and will only recognize the **Identity**, **Centered**, or **Stretched** members. If the driver attempts to pin the **D3DKMDT\_VPPS\_ASPECTRATIOCENTEREDMAX** scaling mode on any VidPN path, DMM will return the status code **STATUS\_GRAPHICS\_INVALID\_PATH\_CONTENT\_GEOMETRY\_TRANSFORMATION** and will treat this scaling mode the same as full-screen stretch mode.

Windows 7

The operating system clears the values of the **AspectRatioCenteredMax** and **Custom** members and assumes that the driver does not support aspect-ratio-preserving stretched scaling and custom scaling modes. DMM will only set scaling modes **D3DKMDT\_VPPS\_IDENTITY**, **D3DKMDT\_VPPS\_STRETCHED**, or **D3DKMDT\_VPPS\_CENTERED**. The driver behaves as on Windows Vista.

The driver should support the **AspectRatioCenteredMax** member, and the operating system uses it from Control Panel applications. The driver can optionally implement customized functionality by setting the **Custom** member.

 

DMM will always confirm that the driver interface &gt;= **DXGKDDI\_INTERFACE\_VERSION\_WIN7** before it attempts to check and use the **AspectRatioCenteredMax** or **Custom** members of [**D3DKMDT\_VIDPN\_PRESENT\_PATH\_SCALING\_SUPPORT**](https://msdn.microsoft.com/library/windows/hardware/ff546712).

**Important**   A display miniport driver that supports the **D3DKMDT\_VPPS\_ASPECTRATIOCENTEREDMAX** or **D3DKMDT\_VPPS\_CUSTOM** values should never set a value of **D3DKMDT\_VPPS\_NOTSPECIFIED**.

 

### <span id="scaling_with_multiple_adapters"></span><span id="SCALING_WITH_MULTIPLE_ADAPTERS"></span> Scaling With Multiple Adapters

The values of the scaling types **D3DKMDT\_VPPS\_ASPECTRATIOCENTEREDMAX** and **D3DKMDT\_VPPS\_CUSTOM** introduced with Windows 7 are stored in the CCD connection database that is associated with a graphics processing unit (GPU). If the user moves a monitor from one GPU with a driver that supports these scaling members to another GPU, the second GPU might not be supported by the original driver. In this case the operating system will map these scaling types to the system default scaling.

If both GPUs support the scaling types **D3DKMDT\_VPPS\_ASPECTRATIOCENTEREDMAX** and **D3DKMDT\_VPPS\_CUSTOM**, and the driver for the first GPU implements the **D3DKMDT\_VPPS\_CUSTOM** custom scaling request, then if the user switches the monitor to the second GPU, the driver for the second GPU will probably not know how to interpret the custom scaling request. In this case the second driver should fail a call to the [**DxgkDdiCommitVidPn**](https://msdn.microsoft.com/library/windows/hardware/ff559597) function and should return the **STATUS\_GRAPHICS\_VIDPN\_MODALITY\_NOT\_SUPPORTED** status code; the operating system will map this scaling type to the system default scaling.

 

 





