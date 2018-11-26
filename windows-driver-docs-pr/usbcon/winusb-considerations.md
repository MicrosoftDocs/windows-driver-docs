---
Description: Guidelines for choosing the best driver model for developing a USB client driver that acts as the device's function driver.
title: Choose a driver model for developing a USB driver
ms.date: 05/09/2018
ms.localizationpriority: medium
---

# Choosing a driver model for developing a USB client driver


This topic provides guidelines for choosing the best driver model for developing a USB client driver that acts as the device's function driver.

USB device manufacturers must often provide a way for applications to access the device's features. To choose the best mechanism for accessing a USB device, start with the simplest approach and move to more complex solutions only if it is necessary. The following list summarizes the choices discussed in this topic:

1.  If your device belongs to a USB device class for which Windows includes an inbox driver, you don’t need to write a driver.
2.  If your device does not have a Microsoft-provided class driver, and the device is accessed by a single application, then load WinUSB as the function driver.
3.  If the device needs to be accessed by concurrent applications and your device does not have isochronous endpoints, write a UMDF-based client driver.
4.  If class driver, WinUSB, or UMDF solutions are not options that work for you, write a KMDF-based client driver.
5.  If a particular feature is not supported by KMDF, write a hybrid driver that calls WDM routines.

The most common approach has been to implement a device driver, (termed as a *USB client driver* in this documentation set) and provide an installation package that installs the driver as the function driver in the device stack above the Microsoft-provided USB driver stack. The client driver exposes a device interface that applications can use to obtain the device's file handle. Applications can then use this file handle to communicate with the driver by calling Windows APIs.

Writing a driver that is customized to the device's requirements is the most flexible way to provide access to a USB device. However, implementing a driver requires a lot of work. The driver must perform complex tasks, such as driver initialization when new devices are detected, power management, I/O operations, surprise removal, state management, and cleanup when the device is removed. Before you choose to write a driver, ask the following questions:

-   [Can you use a Microsoft-provided driver?](#can-you-use-a-microsoft-provided-driver)
-   [If you write a USB client driver, which driver model is best?](#if-you--write-a-usb-client-driver--which-driver-model-is-best-)

## Can you use a Microsoft-provided driver?


You might *not* need to write a driver if:

-   Your device belongs to a USB device class that is supported by Microsoft.

    In that case, the corresponding class driver is loaded as the device driver. For a list of device classes for which Windows includes an inbox driver, see [USB device class drivers included in Windows](supported-usb-classes.md).

-   Your device does not belong to a device class.

    For such devices, evaluate the device features to determine whether you can load the Microsoft-provided [WinUSB](winusb.md) (Winusb.sys) as the device's function driver. Using WinUSB is the best solution if:

    -   Your device is accessed by a single application.
    -   Your device supports bulk, interrupt, or isochronous endpoints.
    -   Your device is intended to work with a target computer running Windows XP with Service Pack 2 (SP2) and later versions of Windows.

    Loading WinUSB as the function driver provides a simpler alternative to implementing a custom USB driver. For example, WinUSB is the preferred approach for an electronic weather station that is accessed only by an application that is packaged with the device. It is also useful for diagnostic communication with a device and for flashing firmware.

    To make it easy for applications to send requests to Winusb.sys, we provide a user-mode DLL, Winusb.dll, that exposes [WinUSB functions](https://msdn.microsoft.com/library/windows/hardware/ff540046#winusb). An application can call those functions to access the device, configure it, and transfer data to the device’s endpoints.

    WinUSB is not an option if:

    -   Your device is accessed by multiple applications.
    -   Your device has functions that already have kernel-mode support in the Windows operating system. For example, for modem functions (which TAPI supports) or LAN functions (which NDIS supports), you must use the interface that the Usbser.sys driver supports to manage modem devices with user-mode software.

    In Windows 8, we've added a new compatible ID to the INF for WinUSB installation. If the device firmware contains that compatible ID, WinUSB is loaded by default as the function driver for the device. This means that hardware manufacturers are not required to distribute INF files for their WinUSB devices. For more information, see [WinUSB Device](automatic-installation-of-winusb.md).

## If you write a USB client driver, which driver model is best?


The answer depends on the design of your device. First, determine whether a particular driver model meets your requirements. Some design considerations are based on whether you want the USB device to be accessed by multiple concurrent applications and support data streaming through isochronous endpoints.

If you choose to write a driver, here are your options:

-   [User-Mode Driver Framework](https://docs.microsoft.com/windows-hardware/drivers/wdf/) (UMDF)

    UMDF provides device driver interfaces (DDIs) that a client driver can use to integrate with Windows components such as the Plug and Play Manager and Power Manager. UMDF also provides specialized target objects for USB devices, which abstract the hardware in user mode and simplify I/O operations for the driver. In addition to the UMDF interfaces, WDF provides enhanced debugger extensions and tracing tools for user-mode drivers. UMDF is based on the component object model (COM) and developing a user-mode driver is easier for a C++ developer.

    Implement a UMDF-based client driver for a USB device in the following cases:

    -   The device is accessed by concurrently by multiple applications.
    -   The device supports bulk or interrupt transfers.

    Drivers that run in user mode can access only the (virtual) user address space and pose a much lower risk to the system. Kernel-mode drivers can access the system address space and the internal system structures. A badly coded kernel-mode driver might cause problems that affect other drivers or the system, and eventually crash the computer. Therefore, a user-mode driver can be safer than a kernel-mode driver in terms of security and stability.

    Another advantage of user-mode drivers is that they leverage all the Win32 APIs. For example, the drivers can call APIs such as Winsock, Compression, Encryption APIs, and so on. Those APIs are not available to kernel-mode drivers.

    A UMDF-based client driver is not an option for USB devices that support isochronous endpoints.

    **Note**  Windows 8.1 introduces version 2.0 of UMDF. With UMDF version 2.0, you can write a UMDF driver in the C programming language that calls many of the methods that are available to KMDF drivers. You cannot use UMDF version 2.0 to write lower filter drivers for USB.

     

-   [Kernel-Mode Driver Framework](https://docs.microsoft.com/windows-hardware/drivers/wdf/) (KMDF)

    KMDF was designed to make the driver models easy to extend to support new types of hardware. KMDF provides DDIs and data structures that make kernel-mode USB drivers easier to implement than the earlier Windows Driver Model (WDM) drivers. In addition, KMDF provides specialized input/output (I/O) targets that you can use to write a fully functional client driver that uses the Microsoft USB driver stack.

    In certain cases where a particular feature is not exposed through KMDF, the driver must call WDM routines. The driver does not need to implement the entire WDM infrastructure but uses KMDF methods to access a select set of WDM routines. For example, to perform isochronous transfers, a KMDF-based client driver can send WDM-style URBs that describe the request to the USB driver stack. Such drivers are called *hybrid drivers* in this documentation set.

    KMDF also supports the port-miniport driver model. For instance, a kernel streaming miniport driver (such as a USB webcam) that uses kernel streaming on the upper edge can use KMDF USB I/O target objects to send requests to the USB driver stack. NDIS drivers can also be written by using KMDF for protocol-based buses such as USB.

    Pure WDM drivers are difficult to write, complex, and not robust. With the evolution of KMDF, writing this type of driver is no longer necessary.

Microsoft Visual Studio 2012 includes **USB User-Mode Driver** and **USB Kernel-Mode Driver** templates that generate starter code for a UMDF and KMDF USB client driver, respectively. The template code initializes a USB target device object to enable communication with the hardware. For more information, see the following topics:
-   [Write your first USB client driver (UMDF)](implement-driver-entry-for-a-usb-driver--umdf-.md)
-   [Write your first USB client driver (KMDF)](tutorial--write-your-first-usb-client-driver--kmdf-.md)

For information about how to implement UMDF and KMDF drivers, see the Microsoft Press book *Developing Drivers with the Windows Driver Foundation*.

## WinUSB, UMDF, KMDF Feature Comparison


The following table summarizes the capabilities of WinUSB, UMDF-based USB drivers, and KMDF-based USB drivers.

| Feature                                                                                                          | WinUSB | UMDF | KMDF |
|------------------------------------------------------------------------------------------------------------------|--------|------|------|
| Supports multiple concurrent applications                                                                        | No     | Yes  | Yes  |
| Isolates driver address space from application address space                                                     | No     | Yes  | No   |
| Supports bulk, interrupt, and control transfers                                                                  | Yes    | Yes  | Yes  |
| Supports isochronous transfers                                                                                   | Yes ⁴  | No   | Yes  |
| Supports the installation of kernel-mode drivers, such as filter drivers, as an overlying layer on the USB stack | No     | No   | Yes  |
| Supports selective suspend and the wait/wake state                                                               | Yes    | Yes  | Yes  |

 

The following table summarizes the WDF options that are supported by different versions of Windows.

| Windows version        | WinUSB | UMDF | KMDF |
|------------------------|--------|------|------|
| Windows 8              | Yes    | Yes  | Yes  |
| Windows 7              | Yes    | Yes  | Yes  |
| Windows Vista          | Yes¹   | Yes¹ | Yes  |
| Windows Server 2003    | No     | No   | Yes  |
| Windows XP             | Yes²   | Yes² | Yes  |
| Microsoft Windows 2000 | No     | No   | Yes³ |

 

**Note**  
Yes¹: WinUSB and UMDF are supported only on x86-based and x64-based versions of Windows.

Yes²: WINUSB and UMDF are supported in Windows XP with Service Pack 2 (SP2) or later versions of Windows.

Yes³: KMDF is supported in Windows 2000 with SP4 or later versions of Windows.

Yes⁴: Isochronous transfers are supported in Windows 8.1 or later versions of Windows.

 

All client SKUs of the 32-bit versions of Windows XP with SP2support WinUSB. WinUSB is not native to Windows XP; it must be installed with the WinUSB co-installer. All Windows Vista SKUs and later versions of Windows support WinUSB.

## Related topics
[Getting started with USB client driver development](getting-started-with-usb-client-driver-development.md)  
[WinUSB](winusb.md)  
[Write your first USB client driver (UMDF)](implement-driver-entry-for-a-usb-driver--umdf-.md)  
[Write your first USB client driver (KMDF)](tutorial--write-your-first-usb-client-driver--kmdf-.md)  



