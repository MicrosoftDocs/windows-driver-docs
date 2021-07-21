---
title: DEVPKEY_DrvPkg_BrandingIcon
description: DEVPKEY_DrvPkg_BrandingIcon
keywords: ["DEVPKEY_DrvPkg_BrandingIcon Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_DrvPkg_BrandingIcon
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPKEY_DrvPkg_BrandingIcon


The DEVPKEY_DrvPkg_BrandingIcon device property represents a list of icons that associate a device instance with a vendor.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_DrvPkg_BrandingIcon</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-string-list.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_STRING_LIST&lt;/strong&gt;](devprop-type-string-list.md)"><strong>DEVPROP_TYPE_STRING_LIST</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read-only access by installation applications and installers</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>Yes</p></td>
</tr>
</tbody>
</table>

 

## Remarks

A branding icon can be specified as an .ico file or as a resource within an executable file.

The format of an icon list is the same as that described for the [**DEVPKEY_DrvPkg_Icon**](devpkey-drvpkg-icon.md) device property.

You can set the value of DEVPKEY_DrvPkg_BrandingIcon by an [**INF AddProperty directive**](./inf-addproperty-directive.md) that is included in the [**INF *DDInstall* section**](./inf-ddinstall-section.md) of the INF file that installs a device. You can retrieve the value of DEVPKEY_DrvPkg_BrandingIcon by calling [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw).

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows Vista and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Devpkey.h (include Devpkey.h)</td>
</tr>
</tbody>
</table>

## See also


[**DEVPKEY_DrvPkg_Icon**](devpkey-drvpkg-icon.md)

[**INF AddProperty Directive**](./inf-addproperty-directive.md)

[**INF *DDInstall* Section**](./inf-ddinstall-section.md)

[**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw)

 

