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
ms.date: 11/28/2017
ms.localizationpriority: medium
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

## See also


[**WIA\_DPC\_EXPOSURE\_MODE**](wia-dpc-exposure-mode.md)

 

 






