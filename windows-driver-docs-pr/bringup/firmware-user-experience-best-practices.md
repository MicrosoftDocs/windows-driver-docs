---
title: Firmware user experience (UX) best practices
description: Firmware user experience (UX) best practices
author: windows-driver-content
ms.author: windowsdriverdev
ms.date: 05/15/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---


# Firmware user experience (UX) best practices


A firmware update to a system can be important to the continued use of that machine. Microsoft wants to ensure that firmware updates are safely delivered, and installation is uninterrupted. To do this, we have recommended the following guidelines that are described in greater detail in the **Related resources** section.

1.  Progress bar/indicator that the system is installing an update.

2.  Windows Boot loader with **UpdateCapsule** function will provide a bitmap containing message for user.

3.  UEFI check for AC Power, or sufficient battery life (RSOC) or fail out with error codes recorded in ESRT.

The **Related resources** links contain the most recent information on firmware UX guidance.

## Related resources

[Windows UEFI firmware update platform](https://msdn.microsoft.com/en-us/windows/hardware/drivers/bringup/windows-uefi-firmware-update-platform)                                           
 
[Seamless crisis prevention and recovery ](https://msdn.microsoft.com/en-us/library/windows/hardware/dn917851)                                                               

[User experience for UEFI firmware updates](https://msdn.microsoft.com/en-us/windows/hardware/drivers/bringup/user-experience-for-uefi-firmware-updates)                                   

[Boot screen components](https://msdn.microsoft.com/en-us/windows/hardware/drivers/bringup/boot-screen-components)                                                                         

[ESRT table definition](https://msdn.microsoft.com/windows/hardware/drivers/bringup/esrt-table-definition)    

[Validating Windows UEFI Firmware Update Platform Functionality](https://msdn.microsoft.com/windows/hardware/commercialize/manufacture/desktop/validating-windows-uefi-firmware-update-platform-functionality) 




--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Slicer%20settings%20%20RELEASE:%20%289/2/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


