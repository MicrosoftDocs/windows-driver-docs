---
title: Overview of developing Windows drivers for USB host controllers
description: This article describes support in the Windows operating system, for developing a USB host controller driver that communicates with the Microsoft-provided USB host controller extension (UCX).
ms.date: 01/19/2023
---

# Overview of developing Windows drivers for USB host controllers

This article describes support in the Windows operating system, for developing a Universal Serial Bus (USB) host controller driver that communicates with the Microsoft-provided USB host controller extension (UCX).

If you're developing an xHCI host controller that isn't compliant with the specification or developing a custom non-xHCI hardware (such as a virtual host controller), you can write a host controller driver that communicates with UCX. For example, consider a wireless dock that supports USB devices. The PC communicates with USB devices through the wireless dock by using USB over TCP as a transport.

## USB host controller extension (UCX)

The USB host controller extension is a system-supplied driver (Ucx01000.sys). This driver is implemented as a framework class extension by using the [Windows Driver Framework](../wdf/index.md) programming interfaces. The host controller driver serves as the client driver to that class extension. While a host controller driver handles hardware operations and events, power management, and PnP events, UCX serves as an abstracted interface that queues requests to the host controller driver, and performs other tasks.

UCX is one of the [USB host-side drivers in Windows](usb-3-0-driver-stack-architecture.md). It's loaded as the FDO in the host controller device stack.

## USB host controller driver

UCX is extensible and is designed to support various host controller drivers. Windows provides an xHCI driver (Usbxhci.sys) that targets USB xHCI host controllers.

The host controller driver is a client of UCX, written as [Kernel-Mode Driver Framework](../debugger/kernel-mode-driver-framework-debugging.md) (KMDF) driver.

## Microsoft-provided binaries

To write a host controller driver, you need UCX (Ucx01000.sys) and the stub library (Ucx01000.lib). The stub library is in the Windows Driver Kit (WDK). The library performs two main functions.

- Translate calls made by the host controller driver and pass them up to UCX.
- Provides support for versioning. A host controller driver will work with UCX, only if UCX has the same Major version number as the host controller driver, and the same or higher Minor version number as the host controller driver.

## Development tools

The WDK contains resources that are required for driver development, such as headers, libraries, tools, and samples.

[Download kits and tools for Windows](https://go.microsoft.com/fwlink/p/?linkid=617155)

## Get started

Read the official specification that describes the expected behavior of different components (device, host controller, and hub) of the architecture.

[xHCI for Universal Serial Bus: Specification](https://www.intel.com/content/www/us/en/products/docs/io/universal-serial-bus/extensible-host-controler-interface-usb-xhci.html)

[Official Universal Serial Bus Documents]( https://go.microsoft.com/fwlink/p/?linkid=224892)

## Understand the architecture of UCX

Familiarize yourself with the Microsoft-provided USB driver stack:

[USB host-side drivers in Windows](usb-3-0-driver-stack-architecture.md)

[Architecture: USB host controller extension (UCX)](get-started-with-host-controller-driver-development.md)

## Familiarize yourself with UCX objects and handles

UCX extends the WDF object functionality to define its own USB-specific UCX objects. For more details on WDF objects, see [Introduction to Framework Objects](../wdf/introduction-to-framework-objects.md).

For queuing requests to any underlying host controller driver, UCX uses these objects. For more information, see [UCX objects and handles used by a host controller driver](ucx-objects-and-handles-used-by-host-controller-driver.md).

| UCX object | Description |
|---|---|
| Host controller object (UCXCONTROLLER) | Represents the host controller that is created by the host controller driver. The driver must create only one host controller object per host controller instance. Typically created within the **[EVT_WDF_DRIVER_DEVICE_ADD](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add)** callback by calling the **[UcxControllerCreate](/previous-versions/windows/hardware/drivers/mt188033(v=vs.85))** method. |
| Root hub object (UCXROOTHUB) | Gets and controls the status of the root ports of the host controller. Created by the host controller driver typically within the [**EVT_WDF_DRIVER_DEVICE_ADD**](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback by calling the **[UcxRootHubCreate](/previous-versions/windows/hardware/drivers/mt188048(v=vs.85))** method. |
| USB device object (UCXUSBDEVICE) | Represents a physical USB device connected to the bus. Created by the host controller driver typically within the *[EVT_UCX_CONTROLLER_USBDEVICE_ADD](/windows-hardware/drivers/ddi/ucxcontroller/nc-ucxcontroller-evt_ucx_controller_usbdevice_add)* callback by calling the **[UcxUsbDeviceCreate](/windows-hardware/drivers/ddi/ucxusbdevice/nf-ucxusbdevice-ucxusbdevicecreate) method. |
| Endpoint object (UCXENDPOINT) | Represents an endpoint on a USB device object. Created by the host controller driver typically within the *[EVT_UCX_USBDEVICE_DEFAULT_ENDPOINT_ADD](/windows-hardware/drivers/ddi/ucxusbdevice/nc-ucxusbdevice-evt_ucx_usbdevice_default_endpoint_add)* or *[EVT_UCX_USBDEVICE_ENDPOINT_ADD](/windows-hardware/drivers/ddi/ucxusbdevice/nc-ucxusbdevice-evt_ucx_usbdevice_endpoint_add)* callback by calling the **[UcxEndpointCreate](/windows-hardware/drivers/ddi/ucxendpoint/nf-ucxendpoint-ucxendpointcreate) method. |
| Stream object (UCXSTREAMS) | Represents a number of pipes to the device across a single bulk endpoint. Created by the host controller driver typically within the *[EVT_UCX_ENDPOINT_STATIC_STREAMS_ADD](/windows-hardware/drivers/ddi/ucxendpoint/nc-ucxendpoint-evt_ucx_endpoint_static_streams_add)* callback by calling the **[UcxStaticStreamsCreate](/windows-hardware/drivers/ddi/ucxsstreams/nf-ucxsstreams-ucxstaticstreamscreate)** method. |

## Documentation sections

[Root hub callback functions of a host controller driver](manage-the-root-hub-in-a-host-controller-driver.md)

UCX handles most operations related to the root hub. This allows the USB hub driver to interact with the root hub in the same way that it interacts with a regular hub. The host controller driver can register its callback functions.

[Handle I/O requests in a USB host controller driver](handling-i-o-requests-in-a-host-controller-driver.md)

UCX triages incoming USB request blocks (URBs), and then forwards them to the correct endpoint queue.

[Configure USB endpoints in a host controller driver](configuring-usb-endpoints-in-a-host-controller-driver.md)

The host controller driver plays a role in UCX's management of the queues that are associated with its endpoints, and in the programming of endpoints into controller hardware.

[USB host controller extension (UCX) reference](/windows-hardware/drivers/ddi/_usbref/#host-controller-driver-reference)

Gives specifications for I/O requests, support routines, structures, and interfaces used by the client driver. Those routines and related data structures are defined in the WDK headers.

UCX is referred to as the *framework class extension*.

The host controller driver is referred to as the *client driver*.

## Related topics

- [Universal Serial Bus (USB)](../index.yml)
