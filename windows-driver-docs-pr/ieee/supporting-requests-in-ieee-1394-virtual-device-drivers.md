---
title: Supporting Requests in IEEE 1394 Virtual Device Drivers
description: Supporting Requests in IEEE 1394 Virtual Device Drivers
ms.assetid: 17e0c84b-29d9-461f-a5f6-7677ecb7fb6e
keywords:
- emulation drivers WDK IEEE 1394 bus
- hardware emulation drivers WDK IEEE 1394 bus
- virtual devices WDK IEEE 1394 bus
- REQUEST_ASYNC_READ
- REQUEST_ASYNC_WRITE
- REQUEST_ASYNC_LOCK
- REQUEST_ALLOCATE_ADDRESS_RANGE
- REQUEST_GET_ADDR_FROM_DEVICE_OBJECT
- REQUEST_SET_DEVICE_XMIT_PROPERTIES
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Requests in IEEE 1394 Virtual Device Drivers





Virtual PDOs and the drivers that are loaded above them have the same level of access to the 1394 bus DDI that a functional driver loaded on a PDO has to actual hardware. However, because there is no actual hardware in the case of a virtual driver, the 1394 bus driver must treat certain requests as special cases. This topic describes requests that exhibit different behavior if addressed to a virtual PDO:

-   [**REQUEST\_ASYNC\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff537634), [**REQUEST\_ASYNC\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff537636), and [**REQUEST\_ASYNC\_LOCK**](https://msdn.microsoft.com/library/windows/hardware/ff537633)

    Normally, when an application or a driver addresses an asynchronous I/O request to a target device, the 1394 bus driver extracts the node ID of the device from the device extension of the device's physical device object (PDO). This information is recorded in the device's PDO extension when the device is enumerated. Virtual devices, however, are not enumerated in the usual fashion, so the driver that generates the request *must* provide a node ID when sending a request to a virtual device, just as it would if it were doing asynchronous I/O in raw mode. For a discussion of raw mode addressing, see [Sending Asynchronous I/O Request Packets on the IEEE 1394 Bus](https://msdn.microsoft.com/library/windows/hardware/ff538087).

    When the bus driver receives a request for the PDO of a virtual device, it uses the node ID provided by the driver that originated the request rather than attempting to extract the node ID from the device extension. Strictly speaking, virtual devices do not have node IDs, so the drivers that send requests to virtual devices must provide an alternative node ID. By convention, virtual devices use the node ID of the PC's host controller.

    When the driver for the virtual device allocates memory, it specifies that it will receive all packets that are broadcast on the 1394 bus. The driver then identifies its packets by checking for the node ID of the host controller in every packet that it receives.

    Virtual devices do not have packet size or transfer rate information recorded in their device extensions, because these are hardware parameters. In the case of virtual devices, the bus driver uses packet size and transfer rate information that was stored in the device object for the port.

-   [**REQUEST\_ALLOCATE\_ADDRESS\_RANGE**](https://msdn.microsoft.com/library/windows/hardware/ff537632)

    Drivers for virtual devices must set the ACCESS\_FLAGS\_TYPE\_BROADCAST flag in the **fulAccessType** member of the IRB when allocating memory by means of a REQUEST\_ALLOCATE\_ADDRESS\_RANGE request. Because virtual devices have no actual node numbers, drivers for virtual devices have no means of receiving requests unless they receive packets in broadcast mode. If multiple nodes have allocated the same address range, only one will receive asynchronous requests that are addressed to that range. If drivers for a virtual device and a physical device both allocate the same address range, the physical device has priority over the virtual device, and so the physical device receives the packets. If multiple virtual devices allocate the same address range, the first driver to allocate the range has priority.

-   [**REQUEST\_GET\_ADDR\_FROM\_DEVICE\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff537641)

    Virtual devices have no corresponding hardware node and no node ID of their own. Virtual device drivers return the node ID of the host controller whenever they receive this request, rather than the node ID of a physical node on the bus.

-   [**REQUEST\_SET\_DEVICE\_XMIT\_PROPERTIES**](https://msdn.microsoft.com/library/windows/hardware/ff537662)

    This request is not supported for virtual devices because there is no corresponding hardware node from which to get the node ID.

For all other requests, the behavior between virtual and physical devices is identical.

 

 




