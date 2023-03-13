---
title: Common tasks for USB client drivers
description: This article lists the "How to" articles in the USB driver documentation set. Each how-to article presents a set of tasks as a sequence of steps with code examples.
ms.date: 03/08/2023
---

# Common tasks for USB client drivers

This article lists the "How to" articles in this documentation set. Each how-to article presents a set of tasks as a sequence of steps with code examples.

A How to article provides you with step-by-step instructions about a process related to a USB client driver task. Generally, the articles are written with the assumption that you're extending the drivers created by USB templates included with Microsoft Visual Studio 2012.

This list contains links to the how-to articles for USB client drivers.

| Task | Description |
|---|---|
| [How to write your first USB client driver (KMDF)](tutorial--write-your-first-usb-client-driver--kmdf-.md) | In this article, you use the USB Kernel-Mode Driver template provided with Microsoft Visual Studio 11 Professional Beta to write a kernel-mode driver framework (KMDF)-based client driver. After building and installing the client driver, you'll view the client driver in Device Manager and view the driver output in a debugger. |
| [How to write your first USB client driver (UMDF)](implement-driver-entry-for-a-usb-driver--umdf-.md) | In this article, you use the USB User-Mode Driver template provided with Microsoft Visual Studio 11 Beta to write a user-mode driver framework (UMDF)-based client driver. After building and installing the client driver, you'll view the client driver in Device Manager and view the driver output in a debugger. |
| [How to get the configuration descriptor](usb-configuration-descriptors.md) | This article describes the important fields of a configuration and includes step-by-step guidance about how to obtain the configuration descriptor from a USB device. |
| [How to Submit an URB (WDM)](send-requests-to-the-usb-driver-stack.md) | This article describes the steps that are required to submit an initialized URB to the USB driver stack to process a particular request. |
| [How to select a configuration for a USB device](how-to-select-a-configuration-for-a-usb-device.md) | In this article, you learn about how to select a configuration in a universal serial bus (USB) device. This article describes the process of sending a select-configuration request by submitting an URB. |
| [How to select an alternate setting in a USB interface](select-a-usb-alternate-setting.md) | This article describes the steps for issuing a select-interface request to activate an alternate setting in a USB interface. The client driver must issue this request after selecting a USB configuration. Selecting a configuration, by default, also activates the first alternate setting in each interface in that configuration. |
| [How to enumerate USB pipes](how-to-get-usb-pipe-handles.md) | This article provides an overview of USB pipes and describes the steps required by a USB client driver to obtain pipe handles from the USB driver stack. |
| [How to use the continuous reader for reading data from a USB pipe](how-to-use-the-continous-reader-for-getting-data-from-a-usb-endpoint--umdf-.md) | This article describes the WDF-provided continuous reader object. The procedures in this article provided step-by-step instructions about how to configure the object and use it to read data from a USB pipe. |
| [How to send a USB control transfer](usb-control-transfer.md) | This article explains the structure of a control transfer and how a client driver should send a control request to the device. |
| [How to transfer data to USB bulk endpoints](usb-bulk-and-interrupt-transfer.md) | This article provides a brief overview about USB bulk transfers. It also provides step-by-step instructions about how a client driver can send and receive bulk data from the device. |
| [How to open and close static streams in a USB bulk endpoint](how-to-open-streams-in-a-usb-endpoint.md) | This article discusses static streams capability and explains how a USB client driver can open and close streams in a bulk endpoint of a USB 3.0 device. |
| [How to transfer data to USB isochronous endpoints](transfer-data-to-isochronous-endpoints.md) | This article describes how a client driver can build a USB Request Block (URB) to transfer data to and from supported isochronous endpoints in a USB device. |
| [How to recover from USB pipe errors](how-to-recover-from-usb-pipe-errors.md) | This article provides information about steps you can try when a data transfer to a USB pipe fails. The mechanisms described in this article cover abort, reset, and cycle port operations on bulk, interrupt, and isochronous pipes. |
| [How to send chained MDLs](how-to-send-chained-mdls.md) | In this article, learn about the chained MDLs capability in the USB driver stack, and how a client driver can send a transfer buffer as a chain of MDL structure. |
| [How to Register a Composite Device](register-a-composite-driver.md) | This article describes how a driver of a USB multi-function device, called a composite driver, can register and unregister the composite device with the underlying USB driver stack. The Microsoft-provided driver, Usbccgp.sys, is the default composite driver that Windows loads. The procedure in this article applies to a custom Windows Driver Model (WDM)-based composite driver that replaces Usbccgp.sys. |
| [How to Implement Function Suspend in a Composite Driver](how-to--implement-remote-and-function-wake-support.md) | This article provides an overview of function suspend and function remote wake-up features for Universal Serial Bus (USB) 3.0 multi-function devices (composite devices). In this article, you learn about implementing those features in a driver that controls a composite device. The article applies to composite drivers that replace Usbccgp.sys. |

## Related topics

- [Universal Serial Bus (USB) Drivers](../index.yml)
