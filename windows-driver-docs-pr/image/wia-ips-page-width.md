---
title: WIA\_IPS\_PAGE\_WIDTH
description: The WIA\_IPS\_PAGE\_WIDTH property contains the width of the current page selected, in thousandths of an inch (.001). The WIA minidriver creates and maintains this property.
MS-HAID:
- 'WIA\_PropTable\_80a4e78f-6669-4a4d-813e-bb4f79e3782e.xml'
- 'image.wia\_ips\_page\_width'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: b72d32bf-6f1b-4eb2-8f7c-f0de4e2caf26
keywords: ["WIA_IPS_PAGE_WIDTH Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PAGE_WIDTH
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_IPS\_PAGE\_WIDTH


The WIA\_IPS\_PAGE\_WIDTH property contains the width of the current page selected, in thousandths of an inch (.001). The WIA minidriver creates and maintains this property.

Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

An application reads WIA\_IPS\_PAGE\_WIDTH to determine the physical dimensions of the page that is being scanned. If the extent settings are different from known page sizes, this property reports the width of the page whose [**WIA\_IPS\_PAGE\_SIZE**](wia-ips-page-size.md) property is set to WIA\_PAGE\_CUSTOM.

WIA\_IPS\_PAGE\_WIDTH must be in sync with the value of WIA\_IPS\_XEXTENT, which reports the width, in pixels, of the page to be scanned.

**Note**   The compatibility layer within the WIA service does not add support for the WIA\_IPS\_PAGE\_WIDTH property to the ADF item that is translated from a Windows XP WIA device if the property is not supported on the child item of the device. Applications should not expect an ADF item to always support WIA\_IPS\_PAGE\_WIDTH and should always check if it is supported at run time. (Typically, applications should check the support for any property to be negotiated.)

 

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
<td><p>Available in Windows Vista and later operating systems. For Windows XP, use the WIA_DPS_PAGE_WIDTH property instead.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**WIA\_DPS\_PAGE\_WIDTH**](wia-dps-page-width.md)

[**WIA\_IPS\_PAGE\_HEIGHT**](wia-ips-page-height.md)

[**WIA\_IPS\_PAGE\_SIZE**](wia-ips-page-size.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPS_PAGE_WIDTH%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





