---
Description: This section introduces you to high-level concepts and tasks for host driver development.
title: Architecture of USB host controller extension (UCX)
author: windows-driver-content
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Architecture: USB host controller extension (UCX)


This section introduces you to high-level concepts and tasks for host driver development. The section applies to you if you are writing a new host controller driver that communicates with the Microsoft-provided USB host controller extension driver (Ucx01000.sys).

Here is a modified version of a diagram shown in [USB host-side drivers in Windows](usb-3-0-driver-stack-architecture.md). This version hides the details of the USB client driver layer, which are not relevant to host controller driver development.

![ucx architecture](images/ucx.png)

In the preceding image,

-   **USB hub driver (Usbhub3.sys)** is a KMDF driver. The hub driver is responsible for managing USB hubs and their ports, enumeration and creating physical device objects (PDOs) of USB devices and other hubs that may be attached to their downstream ports.
-   **USB host controller extension (Ucx01000.sys)** is an abstraction layer to the hub driver above in the stack, and provides a generic mechanism for queuing requests to the underlying host controller driver.
-   **USB host controller driver** manages the hardware. Usbxhci.sys is one such driver that is provided by Microsoft, that targets xHCI spec compliant USB controller hardware, in particular. It may be necessary for independent hardware developers to write their own host controller driver, rather than use the inbox Usbxhci.sys. For example, for an XHCI hardware that is not fully compliant with the spec and therefore cannot use Usbxhci.sys or for non-XHCI hardware, such as USB over TCP connection.

The bidirectional communication that takes place between UCX and the host controller driver takes place by using [USB host controller extension (UCX) programming interfaces](https://msdn.microsoft.com/library/windows/hardware/mt188009). Each driver statically links to the entry points in the Microsoft-provided stub library (Ucx01000.lib) when the driver is compiled.

Here are the device stacks loaded for the host controller driver:

![ucx device stack](images/ucx-device-stack.png)

## Related topics
[Universal Serial Bus (USB) Drivers](https://msdn.microsoft.com/library/windows/hardware/ff538930)  
[USB Driver Development Guide](usb-driver-development-guide.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Architecture:%20USB%20host%20controller%20extension%20%28UCX%29%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


