---
title: Device Property Representations (Windows Server 2003, Windows XP)
description: Device Property Representations (Windows Server 2003, Windows XP, and Windows 2000)
keywords:
- device properties WDK device installations , representations
ms.date: 04/04/2022
---

# Device Property Representations (Windows Server 2003, Windows XP, and Windows 2000)

Windows Server 2003, Windows XP, and Windows 2000 do not support the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) that Windows Vista and later versions of Windows support. However, most of the [system-defined device properties](/previous-versions/ff553413(v=vs.85)) that are included in the unified device property model have corresponding representations that are supported by these earlier versions of Windows. On these earlier versions of Windows, the way a device property is represented, and the mechanism to access a property, depends on the component type and property type. These representations and mechanisms include the following:

-   A device property is represented by a system-defined identifier that is supplied as an input parameter to a [Plug and Play (PnP) configuration manager function](/windows/win32/api/cfgmgr32/) or [SetupAPI function](setupapi.md) to access the device property.

-   A device property does not have an explicit representation. However, the information that is associated with a device property can be retrieved by calls to [SetupAPI functions](setupapi.md) or [Plug and Play (PnP) configuration manager functions](/windows/win32/api/cfgmgr32/).

-   A device property is represented by a registry entry value that can be accessed by using the Windows registry functions.

-   INF file entry values modify device properties.

The following topics provide information about how to access device properties on Windows Server 2003, Windows XP, and Windows 2000:

[INF File Entry Values that Modify Device Properties](inf-file-entry-values-that-modify-device-properties.md)

[Using SetupAPI and Configuration Manager to Access Device Properties](using-setupapi-and-configuration-manager-to-access-device-properties.md)

> [!NOTE]
> To maintain compatibility with these earlier versions of Windows, Windows Vista and later versions also support these mechanisms. However, you should use the unified device property model to access device properties on Windows Vista and later versions.
