---
title: Common tasks for USB client drivers
description: This topic lists the "How to" topics in the USB driver documentation set. Each how-to topic presents a set of tasks as a sequence of steps with code examples.
ms.date: 03/08/2023
---

# Common tasks for USB client drivers

This topic lists the "How to" topics in this documentation set. Each how-to topic presents a set of tasks as a sequence of steps with code examples.

A How to topic provides you with step-by-step instructions about a process related to a USB client driver task. Generally, the topics are written with the assumption that you are extending the drivers created by USB templates included with Microsoft Visual Studio 2012.

This list contains links to the how-to topics for USB client drivers.

| Task | Description |
|---|---|
| [How to write your first USB client driver (KMDF)](tutorial--write-your-first-usb-client-driver--kmdf-.md) | In this topic you'll use the USB Kernel-Mode Driver template provided with Microsoft Visual Studio 11 Professional Beta to write a simple kernel-mode driver framework (KMDF)-based client driver. After building and installing the client driver, you'll view the client driver in Device Manager and view the driver output in a debugger. |
| [How to write your first USB client driver (UMDF)](implement-driver-entry-for-a-usb-driver--umdf-.md) | In this topic you'll use the USB User-Mode Driver template provided with Microsoft Visual Studio 11 Beta to write a user-mode driver framework (UMDF)-based client driver. After building and installing the client driver, you'll view the client driver in Device Manager and view the driver output in a debugger. |
| [How to get the configuration descriptor](usb-configuration-descriptors.md) | This topic describes the important fields of a configuration and includes step-by-step guidance about how to obtain the configuration descriptor from a USB device. |
| [How to Submit an URB (WDM)](send-requests-to-the-usb-driver-stack.md) | This topic describes the steps that are required to submit an initialized URB to the USB driver stack to process a particular request. |
| [How to select a configuration for a USB device](how-to-select-a-configuration-for-a-usb-device.md) | In this topic, you'll learn about how to select a configuration in a universal serial bus (USB) device. This topic describes the process of sending a select-configuration request by submitting an URB. |
| [How to select an alternate setting in a USB interface](select-a-usb-alternate-setting.md) | This topic describes the steps for issuing a select-interface request to activate an alternate setting in a USB interface. The client driver must issue this request after selecting a USB configuration. Selecting a configuration, by default, also activates the first alternate setting in each interface in that configuration. |
| [How to enumerate USB pipes](how-to-get-usb-pipe-handles.md) | This topic provides an overview of USB pipes and describes the steps required by a USB client driver to obtain pipe handles from the USB driver stack. |
| [How to use the continuous reader for reading data from a USB pipe](how-to-use-the-continous-reader-for-getting-data-from-a-usb-endpoint--umdf-.md) | This topic describes the WDF-provided continuous reader object. The procedures in this topic provided step-by-step instructions about how to configure the object and use it to read data from a USB pipe. |
| [How to send a USB control transfer](usb-control-transfer.md) | This topic explains the structure of a control transfer and how a client driver should send a control request to the device. |
| [How to transfer data to USB bulk endpoints](usb-bulk-and-interrupt-transfer.md) | This topic provides a brief overview about USB bulk transfers. It also provides step-by-step instructions about how a client driver can send and receive bulk data from the device. |
| [How to open and close static streams in a USB bulk endpoint](how-to-open-streams-in-a-usb-endpoint.md) | This topic discusses static streams capability and explains how a USB client driver can open and close streams in a bulk endpoint of a USB 3.0 device. |
| [How to transfer data to USB isochronous endpoints](transfer-data-to-isochronous-endpoints.md) | This topic describes how a client driver can build a USB Request Block (URB) to transfer data to and from supported isochronous endpoints in a USB device. |
| [How to recover from USB pipe errors](how-to-recover-from-usb-pipe-errors.md) | This topic provides information about steps you can try when a data transfer to a USB pipe fails. The mechanisms described in this topic cover abort, reset, and cycle port operations on bulk, interrupt, and isochronous pipes. |
| [How to send chained MDLs](how-to-send-chained-mdls.md) | In this topic, you will learn about the chained MDLs capability in the USB driver stack, and how a client driver can send a transfer buffer as a chain of MDL structure. |
| [How to Register a Composite Device](register-a-composite-driver.md) | This topic describes how a driver of a USB multi-function device, called a composite driver, can register and unregister the composite device with the underlying USB driver stack. The Microsoft-provided driver, Usbccgp.sys, is the default composite driver that is loaded by Windows. The procedure in this topic applies to a custom Windows Driver Model (WDM)-based composite driver that replaces Usbccgp.sys. |
| [How to Implement Function Suspend in a Composite Driver](how-to--implement-remote-and-function-wake-support.md) | This topic provides an overview of function suspend and function remote wake-up features for Universal Serial Bus (USB) 3.0 multi-function devices (composite devices). In this topic you will learn about implementing those features in a driver that controls a composite device. The topic applies to composite drivers that replace Usbccgp.sys. |

## Related topics

- [Universal Serial Bus (USB) Drivers](../index.yml)
