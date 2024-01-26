---
title: Overview of Sending USB Data Transfers in USB Client Drivers
description: The articles in this section provide information about USB pipes and URBs for I/O requests, and describe how a client driver can use device driver interfaces (DDIs) to transfer data to and from a USB device.
ms.date: 01/17/2024
---

# Overview of sending USB data transfers in USB client drivers

The articles in this section provide information about USB pipes and URBs for I/O requests, and describe how a client driver can use device driver interfaces (DDIs) to transfer data to and from a USB device.

A transfer takes place every time data is moved between the host controller and the USB device. In general, USB transfers can be broadly categorized into control transfers and data transfers. All USB devices must support control transfers and can support endpoints for data transfers. Each type of transfer is associated with the type of *USB endpoint* (a buffer in the device). Control transfer is associated with the default endpoint and data transfers use unidirectional endpoints. The data transfer types use interrupt, bulk, and isochronous endpoints. The USB driver stack creates a communication channel called a *pipe* for each endpoint supported by the device. One end of the pipe is the device's endpoint. The other end of the pipe is always the host controller.

Before sending I/O requests to the device, the client driver must retrieve information about configurations, interfaces, endpoints, the vendor, and class-specific descriptors from a USB device. In addition, the driver must also configure the device. Device configuration involves tasks such as selecting a configuration and an alternate setting within each interface. Each alternate setting can specify one or more USB endpoints that are available for data transfers.

For information about device configuration, see [How to Select a Configuration for a USB Device](how-to-select-a-configuration-for-a-usb-device.md) and [How to select an alternate setting in a USB interface](select-a-usb-alternate-setting.md).

After the client driver has configured the device, the driver has access to the pipe handles created by the USB driver stack for each endpoint in the currently selected alternate setting. To transfer data to an endpoint, a client driver creates a request by formatting an URB specific to the type of request.

## In this section

| Article | Description |
|---|---|
| [How to send a USB control transfer](usb-control-transfer.md) | This article explains the structure of a control transfer and how a client driver should send a control request to the device. |
| [How to enumerate USB pipes](how-to-get-usb-pipe-handles.md) | This article provides an overview of USB pipes and describes the steps required by a USB client driver to obtain pipe handles from the USB driver stack. |
| [How to use the continuous reader for reading data from a USB pipe](how-to-use-the-continous-reader-for-getting-data-from-a-usb-endpoint--umdf-.md) | This article describes the WDF-provided continuous reader object. The procedures in this article provide step-by-step instructions about how to configure the object and use it to read data from a USB pipe. |
| [How to send USB bulk transfer requests](usb-bulk-and-interrupt-transfer.md) | This article provides a brief overview about USB bulk transfers. It also provides step-by-step instructions about how a client driver can send and receive bulk data from the device. |
| [How to open and close static streams in a USB bulk endpoint](how-to-open-streams-in-a-usb-endpoint.md) | This article discusses static streams capability and explains how a USB client driver can open and close streams in a bulk endpoint of a USB 3.0 device. |
| [How to transfer data to USB isochronous endpoints](transfer-data-to-isochronous-endpoints.md) | This article describes how a client driver can build a USB Request Block (URB) to transfer data to and from isochronous endpoints in a USB device. |
| [How to send chained MDLs](how-to-send-chained-mdls.md) | In this article, you'll learn about the chained MDLs capability in the USB driver stack, and how a client driver can send a transfer buffer as a chain of **[MDL](/windows-hardware/drivers/ddi/wdm/ns-wdm-_mdl)** structure. |
| [How to recover from USB pipe errors](how-to-recover-from-usb-pipe-errors.md) | This article provides information about steps you can try when a data transfer to a USB pipe fails. The mechanisms described in this article cover abort, reset, and cycle port operations on bulk, interrupt, and isochronous pipes. |
| [USB Bandwidth Allocation](usb-bandwidth-allocation.md) | This section provides guidance concerning the careful management of USB bandwidth. |

## Related topics

- [USB Driver Development Guide](usb-driver-development-guide.md)
