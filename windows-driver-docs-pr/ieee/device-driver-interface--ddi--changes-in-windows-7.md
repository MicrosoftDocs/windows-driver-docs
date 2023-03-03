---
title: Device Driver Interface (DDI) Changes in Windows 7
description: This topic summarizes the general DDI changes that support the new 1394 bus driver.
ms.date: 03/03/2023
---

# Device Driver Interface (DDI) Changes in Windows 7

Windows 7 includes 1394ohci.sys, a new IEEE 1394 bus driver that is implemented by using the kernel-mode driver framework (KMDF). The new 1394 bus driver replaces the legacy IEEE bus drivers in port/miniport configuration--1394bus.sys and ochi1394.sys. New DDIs were added to the new features supported by 1394ohci.sys. In addition, certain 1394 DDIs were changed to support greater speeds as defined by the 1394b specification and improved to simplify the development of 1394 client drivers.

This topic summarizes the general DDI changes that support the new 1394 bus driver.

* [Extended Bus Reset Notification](#extended-bus-reset-notification)
* [New IOCTLs for PHY Packet Support](#new-ioctls-for-phy-packet-support)
* [New IOCTL to Retrieve Configuration ROM](#new-ioctl-to-retrieve-configuration-rom)
* [IEEE Bus Driver DDI Changes](#ieee-bus-driver-ddi-changes)
* [New Flags for Speed and Payload Size](#new-flags-for-speed-and-payload-size)
* [IEEE 1394 IOCTL Changes](#ieee-1394-ioctl-changes)
* [Related topics](#related-topics)

## Extended Bus Reset Notification

The 1394ohci.sys bus driver supports an extended bus reset notification. This notification returns information about the current generation of the bus (such as the generation count and node ids) to 1394 client drivers in the context of the bus reset notification. This information can eliminate the need for a 1394 client driver to synchronize the retrieval of the generation count, node ids, and other information, with its bus reset notification handler.

To register for extended bus reset notifications, a client driver uses the existing [**REQUEST_BUS_RESET_NOTIFICATION**](/windows-hardware/drivers/ddi/1394/ni-1394-ioctl_1394_class) I/O request and specifies the new EXTENDED_NOTIFICATION_ROUTINE flag in the **u.BusResetNotification.fulFlags** parameter. When the EXTENDED_NOTIFICATION_ROUTINE flag is specified, the **u.BusResetNotification.ResetContext** parameter points to a [**BUS_RESET_DATA**](/windows-hardware/drivers/ddi/1394/ns-1394-_bus_reset_data) structure.

## New IOCTLs for PHY Packet Support

The 1394ohci.sys bus driver exposes the following new DDIs for sending and receiving PHY packets, as defined in the IEEE-1394a specification.

* [**REQUEST_SEND_PHY_PACKET**](/windows-hardware/drivers/ddi/1394/ni-1394-ioctl_1394_class)
* [**REQUEST_RECEIVE_PHY_PACKETS**](/windows-hardware/drivers/ddi/1394/ni-1394-ioctl_1394_class)

You should use the new [**REQUEST_SEND_PHY_PACKET**](/windows-hardware/drivers/ddi/1394/ni-1394-ioctl_1394_class) I/O request instead of [**REQUEST_SEND_PHY_CONFIG_PACKET**](/windows-hardware/drivers/ddi/1394/ni-1394-ioctl_1394_class). The latter I/O request does not allow for specifying the generation count, which could result in a PHY packet being sent to the wrong generation of the 1394 bus.

## New IOCTL to Retrieve Configuration ROM

The new IOCTL, [**REQUEST_GET_CONFIG_ROM**](/windows-hardware/drivers/ddi/1394/ni-1394-ioctl_1394_class), returns the contents of a node's configuration ROM, up to a maximum size of 1 kilobyte (KB). The 1394ohci.sys bus driver supports only 1 KB configuration ROMs, which is the same as the legacy 1394 bus driver.

## IEEE Bus Driver DDI Changes

The following table describes the changes in functional behavior of the DDIs exposed by the new 1394 bus driver and the legacy 1394 bus driver:

| Device Driver Interface                                                              | Description                                                                                                                                                                                                                                                                          |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**REQUEST_GET_LOCAL_HOST_INFO**](/windows-hardware/drivers/ddi/1394/ni-1394-ioctl_1394_class)             | The 1394ohci.sys bus driver does not support setting **nLevel** to GET_HOST_CSR_CONTENTS and specifying the SPEED_MAP_LOCATION as **CsrBaseAddress**. The speed map is obsolete in the IEEE-1394a specification.                                                                |
| [**REQUEST_GET_SPEED_TOPOLOGY_MAPS**](/windows-hardware/drivers/ddi/1394/ni-1394-ioctl_1394_class)     | [**REQUEST_GET_SPEED_TOPOLOGY_MAPS**](/windows-hardware/drivers/ddi/1394/ni-1394-ioctl_1394_class) has been deprecated in Windows 2000 and later versions of the operating system. Sending this request to 1394ohci.sys returns STATUS_INVALID_PARAMETER.                                            |
| [**REQUEST_GET_SPEED_BETWEEN_DEVICES**](/windows-hardware/drivers/ddi/1394/ni-1394-ioctl_1394_class) | Sending the [**REQUEST_GET_SPEED_BETWEEN_DEVICES**](/windows-hardware/drivers/ddi/1394/ni-1394-ioctl_1394_class) request to 1394ohci.sys retrieves the speed between the local node and the device. The USE_LOCAL_NODE flag must be set in the **u.GetMaxSpeedBetweenDevices.fulFlags** parameter. |

## New Flags for Speed and Payload Size

The 1394 header file, 1394.h, in the Windows 7 Windows Driver Kit defines new flags for faster speeds and larger payloads. This section describes these new flags and values.

The following table describes the maximum asynchronous payload size for each newly supported speed.

| Flag                       | Value | Description |
|----------------------------|-------|-------------|
| ASYNC_PAYLOAD_800_RATE  | 4096  | 800 Mb/s    |
| ASYNC_PAYLOAD_1600_RATE | 4096  | 160 Mb/s    |
| ASYNC_PAYLOAD_3200_RATE | 4096  | 3200 Mb/s   |

The following table describes the speed flags for each newly supported speed.

| Flag               | Value | Description |
|--------------------|-------|-------------|
| SPEED_FLAGS_800  | 0x08  | 800 Mb/s    |
| SPEED_FLAGS_1600 | 0x10  | 160 Mb/s    |
| SPEED_FLAGS_3200 | 0x20  | 3200 Mb/s   |

The following table describes the speed code values for each newly supported speed.

| Flag              | Value | Description |
|-------------------|-------|-------------|
| SCODE_800_RATE  | 3     | 800 Mb/s    |
| SCODE_1600_RATE | 4     | 160 Mb/s    |
| SCODE_3200_RATE | 5     | 3200 Mb/s   |

## IEEE 1394 IOCTL Changes

This section describes the 1394 I/O requests that use the new speed and payload size values.

[**REQUEST_ASYNC_READ**](/windows-hardware/drivers/ddi/1394/ni-1394-ioctl_1394_class)  
**u.AsyncRead.nBlockSize**

Specifies the size of each block within the data stream that is read from the 1394 node. If this parameter is zero, the maximum packet size for the device and speed selected is used to issue these read requests, unless raw-mode addressing is used.

You can specify ASYNC_PAYLOAD_*XXX* flags in the **nBlockSize** member. Microsoft recommends that client drivers set the **nBlockSize** member to 0 so that the 1394 bus driver1394ohci.sys uses the maximum supported value, unless raw-mode addressing is used.

If raw-mode addressing is used, the client driver should set the **nBlockSize** member to the maximum asynchronous payload size that is supported by the device at the connected speed.

For more information on raw-mode addressing, see [Sending Asynchronous I/O Request Packets on the IEEE 1394 Bus](./sending-asynchronous-i-o-request-packets-on-the-ieee-1394-bus.md).

[**REQUEST_ASYNC_WRITE**](/windows-hardware/drivers/ddi/1394/ni-1394-ioctl_1394_class)  

### u.AsyncRead.nBlockSize

Specifies the size of each block within the data stream that is written to the 1394 node. If this parameter is zero, then the maximum packet size for the selected speed is used to divide these write requests, unless raw-mode addressing is used.

You can specify ASYNC_PAYLOAD_*XXX* flags in the **nBlockSize** member. Microsoft recommends that client drivers set the **nBlockSize** member to 0 so that the 1394 bus driver uses the maximum supported value, unless raw-mode addressing is used.

If raw-mode addressing is used, the client driver should set the **nBlockSize** member to the maximum asynchronous payload size that is supported by the device at the connected speed.

[**REQUEST_ISOCH_ALLOCATE_BANDWIDTH**](/windows-hardware/drivers/ddi/1394/ni-1394-ioctl_1394_class)  
You can specify SPEED_FLAGS_*XXX* flags in the **fulSpeed** member. The new 1394 bus driver can return the new SPEED_FLAGS_*XXX* flags in the **SpeedSelected** member.

### u.IsochAllocateBandwidth.fulSpeed

Specifies the connection speed to use to allocate bandwidth. The possible speed values are SPEED_FLAGS_*XXX*, where *XXX* is the (approximate) transfer rate in mbps.

### u.IsochAllocateBandwidth.SpeedSelected

Specifies the actual speed that is selected to allocate bandwidth. The value is one of SPEED_FLAGS_*XXX* (see the **fulSpeed** member description).

[**REQUEST_ISOCH_ALLOCATE_RESOURCES**](/windows-hardware/drivers/ddi/1394/ni-1394-ioctl_1394_class)  
You can specify SPEED_FLAGS_*XXX* flags in the **fulSpeed** member.

### u.IsochAllocateResources.fulSpeed

Specifies the connection speed to use to communicate on the channel. The possible speed values are SPEED_FLAGS_*XXX*, where *XXX* is the (approximate) transfer rate in mbps.

[**REQUEST_ISOCH_FREE_BANDWIDTH**](/windows-hardware/drivers/ddi/1394/ni-1394-ioctl_1394_class)  
You can specify SPEED_FLAGS_*XXX* flags in the **fulSpeed** member.

### u.IsochFreeBandwidth.fulSpeed

Specifies the connection speed to use to free bandwidth. The possible speed values are SPEED_FLAGS_*XXX*, where *XXX* is the (approximate) transfer rate in mbps.

> [!NOTE]
> The new 1394 bus driver uses the **fulSpeed** member only when the IRB_FLAG_ALLOW_REMOTE_FREE flag is set and the IRB_FLAG_USE_PRE_CALCULATE_VALUE flag is not set in **Flags** of the IRB. In all other cases, the new 1394 bus driver ignores **fulSpeed**.

[**REQUEST_SET_DEVICE_XMIT_PROPERTIES**](/windows-hardware/drivers/ddi/1394/ni-1394-ioctl_1394_class)  
You can specify SPEED_FLAGS_*XXX* flags in the **fulSpeed** member.

### u.SetDeviceXmitProperties.fulSpeed

Specifies the maximum speed for transactions to the device. The possible speed values are SPEED_FLAGS_*XXX*, where *XXX* is the (approximate) transfer rate in mbps.

[**REQUEST_ASYNC_STREAM**](/windows-hardware/drivers/ddi/1394/ni-1394-ioctl_1394_class)  
You can specify SPEED_FLAGS_*XXX* flags in the **nSpeed** member.

### u.AsyncStream.nSpeed

Specifies the transfer rate. The possible speed values are SPEED_FLAGS_*XXX*, where *XXX* is the (approximate) transfer rate in mbps.

[REQUEST_ISOCH_MODIFY_STREAM_PROPERTIES](/windows-hardware/drivers/ddi/1394/ns-1394-_irb_req_isoch_modify_stream_properties)
You can specify SPEED_FLAGS_*XXX* flags in the **fulSpeed** member.

### u.IsochModifyStreamProperties.fulSpeed

Specifies the maximum speed for transactions to the device. The possible speed values are SPEED_FLAGS_*XXX*, where *XXX* is the (approximate) transfer rate in mbps.

[**REQUEST_GET_SPEED_BETWEEN_DEVICES**](/windows-hardware/drivers/ddi/1394/ni-1394-ioctl_1394_class)  
You can specify SPEED_FLAGS_*XXX* flags in the **fulSpeed** member.

### u.GetMaxSpeedBetweenDevices.fulSpeed

Specifies the maximum possible transaction speed between the source device and the set of destination devices. The returned value is the maximum speed that all devices support at the same time. The possible speed values are SPEED_FLAGS_*XXX*, where *XXX* is the (approximate) transfer rate in mbps.

> [!NOTE]
> A client driver can also specify the USE_SCODE_SPEED flag in **u.GetMaxSpeedBetweenDevices.fulFlags** to request that an SCODE_*XXX*_RATE speed code value be returned in **fulSpeed** instead of a SPEED_FLAGS_xxx value.

## Related topics

[The IEEE 1394 Driver Stack](./the-ieee-1394-driver-stack.md)  
[IEEE 1394 Bus Driver in Windows 7](./ieee-1394-bus-driver-in-windows-7.md)
