---
title: DEVPKEY_DrvPkg_BrandingIcon
description: The DEVPKEY_DrvPkg_BrandingIcon device property represents a list of icons that associate a device instance with a vendor.
keywords: ["DEVPKEY_DrvPkg_BrandingIcon Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_DrvPkg_BrandingIcon
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.date: 06/24/2022
---

# DEVPKEY_DrvPkg_BrandingIcon

The DEVPKEY_DrvPkg_BrandingIcon device property represents a list of icons that associate a device instance with a vendor.

| Attribute | Value |
|--|--|
| Property key | DEVPKEY_DrvPkg_BrandingIcon |
| Property-data-type identifier | [**DEVPROP_TYPE_STRING_LIST**](devprop-type-string-list.md) |
| Property access | Read-only access by installation applications and installers |
| Localized? | Yes |

## Remarks

A branding icon can be specified as an .ico file or as a resource within an executable file.

The format of an icon list is the same as that described for the [**DEVPKEY_DrvPkg_Icon**](devpkey-drvpkg-icon.md) device property.

You can set the value of DEVPKEY_DrvPkg_BrandingIcon by an [**INF AddProperty directive**](./inf-addproperty-directive.md) that is included in the [**INF *DDInstall* section**](./inf-ddinstall-section.md) of the INF file that installs a device. You can retrieve the value of DEVPKEY_DrvPkg_BrandingIcon by calling [**CM_Get_DevNode_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_propertyw) or [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw).

## Requirements

**Version**: Windows Vista and later versions of Windows

**Header**: Devpkey.h (include Devpkey.h)

## See also

[**DEVPKEY_DrvPkg_Icon**](devpkey-drvpkg-icon.md)

[**INF AddProperty Directive**](./inf-addproperty-directive.md)

[**INF *DDInstall* Section**](./inf-ddinstall-section.md)

[**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw)
