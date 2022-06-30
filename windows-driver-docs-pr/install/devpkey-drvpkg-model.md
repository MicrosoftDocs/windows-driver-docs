---
title: DEVPKEY_DrvPkg_Model
description: The DEVPKEY_DrvPkg_Model device driver package property represents the model name for a device instance.
keywords: ["DEVPKEY_DrvPkg_Model Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_DrvPkg_Model
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.date: 06/24/2022
---

# DEVPKEY_DrvPkg_Model

The DEVPKEY_DrvPkg_Model device [driver package](./driver-packages.md) property represents the model name for a device instance.

| Attribute | Value |
|--|--|
| Property key | DEVPKEY_DrvPkg_Model |
| Property-data-type identifier | [**DEVPROP_TYPE_STRING**](devprop-type-string.md) |
| Property access | Read-only access by installation applications and installers |
| Localized? | Yes |

## Remarks

You can set the value of DEVPKEY_DrvPkg_Model by an [**INF AddProperty directive**](./inf-addproperty-directive.md) that is included in the [**INF *DDInstall* section**](./inf-ddinstall-section.md) of the INF file that installs the device. You can retrieve the value of the DEVPKEY_DrvPkg_Model property by calling [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw).

The following is an example of how to use an INF **AddProperty** directive to set the value of DEVPKEY_DrvPkg_Model for a device that is installed by an INF *DDInstall* section "SampleDDInstallSection":

```cpp
[SampleDDinstallSection]
...
AddProperty=SampleAddPropertySection
...

[SampleAddPropertySection] 
DeviceModel,,,,"DSC-530"
...
```

## Requirements

**Version**: Windows Vista and later versions of Windows

**Header**: Devpkey.h (include Devpkey.h)

## See also

[**INF AddProperty directive**](./inf-addproperty-directive.md)

[**INF *DDInstall* Section**](./inf-ddinstall-section.md)

[**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw)
