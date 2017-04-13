---
title: Serial I/O Request Interface
author: windows-driver-content
description: To control a peripheral device that is connected to a port on a serial controller, a client application or peripheral device driver sends I/O requests to the port.
ms.assetid: D536A0EC-2B8B-491B-8A14-656F4B5A3843
---

# Serial I/O Request Interface


To control a peripheral device that is connected to a port on a serial controller, a client application or peripheral device driver sends I/O requests to the port. A client uses [**IRP\_MJ\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff546904) and [**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff546883) requests to transmit data to and receive data from a serial port. In addition, Windows defines a set of [serial I/O control](https://msdn.microsoft.com/library/windows/hardware/ff547466) requests (IOCTLs) that a client can use to configure a serial port.

The serial **IRP\_MJ\_*XXX*** requests and serial IOCTLs together form a serial I/O request interface that is supported across a range of serial controller devices. This interface is supported by the Serial.sys driver, and by the combination of SerCx2 or SerCx and an extension-based serial controller driver.

SerCx2, SerCx, and Serial.sys support many of the same serial IOCTLs. However, SerCx2, SerCx, and Serial.sys support different subsets of the IOCTLs specified in [Serial Device Control Requests](https://msdn.microsoft.com/library/windows/hardware/ff547466). The following table summarizes the subsets of IOCTLs that are supported by SerCx2, SerCx, and Serial.sys. A **Yes** entry in the table indicates that the serial framework extension or driver supports the corresponding IOCTL, and a **No** entry indicates that it does not.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Serial IOCTL</th>
<th>SerCx2</th>
<th>SerCx</th>
<th>Serial.sys</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>IOCTL_SERIAL_APPLY_DEFAULT_CONFIGURATION</strong>](https://msdn.microsoft.com/library/windows/hardware/hh406621)</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>No</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IOCTL_SERIAL_CLEAR_STATS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546538)</p></td>
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IOCTL_SERIAL_CLR_DTR</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546541)</p></td>
<td><p>See note 1.</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IOCTL_SERIAL_CLR_RTS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546545)</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IOCTL_SERIAL_CONFIG_SIZE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546548)</p></td>
<td><p>No</p></td>
<td><p>No</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IOCTL_SERIAL_GET_BAUD_RATE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546554)</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IOCTL_SERIAL_GET_CHARS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546558)</p></td>
<td><p>See note 2.</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IOCTL_SERIAL_GET_COMMSTATUS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546562)</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IOCTL_SERIAL_GET_DTRRTS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546566)</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IOCTL_SERIAL_GET_HANDFLOW</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546574)</p></td>
<td><p>See note 1.</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IOCTL_SERIAL_GET_LINE_CONTROL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546582)</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IOCTL_SERIAL_GET_MODEM_CONTROL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546591) (See note 4.)</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IOCTL_SERIAL_GET_MODEMSTATUS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546587)</p></td>
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IOCTL_SERIAL_GET_PROPERTIES</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546597)</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IOCTL_SERIAL_GET_STATS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546600)</p></td>
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IOCTL_SERIAL_GET_TIMEOUTS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546604)</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IOCTL_SERIAL_GET_WAIT_MASK</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546610)</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IOCTL_SERIAL_IMMEDIATE_CHAR</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546620)</p></td>
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IOCTL_SERIAL_LSRMST_INSERT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546649)</p></td>
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IOCTL_SERIAL_PURGE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546655)</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IOCTL_SERIAL_RESET_DEVICE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546671) (See note 5.)</p></td>
<td><p>No</p></td>
<td><p>No</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IOCTL_SERIAL_SET_BAUD_RATE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546672)</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IOCTL_SERIAL_SET_BREAK_OFF</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546680)</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IOCTL_SERIAL_SET_BREAK_ON</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546685)</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IOCTL_SERIAL_SET_CHARS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546688)</p></td>
<td><p>See note 2.</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IOCTL_SERIAL_SET_DTR</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546696)</p></td>
<td><p>See note 1.</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IOCTL_SERIAL_SET_FIFO_CONTROL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546720)</p></td>
<td><p>See note 1.</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IOCTL_SERIAL_SET_HANDFLOW</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546736) (See note 3.)</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IOCTL_SERIAL_SET_LINE_CONTROL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546740)</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IOCTL_SERIAL_SET_MODEM_CONTROL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546748) (See note 4.)</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IOCTL_SERIAL_SET_QUEUE_SIZE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546754)</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IOCTL_SERIAL_SET_RTS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546760)</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IOCTL_SERIAL_SET_TIMEOUTS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546772)</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IOCTL_SERIAL_SET_WAIT_MASK</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546780)</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IOCTL_SERIAL_SET_XOFF</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546784)</p></td>
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IOCTL_SERIAL_SET_XON</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546793)</p></td>
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IOCTL_SERIAL_WAIT_ON_MASK</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546805)</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IOCTL_SERIAL_XOFF_COUNTER</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546812)</p></td>
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
</tbody>
</table>

 

**Notes**

1.  SerCx2 may or may not support this IOCTL depending on the implementation of the serial controller driver and the capabilities of the serial controller hardware.

2.  SerCx2 does not support special characters. SerCx2 always completes an **IOCTL\_SERIAL\_SET\_CHARS** request with a STATUS\_SUCCESS status code, but does not set any special characters or perform any other operation in response to this request. For an **IOCTL\_SERIAL\_GET\_CHARS** request, SerCx2 sets all the character values in the [**SERIAL\_CHARS**](https://msdn.microsoft.com/library/windows/hardware/jj673020) structure to null, and completes the request with a STATUS\_SUCCESS status code.

3.  SerCx2 and SerCx support only subsets of the flags defined for the **FlowReplace** and **ControlHandShake** members of the **SERIAL\_HANDFLOW** structure. Serial.sys supports all of these flags. For more information, see [**SERIAL\_HANDFLOW**](https://msdn.microsoft.com/library/windows/hardware/jj680685).

4.  The **IOCTL\_SERIAL\_GET\_MODEM\_CONTROL** and **IOCTL\_SERIAL\_SET\_MODEM\_CONTROL** requests are used primarily for hardware testing. No standard register layout is defined for the modem control operations. Peripheral drivers that use modem control IOCTLs risk making themselves dependent on the hardware features of a particular serial controller.

5.  The Serial.sys driver always completes an **IOCTL\_SERIAL\_RESET\_DEVICE** request with STATUS\_SUCCESS, but performs no operation in response to this request. SerCx2 and SerCx do not support **IOCTL\_SERIAL\_RESET\_DEVICE** requests and always complete these requests with STATUS\_NOT\_IMPLEMENTED.

For more information about **IOCTL\_SERIAL\_*XXX*** requests, see [Serial Device Control Requests](https://msdn.microsoft.com/library/windows/hardware/ff547466). For more information about read and write requests for serial controllers, see [Serial Major I/O Requests](https://msdn.microsoft.com/library/windows/hardware/ff547484).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bserports\serports%5D:%20Serial%20I/O%20Request%20Interface%20%20RELEASE:%20%288/4/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


