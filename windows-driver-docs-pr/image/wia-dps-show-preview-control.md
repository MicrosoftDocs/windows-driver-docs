---
title: WIA\_DPS\_SHOW\_PREVIEW\_CONTROL
description: The WIA\_DPS\_SHOW\_PREVIEW\_CONTROL property indicates whether an item needs a preview control displayed to the user. The WIA minidriver creates and maintains this property.
ms.assetid: 45bd6030-34b1-466b-b594-e7ee0d2902f9
keywords: ["WIA_DPS_SHOW_PREVIEW_CONTROL Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_SHOW_PREVIEW_CONTROL
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WIA\_DPS\_SHOW\_PREVIEW\_CONTROL


The WIA\_DPS\_SHOW\_PREVIEW\_CONTROL property indicates whether an item needs a preview control displayed to the user. The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_dps_show_preview_control_si"></span><span id="DDK_WIA_DPS_SHOW_PREVIEW_CONTROL_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The following table describes the constants that are valid with WIA\_DPS\_SHOW\_PREVIEW\_CONTROL.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>WIA_DONT_SHOW_PREVIEW_CONTROL</p></td>
<td><p>Do not show a preview control to the user, because this device cannot perform a preview.</p></td>
</tr>
<tr class="even">
<td><p>WIA_SHOW_PREVIEW_CONTROL</p></td>
<td><p>Show a preview control to the user, because this device can perform a preview.</p></td>
</tr>
</tbody>
</table>

 

The WIA\_DPS\_SHOW\_PREVIEW\_CONTROL property helps control devices that cannot preview. For example, some feeder-driven devices cannot reload the paper for a preview scan.

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
<td><p>Available with Microsoft Windows XP. ForWindows Vista and later, use the WIA_IPS_SHOW_PREVIEW_CONTROL property.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**WIA\_IPS\_SHOW\_PREVIEW\_CONTROL**](wia-ips-show-preview-control.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_DPS_SHOW_PREVIEW_CONTROL%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





