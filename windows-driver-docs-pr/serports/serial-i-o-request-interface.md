---
title: Serial I/O Request Interface
description: To control a peripheral device that is connected to a port on a serial controller, a client application or peripheral device driver sends I/O requests to the port.
ms.date: 04/20/2017
---

# Serial I/O Request Interface

To control a peripheral device that is connected to a port on a serial controller, a client application or peripheral device driver sends I/O requests to the port. A client uses [**IRP\_MJ\_WRITE**](/previous-versions/ff546904(v=vs.85)) and [**IRP\_MJ\_READ**](/previous-versions/ff546883(v=vs.85)) requests to transmit data to and receive data from a serial port. In addition, Windows defines a set of serial I/O control requests (IOCTLs) that a client can use to configure a serial port.

The serial **IRP\_MJ\_<em>XXX</em>** requests and serial IOCTLs together form a serial I/O request interface that is supported across a range of serial controller devices. This interface is supported by the Serial.sys driver, and by the combination of SerCx2 or SerCx and an extension-based serial controller driver.

SerCx2, SerCx, and Serial.sys support many of the same serial IOCTLs. However, SerCx2, SerCx, and Serial.sys support different subsets of the IOCTLs specified in *Serial Device Control Requests*. The following table summarizes the subsets of IOCTLs that are supported by SerCx2, SerCx, and Serial.sys. A **Yes** entry in the table indicates that the serial framework extension or driver supports the corresponding IOCTL, and a **No** entry indicates that it does not.

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
<td><p><a href="/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_apply_default_configuration" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_APPLY_DEFAULT_CONFIGURATION&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_apply_default_configuration)"><strong>IOCTL_SERIAL_APPLY_DEFAULT_CONFIGURATION</strong></a></p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>No</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_clear_stats" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_CLEAR_STATS&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_clear_stats)"><strong>IOCTL_SERIAL_CLEAR_STATS</strong></a></p></td>
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_clr_dtr" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_CLR_DTR&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_clr_dtr)"><strong>IOCTL_SERIAL_CLR_DTR</strong></a></p></td>
<td><p>See note 1.</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_clr_rts" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_CLR_RTS&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_clr_rts)"><strong>IOCTL_SERIAL_CLR_RTS</strong></a></p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_config_size" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_CONFIG_SIZE&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_config_size)"><strong>IOCTL_SERIAL_CONFIG_SIZE</strong></a></p></td>
<td><p>No</p></td>
<td><p>No</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_get_baud_rate" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_GET_BAUD_RATE&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_get_baud_rate)"><strong>IOCTL_SERIAL_GET_BAUD_RATE</strong></a></p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_get_chars" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_GET_CHARS&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_get_chars)"><strong>IOCTL_SERIAL_GET_CHARS</strong></a></p></td>
<td><p>See note 2.</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_get_commstatus" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_GET_COMMSTATUS&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_get_commstatus)"><strong>IOCTL_SERIAL_GET_COMMSTATUS</strong></a></p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_get_dtrrts" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_GET_DTRRTS&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_get_dtrrts)"><strong>IOCTL_SERIAL_GET_DTRRTS</strong></a></p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_get_handflow" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_GET_HANDFLOW&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_get_handflow)"><strong>IOCTL_SERIAL_GET_HANDFLOW</strong></a></p></td>
<td><p>See note 1.</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_get_line_control" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_GET_LINE_CONTROL&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_get_line_control)"><strong>IOCTL_SERIAL_GET_LINE_CONTROL</strong></a></p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_get_modem_control" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_GET_MODEM_CONTROL&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_get_modem_control)"><strong>IOCTL_SERIAL_GET_MODEM_CONTROL</strong></a> (See note 4.)</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_get_modemstatus" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_GET_MODEMSTATUS&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_get_modemstatus)"><strong>IOCTL_SERIAL_GET_MODEMSTATUS</strong></a></p></td>
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_get_properties" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_GET_PROPERTIES&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_get_properties)"><strong>IOCTL_SERIAL_GET_PROPERTIES</strong></a></p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_get_stats" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_GET_STATS&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_get_stats)"><strong>IOCTL_SERIAL_GET_STATS</strong></a></p></td>
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_get_timeouts" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_GET_TIMEOUTS&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_get_timeouts)"><strong>IOCTL_SERIAL_GET_TIMEOUTS</strong></a></p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_get_wait_mask" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_GET_WAIT_MASK&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_get_wait_mask)"><strong>IOCTL_SERIAL_GET_WAIT_MASK</strong></a></p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_immediate_char" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_IMMEDIATE_CHAR&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_immediate_char)"><strong>IOCTL_SERIAL_IMMEDIATE_CHAR</strong></a></p></td>
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_lsrmst_insert" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_LSRMST_INSERT&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_lsrmst_insert)"><strong>IOCTL_SERIAL_LSRMST_INSERT</strong></a></p></td>
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_purge" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_PURGE&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_purge)"><strong>IOCTL_SERIAL_PURGE</strong></a></p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_reset_device" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_RESET_DEVICE&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_reset_device)"><strong>IOCTL_SERIAL_RESET_DEVICE</strong></a> (See note 5.)</p></td>
<td><p>No</p></td>
<td><p>No</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_set_baud_rate" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_SET_BAUD_RATE&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_set_baud_rate)"><strong>IOCTL_SERIAL_SET_BAUD_RATE</strong></a></p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_set_break_off" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_SET_BREAK_OFF&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_set_break_off)"><strong>IOCTL_SERIAL_SET_BREAK_OFF</strong></a></p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_set_break_on" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_SET_BREAK_ON&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_set_break_on)"><strong>IOCTL_SERIAL_SET_BREAK_ON</strong></a></p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_set_chars" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_SET_CHARS&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_set_chars)"><strong>IOCTL_SERIAL_SET_CHARS</strong></a></p></td>
<td><p>See note 2.</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_set_dtr" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_SET_DTR&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_set_dtr)"><strong>IOCTL_SERIAL_SET_DTR</strong></a></p></td>
<td><p>See note 1.</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_set_fifo_control" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_SET_FIFO_CONTROL&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_set_fifo_control)"><strong>IOCTL_SERIAL_SET_FIFO_CONTROL</strong></a></p></td>
<td><p>See note 1.</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_set_handflow" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_SET_HANDFLOW&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_set_handflow)"><strong>IOCTL_SERIAL_SET_HANDFLOW</strong></a> (See note 3.)</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_set_line_control" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_SET_LINE_CONTROL&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_set_line_control)"><strong>IOCTL_SERIAL_SET_LINE_CONTROL</strong></a></p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_set_modem_control" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_SET_MODEM_CONTROL&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_set_modem_control)"><strong>IOCTL_SERIAL_SET_MODEM_CONTROL</strong></a> (See note 4.)</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_set_queue_size" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_SET_QUEUE_SIZE&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_set_queue_size)"><strong>IOCTL_SERIAL_SET_QUEUE_SIZE</strong></a></p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_set_rts" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_SET_RTS&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_set_rts)"><strong>IOCTL_SERIAL_SET_RTS</strong></a></p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_set_timeouts" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_SET_TIMEOUTS&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_set_timeouts)"><strong>IOCTL_SERIAL_SET_TIMEOUTS</strong></a></p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_set_wait_mask" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_SET_WAIT_MASK&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_set_wait_mask)"><strong>IOCTL_SERIAL_SET_WAIT_MASK</strong></a></p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_set_xoff" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_SET_XOFF&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_set_xoff)"><strong>IOCTL_SERIAL_SET_XOFF</strong></a></p></td>
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_set_xon" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_SET_XON&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_set_xon)"><strong>IOCTL_SERIAL_SET_XON</strong></a></p></td>
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_wait_on_mask" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_WAIT_ON_MASK&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_wait_on_mask)"><strong>IOCTL_SERIAL_WAIT_ON_MASK</strong></a></p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_xoff_counter" data-raw-source="[&lt;strong&gt;IOCTL_SERIAL_XOFF_COUNTER&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddser/ni-ntddser-ioctl_serial_xoff_counter)"><strong>IOCTL_SERIAL_XOFF_COUNTER</strong></a></p></td>
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
</tbody>
</table>


**Notes**

1. SerCx2 may or may not support this IOCTL depending on the implementation of the serial controller driver and the capabilities of the serial controller hardware.

2. SerCx2 does not support special characters. SerCx2 always completes an **IOCTL\_SERIAL\_SET\_CHARS** request with a STATUS\_SUCCESS status code, but does not set any special characters or perform any other operation in response to this request. For an **IOCTL\_SERIAL\_GET\_CHARS** request, SerCx2 sets all the character values in the [**SERIAL\_CHARS**](/windows-hardware/drivers/ddi/ntddser/ns-ntddser-_serial_chars) structure to null, and completes the request with a STATUS\_SUCCESS status code.

3. SerCx2 and SerCx support only subsets of the flags defined for the **FlowReplace** and **ControlHandShake** members of the **SERIAL\_HANDFLOW** structure. Serial.sys supports all of these flags. For more information, see [**SERIAL\_HANDFLOW**](/windows-hardware/drivers/ddi/ntddser/ns-ntddser-_serial_handflow).

4. The **IOCTL\_SERIAL\_GET\_MODEM\_CONTROL** and **IOCTL\_SERIAL\_SET\_MODEM\_CONTROL** requests are used primarily for hardware testing. No standard register layout is defined for the modem control operations. Peripheral drivers that use modem control IOCTLs risk making themselves dependent on the hardware features of a particular serial controller.

5. The Serial.sys driver always completes an **IOCTL\_SERIAL\_RESET\_DEVICE** request with STATUS\_SUCCESS, but performs no operation in response to this request. SerCx2 and SerCx do not support **IOCTL\_SERIAL\_RESET\_DEVICE** requests and always complete these requests with STATUS\_NOT\_IMPLEMENTED.

For more information about **IOCTL\_SERIAL\_<em>XXX</em>** requests and read and write requests for serial controllers, see the [ntddser.h](/windows-hardware/drivers/ddi/ntddser/) header.
