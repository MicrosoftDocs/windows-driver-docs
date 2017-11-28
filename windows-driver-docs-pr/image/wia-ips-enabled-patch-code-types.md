---
title: WIA\_IPS\_ENABLED\_PATCH\_CODE\_TYPES
description: The WIA\_IPS\_ENABLED\_PATCH\_CODE\_TYPES property is used to select the enabled patch codes for which the Patch Code Reader will search in the current session.
ms.assetid: 278C93EF-661E-41B2-8882-DF05A2FB9723
keywords: ["WIA_IPS_ENABLED_PATCH_CODE_TYPES Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_ENABLED_PATCH_CODE_TYPES
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_IPS\_ENABLED\_PATCH\_CODE\_TYPES


The **WIA\_IPS\_ENABLED\_PATCH\_CODE\_TYPES** property is used to select the enabled patch codes for which the Patch Code Reader will search in the current session. These patch codes can be some or all the values that the WIA minidriver reports for [**WIA\_IPS\_SUPPORTED\_PATCH\_CODE\_TYPES**](wia-ips-supported-patch-code-types.md). The order of the values in the array specifies the priority order in which the respective patch codes are to be searched.

## <span id="ddk_wia_ipa_depth_si"></span><span id="DDK_WIA_IPA_DEPTH_SI"></span>


Property Type: VT\_I4 | VT\_VECTOR

Valid Values: WIA\_PROP\_NONE (single 'array'/vector value)

Access Rights: Read/Write

Remarks
-------

The valid values for the **WIA\_IPS\_ENABLED\_PATCH\_CODE\_TYPES** property are the same WIA\_PATCH\_CODE\_ values that are defined for the [**WIA\_IPS\_SUPPORTED\_PATCH\_CODE\_TYPES**](wia-ips-supported-patch-code-types.md) property.

This property is required for all Patch Code Reader items.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPS_ENABLED_PATCH_CODE_TYPES%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




