---
title: Providing Vendor Icons for the Shell and AutoPlay
description: Providing Vendor Icons for the Shell and AutoPlay
ms.assetid: 2e3afbf6-57f6-4b83-b10a-c33d9b1c1731
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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Providing Vendor Icons for the Shell and AutoPlay





[AutoPlay](http://go.microsoft.com/fwlink/p/?linkid=12031) is an extension of the Shell, and is supported by Microsoft Windows XP and later versions of Windows. AutoPlay detects different types of content, such as audio or video files, on removable media or removable devices. AutoPlay can display custom icons for content and devices, and it can automatically start an application to play or display content when the system detects a medium or device.

This topic describes how you can provide custom icons for a device. The Shell and AutoPlay use these icons to represent the device in the AutoPlay, My Computer, and file Open dialog boxes. The icons indicate whether a device is present and whether a medium is inserted. You can provide the following icons:

-   The *media-inserted icon* indicates that the device is present and a medium is inserted.

-   The *no-media-inserted icon* indicates that the device is present but a medium is not inserted.

In addition to specifying icons for individual devices, you can also specify icons for all devices in a user-defined device group or a [device setup class](device-setup-classes.md). For more information, see the [Preparing Hardware and Software for Use with AutoPlay](http://go.microsoft.com/fwlink/p/?linkid=12032) website.

If an updated [driver package](driver-packages.md) that contains a custom icon is posted on [Windows Update](https://msdn.microsoft.com/windows-drivers/develop/distributing_a_driver_package_win8), the user is prompted that a new download is available.

There are two steps to including icon files in a driver package:

1.  Add the icon files to the driver package.

2.  In the package's INF file, add entries that specify the icon files and copy them to the system.

If a system-supplied driver handles your device, you do not have to supply a full [driver package](driver-packages.md). You only have to provide an INF file and the icon files. This INF file must include the required icon-specific entries, plus **Include** and **Needs** entries that refer to your device's installation sections in the system-supplied driver's INF file.

### To create icons

-   Follow the guidelines that are provided at the Creating [Windows XP Icons](http://go.microsoft.com/fwlink/p/?linkid=6938) website. These guidelines describe how to create icons that have the appearance and behavior of Windows XP graphical elements.

### To specify the icons in an INF file

-   Include an [**INF AddReg directive**](inf-addreg-directive.md) under an [**INF DDInstall.HW section**](inf-ddinstall-hw-section.md) for the device. In the **AddReg** section, specify **Icons** and **NoMediaIcons** value entries, as indicated in the following example:

    ```cpp
    [DDInstall.NT.HW]
    AddReg = IconInformation

    [IconInformation]
    HKR, , Icons, 0x10000, "media-inserted-icon-file"
    HKR, , NoMediaIcons, 0x10000, "no-media-inserted-icon-file"
    ```

    <a href="" id="icons"></a>**Icons**  
    Specifies the name of the file that contains the media-inserted icon. The *media-inserted-icon-file* value is a placeholder for the actual file name.

    <a href="" id="nomediaicons"></a>**NoMediaIcons**  
    Specifies the name of the file that contains the no-media-inserted icon. The *no-media-inserted-icon-file* value is a placeholder for the actual file name.

### <a href="" id="to-direct-setup-to-copy-the-icon-files-to-the-system"></a>To direct Windows to copy the icon files to the system

-   Include an [**INF SourceDisksFiles section**](inf-sourcedisksfiles-section.md) that lists the icon files and a corresponding [**INF CopyFiles directive**](inf-copyfiles-directive.md) that copies them to the system.

Windows saves the **Icons** and **NoMediaIcons** value entries under the **Device Parameters** key under the device's [*hardware key*](https://msdn.microsoft.com/library/windows/hardware/ff556288#wdkgloss-hardware-key). The following example specifies the registry location, value-entry-type, and value of the **Icons** and **NoMediaIcons** value entries for the device whose device instance ID is USB\\Vid_0000&Pid_0000\\059B003112010E93.

**HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Enum\\**<em>USB\\Vid_0000&Pid_0000\\059B003112010E93</em>\\**Device Parameters**

**Icons** \[REG_MULTI_SZ\] = %*SystemRoo*t%*\\system32\\icon.ico*

**NoMediaIcons** \[REG_MULTI_SZ\] = %*SystemRoot*%*\\system32\\noicon.ico*

Drivers or other code should never access or modify the **Device Parameters** key directly. Instead, you should use the following system functions:

-   From user mode, use [**SetupDiCreateDevRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff550973) and [**SetupDiOpenDevRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff552079).

-   From kernel mode, use [**IoOpenDeviceRegistryKey**](https://msdn.microsoft.com/library/windows/hardware/ff549443).

 

 





