---
title: Supporting Requests in IEEE 1394 Virtual Device Drivers
author: windows-driver-content
description: Supporting Requests in IEEE 1394 Virtual Device Drivers
MS-HAID:
- '1394-configrom\_f6f4ff3f-80cc-4a84-a316-4aad16717c1f.xml'
- 'IEEE.supporting\_requests\_in\_ieee\_1394\_virtual\_device\_drivers'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 17e0c84b-29d9-461f-a5f6-7677ecb7fb6e
keywords: ["emulation drivers WDK IEEE 1394 bus", "hardware emulation drivers WDK IEEE 1394 bus", "virtual devices WDK IEEE 1394 bus", "REQUEST_ASYNC_READ", "REQUEST_ASYNC_WRITE", "REQUEST_ASYNC_LOCK", "REQUEST_ALLOCATE_ADDRESS_RANGE", "REQUEST_GET_ADDR_FROM_DEVICE_OBJECT", "REQUEST_SET_DEVICE_XMIT_PROPERTIES"]
---

# Supporting Requests in IEEE 1394 Virtual Device Drivers


## <a href="" id="ddk-supporting-requests-in-ieee-1394-virtual-device-drivers-kg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BIEEE\buses%5D:%20Supporting%20Requests%20in%20IEEE%201394%20Virtual%20Device%20Drivers%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


