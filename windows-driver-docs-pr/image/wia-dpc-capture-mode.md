---
title: WIA\_DPC\_CAPTURE\_MODE
description: The WIA\_DPC\_CAPTURE\_MODE property sets the image capture mode.
MS-HAID:
- 'WIA\_PropTable\_337e54d1-039a-4153-b194-6a5e16d3a75b.xml'
- 'image.wia\_dpc\_capture\_mode'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 32d117ac-fa20-49cc-a34e-31a1be88804e
keywords: ["WIA_DPC_CAPTURE_MODE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_CAPTURE_MODE
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_DPC\_CAPTURE\_MODE


The WIA\_DPC\_CAPTURE\_MODE property sets the image capture mode.

## <span id="ddk_wia_dpc_capture_mode_si"></span><span id="DDK_WIA_DPC_CAPTURE_MODE_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/write

Remarks
-------

The following table describes the three constants that are valid with the WIA\_DPC\_CAPTURE\_MODE property.

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
<td><p>CAPTUREMODE_BURST</p></td>
<td><p>Capture more than one image in quick succession as defined by the values of the [<strong>WIA_DPC_BURST_NUMBER</strong>](wia-dpc-burst-number.md) and [<strong>WIA_DPC_BURST_INTERVAL</strong>](wia-dpc-burst-interval.md) properties.</p></td>
</tr>
<tr class="even">
<td><p>CAPTUREMODE_NORMAL</p></td>
<td><p>Normal mode for the camera.</p></td>
</tr>
<tr class="odd">
<td><p>CAPTUREMODE_TIMELAPSE</p></td>
<td><p>Capture more than one image in succession as defined by the [<strong>WIA_DPC_TIMELAPSE_NUMBER</strong>](wia-dpc-timelapse-number.md) and [<strong>WIA_DPC_TIMELAPSE_INTERVAL</strong>](wia-dpc-timelapse-interval.md) properties.</p></td>
</tr>
</tbody>
</table>

 

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


[**WIA\_DPC\_BURST\_INTERVAL**](wia-dpc-burst-interval.md)

[**WIA\_DPC\_BURST\_NUMBER**](wia-dpc-burst-number.md)

[**WIA\_DPC\_TIMELAPSE\_INTERVAL**](wia-dpc-timelapse-interval.md)

[**WIA\_DPC\_TIMELAPSE\_NUMBER**](wia-dpc-timelapse-number.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_DPC_CAPTURE_MODE%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





