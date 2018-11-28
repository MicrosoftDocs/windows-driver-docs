---
title: Device Driver Interface (DDI) Changes in Windows 7
description: This topic summarizes the general DDI changes that support the new 1394 bus driver.
ms.assetid: 5473C6AC-284C-41B1-AA67-75696BE96C24
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Device Driver Interface (DDI) Changes in Windows 7


Windows 7 includes 1394ohci.sys, a new IEEE 1394 bus driver that is implemented by using the kernel-mode driver framework (KMDF). The new 1394 bus driver replaces the legacy IEEE bus drivers in port/miniport configuration--1394bus.sys and ochi1394.sys. New DDIs were added to the new features supported by 1394ohci.sys. In addition, certain 1394 DDIs were changed to support greater speeds as defined by the 1394b specification and improved to simplify the development of 1394 client drivers.

This topic summarizes the general DDI changes that support the new 1394 bus driver.

-   [Extended Bus Reset Notification](#extended-bus-reset-notification)
-   [New IOCTLs for PHY Packet Support](#new-ioctls-for-phy-packet-support)
-   [New IOCTL to Retrieve Configuration ROM](#new-ioctl-to-retrieve-configuration-rom)
-   [IEEE Bus Driver DDI Changes](#ieee-bus-driver-ddi-changes)
-   [New Flags for Speed and Payload Size](#speed)
-   [IEEE 1394 IOCTL Changes](#ioctl)
-   [Related topics](#related-topics)

## Extended Bus Reset Notification


The 1394ohci.sys bus driver supports an extended bus reset notification. This notification returns information about the current generation of the bus (such as the generation count and node ids) to 1394 client drivers in the context of the bus reset notification. This information can eliminate the need for a 1394 client driver to synchronize the retrieval of the generation count, node ids, and other information, with its bus reset notification handler.

To register for extended bus reset notifications, a client driver uses the existing [**REQUEST\_BUS\_RESET\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff537638) I/O request and specifies the new EXTENDED\_NOTIFICATION\_ROUTINE flag in the **u.BusResetNotification.fulFlags** parameter. When the EXTENDED\_NOTIFICATION\_ROUTINE flag is specified, the **u.BusResetNotification.ResetContext** parameter points to a [**BUS\_RESET\_DATA**](https://msdn.microsoft.com/library/windows/hardware/gg266399) structure.

## New IOCTLs for PHY Packet Support


The 1394ohci.sys bus driver exposes the following new DDIs for sending and receiving PHY packets, as defined in the IEEE-1394a specification.

-   [**REQUEST\_SEND\_PHY\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/gg266407)
-   [**REQUEST\_RECEIVE\_PHY\_PACKETS**](https://msdn.microsoft.com/library/windows/hardware/gg266406)

You should use the new [**REQUEST\_SEND\_PHY\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/gg266407) I/O request instead of [**REQUEST\_SEND\_PHY\_CONFIG\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff537661). The latter I/O request does not allow for specifying the generation count, which could result in a PHY packet being sent to the wrong generation of the 1394 bus.

## New IOCTL to Retrieve Configuration ROM


The new IOCTL, [**REQUEST\_GET\_CONFIG\_ROM**](https://msdn.microsoft.com/library/windows/hardware/gg266404), returns the contents of a node's configuration ROM, up to a maximum size of 1 kilobyte (KB). The 1394ohci.sys bus driver supports only 1 KB configuration ROMs, which is the same as the legacy 1394 bus driver.

## IEEE Bus Driver DDI Changes


The following table describes the changes in functional behavior of the DDIs exposed by the new 1394 bus driver and the legacy 1394 bus driver:

| Device Driver Interface                                                              | Description                                                                                                                                                                                                                                                                          |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**REQUEST\_GET\_LOCAL\_HOST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff537644)             | The 1394ohci.sys bus driver does not support setting **nLevel** to GET\_HOST\_CSR\_CONTENTS and specifying the SPEED\_MAP\_LOCATION as **CsrBaseAddress**. The speed map is obsolete in the IEEE-1394a specification.                                                                |
| [**REQUEST\_GET\_SPEED\_TOPOLOGY\_MAPS**](https://msdn.microsoft.com/library/windows/hardware/ff537646)     | [**REQUEST\_GET\_SPEED\_TOPOLOGY\_MAPS**](https://msdn.microsoft.com/library/windows/hardware/ff537646) has been deprecated in Windows 2000 and later versions of the operating system. Sending this request to 1394ohci.sys returns STATUS\_INVALID\_PARAMETER.                                            |
| [**REQUEST\_GET\_SPEED\_BETWEEN\_DEVICES**](https://msdn.microsoft.com/library/windows/hardware/ff537645) | Sending the [**REQUEST\_GET\_SPEED\_BETWEEN\_DEVICES**](https://msdn.microsoft.com/library/windows/hardware/ff537645) request to 1394ohci.sys retrieves the speed between the local node and the device. The USE\_LOCAL\_NODE flag must be set in the **u.GetMaxSpeedBetweenDevices.fulFlags** parameter. |

 

## New Flags for Speed and Payload Size


The 1394 header file, 1394.h, in the Windows 7 Windows Driver Kit defines new flags for faster speeds and larger payloads. This section describes these new flags and values.

The following table describes the maximum asynchronous payload size for each newly supported speed.

| Flag                       | Value | Description |
|----------------------------|-------|-------------|
| ASYNC\_PAYLOAD\_800\_RATE  | 4096  | 800 Mb/s    |
| ASYNC\_PAYLOAD\_1600\_RATE | 4096  | 160 Mb/s    |
| ASYNC\_PAYLOAD\_3200\_RATE | 4096  | 3200 Mb/s   |

 

The following table describes the speed flags for each newly supported speed.

| Flag               | Value | Description |
|--------------------|-------|-------------|
| SPEED\_FLAGS\_800  | 0x08  | 800 Mb/s    |
| SPEED\_FLAGS\_1600 | 0x10  | 160 Mb/s    |
| SPEED\_FLAGS\_3200 | 0x20  | 3200 Mb/s   |

 

The following table describes the speed code values for each newly supported speed.

| Flag              | Value | Description |
|-------------------|-------|-------------|
| SCODE\_800\_RATE  | 3     | 800 Mb/s    |
| SCODE\_1600\_RATE | 4     | 160 Mb/s    |
| SCODE\_3200\_RATE | 5     | 3200 Mb/s   |

 

## IEEE 1394 IOCTL Changes


This section describes the 1394 I/O requests that use the new speed and payload size values.

<a href="" id="request-async-read"></a>[**REQUEST\_ASYNC\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff537634)  
**u.AsyncRead.nBlockSize**

Specifies the size of each block within the data stream that is read from the 1394 node. If this parameter is zero, the maximum packet size for the device and speed selected is used to issue these read requests, unless raw-mode addressing is used.

You can specify ASYNC\_PAYLOAD\_*XXX* flags in the **nBlockSize** member. Microsoft recommends that client drivers set the **nBlockSize** member to 0 so that the 1394 bus driver1394ohci.sys uses the maximum supported value, unless raw-mode addressing is used.

If raw-mode addressing is used, the client driver should set the **nBlockSize** member to the maximum asynchronous payload size that is supported by the device at the connected speed.

For more information on raw-mode addressing, see [Sending Asynchronous I/O Request Packets on the IEEE 1394 Bus](https://msdn.microsoft.com/library/windows/hardware/ff538087).

<a href="" id="request-async-write"></a>[**REQUEST\_ASYNC\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff537636)  
**u.AsyncRead.nBlockSize**

Specifies the size of each block within the data stream that is written to the 1394 node. If this parameter is zero, then the maximum packet size for the selected speed is used to divide these write requests, unless raw-mode addressing is used.

You can specify ASYNC\_PAYLOAD\_*XXX* flags in the **nBlockSize** member. Microsoft recommends that client drivers set the **nBlockSize** member to 0 so that the 1394 bus driver uses the maximum supported value, unless raw-mode addressing is used.

If raw-mode addressing is used, the client driver should set the **nBlockSize** member to the maximum asynchronous payload size that is supported by the device at the connected speed.

<a href="" id="request-isoch-allocate-bandwidth"></a>[**REQUEST\_ISOCH\_ALLOCATE\_BANDWIDTH**](https://msdn.microsoft.com/library/windows/hardware/ff537647)  
You can specify SPEED\_FLAGS\_*XXX* flags in the **fulSpeed** member. The new 1394 bus driver can return the new SPEED\_FLAGS\_*XXX* flags in the **SpeedSelected** member.

**u.IsochAllocateBandwidth.fulSpeed**

Specifies the connection speed to use to allocate bandwidth. The possible speed values are SPEED\_FLAGS\_*XXX*, where *XXX* is the (approximate) transfer rate in mbps.

**u.IsochAllocateBandwidth.SpeedSelected**

Specifies the actual speed that is selected to allocate bandwidth. The value is one of SPEED\_FLAGS\_*XXX* (see the **fulSpeed** member description).

<a href="" id="request-isoch-allocate-resources"></a>[**REQUEST\_ISOCH\_ALLOCATE\_RESOURCES**](https://msdn.microsoft.com/library/windows/hardware/ff537649)  
You can specify SPEED\_FLAGS\_*XXX* flags in the **fulSpeed** member.

**u.IsochAllocateResources.fulSpeed**

Specifies the connection speed to use to communicate on the channel. The possible speed values are SPEED\_FLAGS\_*XXX*, where *XXX* is the (approximate) transfer rate in mbps.

<a href="" id="request-isoch-free-bandwidth"></a>[**REQUEST\_ISOCH\_FREE\_BANDWIDTH**](https://msdn.microsoft.com/library/windows/hardware/ff537652)  
You can specify SPEED\_FLAGS\_*XXX* flags in the **fulSpeed** member.

**u.IsochFreeBandwidth.fulSpeed**

Specifies the connection speed to use to free bandwidth. The possible speed values are SPEED\_FLAGS\_*XXX*, where *XXX* is the (approximate) transfer rate in mbps.

**Note**  The new 1394 bus driver uses the **fulSpeed** member only when the IRB\_FLAG\_ALLOW\_REMOTE\_FREE flag is set and the IRB\_FLAG\_USE\_PRE\_CALCULATE\_VALUE flag is not set in **Flags** of the IRB. In all other cases, the new 1394 bus driver ignores **fulSpeed**.

 

<a href="" id="request-set-device-xmit-properties"></a>[**REQUEST\_SET\_DEVICE\_XMIT\_PROPERTIES**](https://msdn.microsoft.com/library/windows/hardware/ff537662)  
You can specify SPEED\_FLAGS\_*XXX* flags in the **fulSpeed** member.

**u.SetDeviceXmitProperties.fulSpeed**

Specifies the maximum speed for transactions to the device. The possible speed values are SPEED\_FLAGS\_*XXX*, where *XXX* is the (approximate) transfer rate in mbps.

<a href="" id="request-async-stream"></a>[**REQUEST\_ASYNC\_STREAM**](https://msdn.microsoft.com/library/windows/hardware/ff537635)  
You can specify SPEED\_FLAGS\_*XXX* flags in the **nSpeed** member.

**u.AsyncStream.nSpeed**

Specifies the transfer rate. The possible speed values are SPEED\_FLAGS\_*XXX*, where *XXX* is the (approximate) transfer rate in mbps.

<a href="" id="request-isoch-modify-stream-properties"></a>REQUEST\_ISOCH\_MODIFY\_STREAM\_PROPERTIES  
You can specify SPEED\_FLAGS\_*XXX* flags in the **fulSpeed** member.

**u.IsochModifyStreamProperties.fulSpeed**

Specifies the maximum speed for transactions to the device. The possible speed values are SPEED\_FLAGS\_*XXX*, where *XXX* is the (approximate) transfer rate in mbps.

<a href="" id="request-get-speed-between-devices"></a>[**REQUEST\_GET\_SPEED\_BETWEEN\_DEVICES**](https://msdn.microsoft.com/library/windows/hardware/ff537645)  
You can specify SPEED\_FLAGS\_*XXX* flags in the **fulSpeed** member.

**u.GetMaxSpeedBetweenDevices.fulSpeed**

Specifies the maximum possible transaction speed between the source device and the set of destination devices. The returned value is the maximum speed that all devices support at the same time. The possible speed values are SPEED\_FLAGS\_*XXX*, where *XXX* is the (approximate) transfer rate in mbps.

**Note**  A client driver can also specify the USE\_SCODE\_SPEED flag in **u.GetMaxSpeedBetweenDevices.fulFlags** to request that an SCODE\_*XXX*\_RATE speed code value be returned in **fulSpeed** instead of a SPEED\_FLAGS\_xxx value.

 

## Related topics
[The IEEE 1394 Driver Stack](https://msdn.microsoft.com/library/windows/hardware/ff538867)  
[IEEE 1394 Bus Driver in Windows 7](https://msdn.microsoft.com/library/windows/hardware/gg266402)  



