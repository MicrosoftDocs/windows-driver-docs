---
Description: This topic summarizes the new features and improvements for Universal Serial Bus (USB) client drivers in Windows 8.
title: Windows 8 - What's new for USB
ms.date: 05/05/2018
ms.localizationpriority: medium
---

# Windows 8: What's new for USB


This topic summarizes the new features and improvements for Universal Serial Bus (USB) client drivers in Windows 8.

-   [New Driver Stack for USB 3.0 Devices](#new-driver-stack-for-usb-3-0-devices)
-   [Features Supported by the New Stack](#features-supported-by-the-new-stack)
-   [Client contract version for USB client drivers](#client-contract-version-for-usb-client-drivers)
-   [New Routines for Allocating and Building URBs](#new-routines-for-allocating-and-building-urbs)
-   [New User Mode I/O Control Requests for USB 3.0 Hubs](#new-user-mode-i-o-control-requests-for-usb-3-0-hubs)
-   [New Compatible ID for WinUSB](#new-compatible-id-for-winusb)
-   [New Visual Studio templates for USB client drivers *(\*New for Beta)*](#new-visual-studio-templates-for-usb-client-drivers---new-for-beta-)
-   [UASP driver](#uasp-driver)
-   [Boot support](#boot-support)
-   [Enhanced debugging and diagnostic capabilities](#enhanced-debugging-and-diagnostic-capabilities-----)
-   [New USB-specific failure messages in Device Manager](#new-usb-specific-failure-messages-in-device-manager)

For information about new features in USB in general, see [New for USB Drivers](https://msdn.microsoft.com/library/windows/hardware/hh451212).

## New Driver Stack for USB 3.0 Devices


Windows 8 provides a new USB driver stack to support USB 3.0 devices. The new stack includes drivers that are loaded by Windows when a USB 3.0 device is attached to an xHCI host controller. The new drivers are based on [Kernel Mode Driver Framework](https://msdn.microsoft.com/library/windows/hardware/ff557405) (KMDF) and implement features defined in the USB 3.0 specification. The new drivers are as follows:

-   Usbxhci.sys
-   Ucx01000.sys
-   Usbhub3.sys

The new driver stack maintains compatibility with the existing client drivers that were built and tested on earlier versions of the Windows operating system.

To see an architectural block diagram of the USB driver stack and a brief description of the new drivers, see [USB 3.0 Driver Stack Architecture](usb-3-0-driver-stack-architecture.md).

## Features Supported by the New Stack


The USB driver stack for USB 3.0 devices supports many new features. Some of features are configurable by the client driver. Those features are as follows:

-   Static streams for bulk endpoints.

    Streams provide the client driver with the ability to perform multiple data transfers to a single bulk endpoint. The Windows Driver Kit (WDK) for Windows 8 provides new device driver interfaces (DDIs) that allow a client driver to can open up to 255 streams in a bulk endpoint. After streams have been opened, the client driver can perform data transfers to and from specific streams. For more information, see [How to Open and Close Static Streams in a USB Bulk Endpoint](how-to-open-streams-in-a-usb-endpoint.md).

-   Chained MDLs

    A client driver can specify the payload in a chain of MDLs instead of a contiguous buffer. This allows the transfer buffer to be segmented in physical memory hence removing restrictions on the number, size, and alignment of buffers. Using chained MDLs can boost performance during data transfers because it avoids double buffering. For more information, see [How to Send Chained MDL](how-to-send-chained-mdls.md).

-   Function suspend and remote wake-up for composite devices.

    The feature enables a function of a composite device to enter and exit a low-power state, independently of other functions. The function driver can also request a device-initiated remote wake-up. Such a request must be handled by the parent driver of the composite device. The Microsoft-provided parent driver (Usbccgp.sys) supports function suspend and remote wake-up features. The WDK for Windows 8 provides DDIs that allow replacement parent drivers to implement those features. For more information, see [How to Implement Function Suspend in a Composite Driver](how-to--implement-remote-and-function-wake-support.md).

## Client contract version for USB client drivers


A *client contract version* identifies a set of rules that the client driver when sending requests to the USB driver stack. Failure to do so might result in an unexpected behavior. For information about those rules, see [Best Practices: Using URBs](usb-client-driver-contract-in-windows-8.md).

A client driver that intends to use the capabilities of the USB driver stack for 3.0 devices, must identify itself with the client contract version of USBD\_CLIENT\_CONTRACT\_VERSION\_602. Such a client driver is required to register with the USB driver stack. After registration, the client driver must query the underlying USB driver stack to determine whether the stack supports the required capability. To facilitate those operations, the following KMDF-specific methods and WDM routines have been included in the WDK for Windows 8:

| Use case                                                           | A KMDF-based driver should ...                                                                                                              | A WDM driver must ...                                                                                          |
|--------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| To specify a client contract version and with the USB driver stack | Call the [**WdfUsbTargetDeviceCreateWithParameters**](https://msdn.microsoft.com/library/windows/hardware/hh439428) method.                                      | Call the [**USBD\_CreateHandle**](https://msdn.microsoft.com/library/windows/hardware/hh406241) routine.                                                |
| To query for a particular capability                               | Call [**WdfUsbTargetDeviceQueryUsbCapability**](https://msdn.microsoft.com/library/windows/hardware/hh439434) and specify the GUID of the capability to query. | Call [**USBD\_QueryUsbCapability**](https://msdn.microsoft.com/library/windows/hardware/hh406230) and specify the GUID of the capability to query. |

 

## New Routines for Allocating and Building URBs


Windows 8 provides new routines for allocating, formatting, and releasing URBs. The [**URB**](https://msdn.microsoft.com/library/windows/hardware/ff538923) structure is allocated by the USB driver stack. If the underlying stack is the new USB driver stack, the URB is paired with an opaque URB context. The USB driver stack uses the URB context to improve URB tracking and processing. For more information about the routines, see [Allocating and Building URBs](how-to-add-xrb-support-for-client-drivers.md).

The new routines are as follows:

-   [**USBD\_UrbAllocate**](https://msdn.microsoft.com/library/windows/hardware/hh406250)
-   [**USBD\_IsochUrbAllocate**](https://msdn.microsoft.com/library/windows/hardware/hh406231)
-   [**USBD\_SelectConfigUrbAllocateAndBuild**](https://msdn.microsoft.com/library/windows/hardware/hh406243)
-   [**USBD\_SelectInterfaceUrbAllocateAndBuild**](https://msdn.microsoft.com/library/windows/hardware/hh406245)
-   [**USBD\_UrbFree**](https://msdn.microsoft.com/library/windows/hardware/hh406252)
-   [**USBD\_AssignUrbToIoStackLocation**](https://msdn.microsoft.com/library/windows/hardware/hh406228) routine to associate an URB with an IRP. This routine only applies to WDM client drivers.

In addition to the routines in the preceding list, there are new KMDF-specific methods for URB allocation. For KMDF-based client drivers, we recommend that you call,

-   The [**WdfUsbTargetDeviceCreateUrb**](https://msdn.microsoft.com/library/windows/hardware/hh439423) method (instead of [**USBD\_UrbAllocate**](https://msdn.microsoft.com/library/windows/hardware/hh406250)) to allocate an URB.
-   The [**WdfUsbTargetDeviceCreateIsochUrb**](https://msdn.microsoft.com/library/windows/hardware/hh439420) method (instead of [**USBD\_IsochUrbAllocate**](https://msdn.microsoft.com/library/windows/hardware/hh406231))to allocate an URB for an isochronous transfer. Those calls allocate a variable-sized URB that is based on the number of isochronous packets required for the transfer. For more information about isochronous transfers, see [How to Transfer Data to USB Isochronous Endpoints](transfer-data-to-isochronous-endpoints.md).

## New User Mode I/O Control Requests for USB 3.0 Hubs


Windows 8 provides the new IOCTLs that applications can use to retrieve information about USB 3.0 hubs and their ports. The new IOCTLs are as follows:

-   [**IOCTL\_USB\_GET\_HUB\_INFORMATION\_EX**](https://msdn.microsoft.com/library/windows/hardware/hh450860)
-   [**IOCTL\_USB\_GET\_PORT\_CONNECTOR\_PROPERTIES**](https://msdn.microsoft.com/library/windows/hardware/hh450863)
-   [**IOCTL\_USB\_GET\_NODE\_CONNECTION\_INFORMATION\_EX\_V2**](https://msdn.microsoft.com/library/windows/hardware/hh450861)

By sending the preceding I/O requests to the USB driver stack an application retrieve the following set of information:

-   Hub descriptors
-   Properties of all ports and companion ports
-   Operating speed of a device that is attached to a port

## New Compatible ID for WinUSB


Device manufacturers can add "WINUSB" in the firmware (Microsoft OS feature descriptor) so that Windows recognizes the device as a WinUSB device. In Windows 8, Winusb.inf has been modified to include USB\\MS\_COMP\_WINUSB as a device identifier string. That modification enables Windows to automatically load Winusb.sys, as the function driver for the device, as soon as the device is detected. For more information, see [WinUSB Device](automatic-installation-of-winusb.md).

## New Visual Studio templates for USB client drivers *(\*New for Beta)*


Microsoft Visual Studio 2012 includes **USB User-Mode Driver** and **USB Kernel-Mode Driver** templates that generate starter code for a UMDF and KMDF USB client driver, respectively. The template code initializes the USB target device object to enable communication with the hardware. For more information, see the following topics:

-   [How to write your first USB client driver (UMDF)](implement-driver-entry-for-a-usb-driver--umdf-.md)
-   [How to write your first USB client driver (KMDF)](tutorial--write-your-first-usb-client-driver--kmdf-.md)

For more information, see [Getting started with USB client driver development](getting-started-with-usb-client-driver-development.md). Extend your driver by performing [Common tasks for USB client drivers](wdk-resources-for-usb-driver-development.md).

For information about how to implement UMDF and KMDF drivers, see the Microsoft Press book *Developing Drivers with the Windows Driver Foundation*.

## UASP driver


Windows 8 includes a new USB storage driver that implements the USB Attached SCSI Protocol (UASP). The new driver uses static streams for bulk endpoints, as per the official USB 3.0 specification.

## Boot support


The Windows to Go feature allows Windows to boot from a flash drive or an external drive. You can boot with your copy of Windows from those drives on various machines.

## Enhanced debugging and diagnostic capabilities


Windows 8 provides new USB 3.0 debugging tools to improve diagnosing USB issues faster. There are new USB 3.0 kernel debugger extensions that examine USB 3.0 host controller and device states. You can use USB WPP and event tracing to analyze USB interactions and troubleshoot USB device issues more easily. Windows 8 supports debugging over USB 3.0. For more information, see [Setting Up a USB 3.0 Connection Manually](https://msdn.microsoft.com/library/windows/hardware/hh439372).

## New USB-specific failure messages in Device Manager


At times, Windows can fail to enumerate an attached USB device. Typically, enumeration failures occur when requests sent to the USB device fail or the device returns incorrect descriptors.

In Windows 8, when such failures occur, the **General** tab in **Device Manager** displays a USB-specific error message that indicates the reason for failure.

The error strings are as follows:

-   A request for the USB device descriptor failed.
-   The USB set address request failed.
-   A USB port reset request failed.
-   A previous instance of the USB device was not removed.
-   The USB device returned an invalid USB configuration descriptor.
-   The USB device returned an invalid USB device descriptor.
-   Unable to access the registry.
-   A request for the USB configuration descriptor failed.
-   A request for the USB device's port status failed.
-   The USB device returned an invalid serial number string.
-   The USB set SEL request failed.
-   A request for the USB BOS descriptor failed.
-   A request for the USB device qualifier descriptor failed.
-   A request for the USB serial number string descriptor failed.
-   A request for the USB language ID string descriptor failed.
-   A request for the USB product description string descriptor failed.
-   A request for the Microsoft OS extended configuration descriptor failed.
-   A request for the Microsoft OS container ID descriptor failed.
-   The USB device returned an invalid USB BOS descriptor.
-   The USB device returned an invalid USB device qualifier descriptor.
-   The USB device returned an invalid USB language ID string descriptor.
-   The USB device returned an invalid Microsoft OS container ID descriptor.
-   The USB device returned an invalid Microsoft OS extended configuration descriptor.
-   The USB device returned an invalid product description string descriptor.
-   The USB device returned an invalid serial number string descriptor.

## Related topics
[New for USB Drivers](https://msdn.microsoft.com/library/windows/hardware/hh451212)  
[Universal Serial Bus (USB) Drivers](https://msdn.microsoft.com/library/windows/hardware/ff538930)  



