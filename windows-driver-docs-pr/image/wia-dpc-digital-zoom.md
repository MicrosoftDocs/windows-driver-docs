---
title: WIA\_DPC\_DIGITAL\_ZOOM
description: The WIA\_DPC\_DIGITAL\_ZOOM property contains the effective zoom ratio of a digital camera's acquired image, scaled by a factor of 10.
MS-HAID:
- 'WIA\_PropTable\_26a2a9ea-5846-4f31-a0cf-71a979761526.xml'
- 'image.wia\_dpc\_digital\_zoom'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 5f1ec791-fd51-4397-ac7d-5012c020ef0a
keywords: ["WIA_DPC_DIGITAL_ZOOM Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_DIGITAL_ZOOM
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_DPC\_DIGITAL\_ZOOM


The WIA\_DPC\_DIGITAL\_ZOOM property contains the effective zoom ratio of a digital camera's acquired image, scaled by a factor of 10.

## <span id="ddk_wia_dpc_digital_zoom_si"></span><span id="DDK_WIA_DPC_DIGITAL_ZOOM_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST or WIA\_PROP\_RANGE

Access Rights: Read/write

Remarks
-------

A WIA\_DPC\_DIGITAL\_ZOOM value of 10 corresponds to the absence of digital zoom (1X), which is the standard scene size that the camera captures. A value of 20 corresponds to a 2X zoom, where the camera captures one-fourth of the standard scene size.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_DPC_DIGITAL_ZOOM%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




