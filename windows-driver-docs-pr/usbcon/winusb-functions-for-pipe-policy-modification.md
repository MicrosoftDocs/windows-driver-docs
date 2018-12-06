---
Description: Winusb.dll exposes the WinUsb_GetPipePolicy function to retrieve the pipe's default policy.
title: WinUSB Functions for Pipe Policy Modification
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WinUSB Functions for Pipe Policy Modification


To enable applications to get and set an endpoint pipe's default policy parameters, Winusb.dll exposes the [**WinUsb\_GetPipePolicy**](https://msdn.microsoft.com/library/windows/hardware/ff540266) function to retrieve the pipe's default policy. The [**WinUsb\_SetPipePolicy**](https://msdn.microsoft.com/library/windows/hardware/ff540304) function allows an application to set the policy parameter to a new value.

WinUSB allows you to modify its default behavior by applying policies to an endpoint's pipe. By using these policies, you can configure WinUSB to best match your device to its capabilities. The following table provides a list of the pipe policies that are supported by WinUSB.

**Note**  The policies described in the table are valid only for the specified endpoints. Setting the policy on other endpoints has no effect on WinUSB's behavior for read or write requests.

 

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
<th>Policy number</th>
<th>Policy name</th>
<th>Description</th>
<th>Endpoint (direction)</th>
<th>Default value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>0x01</td>
<td>SHORT_PACKET_TERMINATE</td>
<td>Sends a zero length packet for a write request in which the buffer is a multiple of the maximum packet size supported by the endpoint.</td>
<td><p>Bulk (OUT)</p>
<p>Interrupt (OUT)</p></td>
<td>FALSE</td>
</tr>
<tr class="even">
<td>0x02</td>
<td>AUTO_CLEAR_STALL</td>
<td>Automatically clears a stalled pipe without stopping the data flow.</td>
<td><p>Bulk (IN)</p>
<p>Interrupt (IN)</p></td>
<td>FALSE</td>
</tr>
<tr class="odd">
<td>0x03</td>
<td>PIPE_TRANSFER_TIMEOUT</td>
<td>Waits for a time-out interval before canceling the request.</td>
<td><p>Bulk (IN)</p>
<p>Bulk (OUT)</p>
<p>Interrupt (IN)</p>
<p>Interrupt (OUT)</p></td>
<td>5 seconds for control; 0 for others</td>
</tr>
<tr class="even">
<td>0x04</td>
<td>IGNORE_SHORT_PACKETS</td>
<td>Completes a read request when a short packet is received or a certain number of bytes are read. If the file size is unknown, the request is terminated at a short packet.</td>
<td><p>Bulk (IN)</p>
<p>Interrupt (IN)</p></td>
<td>FALSE</td>
</tr>
<tr class="odd">
<td>0x05</td>
<td>ALLOW_PARTIAL_READS</td>
<td>Allows read requests from a device that returns more data than requested by the caller.</td>
<td><p>Bulk (IN)</p>
<p>Interrupt (IN)</p></td>
<td>TRUE</td>
</tr>
<tr class="even">
<td>0x06</td>
<td>AUTO_FLUSH</td>
<td>Saves the excess data from the read request and adds it to the next read request or discards the excess data.</td>
<td><p>Bulk (IN)</p>
<p>Interrupt (IN)</p></td>
<td>FALSE</td>
</tr>
<tr class="odd">
<td>0x07</td>
<td>RAW_IO</td>
<td>Bypasses queuing and error handling to boost performance for multiple read requests.</td>
<td><p>Bulk (IN)</p>
<p>Interrupt (IN)</p></td>
<td>FALSE</td>
</tr>
<tr class="even">
<td>0x08</td>
<td>MAXIMUM_TRANSFER_SIZE</td>
<td>Gets the maximum size of a USB transfer supported by WinUSB. This is a read-only policy that can be retrieved by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff540266" data-raw-source="[&lt;strong&gt;WinUsb_GetPipePolicy&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540266)"><strong>WinUsb_GetPipePolicy</strong></a>.</td>
<td><p>Bulk (IN)</p>
<p>Bulk (OUT)</p>
<p>Interrupt (IN)</p>
<p>Interrupt (OUT)</p></td>
<td></td>
</tr>
<tr class="odd">
<td>0x09</td>
<td>RESET_PIPE_ON_RESUME</td>
<td>Resets the endpoint&#39;s pipe after resuming from suspend before accepting new requests.</td>
<td><p>Bulk (IN)</p>
<p>Bulk (OUT)</p>
<p>Interrupt (IN)</p>
<p>Interrupt (OUT)</p></td>
<td>FALSE</td>
</tr>
</tbody>
</table>

 

The following table identifies best practices for how to use each of the pipe policies and describes the resulting behavior when the policy is enabled.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Policy</th>
<th>Enable if...</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>SHORT_PACKET_TERMINATE(0x01)</td>
<td>The device requires the OUT transfers to be terminated with a zero-length packet. Most devices do not have this requirement.</td>
<td><p>If enabled (policy parameter value is <strong>TRUE</strong> or nonzero), every write request that is a multiple of the maximum packet size supported by the endpoint, is followed by a zero-length packet.</p>
<p>After sending data to the host controller, WinUSB sends a write request with a zero-length packet and then completes the request that was created by <a href="https://msdn.microsoft.com/library/windows/hardware/ff540322" data-raw-source="[&lt;strong&gt;WinUsb_WritePipe&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540322)"><strong>WinUsb_WritePipe</strong></a>.</p></td>
</tr>
<tr class="even">
<td>AUTO_CLEAR_STALL</td>
<td>You do not want the failed transfers to leave the endpoint in a stalled state. This policy is useful only when you have multiple pending read requests to the endpoint when RAW_IO is disabled.</td>
<td><ul>
<li><p>If enabled (policy parameter value is <strong>TRUE</strong> or nonzero), a stall condition is cleared automatically. This policy parameter does not affect control pipes.</p>
<p>When a read request fails and the host controller returns a status other than STATUS_CANCELLED or STATUS_DEVICE_NOT_CONNECTED, WinUSB resets the pipe before completing the failed request. Resetting the pipe clears the stall condition without interrupting the data flow. Data continues to flow in the endpoints as long as new transfers keep arriving from the device. A new transfer can include one that was in the queue when the stall occurred.</p>
<p>Enabling this policy does not significantly impact performance.</p></li>
<li>If disabled (policy parameter value is <strong>FALSE</strong> or zero), all transfers that arrive to the endpoint after the stalled transfer fail until the caller manually resets the endpoint&#39;s pipe by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff540300" data-raw-source="[&lt;strong&gt;WinUsb_ResetPipe&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540300)"><strong>WinUsb_ResetPipe</strong></a>.</li>
</ul></td>
</tr>
<tr class="odd">
<td>PIPE_TRANSFER_TIMEOUT</td>
<td>You expect transfers to an endpoint to complete within a specific time.</td>
<td><ul>
<li>If set to zero (default), transfers will not time out because the host controller will not cancel the transfer. In this case, the transfer waits indefinitely until it is manually canceled or the transfer completes normally.</li>
<li><p>If set to a nonzero value (time-out interval), the host controller starts a timer when it receives the transfer request. When the timer exceeds the set time-out interval, the request is canceled.</p>
<p>A minor performance penalty will occur due to timer management.</p>
<div class="alert">
<strong>Note</strong>  Requests do not time out while waiting in a WinUSB queue.
<p>In Windows Vista, for all transfers (except transfers with RAW_IO enabled), WinUSB queues the request until all previous transfers on the destination endpoint have been completed. The host controller does not include the queuing time in the calculation of the time-out interval.</p>
<p>With RAW_IO enabled, WinUSB does not queue the request. Instead, it passes the request directly to the USB stack, whether the USB stack is busy processing previous transfers. If the USB stack is busy, it can delay processing the new request. Note that this can cause a time-out.</p>
</div>
<div>
 
</div></li>
</ul></td>
</tr>
<tr class="even">
<td>IGNORE_SHORT_PACKETS</td>
<td>RAW_IO is disabled and you do not want short packets to complete the read requests.</td>
<td><ul>
<li>If enabled (policy parameter value is <strong>TRUE</strong> or nonzero), the host controller will not complete a read operation immediately after it receives a short packet. Instead, it completes the operation only if:
<ul>
<li>An error occurs.</li>
<li>The request is canceled.</li>
<li>All the requested bytes have been received.</li>
</ul></li>
<li>If disabled (policy parameter value is <strong>FALSE</strong> or zero), the host controller completes a read operation after it has read the requested number of bytes or has received a short packet.</li>
</ul></td>
</tr>
<tr class="odd">
<td>ALLOW_PARTIAL_READS</td>
<td>The device can send more data than requested. This is possible if the size of your request buffer is a multiple of the maximum endpoint packet size.
<p>Use if your application wants to read a few bytes to determine how many total bytes to read.</p></td>
<td><ul>
<li>If disabled (policy parameter value is <strong>FALSE</strong> or zero) and the device returns more data than was requested, WinUSB completes the request with an error.</li>
<li><p>If enabled (policy parameter value is <strong>TRUE</strong> or nonzero) and the device returns more data than was requested, WinUSB can (depending on AUTO_FLUSH settings) add the excess data from the read request to the beginning of the next read request or discard the excess data.</p>
<p>If enabled, WinUSB immediately completes read requests for zero bytes successfully and will not send the requests down the stack.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>AUTO_FLUSH</td>
<td>ALLOW_PARTIAL _READS policy is enabled.
<p>The device can send more data than was requested, and your application does not require any additional data. This is possible if the size of your request buffer is a multiple of the maximum endpoint packet size.</p></td>
<td><p>AUTO_FLUSH defines WinUSB&#39;s behavior when ALLOW_PARTIAL_READS is enabled. If ALLOW_PARTIAL_READS is disabled, the AUTO_FLUSH value is ignored by WinUSB.</p>
<p>WinUSB can either discard the remaining data or send it with the caller&#39;s next read request.</p>
<ul>
<li>If enabled (policy parameter value is <strong>TRUE</strong> or nonzero), WinUSB discards the extra bytes without any error code.</li>
<li>If disabled (policy parameter value is <strong>FALSE</strong> or zero), WinUSB saves the extra bytes, adds them to the beginning of the caller&#39;s next read request, and then sends the data to the caller in the next read operation.</li>
</ul></td>
</tr>
<tr class="odd">
<td>RAW_IO</td>
<td>Performance is a priority and the application submits simultaneous read requests to the same endpoint.
<p>RAW_IO imposes certain restrictions on the buffer that is passed by the caller in <a href="https://msdn.microsoft.com/library/windows/hardware/ff540297" data-raw-source="[&lt;strong&gt;WinUsb_ReadPipe&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540297)"><strong>WinUsb_ReadPipe</strong></a>:</p>
<ul>
<li>The buffer length must be a multiple of the maximum endpoint packet size.</li>
<li>The length must be less than or equal to the value of MAXIMUM_TRANSFER_SIZE retrieved by <a href="https://msdn.microsoft.com/library/windows/hardware/ff540266" data-raw-source="[&lt;strong&gt;WinUsb_GetPipePolicy&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540266)"><strong>WinUsb_GetPipePolicy</strong></a>.</li>
</ul></td>
<td><p>If enabled, transfers bypass queuing and error handling to boost performance for multiple read requests. WinUSB handles read requests as follows:</p>
<ul>
<li>A request that is not a multiple of the maximum endpoint packet size fails.</li>
<li>A request that is greater than the maximum transfer size supported by WinUSB fails.</li>
<li>All well-formed requests are immediately sent down to the USB core stack to be scheduled in the host controller.</li>
</ul>
Enabling this setting significantly improves the performance of multiple read requests by reducing the delay between the last packet of one transfer and the first packet of the next transfer.</td>
</tr>
<tr class="even">
<td>RESET_PIPE_ON_RESUME</td>
<td>The device does not preserve its data toggle state across suspend.</td>
<td>On resume from suspend, WinUSB resets the endpoint before it allows the caller to send new requests to the endpoint.</td>
</tr>
</tbody>
</table>

 

## Related topics
[WinUSB Power Management](winusb-power-management.md)  
[WinUSB Architecture and Modules](winusb-architecture.md)  
[Choosing a driver model for developing a USB client driver](winusb-considerations.md)  
[WinUSB (Winusb.sys) Installation](winusb-installation.md)  
[How to Access a USB Device by Using WinUSB Functions](using-winusb-api-to-communicate-with-a-usb-device.md)  
[WinUSB Functions](https://msdn.microsoft.com/library/windows/hardware/ff540046#winusb)  
[**WinUsb\_GetPipePolicy**](https://msdn.microsoft.com/library/windows/hardware/ff540266)  
[**WinUsb\_SetPipePolicy**](https://msdn.microsoft.com/library/windows/hardware/ff540304)  
[WinUSB](winusb.md)  



