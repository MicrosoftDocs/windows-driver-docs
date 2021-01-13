---
title: Providing Icons for a Device
description: Providing Icons for a Device
keywords:
- AutoPlay icons WDK
- custom icons WDK device installations
- vendor icons WDK
- icons WDK Shell
- Shell icons WDK
- media-inserted icons WDK
- no-media-inserted icons WDK
- icons WDK AutoPlay
- copying icon files
ms.date: 04/30/2020
ms.localizationpriority: medium
---

# Providing Icons for a Device

This topic describes how you can provide custom icons for a device by referencing them in a driver's INF file. You can provide icons that appear in Device Manager, Windows Explorer, or both, as appropriate.

## Adding icons for Device Manager

You can either embed a custom icon in a DLL or provide a standalone .ico file. If your driver is already a DLL file, the first is the easiest option because it does not require copying any additional files.

To embed the icon in a DLL, use an entry like this:

```inf
[<DDInstall>]
AddProperty = DeviceIconProperty

[DeviceIconProperty]
DeviceIcon,,,,"%13%\UmdfDriver.dll,-100"
```

The above example uses DIRID 13 to copy the file to the Driver Store, which avoids needing to copy it anywhere else. The entry follows the format `<Resource.dll>,-<IconResourceID>`, so the 100 signifies the resource ID of the icon in the resource table of the DLL. For more on DIRID 13, see [Using a Universal INF File](./using-a-universal-inf-file.md).

To reference a standalone .ico file, use an entry like this:


```inf
[<DDInstall>]
AddProperty = DeviceIconProperty

[DeviceIconProperty]
DeviceIcon,,,,"%13%\vendor.ico"
```

## Adding icons for storage volumes in Explorer

The shell uses **Icons** and **NoMediaIcons** registry values to represent the device in AutoPlay, My Computer, and file Open dialog boxes.

To add these, include an [**INF AddReg directive**](inf-addreg-directive.md) under an [**INF DDInstall.HW section**](inf-ddinstall-hw-section.md) for the device. In the **AddReg** section, specify **Icons** and **NoMediaIcons** value entries, as shown in the following example:

```inf
[DDInstall.NT.HW]
AddReg = IconInformation

[IconInformation]
HKR, , Icons, 0x10000, "media-inserted-icon-file"
HKR, , NoMediaIcons, 0x10000, "no-media-inserted-icon-file"
```

Then include an [**INF SourceDisksFiles section**](inf-sourcedisksfiles-section.md) that lists the icon files and a corresponding [**INF CopyFiles directive**](inf-copyfiles-directive.md) that copies them to the system.

The **Icons** and **NoMediaIcons** value entries are stored under the **Device Parameters** key under the device's *hardware key*. For example, `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Enum\<Hardware ID>\Device Parameters` would contain entries like the following:

* `Icons [REG_MULTI_SZ] = %SystemRoot%\system32\icon.ico`

* `NoMediaIcons [REG_MULTI_SZ] = %SystemRoot%\system32\noicon.ico`

To modify the **Device Parameters** key from user mode, use [**SetupDiCreateDevRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdicreatedevregkeya) or [**SetupDiOpenDevRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdiopendevregkey).

From kernel mode, use [**IoOpenDeviceRegistryKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendeviceregistrykey).

## Resources

When you create icons, follow the guidelines that are provided in [Icons](/windows/win32/uxguide/vis-icons). These guidelines describe how to create icons that have the appearance and behavior of Windows graphical elements.
