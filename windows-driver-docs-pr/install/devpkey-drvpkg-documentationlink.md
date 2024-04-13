---
title: DEVPKEY_DrvPkg_DocumentationLink
description: DEVPKEY_DrvPkg_DocumentationLink
keywords: ["DEVPKEY_DrvPkg_DocumentationLink Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_DrvPkg_DocumentationLink
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.date: 10/17/2018
ms.topic: reference
---

# DEVPKEY_DrvPkg_DocumentationLink

The DEVPKEY_DrvPkg_DocumentationLink device property represents a URL to the documentation for a device instance.

|Attribute|Value|
|----|----|
|**Property key**|DEVPKEY_DrvPkg_DocumentationLink|
|**Property-data-type identifier**|[DEVPROP_TYPE_STRING](devprop-type-string.md)|
|**Property access**|Read-only access by installation applications and installers|
|**Localized?**|Yes|

## Remarks

The documentation link URL should be a link to a file that contains information about a device. This property is intended to provide Web-accessible documentation for a device. The file can be an HTML page, a *.pdf* file, a *.doc* file, or other file type. The only restriction is that all the documentation content must be contained within the URL-specified file. For example, an \**.htm* file that is self-contained is valid, an \**.htm* file that refers to other graphics files is not valid, and an \**.mta* Web archive file that contains referenced graphic files is valid.

The URL can contain parameters. For example, the following URL contains a **prod** parameter that supplies the value "DSC530", a **rev** parameter that supplies the value "34", and a **type** parameter that supplies the value "doc":

```cpp
http://www.microsoft.com/redirect?prod=DSC530&rev=34&type=docs
```

Microsoft does not provide Web hosting or redirection for a webpage that is specified by a DEVPKEY_DrvPkg_DocumentationLink property value. The URL must link to a webpage that is maintained by the [driver package](./driver-packages.md) provider.

When a user clicks the website link that is displayed in Setup-generated end-user dialog box, Windows adds the following information to the HTTP request that includes the URL supplied by DEVPKEY_DrvPkg_DocumentationLink:

- The Windows version, as specified by a **pver** parameter. For example, "pver=6.0" specifies Windows Vista.

- The stock keeping unit (SKU), as specified by the **sbp** parameter, which can be set to per or pro. For example, "sbp=pro" specifies the professional edition.

- The local identifier (LCID), as specified by the **olcid** parameter. For example, "olcid=0x409" specifies the English (Standard) language.

- The most specific hardware identifier for a device, as specified by the **pnpid** parameter. For example, "pnpid=PCI%5CVEN_8086%26DEV_2533%26SUBSYS_00000000%26REV_04" specifies the hardware identifier for a PCI device.

For privacy reasons, user information and the serial number of device is not included in the HTTP request.

```cpp
The following example shows the type of HTTP request that would be sent to a web server: http://www.microsoft.com/redirect?prod=DSC530&rev34&type=docs&pver=6.0&spb=pro&olcid=0x409&pnpid=PCI%5CVEN_8086%26DEV_2533%26SUBSYS_00000000%26REV_04
```

You can set the value of DEVPKEY_DrvPkg_DocumentationLink by an [**INF AddProperty directive**](./inf-addproperty-directive.md) that is included in the [**INF *DDInstall* section**](./inf-ddinstall-section.md) of the INF file that installs the device. You can retrieve the value of DEVPKEY_DrvPkg_DocumentationLinkproperty by calling [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw).

The following is an example of how to use an INF **AddProperty** directive to set the value of DEVPKEY_DrvPkg_DocumentationLink for a device that is installed by an INF *DDInstall* section "SampleDDInstallSection":

```cpp
[SampleDDinstallSection]
...
AddProperty=SampleAddPropertySection
...

[SampleAddPropertySection]
DeviceDocumentationLink,,,,"http://www.microsoft.com/redirect?prod=DSC530&rev34&type="docs"
...
```

## Requirements

|Requirement| Description|
|----|----|
|Version|Available in Windows Vista and later versions of Windows.|
|Header|Devpkey.h (include Devpkey.h)|

## See also

[**INF AddProperty Directive**](./inf-addproperty-directive.md)

[**INF *DDInstall* Section**](./inf-ddinstall-section.md)

[**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw)
