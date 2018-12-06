---
title: INF Reboot Directive
description: A Reboot directive indicates that the caller should be notified to reboot the system after installation is complete.
ms.assetid: 0E2640EA-921D-4677-82EF-EF9707254E66
keywords:
- INF Reboot Directive Device and Driver Installation
topic_type:
- apiref
api_name:
- INF Reboot Directive
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF Reboot Directive

A **Reboot** directive indicates that the caller should be notified to reboot the system after installation is complete.

```cpp
[DDInstall]
  
Reboot
```

**Warning**  The **Reboot** directive is only processed when specified directly in the **\[DDInstall\]** section.

 

The **Reboot** directive is almost never specified in INF files for installations on Windows because the need to reboot the system will automatically be detected based on the common conditions that it encounters as a part of device installation. For example, the system will notify the caller that a reboot is required if some target destination file of a file copy operation is in use, or if the device cannot be automatically restarted during the installation. The **Reboot** directive should only be used when there is some specific condition for which a system reboot is always required after the installation of this driver, which cannot be automatically detected by the system itself.

When the reboot directive is specified, the caller will be notified that a system reboot is required to complete the installation of any devices using this INF install section. When the installation has been initiated through a function such as [**UpdateDriverForPlugAndPlayDevices**](https://msdn.microsoft.com/library/windows/hardware/ff553534), [**DiInstallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff544717), or [**DiInstallDevice**](https://msdn.microsoft.com/library/windows/hardware/ff544710), this will result in the *NeedReboot* out parameter of these routines being set to TRUE.

Remarks
-------

On Windows 7 and earlier, the installation of a device using a driver with the **Reboot** directive will always result in the caller being notified that a system reboot is required to complete the installation.

On Windows 8 and above, the behavior described above only occurs when one or more of the devices to be installed are already started. Rather than restarting the devices during the installation of the new driver, the system will notify the caller that a system reboot is required to complete the installation of the new driver. If the devices to be installed are not currently started, the system will attempt to perform the installation without requiring a system reboot. Note that a reboot may still be required if one of the actions of installation still requires it. For example, if the destination file location of some file to be copied is currently in use, a system reboot will still be required to complete the installation.

 

 





