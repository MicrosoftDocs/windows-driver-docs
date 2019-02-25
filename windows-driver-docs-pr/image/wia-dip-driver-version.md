---
title: WIA\_DIP\_DRIVER\_VERSION
description: The WIA\_DIP\_DRIVER\_VERSION property contains the current DLL version of a WIA minidriver. The WIA service creates and maintains this property.
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
ms.date: 11/28/2017
ms.localizationpriority: medium
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

 

 





