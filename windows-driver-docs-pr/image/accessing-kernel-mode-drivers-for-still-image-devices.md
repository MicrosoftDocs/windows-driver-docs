---
title: Accessing Kernel-Mode Drivers for Still Image Devices
author: windows-driver-content
description: Accessing Kernel-Mode Drivers for Still Image Devices
ms.assetid: f9216d3c-4930-4c26-8eac-6ee500b038e0
---

# Accessing Kernel-Mode Drivers for Still Image Devices


## <a href="" id="ddk-accessing-kernel-mode-drivers-for-still-image-devices-si"></a>


Microsoft provides WDM-based kernel-mode drivers to support still image devices connected to SCSI and USB buses. Both drivers support Plug and Play devices and provide services for adding, removing, starting, stopping, and creating registry entries for Plug and Play devices. Additionally, both drivers provide suspend and resume operations for devices that support power management.

User-mode still image minidrivers can access these kernel-mode drivers by calling [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858), **ReadFile**, **WriteFile**, and [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) (described in the Microsoft Windows SDK documentation). **ReadFile** and **WriteFile** are used for block data transfers. Specifically, **ReadFile** is called to obtain image data, and **WriteFile** is used for sending commands to devices that accept commands as data streams.

Before calling **ReadFile**, **Writefile** or [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216), the minidriver must call [**IStiDeviceControl::GetMyDevicePortName**](https://msdn.microsoft.com/library/windows/hardware/ff542944) to obtain the device's port name and then use that port name as a parameter to [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858).

[SCSI Driver](scsi-driver.md)

[USB Driver](usb-driver.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Accessing%20Kernel-Mode%20Drivers%20for%20Still%20Image%20Devices%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


