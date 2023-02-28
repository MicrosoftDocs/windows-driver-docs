---
title: DEVPKEY_DrvPkg_DetailedDescription
description: The DEVPKEY_DrvPkg_DetailedDescription device property represents a detailed description of the capabilities of a device instance.
keywords: ["DEVPKEY_DrvPkg_DetailedDescription Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_DrvPkg_DetailedDescription
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.date: 06/24/2022
ms.topic: reference
---

# DEVPKEY_DrvPkg_DetailedDescription

The DEVPKEY_DrvPkg_DetailedDescription device property represents a detailed description of the capabilities of a device instance.

| Attribute | Value |
|--|--|
| Property key | DEVPKEY_DrvPkg_DetailedDescription |
| Property-data-type identifier | [**DEVPROP_TYPE_STRING**](devprop-type-string.md) |
| Data format | Limited set of XML tags |
| Property access | Read-only access by installation applications and installers |
| Localized? | Yes |

## Remarks

The detailed description string is in XML format. XML format makes it possible for Windows to format the display of the information based on the following subset of supported Hypertext Markup Language (HTML) tags. The operation of these tags resembles the operation of HTML tags.

- Heading level tags  

    `<h1>, <h2>, <h3>`

- List tags  

    `<ul>, <ol>, <li>`

- Paragraph tag  

    `<p>`

You can set the value of DEVPKEY_DrvPkg_DetailedDescription by an [**INF AddProperty directive**](./inf-addproperty-directive.md) that is included in the [**INF *DDInstall* section**](./inf-ddinstall-section.md) of the INF file that installs the device. You can retrieve the value of DEVPKEY_DrvPkg_DetailedDescription by calling [**CM_Get_DevNode_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_propertyw) or [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw).

The following is an example of how to use an INF **AddProperty** directive to set the value of DEVPKEY_DrvPkg_DetailedDescription for a device instance that is installed by an INF *DDInstall* section "SampleDDInstallSection":

```cpp
[SampleDDinstallSection]
...
AddProperty=SampleAddPropertySection
...

[SampleAddPropertySection] 
DeviceDetailedDescription,,,,"<xml><h1>Microsoft DiscoveryCam 530</h1><h2>Overview<h2>The Microsoft DiscoveryCam is great.<p>Really.<p><h2>Features</h2>The Microsoft DiscoveryCam has three features.<ol><li>Feature 1</li><li>Feature 2</li><li>Feature 3</li></ol></xml>"
...
```

## Requirements

**Version**: Windows Vista and later versions of Windows

**Header**: Devpkey.h (include Devpkey.h)

## See also

[**INF AddProperty Directive**](./inf-addproperty-directive.md)

[**INF *DDInstall* Section**](./inf-ddinstall-section.md)

[**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw)
