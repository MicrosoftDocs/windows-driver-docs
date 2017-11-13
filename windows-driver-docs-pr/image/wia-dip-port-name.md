---
title: WIA\_DIP\_PORT\_NAME
description: The WIA\_DIP\_PORT\_NAME property contains an installed device's port name, which is assigned by the kernel-mode driver that operates the device. The WIA service creates and maintains this property.
MS-HAID:
- 'WIA\_PropTable\_9a7017a0-4f3a-4f3b-9c2a-ab77f71a60c8.xml'
- 'image.wia\_dip\_port\_name'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ccb5d335-de56-477f-909c-cb2e55a0889a
keywords: ["WIA_DIP_PORT_NAME Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DIP_PORT_NAME
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_DIP\_PORT\_NAME


The WIA\_DIP\_PORT\_NAME property contains an installed device's port name, which is assigned by the kernel-mode driver that operates the device. The WIA service creates and maintains this property.

## <span id="ddk_wia_dip_port_name_si"></span><span id="DDK_WIA_DIP_PORT_NAME_SI"></span>


Property Type: VT\_BSTR

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

An application reads the WIA\_DIP\_PORT\_NAME property to determine the port name.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_DIP_PORT_NAME%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




