---
Description: Highlights the new features and improvements for Universal Serial Bus (USB) in Windows 10.
title: Windows 10 - What's new for USB
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Windows 10: What's new for USB


This topic highlights the new features and improvements for Universal Serial Bus (USB) in Windows 10.

-   **USB Type-C Port Controller Interface** 

    Windows 10 version 1703 provides a class extension (UcmTcpciCx.sys) that supports the Universal Serial Bus Type-C Port Controller Interface Specification. A USB Type-C connector driver does not need to maintain any internal PD/Type-C state. 
    The complexity of managing the USB Type-C connector and USB Power Delivery (PD) state machines is handled by the system. You only need to write a client driver that communicates hardware events to the system through the class extension. 

    [USB Type-C Port Controller Interface driver class extensions reference](https://msdn.microsoft.com/library/windows/hardware/mt805826)

-   **USB Dual Role support.**

    USB Dual Role controllers are now supported in Windows. Windows includes in-box client drivers for ChipIdea and Synopsys controllers. For other controllers, Microsoft provides a set of programming interfaces that allow the dual-role class extension (UrsCx) and its client driver to communicate with each other to handle the role-switching capability of a dual-role controller.

    For more information about this feature, see:

    [USB Dual Role Driver Stack Architecture](usb-dual-role-driver-stack-architecture.md)

    [USB dual-role controller driver programming reference](https://msdn.microsoft.com/library/windows/hardware/mt628026)

-   **New set of programming interfaces for developing a USB Type-C connector driver.**

    This version introduces native support for USB Type-C as defined in the USB 3.1 specification. The feature allows devices to use a reversible connector, a symmetric cable, faster charging, and Alternate Modes running over the USB cable. These programming interfaces allow you to write a driver for the connector (called the client driver in this section) that communicates with the Microsoft-provided class extension module: UcmCx to handle scenarios related to Type-C connectors such as, which ports support Type-C, which ports support power delivery.

    [Developing Windows drivers for USB Type-C connectors](developing-windows-drivers-for-usb-type-c-connectors.md)

    [USB connector manager class extension (UcmCx)](https://msdn.microsoft.com/library/windows/hardware/mt188011)

-   **New set of programming interfaces for developing an emulated host controller and a connected virtual device.**

    Windows 10 introduces support for emulated devices. Now you can develop an emulated Universal Serial Bus (USB) host controller driver and a connected virtual USB device. Both components are combined into a single KMDF driver that communicates with the Microsoft-provided USB device emulation class extension (UdeCx).

    [Developing Windows drivers for emulated USB devices (UDE)](developing-windows-drivers-for-emulated-usb-host-controllers-and-devices.md)

    [Emulated USB host controller driver programming reference](https://msdn.microsoft.com/library/windows/hardware/mt628025)

-   **New set of programming interfaces for developing a USB host controller driver.**

    You can develop a host controller if your hardware is not xHCI specification-compliant or your are writing a virtual host controller, such as a controller that routes USB traffic over a TCP connection to the peripherals attached to a device. Your host controller driver is a client to the USB host controller extension, which is a system-supplied driver that follows the framework class extension model. Within the [Microsoft USB 3.0 Driver Stack](http://msdn.microsoft.com/library/windows/hardware/hh406256.aspx#usb-3-0-driver-stack), UCX provides functionality to assist the host controller driver in managing a USB host controller device.

    [Developing Windows drivers for USB host controllers](developing-windows-drivers-for-usb-host-controllers.md)

    [USB host controller extension (UCX) reference](https://msdn.microsoft.com/library/windows/hardware/mt188009)

-   **New set of programming interfaces for developing a USB function controller driver.**

    You can write a client driver that communicates with the USB function class extension (UFX) and implements controller-specific operations. UFX handles USB function logic that is common to all USB function controllers.

    [USB device-side drivers in Windows](usb-device-side-drivers-in-windows.md)

    [UFX objects and handles used by a USB function client driver](ufx-objects-and-handles-used-by-a-usb-function-controller.md)

    [Tasks for a function controller client driver](function-client-driver.md)

    [User mode services to UFX programming reference](https://msdn.microsoft.com/library/windows/hardware/mt188014)

    [USB function class driver to UFX programming reference](https://msdn.microsoft.com/library/windows/hardware/mt188008)

    [USB function controller client driver programming reference](https://msdn.microsoft.com/library/windows/hardware/mt188010)

    [USB filter driver for supporting proprietary chargers](https://msdn.microsoft.com/library/windows/hardware/mt188012)

-   **Improved experience for USB CDC (serial) devices.**

    Allows devices that are compliant with the USB communication devices Class (Class\_02 & SubClass\_02) to work with Windows 10 by using the Usbser.sys driver. Device manufacturers are no longer required to write a custom INF to install that driver.

    [USB serial driver (Usbser.sys)](usb-driver-installation-based-on-compatible-ids.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Windows%2010:%20What's%20new%20for%20USB%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


