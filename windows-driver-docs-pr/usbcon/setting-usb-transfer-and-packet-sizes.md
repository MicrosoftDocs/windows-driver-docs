---
Description: This topic describes USB transfer sizes allowed in various versions of the Windows operating system.
MS-HAID:
- 'usb-io\_e0c77eb5-d512-4fa8-84d1-e53e3306aa06.xml'
- 'buses.setting\_usb\_transfer\_and\_packet\_sizes'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: USB Transfer and Packet Sizes
---

# USB Transfer and Packet Sizes


This topic describes USB transfer sizes allowed in various versions of the Windows operating system.

-   [Maximum transfer size](#maximum-transfer-size)
-   [Maximum packet size](#maximum-packet-size)
-   [Maximum packet size restriction on read transfer buffers](#maximum-packet-size-restriction-on-read-transfer-buffers)
-   [Delimiting write transfers with short packets](#delimiting-write-transfers-with-short-packets)

## Maximum transfer size


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
<td><p>1024*<strong>wBytesPerInterval</strong> (see [<strong>USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR</strong>](https://msdn.microsoft.com/library/windows/hardware/hh406269)) for SuperSpeed (xHCI)</p>
<p>1024* <strong>MaximumPacketSize</strong> for high speed (xHCI, EHCI)</p>
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

## Maximum packet size


The *maximum packet size* is defined by the **wMaxPacketSize** field of the endpoint descriptor. A client driver can regulate the USB packet size in a select-interface request to the device. Changing this value does not change the **wMaxPacketSize** on the device.

In the [**URB**](https://msdn.microsoft.com/library/windows/hardware/ff538923) for the request is a [**USBD\_PIPE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff539114) structure for the pipe. In that structure,

-   Modify the **MaximumPacketSize** member of the [**USBD\_PIPE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff539114) structure. Set it to a value less than or equal to the value of **wMaxPacketSize** defined in device firmware for the current interface setting.
-   Set the USBD\_PF\_CHANGE\_MAX\_PACKET flag in the **PipeFlags** member [**USBD\_PIPE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff539114) structure.

For information about selecting an interface setting, see [How to Select a Configuration for a USB Device](how-to-select-a-configuration-for-a-usb-device.md).

## Maximum packet size restriction on read transfer buffers


When a client driver makes a read request, the transfer buffer must be a multiple of the maximum packet size. Even when the driver expects data less than the maximum packet size, it must still request the entire packet. When the device sends a packet less than the maximum size (a short packet), it's an indication that the transfer is complete.

**Note**  

On older controllers, the client driver can override the behavior. In the **TransferFlags** member of the data transfer [**URB**](https://msdn.microsoft.com/library/windows/hardware/ff538923), the client driver must set the USBD\_SHORT\_TRANSFER\_OK flag. That flag permits the device to send packets smaller than **wMaxPacketSize**.

On xHCI host controllers, USBD\_SHORT\_TRANSFER\_OK ignored for bulk and interrupt endpoints. Transfer of short packets on EHCI controllers does not result in an error condition.

On EHCI host controllers, USBD\_SHORT\_TRANSFER\_OK is ignored for bulk and interrupt endpoints.

On UHCI and OHCI host controllers, if USBD\_SHORT\_TRANSFER\_OK is not set for a bulk or interrupt transfer, a short packet transfer halts the endpoint and an error code is returned for the transfer.

## Delimiting write transfers with short packets


The USB driver stack driver does not impose the same restrictions on packet size, when writing to the device, that it imposes when reading from the device. Some client drivers must make frequent transmissions of small quantities of control data to manage their devices. It is impractical to restrict data transmissions to packets of uniform size in such cases. Therefore, the driver stack does not assign any special significance to packets of size less than the endpoint's maximum size during data writes. This allows a client driver to break a large transfer to the device into multiple URBs of any size less than or equal to the maximum.

The driver must either end the transmission by means of a packet of less than maximum size, or delimit the end of the transmission by means of a zero-length packet. The transmission is not complete until the driver sends a packet smaller than *wMaxPacketSize*. If the transfer size is an exact multiple of the maximum, the driver must send a zero-length delimiting packet to explicitly terminate the transfer

Delimiting the data transmission with zero-length packets, as required by the USB specification, is the responsibility of the client driver. The USB driver stack does not generate these packets automatically.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20USB%20Transfer%20and%20Packet%20Sizes%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")



