---
Description: The section describes architecture of USB Device Emulation(UDE) that emulates the behavior of a USB host controller and a connected device.
title: Architecture of USB Device Emulation (UDE)
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Architecture: USB Device Emulation (UDE)


The section describes architecture of USB Device Emulation(UDE) that emulates the behavior of a USB host controller and a connected device. By using UDE, a non-USB hardware can communicate with the upper layers by using the [USB host-side drivers in Windows](usb-device-side-drivers-in-windows.md).

## UDE drivers


![usb device emulation (ude)](images/ude-arch.png)

In the preceding image,

-   **USB hub driver (Usbhub3.sys)** is a KMDF driver. The hub driver is responsible for managing USB hubs and their ports, enumeration and creating physical device objects (PDOs) of USB devices and other hubs that may be attached to their downstream ports.
-   **USB host controller extension (Ucx01000.sys)** is an abstraction layer to the hub driver above in the stack, and provides a generic mechanism for queuing requests to the underlying host controller driver.
-   **UDE class extension** (UdeCx) is calls into the UDE client driver through client-implemented callback functions. The class extension provides routines for client driver to create UDE objects and manage them.
-   **UDE client driver** manages the hardware, interacting with both the WDF and UDE APIs. The upper edge communicates with both WDF and UDE class extension using USB constructs. Its lower edge communicates with the hardware using the hardware’s interface.
-   Custom hardware: For example, a PCI hardware can be emulated to work as a USB device.

## UDE device nodes


Here are the device stacks loaded for the UDE client driver:

![usb device emulation (ude) device nodes](images/ude-dev-nodes.png)

 

 




