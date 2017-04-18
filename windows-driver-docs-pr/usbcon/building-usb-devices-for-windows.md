---
Description: This section provides links for manufacturers of USB peripheral devices.
title: Building USB devices for Windows
---

# Building USB devices for Windows


**Summary**

-   Resources for USB device builders

This section provides links for manufacturers of USB peripheral devices.

## USB device enumeration process


[How does USB stack enumerate a device?](http://go.microsoft.com/fwlink/p/?linkid=617517)  
A detailed description of the enumeration process used by the Microsoft USB driver stack - starting from when the stack detects the presence of a device and indicates to the PnP manager that a new device has arrived.

[USB 2.1, 2.0, 1.1 device enumeration changes in Windows 8](http://go.microsoft.com/fwlink/p/?linkid=617518)  
In Windows 8, we’ve made modifications in the USB driver stack in how the stack enumerates USB 2.1, 2.0, and 1.1 devices. Those modifications support new USB features and improve device enumeration performance. Read the post is to bring awareness to those subtle changes and enable device/firmware builders to easily determine the root cause of enumeration failures.

## Microsoft OS descriptors


USB devices store standard descriptors in firmware for the device and its interfaces and endpoints. In addition, the device can store class and vendor-specific descriptors. However, the types of information that those descriptors can contain is limited. IHVs typically must use Windows Update or media such as CDs to provide their users with a variety of device-specific information such as pictures, icons, and custom drivers.

An IHV can use Microsoft OS descriptors to store the information in firmware instead of providing it separately. Window retrieves that information by reading Microsoft OS descriptors, and uses it to install and configure the device without requiring any user interaction. See [Microsoft OS Descriptors for USB Devices](microsoft-defined-usb-descriptors.md).

[Microsoft OS 1.0 Descriptors Specification](http://go.microsoft.com/fwlink/p/?linkid=617519)  
This document introduces Microsoft OS descriptors. It includes a specification for the OS string descriptor, extended properties OS feature descriptor, and OS feature descriptors formats.

[Microsoft OS 2.0 Descriptors Specification](http://go.microsoft.com/fwlink/p/?linkid=306681)  
This document defines and describes the implementation of version 2.0 of the Microsoft OS Descriptors. The goal of Microsoft OS 2.0 Descriptors is to address the limitations and reliability problems with version 1.0 of OS descriptors and enable new Windows-specific functionality for USB devices.

[Loading Winusb.sys as the function driver by using Microsoft OS descriptors](automatic-installation-of-winusb.md)  
The IHV can define certain Microsoft operating system (OS) feature descriptors that report the compatible ID as "WINUSB". Those descriptors allow Windows to load Winusb.sys as the device's function driver without a custom INF file. For examples about how to define the compatible ID, see the example section of the Extended Compat ID OS Feature Descriptor Specification. The specification is included in the download for [Microsoft OS 1.0 Descriptors Specification](http://go.microsoft.com/fwlink/p/?linkid=617519).

<a href="" id="setting-a-container-id-for-an-external-device-by-using-microsoft-os-descriptors"></a>Setting a container ID for an external device by using Microsoft OS descriptors  
See [Setting a container ID](#container).

## <a href="" id="container"></a>Setting a container ID


[Container IDs for USB Devices](https://msdn.microsoft.com/library/windows/hardware/ff540084)  
Describes how Container IDs for Universal Serial Bus (USB) devices are generated.

[USB ContainerIDs in Windows](usb-containerids-in-windows.md)  
Guidelines for device manufacturers to program their multifunction USB devices so that they can be correctly detected by Windows.

[How to Generate a Container ID for a USB Device](http://go.microsoft.com/fwlink/p/?linkid=617520)  
The blog post describes how a device must report a container ID such that Windows enumerates and shows the device in **Devices and Printers** properly. For devices that support multiple functions (composite device) or components (compound device), the device must report the same ID for each portion. The device must report the ID in a Microsoft OS ContainerID descriptor.

## Implementing power management


[Link Power management in USB 3.0 Hardware](link-power-management-in-usb-3-0-hardware.md)  
This document provides guidelines for hardware vendors and OEMs to implement power management for USB devices by using Link Power Management (LPM) in conjunction with Selective Suspend. It explains hardware transitions from U1 to U2 and provides information about common pitfalls in LPM implementation in USB controllers, hubs, and devices.

[Demystifying selective suspend](link-power-management-in-usb-3-0-hardware.md)  
This blog post describes how the USB driver stack handles function and selective suspend in USB 3.0 devices.

## Debugging and diagnostic tools


<a href="" id="usb-event-tracing-for-windows"></a>[USB Event Tracing for Windows](usb-event-tracing-for-windows.md)  
Event Tracing for Windows (ETW) is a general-purpose, high-speed tracing facility that is provided by the operating system. It includes information on how to install the tools, create trace files, and analyze the events in a USB trace file.

<a href="" id="wpp-software-tracing"></a>[WPP Software Tracing](https://msdn.microsoft.com/library/windows/hardware/ff556204)  
How to use the default operation of the Windows software trace preprocessor (WPP) to trace the operation of a software component (trace provider).

<a href="" id="usb-3-0-extensions--usb3kd-dll-"></a>[USB 3.0 Extensions](https://msdn.microsoft.com/library/windows/hardware/hh869258) (usb3kd.dll)  
These commands display information from data structures maintained by three drivers in the USB 3.0 stack: the USB 3.0 hub driver, the USB host controller extension driver, and the USB 3.0 host controller driver.

<a href="" id="usb-2-0-extensions---usb2kd-dll-"></a>[USB 2.0 Extensions](https://msdn.microsoft.com/library/windows/hardware/dn367056) (usb2kd.dll)  
These commands display information from data structures maintained by drivers in the USB 2.0 stack: the USB 2.0 hub driver and the USB 2.0 host controller driver.

## Related topics


[Universal Serial Bus (USB)](https://msdn.microsoft.com/library/windows/hardware/ff538930)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Building%20USB%20devices%20for%20Windows%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




