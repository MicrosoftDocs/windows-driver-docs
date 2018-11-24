---
title: Serial I/O Request Interface
description: To control a peripheral device that is connected to a port on a serial controller, a client application or peripheral device driver sends I/O requests to the port.
ms.assetid: D536A0EC-2B8B-491B-8A14-656F4B5A3843
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh406621" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_APPLY_DEFAULT_CONFIGURATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh406621)"><strong>IOCTL_SERIAL_APPLY_DEFAULT_CONFIGURATION</strong></a></p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>No</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546538" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_CLEAR_STATS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546538)"><strong>IOCTL_SERIAL_CLEAR_STATS</strong></a></p></td>
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546541" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_CLR_DTR&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546541)"><strong>IOCTL_SERIAL_CLR_DTR</strong></a></p></td>
<td><p>See note 1.</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546545" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_CLR_RTS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546545)"><strong>IOCTL_SERIAL_CLR_RTS</strong></a></p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546548" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_CONFIG_SIZE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546548)"><strong>IOCTL_SERIAL_CONFIG_SIZE</strong></a></p></td>
<td><p>No</p></td>
<td><p>No</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546554" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_GET_BAUD_RATE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546554)"><strong>IOCTL_SERIAL_GET_BAUD_RATE</strong></a></p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546558" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_GET_CHARS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546558)"><strong>IOCTL_SERIAL_GET_CHARS</strong></a></p></td>
<td><p>See note 2.</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546562" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_GET_COMMSTATUS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546562)"><strong>IOCTL_SERIAL_GET_COMMSTATUS</strong></a></p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546566" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_GET_DTRRTS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546566)"><strong>IOCTL_SERIAL_GET_DTRRTS</strong></a></p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546574" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_GET_HANDFLOW&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546574)"><strong>IOCTL_SERIAL_GET_HANDFLOW</strong></a></p></td>
<td><p>See note 1.</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546582" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_GET_LINE_CONTROL&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546582)"><strong>IOCTL_SERIAL_GET_LINE_CONTROL</strong></a></p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546591" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_GET_MODEM_CONTROL&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546591)"><strong>IOCTL_SERIAL_GET_MODEM_CONTROL</strong></a> (See note 4.)</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546587" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_GET_MODEMSTATUS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546587)"><strong>IOCTL_SERIAL_GET_MODEMSTATUS</strong></a></p></td>
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546597" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_GET_PROPERTIES&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546597)"><strong>IOCTL_SERIAL_GET_PROPERTIES</strong></a></p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546600" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_GET_STATS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546600)"><strong>IOCTL_SERIAL_GET_STATS</strong></a></p></td>
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546604" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_GET_TIMEOUTS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546604)"><strong>IOCTL_SERIAL_GET_TIMEOUTS</strong></a></p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546610" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_GET_WAIT_MASK&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546610)"><strong>IOCTL_SERIAL_GET_WAIT_MASK</strong></a></p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546620" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_IMMEDIATE_CHAR&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546620)"><strong>IOCTL_SERIAL_IMMEDIATE_CHAR</strong></a></p></td>
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546649" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_LSRMST_INSERT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546649)"><strong>IOCTL_SERIAL_LSRMST_INSERT</strong></a></p></td>
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546655" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_PURGE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546655)"><strong>IOCTL_SERIAL_PURGE</strong></a></p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546671" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_RESET_DEVICE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546671)"><strong>IOCTL_SERIAL_RESET_DEVICE</strong></a> (See note 5.)</p></td>
<td><p>No</p></td>
<td><p>No</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546672" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_SET_BAUD_RATE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546672)"><strong>IOCTL_SERIAL_SET_BAUD_RATE</strong></a></p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546680" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_SET_BREAK_OFF&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546680)"><strong>IOCTL_SERIAL_SET_BREAK_OFF</strong></a></p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546685" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_SET_BREAK_ON&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546685)"><strong>IOCTL_SERIAL_SET_BREAK_ON</strong></a></p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546688" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_SET_CHARS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546688)"><strong>IOCTL_SERIAL_SET_CHARS</strong></a></p></td>
<td><p>See note 2.</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546696" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_SET_DTR&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546696)"><strong>IOCTL_SERIAL_SET_DTR</strong></a></p></td>
<td><p>See note 1.</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546720" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_SET_FIFO_CONTROL&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546720)"><strong>IOCTL_SERIAL_SET_FIFO_CONTROL</strong></a></p></td>
<td><p>See note 1.</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546736" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_SET_HANDFLOW&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546736)"><strong>IOCTL_SERIAL_SET_HANDFLOW</strong></a> (See note 3.)</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546740" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_SET_LINE_CONTROL&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546740)"><strong>IOCTL_SERIAL_SET_LINE_CONTROL</strong></a></p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546748" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_SET_MODEM_CONTROL&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546748)"><strong>IOCTL_SERIAL_SET_MODEM_CONTROL</strong></a> (See note 4.)</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546754" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_SET_QUEUE_SIZE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546754)"><strong>IOCTL_SERIAL_SET_QUEUE_SIZE</strong></a></p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546760" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_SET_RTS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546760)"><strong>IOCTL_SERIAL_SET_RTS</strong></a></p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546772" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_SET_TIMEOUTS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546772)"><strong>IOCTL_SERIAL_SET_TIMEOUTS</strong></a></p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546780" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_SET_WAIT_MASK&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546780)"><strong>IOCTL_SERIAL_SET_WAIT_MASK</strong></a></p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546784" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_SET_XOFF&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546784)"><strong>IOCTL_SERIAL_SET_XOFF</strong></a></p></td>
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546793" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_SET_XON&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546793)"><strong>IOCTL_SERIAL_SET_XON</strong></a></p></td>
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546805" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_WAIT_ON_MASK&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546805)"><strong>IOCTL_SERIAL_WAIT_ON_MASK</strong></a></p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546812" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_XOFF_COUNTER&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546812)"><strong>IOCTL_SERIAL_XOFF_COUNTER</strong></a></p></td>
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

 

 




