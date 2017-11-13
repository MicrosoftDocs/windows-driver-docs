---
title: WIA\_DIP\_BAUDRATE
description: The WIA\_DIP\_BAUDRATE property contains the current baud rate setting for a device. The WIA service creates and maintains this property.
MS-HAID:
- 'WIA\_PropTable\_c657c07b-ddf1-4a4a-b0ca-740eb411ccc9.xml'
- 'image.wia\_dip\_baudrate'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 38b7c12b-ff74-49eb-9a04-6b906dcc7d44
keywords: ["WIA_DIP_BAUDRATE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DIP_BAUDRATE
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_DIP\_BAUDRATE


The WIA\_DIP\_BAUDRATE property contains the current baud rate setting for a device. The WIA service creates and maintains this property.

## <span id="ddk_wia_dip_baudrate_si"></span><span id="DDK_WIA_DIP_BAUDRATE_SI"></span>


Property Type: VT\_BSTR

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The value of the WIA\_DIP\_BAUDRATE property should be "Empty" if the device is not connected by a serial cable.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_DIP_BAUDRATE%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




