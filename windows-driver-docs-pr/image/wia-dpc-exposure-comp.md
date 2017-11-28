---
title: WIA\_DPC\_EXPOSURE\_COMP
description: The WIA\_DPC\_EXPOSURE\_COMP property enables you to adjust the set point of a digital camera's auto-exposure control.
ms.assetid: 4b3cb013-d5fa-4f9f-9d7b-43136fab0e30
keywords: ["WIA_DPC_EXPOSURE_COMP Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_EXPOSURE_COMP
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_DPC\_EXPOSURE\_COMP


The WIA\_DPC\_EXPOSURE\_COMP property enables you to adjust the set point of a digital camera's auto-exposure control.

## <span id="ddk_wia_dpc_exposure_comp_si"></span><span id="DDK_WIA_DPC_EXPOSURE_COMP_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_RANGE or WIA\_PROP\_LIST

Access Rights: Read/write

Remarks
-------

You can use the WIA\_DPC\_EXPOSURE\_COMP property to adjust the set point of a digital camera's auto-exposure control. Setting WIA\_DPC\_EXPOSURE\_COMP to zero does not change the factory-set auto-exposure level.

The units of WIA\_DPC\_EXPOSURE\_COMP are in "stops" that are scaled by a factor of 1000, to allow for fractional stop values. Setting WIA\_DPC\_EXPOSURE\_COMP to 2000 corresponds to two stops more exposure (four times more energy on the sensor), so images will be brighter. Setting WIA\_DPC\_EXPOSURE\_COMP to −1000 corresponds to one stop less exposure (one-half the energy on the sensor), so images will be darker.

The setting values are in Additive System of Photographic Exposure (APEX) units.

This property may be expressed as either a list or a range of values. This property is typically used only when a device has the [**WIA\_DPC\_EXPOSURE\_MODE**](wia-dpc-exposure-mode.md) property set to EXPOSUREMODE\_MANUAL.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Obsolete in Windows Vista and later operating systems and should no longer be used. However, this property is still defined in Windows Vista for compatibility with applications and devices designed for Windows Server 2003, Windows XP, and previous versions of Windows.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**WIA\_DPC\_EXPOSURE\_MODE**](wia-dpc-exposure-mode.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_DPC_EXPOSURE_COMP%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





