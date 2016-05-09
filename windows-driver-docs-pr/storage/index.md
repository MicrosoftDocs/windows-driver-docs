---
title: Introduction
author: windows-driver-content
description: Introduction
ms.assetid: 0AEFA19D-C270-4777-8C08-E6056FBB6BC5
---

# Introduction


Storage drivers include [class](storage-class-drivers.md), [port](storage-port-drivers.md), [miniport](storage-miniport-drivers.md), and [filter](storage-filter-drivers.md) drivers. Typically, a device vendor will implement a miniport driver for a specific adapter or adapter type. Although not common, a new storage class can be defined and a new class driver developed for it. Storage classes in Windows include the Disk, CDROM, USB storage, and encrypted drive classes. Storage driver development is usually limited to writing a miniport driver to work with the [StorPort](storport-driver.md) port driver.

Other types of storage drivers are secure [silo](storage-silo-drivers.md) drivers and Device Specific Modules (DSM) for multipath I/O. For storage management, [WMI](https://msdn.microsoft.com/library/windows/hardware/ff567016) providers are developed as a control interface to a driver.

## <span id="Storage_Driver_WDK_Resources"></span><span id="storage_driver_wdk_resources"></span><span id="STORAGE_DRIVER_WDK_RESOURCES"></span>Storage Driver WDK Resources


Getting started information is found in the [Storage Devices Design Guide](https://msdn.microsoft.com/library/windows/hardware/ff566969) section.

Studying samples is a practical way to see how working storage drivers are developed. [Sample storage drivers](http://go.microsoft.com/fwlink/p/?LinkId=616047) are available on GitHub.

## <span id="Driver_Verification_for_StorPort"></span><span id="driver_verification_for_storport"></span><span id="DRIVER_VERIFICATION_FOR_STORPORT"></span>Driver Verification for StorPort


Using code analysis tools during driver development and testing helps to catch performance problems and defects in a storage driver. The [Static Driver Verifier (SDV)](https://msdn.microsoft.com/library/windows/hardware/ff552808) tool is available to discover defects in storage driver code. Included with SDV are compliance [rules](https://msdn.microsoft.com/library/windows/hardware/hh454238) for verifying proper usage of StorPort routines by miniport drivers.

Tests for storage hardware certification are found in the [Windows Hardware Certification Kit (HCK)](https://go.microsoft.com/fwlink/p/?LinkId=733613). Test for storage devices are found in the [Devices.Storage](http://msdn.microsoft.com/library/windows/hardware/jj125097) category of the HCK.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Introduction%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


