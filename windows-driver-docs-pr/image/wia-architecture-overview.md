---
title: WIA Architecture Overview
author: windows-driver-content
description: WIA Architecture Overview
MS-HAID:
- 'WIA\_intro\_1b17ef5f-807a-4077-9cc3-e8e33b178bf1.xml'
- 'image.wia\_architecture\_overview'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 47f44042-f22b-4ee0-88c5-fc977bf13791
---

# WIA Architecture Overview


## <a href="" id="ddk-wia-architecture-overview-si"></a>


WIA is implemented as a Component Object Model (COM) out-of-process server to ensure the robust operation of client applications. WIA is available in Microsoft Windows Me, Windows XP and later. There are no plans to port all of the system components that WIA depends on to Windows 95/98 or to Windows 2000. For information about the imaging architecture used on Windows 95/98 and Windows 2000, see [Overview of Microsoft STI and Microsoft WIA](overview-of-microsoft-sti-and-microsoft-wia.md).

WIA has three main components: the WIA service, the WIA driver service library, and a vendor user-mode driver.

-   The WIA service enumerates imaging devices, retrieves device properties, sets up events for devices, and creates device objects.

-   The WIA driver service library implements all services that are device independent.

-   The vendor user-mode driver maps WIA properties and commands to the specific device. There are two types of WIA vendor user-mode drivers:
    Minidriver: This is the most common type of vendor driver. It is a COM object that implements the WIA minidriver interfaces. A vendor can take advantage of all the WIA capabilities and features with this type of driver.
    Microdriver: This driver is much more limited than a minidriver and, therefore, simpler to develop. It is used primarily for basic scanner devices. This driver is not a COM object; it is a DLL that exports a few functions. Microdrivers cannot be used for camera devices.

The following diagram illustrates the WIA architecture.

![diagram illustrating the wia components](images/art-1.png)

### Imaging Applications

Imaging applications do not communicate directly with the minidriver, but communicate with the WIA service through the WIA application programming interface (API) to access images and acquire data from WIA devices. These applications can use a common, system-supplied user interface or a vendor-supplied user interface. For more information about the WIA API for imaging applications, see the Microsoft Windows SDK documentation.

### WIA Service

The WIA service is a system-supplied component that communicates with imaging applications and WIA minidrivers. The WIA service executes in a separate process from applications and in the same process as WIA minidrivers. Applications direct their device requests to the WIA service, which in turn directs the requests to the appropriate minidriver through the WIA device driver interface (DDI).

### WIA Driver Services Library

The WIA driver services library is a system-supplied component that provides helper functions for WIA minidrivers. A minidriver can call helper functions to perform tasks such as the following:

-   Initialize the WIA driver item tree.

-   Read, write, and validate device properties.

-   Transfer data.

Alternatively, a minidriver can perform such tasks itself. By taking advantage of the helper functions, you can reduce development time and the size of a WIA minidriver while still having the flexibility to develop individual solutions.

### WIA User-Mode Minidrivers

WIA minidrivers are vendor-supplied, user-mode components that direct WIA property changes and commands to an imaging device. A minidriver implements the WIA DDI, which is called by the WIA service to communicate with the minidriver.

A WIA minidriver implements the standard WIA minidriver interfaces. The minidriver communicates with the imaging device through a standard Microsoft Windows kernel-mode driver, such as the USB driver. The minidriver communicates with the kernel-mode driver by calling the [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858), **ReadFile**, **WriteFile**, and **DeviceIoControl** Win32 functions (described in the Microsoft Windows SDK documentation).

An imaging application cannot make direct calls to the WIA minidriver. Only the WIA service is permitted to call the driver directly.

### Kernel I/O Drivers

Kernel-mode still image drivers are system-supplied or IHV-supplied components that deliver data to or from the still image device. A kernel-mode still image driver is bus-specific.

Microsoft provides WDM-based, kernel-mode still image drivers for the USB, SCSI, and IEEE 1394 buses. See [Accessing Kernel-Mode Drivers for Still Image Devices](accessing-kernel-mode-drivers-for-still-image-devices.md) for more information.

A vendor must provide a kernel-mode still image driver *only* if its imaging device is incompatible with Microsoft-supplied, kernel-mode I/O drivers.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA%20Architecture%20Overview%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


