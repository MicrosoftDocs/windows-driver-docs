---
title: WIA\_DIP\_DRIVER\_VERSION
description: The WIA\_DIP\_DRIVER\_VERSION property contains the current DLL version of a WIA minidriver. The WIA service creates and maintains this property.
MS-HAID:
- 'WIA\_PropTable\_02c325e1-13e8-4fea-887d-c85cd9c823eb.xml'
- 'image.wia\_dip\_driver\_version'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 708d85b0-0daa-40d9-af38-6bf69834750b
keywords: ["WIA_DIP_DRIVER_VERSION Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DIP_DRIVER_VERSION
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_DIP\_DRIVER\_VERSION


The WIA\_DIP\_DRIVER\_VERSION property contains the current DLL version of a WIA minidriver. The WIA service creates and maintains this property.

## <span id="ddk_wia_dip_driver_version_si"></span><span id="DDK_WIA_DIP_DRIVER_VERSION_SI"></span>


Property Type: VT\_BSTR

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

If the WIA minidriver does not supply a version resource, the WIA service supplies the value "0.0.0.0" as a default. An application reads WIA\_DIP\_DRIVER\_VERSION to determine the version of the WIA minidriver DLL.

**Note**   Beginning with Windows Vista, the wildcard IP address 0.0.0.0 is not available.
Also beginning with Windows Vista, if the **IPAutoconfigurationEnabled** registry key is set to a value of 0, automatic IP address assignment is disabled, and no IP address is assigned. In this case, the **ipconfig** command line tool will not display an IP address. If the key is set to a nonzero value, an IP address is automatically assigned. This key can be located at the following paths in the registry:

**HKEY\_LOCAL\_MACHINE\\SYSTEM\\Current Control Set\\Services\\Tcpip\\Parameters\\IPAutoconfigurationEnabled**

**HKEY\_LOCAL\_MACHINE\\SYSTEM\\Current Control Set\\Services\\Tcpip\\Parameters\\Interfaces\\*GUID*\\IPAutoconfigurationEnabled**

 

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
<td><p>Available in Microsoft Windows XP and later operating systems.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_DIP_DRIVER_VERSION%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




