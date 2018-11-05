---
title: Bug Check 0x144 BUGCODE_USB3_DRIVER
description: The BUGCODE_USB3_DRIVER bug check has a value of 0x00000144. This is the code used for all USB 3 bug checks.
ms.assetid: 39414287-3E20-405B-846A-B7F9F8AEE078
keywords: ["Bug Check 0x144 BUGCODE_USB3_DRIVER", "BUGCODE_USB3_DRIVER"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- BUGCODE_USB3_DRIVER
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x144: BUGCODE\_USB3\_DRIVER


The **BUGCODE\_USB3\_DRIVER** bug check has a value of 0x00000144. This is the code used for all USB 3 bug checks. Parameter 1 specifies the type of the USB 3 bug check, and the meanings of the other parameters are dependent on Parameter 1.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## BUGCODE\_USB3\_DRIVER Parameters


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
<th align="left">Parameter 1</th>
<th align="left">Parameter 2</th>
<th align="left">Parameter 3</th>
<th align="left">Parameter 4</th>
<th align="left">Cause of error</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x1</p></td>
<td align="left"><p>Optional. Pointer to the IRP used to resend the URB</p></td>
<td align="left"><p>Pointer to the URB</p></td>
<td align="left"><p>Pointer to the client driver&#39;s device object</p></td>
<td align="left"><p>A client driver used an URB that it had previously sent to the core stack.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x2</p></td>
<td align="left"><p>Pointer to the physical device object (PDO) for the boot device</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A boot or paging device failed re-enumeration.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x3</p></td>
<td align="left"><p>Optional. Pointer to the IRP used to send the URB</p></td>
<td align="left"><p>Pointer to the corrupted URB</p></td>
<td align="left"><p>Pointer to the client driver&#39;s device object</p></td>
<td align="left"><p>A client driver sent a corrupted URB to the core stack. This can happen because the client driver did not allocate the URB using <strong>USBD_<em>xxx</em>UrbAllocate</strong> or because the client driver did a buffer underrun for the URB.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x800</p></td>
<td align="left"><p>IRQL at which the Open Static Streams request was sent</p></td>
<td align="left"><p>Pointer to the Open Static Streams IRP</p></td>
<td align="left"><p>Pointer to the client driver&#39;s device object</p></td>
<td align="left"><p>An Open Static Streams request was sent at IRQL &gt; PASSIVE LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x801</p></td>
<td align="left"><p>Pointer to the Open Static Streams IRP</p></td>
<td align="left"><p>Pointer to the Open Static Streams URB</p></td>
<td align="left"><p>Pointer to the client driver&#39;s device object</p></td>
<td align="left"><p>A client driver attempted to open static streams before querying for streams capability. A client driver cannot open a static stream until after it successfully queries for the streams capability. For more information, see Remarks.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x802</p></td>
<td align="left"><p>Number of static streams that the client driver tried to open</p></td>
<td align="left"><p>Number of static streams that were granted to the client driver</p></td>
<td align="left"><p>Pointer to the client driver&#39;s device object</p></td>
<td align="left"><p>A Client driver tried to open an invalid number of static streams. The number of streams cannot be 0 and cannot be greater than the value returned to the client driver in the query USB capability call.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x803</p></td>
<td align="left"><p>Pointer to the Open Static Streams IRP</p></td>
<td align="left"><p>Pointer to the Open Static Streams URB</p></td>
<td align="left"><p>Pointer to the client driver&#39;s device object</p></td>
<td align="left"><p>A client driver attempted to open static streams for an endpoint that already had static streams open. Before opening static streams, the client driver must close the previously opened static streams.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x804</p></td>
<td align="left"><p>The leaked handle context. Run <strong>!usbanalyze -v</strong> to get information about the leaked handle and URBs. You must enable Driver Verifier for the client driver.</p></td>
<td align="left"><p>Device object passed to <strong><a href="https://msdn.microsoft.com/library/windows/hardware/hh406241" data-raw-source="[USBD_CreateHandle](https://msdn.microsoft.com/library/windows/hardware/hh406241)">USBD_CreateHandle</a></strong>.</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A client driver forgot to close a handle it created earlier using <strong><a href="https://msdn.microsoft.com/library/windows/hardware/hh406241" data-raw-source="[USBD_CreateHandle](https://msdn.microsoft.com/library/windows/hardware/hh406241)">USBD_CreateHandle</a></strong> or forgot to free an URB it allocated.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x805</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff542962" data-raw-source="[WDFREQUEST](https://msdn.microsoft.com/library/windows/hardware/ff542962)">WDFREQUEST</a> handle for the Close Static Streams URB</p></td>
<td align="left"><p>Pointer to the Close Static Streams URB</p></td>
<td align="left"><p>Pointer to the client driver&#39;s device object</p></td>
<td align="left"><p>A client driver sent a Close Static Streams URB in an invalid state (for example, after processing D0 Exit).</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x806</p></td>
<td align="left"><p>Pointer to the IRP</p></td>
<td align="left"><p>Pointer to the URB</p></td>
<td align="left"><p>Pointer to the client driver&#39;s device object</p></td>
<td align="left"><p>A client driver attempted to send a chained <strong><a href="https://msdn.microsoft.com/library/windows/hardware/ff554414" data-raw-source="[MDL](https://msdn.microsoft.com/library/windows/hardware/ff554414)">MDL</a></strong> before querying for chained <strong>MDL</strong> capability. A client driver cannot send a chained <strong>MDL</strong> until after it successfully queries for the chained <strong>MDL</strong> capability. For more information, see Remarks.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x807</p></td>
<td align="left"><p>Pointer to the chained <strong><a href="https://msdn.microsoft.com/library/windows/hardware/ff554414" data-raw-source="[MDL](https://msdn.microsoft.com/library/windows/hardware/ff554414)">MDL</a></strong></p></td>
<td align="left"><p>Pointer to the URB</p></td>
<td align="left"><p>Pointer to the client driver&#39;s device object if available</p></td>
<td align="left"><p>A client driver sent an URB to the core stack with a transfer buffer length longer than the byte count (returned by <strong><a href="https://msdn.microsoft.com/library/windows/hardware/ff554530" data-raw-source="[MmGetMdlByteCount](https://msdn.microsoft.com/library/windows/hardware/ff554530)">MmGetMdlByteCount</a></strong>) of the <strong><a href="https://msdn.microsoft.com/library/windows/hardware/ff554414" data-raw-source="[MDL](https://msdn.microsoft.com/library/windows/hardware/ff554414)">MDL</a></strong> passed in. For more information, see Remarks.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1001</p></td>
<td align="left"><p>XHCI_LIVEDUMP_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The xHCI controller asserted the HSE bit, which indicates a host system error.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x1002</p></td>
<td align="left"><p>XHCI_LIVEDUMP_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The xHCI controller asserted the HCE bit, which indicates a host controller error.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1003</p></td>
<td align="left"><p>XHCI_LIVEDUMP_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The xHCI stop endpoint command returned an unhandled completion code.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x1004</p></td>
<td align="left"><p>XHCI_LIVEDUMP_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The xHCI endpoint state received a context state error after an xHCI endpoint stop command was issued.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1005</p></td>
<td align="left"><p>XHCI_LIVEDUMP_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Set dequeue pointer failed during an attempt to clear stall on control endpoint.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x1006</p></td>
<td align="left"><p>XHCI_LIVEDUMP_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reset EP failed during an attempt to clear stall on control endpoint.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1007</p></td>
<td align="left"><p>XHCI_LIVEDUMP_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The reset of the xHCI controller failed during reset recovery.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x1008</p></td>
<td align="left"><p>XHCI_LIVEDUMP_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The restart of the xHCI controller failed during reset recovery.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1009</p></td>
<td align="left"><p>XHCI_LIVEDUMP_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>An xHCI controller command failed to complete after the command timeout abort.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x100A</p></td>
<td align="left"><p>XHCI_LIVEDUMP_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Set dequeue pointer failed during an attempt to set the dequeue pointer after endpoint stop completion.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x100B</p></td>
<td align="left"><p>XHCI_LIVEDUMP_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The stop of the xHCI controller failed during reset recovery.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x100C</p></td>
<td align="left"><p>XHCI_LIVEDUMP_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The firmware in the xHCI controller is not supported. The xHCI driver will not load on this controller unless the firmware is updated.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x100D</p></td>
<td align="left"><p>XHCI_LIVEDUMP_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The controller was detected to be physically removed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x100E</p></td>
<td align="left"><p>XHCI_LIVEDUMP_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The driver detect an error on a stream enabled endpoint.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x100F</p></td>
<td align="left"><p>XHCI_LIVEDUMP_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The firmware in the xHCI controller is outdated. The xHCI driver will continue working with this controller but may run into some issues. A firmware update is recommended.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x1010</p></td>
<td align="left"><p>XHCI_LIVEDUMP_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A transfer event TRB completed with an unhandled completion code.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1011</p></td>
<td align="left"><p>XHCI_LIVEDUMP_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The controller reported that the event ring became full. The controller is also known to drop events when this happens.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x1012</p></td>
<td align="left"><p>XHCI_LIVEDUMP_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The controller completed a command out of order.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1013</p></td>
<td align="left"><p>XHCI_LIVEDUMP_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>After command abort completion, the command ring dequeue pointer reported by the controller is incorrect.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x1014</p></td>
<td align="left"><p>XHCI_LIVEDUMP_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>After enable slot completion, controller gave us a bad slot id.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1015</p></td>
<td align="left"><p>XHCI_LIVEDUMP_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Controller failed a SetAddress command with BSR1. That is unexpected.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x1016</p></td>
<td align="left"><p>XHCI_LIVEDUMP_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Controller failed to enable a slot during a usbdevice reset. This is unexpected.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1017</p></td>
<td align="left"><p>XHCI_LIVEDUMP_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Controller failed an endpoints configure command where we were deconfiguring the endpoints. That is unexpected.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x1018</p></td>
<td align="left"><p>XHCI_LIVEDUMP_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Controller failed a disable slot command. That is unexpected.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1019</p></td>
<td align="left"><p>XHCI_LIVEDUMP_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Controller failed a USB device reset command. That is unexpected.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x101A</p></td>
<td align="left"><p>XHCI_LIVEDUMP_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>After endpoint reset, Set Dequeue Pointer command failed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x101B</p></td>
<td align="left"><p>XHCI_LIVEDUMP_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The xHCI reset endpoint command returned an unhandled completion code.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x101C</p></td>
<td align="left"><p>XHCI_LIVEDUMP_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The D0Entry for xHCI failed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x101D</p></td>
<td align="left"><p>XHCI_LIVEDUMP_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Temporarily dropping and adding a stream endpoint (as two commands) failed, when using the Configure Endpoint command instead of Set Dequeue Pointer during request cancellation.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x101E</p></td>
<td align="left"><p>XHCI_LIVEDUMP_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The controller indicated a transfer completion that was not pending on the controller. EventData == 1 (dereferencing the Transfer Event TRB&#39;s pointer would have caused a bugcheck)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x101F</p></td>
<td align="left"><p>XHCI_LIVEDUMP_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The controller indicated a transfer completion that was not pending on the controller. EventData == 0 (logical address in transfer event TRB not matched)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x1020</p></td>
<td align="left"><p>XHCI_LIVEDUMP_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The controller indicated a transfer completion that was not pending on the controller. EventData == 0 (logical address in transfer event TRB not matched) The Transfer Event TRB may be redundant (points somewhere near a recently completed request).</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1021</p></td>
<td align="left"><p>XHCI_LIVEDUMP_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Temporarily dropping and adding a stream endpoint (as two commands) failed, when using the Configure Endpoint command as part of resetting an endpoint that was not Halted.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x1022</p></td>
<td align="left"><p>XHCI_LIVEDUMP_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Dropping and adding the same endpoint (as one command) failed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x3000</p></td>
<td align="left"><p>USBHUB3_LIVEDUMP_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A misbehaving hub was successfully reset by the hub driver.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x3001</p></td>
<td align="left"><p>USBHUB3_LIVEDUMP_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A misbehaving hub failed to be reset successfully by the hub driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x3002</p></td>
<td align="left"><p>USBHUB3_LIVEDUMP_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A non-function SuperSpeed hub was disabled by the hub driver.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x3003</p></td>
<td align="left"><p>USBHUB3_LIVEDUMP_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A USB device failed enumeration.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

To query for a USB capability, the client driver must call [**WdfUsbTargetDeviceQueryUsbCapability**](https://msdn.microsoft.com/library/windows/hardware/hh439434) or [**USBD\_QueryUsbCapability**](https://msdn.microsoft.com/library/windows/hardware/hh406230)

To send a chained [**MDL**](https://msdn.microsoft.com/library/windows/hardware/ff554414), the client driver must call [**USBD\_QueryUsbCapability**](https://msdn.microsoft.com/library/windows/hardware/hh406230) and use **URB\_FUNCTION\_BULK\_OR\_INTERRUPT\_TRANSFER\_USING\_CHAINED\_MDL** or **URB\_FUNCTION\_ISOCH\_TRANSFER\_USING\_CHAINED\_MDL**.

## <span id="see_also"></span>See also


[Universal Serial Bus (USB)](https://msdn.microsoft.com/library/windows/hardware/ff538930)

 

 




