---
title: Setting Up Isochronous Transfer for IEEE 1394 Devices
description: Setting Up Isochronous Transfer for IEEE 1394 Devices
ms.assetid: 5161da54-0f20-496c-bf64-dc756b987de2
keywords:
- isochronous I/O WDK IEEE 1394 bus , setting up
- bus cycles WDK IEEE 1394 bus
- isochronous channels WDK IEEE 1394 bus
- resource handles WDK IEEE 1394 bus
- buffers WDK IEEE 1394 bus
- speed WDK IEEE 1394 bus
- allocating bandwidth
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting Up Isochronous Transfer for IEEE 1394 Devices


Before drivers can start their device, they must follow these steps:

### <a href="" id="step-1---choose-the-transfer-speed-"></a>Step 1. Choose the transfer speed.

The IEEE 1394 bus can support several different speeds, limited by what the hardware allows. Even if a specific device supports a certain speed, it may be plugged into another device that only supports lower speeds. Drivers must determine at run-time the transfer speed between the device and the computer. They query the bus driver with the [**REQUEST\_GET\_SPEED\_BETWEEN\_DEVICES**](https://msdn.microsoft.com/library/windows/hardware/ff537645) request to determine the maximum possible speed between two devices on the bus, or the device and the host computer.

### <a href="" id="step-2---allocate-bandwidth-"></a>Step 2. Allocate bandwidth.

Before any isochronous data transfer can take place, the driver must reserve bandwidth on the bus. The bus tracks the amount of bandwidth allocated until it reaches a fixed amount (according to the IEEEE 1394-1995 specification, the maximum bandwidth that can be sent is 80% of one *bus cycle*, which is 125 nanoseconds); it then does not allow any other device to acquire bandwidth until some of the currently allocated bandwidth is freed. The driver submits the [**REQUEST\_ISOCH\_ALLOCATE\_BANDWIDTH**](https://msdn.microsoft.com/library/windows/hardware/ff537647) request to the bus driver to reserve bandwidth.

If the request succeeds, the bus driver returns a bandwidth handle. The driver uses this handle in future bandwidth-related requests to the bus driver. For example, the driver can use [**REQUEST\_ISOCH\_SET\_CHANNEL\_BANDWIDTH**](https://msdn.microsoft.com/library/windows/hardware/ff537658) on the handle to adjust the amount of bandwidth allocated. When the driver has finished with the allocated bandwidth, it must use [**REQUEST\_ISOCH\_FREE\_BANDWIDTH**](https://msdn.microsoft.com/library/windows/hardware/ff537652) to free the bandwidth, so that it can be used by other devices on the bus.

If the request fails, the driver must not attempt any data transfer. Drivers that fail to allocate bandwidth might be able to allocate it in subsequent tries, so they should leave themselves in a state where they can attempt to allocate bandwidth later when appropriate. Attempts to allocate bandwidth after a bus reset are likely to succeed, because the system automatically releases all previously-allocated bandwidth and channels after a bus reset.

Drivers that succeed in allocating bandwidth, must reallocate their bandwidth and channels after a bus reset, for the reasons just mentioned. Furthermore, after a reset, bandwidth handles become stale and must be freed by a call to [**REQUEST\_ISOCH\_FREE\_BANDWIDTH**](https://msdn.microsoft.com/library/windows/hardware/ff537652), unless the bandwidth was allocated with the IRB\_FLAG\_ALLOW\_REMOTE\_FREE flag set.

### <a href="" id="step-3---allocate-a-channel-"></a>Step 3. Allocate a channel.

After a bandwidth allocation request succeeds, the driver requests an *isochronous channel* on which to write data. Multiple devices can read packets on one isochronous channel, but only one device can write to a channel. Devices that receive isochronous packets do not send acknowledgment packets in return.

Drivers request a channel by sending the [**REQUEST\_ISOCH\_ALLOCATE\_CHANNEL**](https://msdn.microsoft.com/library/windows/hardware/ff537648) request to the bus driver. The driver may request a specific channel, or ISOCH\_ANY\_CHANNEL to allocate any free channel. On success, the bus driver returns the allocated channel. If the bus driver returns an error code, drivers must not attempt any data transfer, and they must deallocate the bandwidth they allocated in Step 2.

Drivers should not assume that because a channel is not currently available, it will never be available. Channels may become free at any time, so drivers should leave themselves in a state where they can attempt to allocate a channel later when appropriate.

### <a href="" id="step-4---allocate-a-resource-handle-"></a>Step 4. Allocate a resource handle.

Once the driver allocates a channel, it allocates a resource handle for that channel. In all subsequent steps, the driver uses the resource handle to specify the channel.

Drivers allocate a resource handle for the channel by submitting the [**REQUEST\_ISOCH\_ALLOCATE\_RESOURCES**](https://msdn.microsoft.com/library/windows/hardware/ff537649) request to the bus driver.

When the driver allocates a resource handle, it also specifies flags indicating how the buffers attached to the handle will be used:

-   If the driver will use the channel to read data from a device (a [**REQUEST\_ISOCH\_LISTEN**](https://msdn.microsoft.com/library/windows/hardware/ff537655) operation), it sets the RESOURCE\_USED\_IN\_LISTENING flag. If the driver will use the channel to write data to the device (a [**REQUEST\_ISOCH\_TALK**](https://msdn.microsoft.com/library/windows/hardware/ff537660) operation), it sets the RESOURCE\_USED\_IN\_TALKING flag.

-   The driver uses the handle to provide data buffers for the transaction. (See Step 5 for details.) The bus driver uses the buffers in order until it runs out, and then pauses the operation until the device driver attaches more buffers. See [Buffering Isochronous DMA Transfers for IEEE 1394 Devices](https://msdn.microsoft.com/library/windows/hardware/ff537014) for details.

-   The driver may specify that the operation be synchronized to a certain value of the isochronous cycle clock. See [Isochronous Synchronization Options for IEEE 1394 Devices](https://msdn.microsoft.com/library/windows/hardware/ff537379) for details.

-   The driver can set options for isochronous listens. The driver can indicate whether the isochronous packet headers are stripped from the data packets. The driver can also indicate whether arriving data should be copied into the waiting data buffers one packet per buffer, or if each buffer should be filled with data. See [Isochronous Listen Options for IEEE 1394 Devices](https://msdn.microsoft.com/library/windows/hardware/ff537377) for details.

If this request fails, drivers should deallocate all isochronous resources they allocated in the previous steps.

### <a href="" id="step-5---attach-buffers-to-the-resource-handle-"></a>Step 5. Attach buffers to the resource handle.

Once the driver allocates a resource handle, it attaches buffers to the handle. The host DMA controller will read data from or write data to the attached buffers.

With each buffer, the driver passes an [**ISOCH\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff537401) structure -describing how the buffer will be used. In the buffer's ISOCH\_DESCRIPTOR structure, the driver can specify the following information:

-   The maximum number of bytes per frame. When transmitting data, the host controller splits the data buffer into packets of this size.

-   An optional callback routine. The bus driver calls this routine when it has finished processing

-   Synchronization options. See [Isochronous Synchronization Options for IEEE 1394 Devices](https://msdn.microsoft.com/library/windows/hardware/ff537379) for a description of the synchronization options.

-   On isochronous talk operations, the driver can designate this buffer as a list of headers to be prepended to the next few data packets. See [Isochronous Talk Options for IEEE 1394 Devices](https://msdn.microsoft.com/library/windows/hardware/ff537380) for details.

Once the operation has begun, the driver can detach buffers that it no longer needs, and can attach additional buffers. The driver can use the callback routine identified in [**ISOCH\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff537401) to signal itself when the bus driver has completed processing the last buffer attached. See [Buffering Isochronous DMA Transfers for IEEE 1394 Devices](https://msdn.microsoft.com/library/windows/hardware/ff537014) for a description of DMA buffering for IEEE 1394 devices.

### <a href="" id="step-6---begin-the-data-transfer"></a>Step 6. Begin the data transfer

To read from the device, the driver issues the [**REQUEST\_ISOCH\_LISTEN**](https://msdn.microsoft.com/library/windows/hardware/ff537655) request. To write to the device, the driver issues the [**REQUEST\_ISOCH\_TALK**](https://msdn.microsoft.com/library/windows/hardware/ff537660) request. The driver can then activate the device for reading or writing, in the appropriate device-specific fashion.

 

 




