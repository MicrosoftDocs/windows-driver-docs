---
title: INF Reboot Directive
description: A Reboot directive indicates that the caller should be notified to reboot the system after installation is complete.
ms.assetid: 0E2640EA-921D-4677-82EF-EF9707254E66
keywords: ["INF Reboot Directive Device and Driver Installation"]
topic_type:
- apiref
api_name:
- INF Reboot Directive
api_type:
- NA
---

# INF Reboot Directive


**Note**  If you are building a universal or mobile driver package, this directive is not valid. See [Using a Universal INF File](using-a-configurable-inf-file.md).

 

A **Reboot** directive indicates that the caller should be notified to reboot the system after installation is complete.

``` syntax
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20INF%20Reboot%20Directive%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




