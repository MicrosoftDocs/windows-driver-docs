---
title: First Steps for USB Client Driver Development
description: This section introduces you to USB driver development.
ms.date: 01/12/2024
---

# First steps for USB client driver development

This section introduces USB driver development concepts and tools. The section applies to devlopers new to driver development that wish to implement a driver for a USB device that Microsoft does not provide an in-box driver for. These drivers are called a *USB client driver* in this documentation. The topics in this section describe high-level USB concepts and provide step-by-step instructions about performing common tasks of a USB client driver. For detailed information about those concepts see USB specifications at [USB Documents](https://usb.org/documents).

Driver developers must have coding experience in the C++ programming language and understand the concepts of *function pointers*, *callback functions*, and *event handlers*. If writing a driver based on the User-Mode Driver Framework the developer must be familiar with C++ and COM.

## Learning path for USB client driver developers

1. Read the [USB Specification 3.2](https://usb.org/document-library/usb-32-specification-released-september-22-2017-and-ecns).
    - Learn about the industry specification and different components (device, host controller, and hub) of the architecture. It's important to understand the data flow model, how the host and device communicate with each other, and the format of the requests that the device expects.

1. Obtain a test USB device.
     - Have a USB device and its hardware specification. The specification describes device capabilities and the supported vendor commands. Use the specification to determine the functionality of the device driver and the related design decisions.

     - Have the [OSR USB FX2 learning kit](https://www.amazon.com/OSR-USB-FX2-Learning-Kit/dp/B07FNSYCLR) if new to USB driver development. The kit is the most suitable to study USB samples included in this documentation set.
     - Have a Microsoft USB Test Tool (MUTT) devices. MUTT hardware can be purchased from [JJG Technologies](http://www.jjgtechnologies.com/Mutt20.htm). The device does not have installed firmware installed. To install firmware, download the [MUTT software package](./microsoft-usb-test-tool--mutt--devices.md). For more information, see the documentation included with the package.

1. Study the [USB device layout](usb-device-layout.md) and the related [USB descriptors](usb-descriptors.md).
    - Describe your device capabilities by reading the configuration descriptor, interface descriptors for each supported alternate settings, and their endpoint descriptors. By using [USBView](../debugger/usbview.md), the developer can browse all USB controllers and the USB devices connected to them and also inspect the device configuration.

1. [Choose a driver model for developing a USB client driver](winusb-considerations.md)
    - Determine if the driver should be a custom driver or use one of the Microsoft-provided drivers based on the design of the target device. Choose the best driver model and describe the features supported by each model.

1. Review the Microsoft-provided USB driver stack and driver development concepts.
    - [USB host-side drivers in Windows](usb-3-0-driver-stack-architecture.md).
    - [Concepts for All Driver Developers](../gettingstarted/concepts-and-knowledge-for-all-driver-developers.md).
    - [Concepts for all USB developers](usb-concepts-for-all-developers.md).
    - [Device nodes and device stacks](../gettingstarted/device-nodes-and-device-stacks.md).
    - *Developing Drivers with Windows Driver Foundation* written by Penny Orwick and Guy Smith. For more information see [Developing Drivers with WDF](../wdf/developing-drivers-with-wdf.md).
    - [USB driver samples](usb-driver-samples-in-wdk.md).
    - Understand the fundamentals of how drivers work in Windows operating systems. Knowing the fundamentals will help make appropriate design decisions and streamline the development process.
    - Differentiate between user mode and kernel mode driver architecture models.
    - Understand driver loading and how Windows organizes Plug and Play (PnP) devices in a device tree and device nodes. The developer should also understand how PnP manager builds device stacks and where the driver and its device objects are placed in the device stack.

1. Prepare the development and debugging environment.
    - Install the latest [Windows Driver Kit (WDK)](../download-the-wdk.md).
    - [Install Microsoft Visual Studio](https://visualstudio.microsoft.com/downloads/).
    - [Get Set Up for Debugging](../debugger/getting-set-up-for-debugging.md).
    - Make sure the [Headers and libraries required by a USB client driver](headers-and-libraries-for-a-usb-client-driver.md) are available.
    - If writing a kernel-mode driver debugging on host and target computers over an Ethernet network, 1394 cable, USB 2.0 or 3.0 debug cable, or a null-modem cable must be configured.
    - If writing a user-mode driver, user-mode debuggers available in the Microsoft Visual Studio environment. The developer should be familiar with [how to attach to a process or launch a process under the debugger](../debugger/debugging-a-user-mode-process-using-visual-studio.md).

1. Write your first driver.
    - [How to write your first USB client driver (KMDF)](tutorial--write-your-first-usb-client-driver--kmdf-.md).
    - [How to write your first USB client driver (UMDF)](implement-driver-entry-for-a-usb-driver--umdf-.md).
    - Write, build, and install your first USB client driver by using the USB templates included with Visual Studio 2012. The developer should be able to describe framework driver, device, and queue objects and understand how the framework communicates with your driver.

1. Extend your driver by sending a USB control transfer request.
    - Send standard control requests and vendor commands to your device. For more information, see [How to send a USB control transfer](usb-control-transfer.md).

1. Extend your driver to use WDF USB I/O target objects to perform [USB data transfers](usb-device-i-o.md).
    - Extend your driver to perform common tasks as outlined in [Common tasks for USB client drivers](wdk-resources-for-usb-driver-development.md).

## Community Resources for USB

- [Microsoft Windows USB Core Team Blog](https://techcommunity.microsoft.com/t5/microsoft-usb-blog/bg-p/MicrosoftUSBBlog)

   Check out posts written by the Microsoft USB Team. The blog focuses on the Windows USB driver stack that works with various USB Host controllers and USB hubs found in Windows PC. A useful resource for USB client driver developers and USB hardware designers understand the driver stack implementation, resolve common issues, and explain how to use tools for gathering traces and log files.

- [OSR Online Lists](https://www.osronline.com/)

   Discussion list managed by [OSR Online](https://www.osronline.com/) for kernel-mode driver developers.

- [Windows Dev-Center for Hardware Development](../dashboard/index.yml)

   [Windows Driver Kit](../download-the-wdk.md), ensure that your product is reliable and compatible with Windows through the [Windows Hardware Lab Kit](/windows-hardware/test/hlk/), learn [Windows driver samples](../samples/index.md).

## Related topics

- [Universal Serial Bus (USB) Drivers](../index.yml)
- [How to enable USB selective suspend and system wake in the UMDF driver for a USB device](./selective-suspend-in-umdf-drivers.md)
- [USB Driver Development Guide](usb-driver-development-guide.md)
