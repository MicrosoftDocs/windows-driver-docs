---
title: DEVPKEY_DrvPkg_VendorWebSite
description: The DEVPKEY_DrvPkg_VendorWebSite device property represents a vendor URL for a device instance.
keywords: ["DEVPKEY_DrvPkg_VendorWebSite Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_DrvPkg_VendorWebSite
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.date: 06/24/2022
ms.topic: reference
---

# DEVPKEY_DrvPkg_VendorWebSite

The DEVPKEY_DrvPkg_VendorWebSite device property represents a vendor URL for a device instance.

| Attribute | Value |
|--|--|
| Property key | DEVPKEY_DrvPkg_VendorWebSite |
| Property-data-type identifier | [DEVPROP_TYPE_STRING](devprop-type-string.md) |
| Property access | Read-only access by installation applications and installers |
| Localized? | Yes |

## Remarks

The URL can be a link to the root of the vendor website, a webpage within a website, or a redirection page. The URL can also contain parameters, for example, the following URL contains a **prod** parameter that supplies the product identifier "DSC530" and a **rev** parameter that supplies the number "34":

```cpp
http://www.microsoft.com/redirect?prod=DSC530&rev=34
```

You can set the value of DEVPKEY_DrvPkg_VendorWebSite by an [**INF AddProperty directive**](./inf-addproperty-directive.md) that is included in the [**INF DDInstall section**](./inf-ddinstall-section.md) of the INF file that installs the device. You can retrieve the value of DEVPKEY_DrvPkg_VendorWebSite by calling [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw).

The following is an example of how to use an INF **AddProperty** directive to set the DEVPKEY_DrvPkg_VendorWebSite property value for a device that is installed by an INF *DDInstall* section "SampleDDInstallSection":

```cpp
[SampleDDinstallSection]
...
AddProperty=SampleAddPropertySection
...

[SampleAddPropertySection]
DeviceVendorWebsite,,,,"http://www.microsoft.com/redirect?prod=DSC530&rev=34"
...
```

## Requirements

**Version**: Windows Vista and later versions of Windows

**Header**: Devpkey.h (include Devpkey.h)

## See also

[**INF AddProperty Directive**](./inf-addproperty-directive.md)

[**INF *DDInstall* Section**](./inf-ddinstall-section.md)

[**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw)
