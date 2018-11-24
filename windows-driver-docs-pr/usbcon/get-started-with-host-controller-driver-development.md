---
Description: This section introduces you to high-level concepts and tasks for host driver development.
title: Architecture of USB host controller extension (UCX)
ms.date: 04/20/2017
ms.localizationpriority: medium
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



