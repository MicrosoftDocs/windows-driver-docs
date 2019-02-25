---
Description: This section provides guidance concerning the careful management of USB bandwidth.
title: USB Bandwidth Allocation
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# USB Bandwidth Allocation


This section provides guidance concerning the careful management of USB bandwidth.

It is the responsibility of every USB client driver to minimize the USB bandwidth it uses, and return unused bandwidth to the free bandwidth pool as promptly as possible.

This section includes the following topics:

## Why is my USB driver getting out of bandwidth errors?


Competition for bandwidth on the USB bus comes from multiple sources, both hardware and software, so it is difficult to predict exactly how much bandwidth will be available for a USB client driver. The USB host controller requires a certain amount of bandwidth for its operations, but the amount required depends on whether the controller is high speed or not, so it will vary from system to system. USB hubs that operate at high speed must sometimes translate transactions between high-speed upstream ports and low-speed devices downstream, and this translation process consumes bandwidth. But whether bandwidth is required for transaction translation depends on the kind of devices that are connected and the topology of the device tree.

The most serious strain on bandwidth resource usually comes from USB client drivers that monopolize bandwidth. The system allocates bandwidth on a first-come-first-serve basis. If the first USB driver loaded requests all of the available bandwidth, a USB driver that loads at a later time will not obtain any bandwidth at all for its device. When this occurs, the system cannot configure the device and fails to enumerate it. Since it is usually not apparent why the enumeration failed, this can lead to a bad user experience.

Occasionally, a client driver will exhaust the available bandwidth with a high-speed interrupt transfer. But the most common case, by far, is that of a client driver that allocates too much bandwidth for an isochronous transfer, then fails to release the bandwidth in a timely fashion. The system reserves allocated bandwidth until the driver that requested it closes its endpoint (by opening another endpoint), or the device for which the bandwidth was allocated is removed. The system does not allocate guaranteed bandwidth for bulk transfers, so bulk transfers are never the cause of enumeration failures. However, the performance of bulk transfer devices depends on how much bandwidth is allocated for devices that do periodic (isochronous and interrupt) transfers.

The USB 2.0 specification requires an isochronous device to have zero-bandwidth endpoints on its default interface setting. This ensures that no bandwidth is reserved for the device until a function driver opens a non-default interface, which, in turn, helps prevent enumeration failures caused by excessive bandwidth requests during device configuration. However, it does not prevent a client driver from allocating too much bandwidth after configuring its device, thereby preventing other devices from functioning properly.

The key to proper bandwidth management is that every USB device in the system that does isochronous transfers must offer multiple alternative (Alt) settings for each interface that contains isochronous endpoints, and client drivers must make judicious use of these Alt settings. Client drivers should begin by requesting the interface setting with the highest bandwidth. If the request fails, the client driver should request interface settings with smaller and smaller bandwidths until a request succeeds.

For instance, suppose a webcam device has the following interfaces:

Interface 0 (Default interface setting: No endpoints with nonzero isochronous bandwidth in the default setting)

Isochronous Endpoint 1: maximum packet size = 0 bytes

Isochronous Endpoint 2: maximum packet size = 0 bytes

Interface 0 Alt setting 1

Isochronous Endpoint 1: maximum packet size = 256 bytes

Isochronous Endpoint 2: maximum packet size = 256 bytes

Interface 0 Alt setting 2

Isochronous Endpoint 1: maximum packet size = 512 bytes

Isochronous Endpoint 2: maximum packet size = 512 bytes

The driver for the webcam configures the webcam to use the default interface setting when it initializes. The default setting has no isochronous bandwidth, so using the default setting during initialization avoids the danger that the webcam might fail to enumerate, because of a failed request for isochronous bandwidth.

When the client driver is ready to do an isochronous transfer, it should attempt to use Alt setting 2, because Alt setting 2 has the largest packet size. If the request fails, the driver can make a second attempt, using Alt setting 1. Since Alt setting 1 requires less bandwidth, this request might succeed, even though the first request failed. Multiple Alt settings allow the driver to make several attempts, before giving up.

After the webcam becomes idle, it can return the allocated bandwidth to the free bandwidth pool by selecting the default setting once again.

Starting with Windows Vista, users can see how much bandwidth a USB controller has allocated by checking the controller's properties in the Device Manager. Select the controller's properties then look under the Advanced tab. This reading does not indicate how much bandwidth USB hubs have allocated for transaction translation.

The Device Manager feature that reports the bandwidth usage of a USB controller does not work properly in Windows XP.

 
## USB Transfer and Packet Sizes


This topic describes USB transfer sizes allowed in various versions of the Windows operating system.

-   [Maximum transfer size](#maximum-transfer-size)
-   [Maximum packet size](#maximum-packet-size)
-   [Maximum packet size restriction on read transfer buffers](#maximum-packet-size-restriction-on-read-transfer-buffers)
-   [Delimiting write transfers with short packets](#delimiting-write-transfers-with-short-packets)

### Maximum transfer size


The *maximum transfer size* specifies hard-coded limits in the USB driver stack. It is possible that transfer sizes below these limits will fail because of system resource limitations. To avoid these types of failures and to ensure compatibility across all versions of Windows, avoid using large transfer sizes for USB transfers.

> **Note**  
>
> In Windows XP, Windows Server 2003, and later versions, **MaximumTransferSize** member of the [**USBD\_PIPE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff539114) structure is obsolete. The USB driver stack ignores the value in **MaximumTransferSize** for both composite and non-composite devices.
>
> In Windows 2000, the USB driver stack initializes **MaximumTransferSize** to USBD\_DEFAULT\_MAXIMUM\_TRANSFER\_SIZE. A client driver can set a smaller value while configuring the device. For a composite device, the client driver for each function can only change **MaximumTransferSize** for pipes in the non-default interface setting.

USB transfer sizes are subject to the following limits:

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Transfer pipe</th>
<th>Windows 8.1, Windows 8</th>
<th>Windows 7, Windows Vista</th>
<th>Windows XP, Windows Server 2003</th>
<th>Windows 2000</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Control</td>
<td><p>64K for SuperSpeed and high speed (xHCI)</p>
<p>4K for full and low speed (xHCI, EHCI, UHCI, OHCI)</p>
<p>For UHCI, 4K on the default endpoint; 64K on non-default control pipes</p></td>
<td><p>64K for high speed (EHCI)</p>
<p>4K for full and low speed (EHCI, UHCI, OHCI)</p>
<p>For UHCI, 4K on the default endpoint; 64K on non-default control pipes (UHCI)</p></td>
<td><p>64K for high speed (EHCI)</p>
<p>4K for full and low speed (EHCI, UHCI, OHCI)</p>
<p>For UHCI, 4K on the default endpoint; 64K on non-default control pipes (UHCI)</p></td>
<td><p>4K on the default endpoint; 64K on non-default control pipes (OHCI)</p></td>
</tr>
<tr class="even">
<td>Interrupt</td>
<td><p>4MB for SuperSpeed, high, full, and low speed (xHCI, EHCI, UHCI, OHCI)</p></td>
<td><p>4MB for high, full, and low speed (EHCI, UHCI, OHCI)</p></td>
<td>Unlimited</td>
<td><p>Undetermined(OHCI)</p></td>
</tr>
<tr class="odd">
<td>Bulk</td>
<td><p>32MB for SuperSpeed (xHCI)</p>
<p>4MB for high and full speed (xHCI)</p>
<p>4MB for high and full speed (EHCI and UHCI)</p>
<p>256K full speed (OHCI)</p></td>
<td><p>4MB for high and full speed (EHCI, UHCI)</p>
<p>256K for full speed (OHCI)</p></td>
<td><p>3MB for high and full speed (EHCI)</p>
<p>Undetermined (UHCI)</p>
<p>256K for full speed (OHCI)</p></td>
<td><p>Undetermined(OHCI)</p></td>
</tr>
<tr class="even">
<td>Isochronous</td>
<td><p>1024<em><strong>wBytesPerInterval</strong> (see <a href="https://msdn.microsoft.com/library/windows/hardware/hh406269" data-raw-source="[&lt;strong&gt;USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh406269)"><strong>USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR</strong></a>) for SuperSpeed (xHCI)</p>
<p>1024</em> <strong>MaximumPacketSize</strong> for high speed (xHCI, EHCI)</p>
<p>256 * <strong>MaximumPacketSize</strong> for full speed (xHCI, EHCI)</p>
<p>64K for full speed (UHCI, OHCI)</p></td>
<td><p>1024* <strong>MaximumPacketSize</strong> for high speed (EHCI)</p>
<p>256 * <strong>MaximumPacketSize</strong> for full-speed (EHCI)</p>
<p>64K for full speed (UHCI, OHCI)</p></td>
<td><p>1024* <strong>MaximumPacketSize</strong> for high-speed (EHCI)</p>
<p>256 * <strong>MaximumPacketSize</strong> for full speed (EHCI)</p>
<p>64K for full speed (UHCI, OHCI)</p></td>
<td><p>64K for full speed (OHCI)</p></td>
</tr>
</tbody>
</table>

 

Restricting the transfer size with **MaximumTransferSize** does not directly affect how much bandwidth a device consumes. The client driver must either change the interface setting or restrict the maximum packet size set in the **MaximumPacketSize** member of [**USBD\_PIPE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff539114).

### Maximum packet size


The *maximum packet size* is defined by the **wMaxPacketSize** field of the endpoint descriptor. A client driver can regulate the USB packet size in a select-interface request to the device. Changing this value does not change the **wMaxPacketSize** on the device.

In the [**URB**](https://msdn.microsoft.com/library/windows/hardware/ff538923) for the request is a [**USBD\_PIPE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff539114) structure for the pipe. In that structure,

-   Modify the **MaximumPacketSize** member of the [**USBD\_PIPE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff539114) structure. Set it to a value less than or equal to the value of **wMaxPacketSize** defined in device firmware for the current interface setting.
-   Set the USBD\_PF\_CHANGE\_MAX\_PACKET flag in the **PipeFlags** member [**USBD\_PIPE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff539114) structure.

For information about selecting an interface setting, see [How to Select a Configuration for a USB Device](how-to-select-a-configuration-for-a-usb-device.md).

### Maximum packet size restriction on read transfer buffers


When a client driver makes a read request, the transfer buffer must be a multiple of the maximum packet size. Even when the driver expects data less than the maximum packet size, it must still request the entire packet. When the device sends a packet less than the maximum size (a short packet), it's an indication that the transfer is complete.

**Note**  

On older controllers, the client driver can override the behavior. In the **TransferFlags** member of the data transfer [**URB**](https://msdn.microsoft.com/library/windows/hardware/ff538923), the client driver must set the USBD\_SHORT\_TRANSFER\_OK flag. That flag permits the device to send packets smaller than **wMaxPacketSize**.

On xHCI host controllers, USBD\_SHORT\_TRANSFER\_OK ignored for bulk and interrupt endpoints. Transfer of short packets on EHCI controllers does not result in an error condition.

On EHCI host controllers, USBD\_SHORT\_TRANSFER\_OK is ignored for bulk and interrupt endpoints.

On UHCI and OHCI host controllers, if USBD\_SHORT\_TRANSFER\_OK is not set for a bulk or interrupt transfer, a short packet transfer halts the endpoint and an error code is returned for the transfer.

### Delimiting write transfers with short packets


The USB driver stack driver does not impose the same restrictions on packet size, when writing to the device, that it imposes when reading from the device. Some client drivers must make frequent transmissions of small quantities of control data to manage their devices. It is impractical to restrict data transmissions to packets of uniform size in such cases. Therefore, the driver stack does not assign any special significance to packets of size less than the endpoint's maximum size during data writes. This allows a client driver to break a large transfer to the device into multiple URBs of any size less than or equal to the maximum.

The driver must either end the transmission by means of a packet of less than maximum size, or delimit the end of the transmission by means of a zero-length packet. The transmission is not complete until the driver sends a packet smaller than *wMaxPacketSize*. If the transfer size is an exact multiple of the maximum, the driver must send a zero-length delimiting packet to explicitly terminate the transfer

Delimiting the data transmission with zero-length packets, as required by the USB specification, is the responsibility of the client driver. The USB driver stack does not generate these packets automatically.

 
## Delimiting USB Data Transfers With Packets Smaller Than wMaxPacketSize


Compliant USB 2.0/1.1 drivers must transmit packets of maximum size (*wMaxPacketSize*) and then either end the transmission by means of a packet of less than maximum size, or delimit the end of the transmission by means of a zero-length packet. The transmission is not complete until the driver sends a packet smaller than *wMaxPacketSize*. If the transfer size is an exact multiple of the maximum, the driver must send a zero-length delimiting packet to explicitly terminate the transfer

Delimiting the data transmission with zero-length packets, as required by the USB specification, is the responsibility of the device driver. The system USB stack will not generate these packets automatically.


 




