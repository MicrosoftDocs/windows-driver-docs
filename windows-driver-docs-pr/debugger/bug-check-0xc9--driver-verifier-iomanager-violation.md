---
title: Bug Check 0xC9 DRIVER_VERIFIER_IOMANAGER_VIOLATION
description: The DRIVER_VERIFIER_IOMANAGER_VIOLATION bug check has a value of 0x000000C9. This is the bug check code for all Driver Verifier I/O Verification violations.
ms.assetid: dcafb0df-cbc1-44f4-8ec4-976df0842f0c
keywords: ["Bug Check 0xC9 DRIVER_VERIFIER_IOMANAGER_VIOLATION", "DRIVER_VERIFIER_IOMANAGER_VIOLATION"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- DRIVER_VERIFIER_IOMANAGER_VIOLATION
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xC9: DRIVER\_VERIFIER\_IOMANAGER\_VIOLATION


The DRIVER\_VERIFIER\_IOMANAGER\_VIOLATION bug check has a value of 0x000000C9. This is the bug check code for all Driver Verifier **I/O Verification** violations.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## DRIVER\_VERIFIER\_IOMANAGER\_VIOLATION Parameters


When Driver Verifier is active and **I/O Verification** is selected, various I/O violations will cause this bug check to be issued. Parameter 1 identifies the type of violation.

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
<th align="left">Cause of Error</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x01</p></td>
<td align="left"><p>Address of IRP being freed</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The driver attempted to free an object whose type is not IO_TYPE_IRP.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x02</p></td>
<td align="left"><p>Address of IRP being freed</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The driver attempted to free an IRP that is still associated with a thread.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x03</p></td>
<td align="left"><p>Address of IRP being sent</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The driver passed <strong>IoCallDriver</strong> an IRP Type not equal to IRP_TYPE.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x04</p></td>
<td align="left"><p>Address of device object</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The driver passed <strong>IoCallDriver</strong> an invalid device object.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x05</p></td>
<td align="left"><p>Address of device object associated with offending driver</p></td>
<td align="left"><p>IRQL before <strong>IoCallDriver</strong></p></td>
<td align="left"><p>IRQL after <strong>IoCallDriver</strong></p></td>
<td align="left"><p>The IRQL changed during a call to the driver dispatch routine.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x06</p></td>
<td align="left"><p>IRP status</p></td>
<td align="left"><p>Address of IRP being completed</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The driver called <strong>IoCompleteRequest</strong> with a status marked as pending (or equal to -1).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x07</p></td>
<td align="left"><p>Address of cancel routine</p></td>
<td align="left"><p>Address of IRP being completed</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The driver called <strong>IoCompleteRequest</strong> while its cancel routine was still set.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x08</p></td>
<td align="left"><p>Address of device object</p></td>
<td align="left"><p>IRP major function code</p></td>
<td align="left"><p>Exception status code</p></td>
<td align="left"><p>The driver passed <strong>IoBuildAsynchronousFsdRequest</strong> an invalid buffer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x09</p></td>
<td align="left"><p>Address of device object</p></td>
<td align="left"><p>I/O control code</p></td>
<td align="left"><p>Exception status code</p></td>
<td align="left"><p>The driver passed <strong>IoBuildDeviceIoControlRequest</strong> an invalid buffer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x10</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>IoCallDriver was called above DISPATCH_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x11</p></td>
<td align="left"><p>Driver fast I/O dispatch routine address</p></td>
<td align="left"><p>IRQL before calling driver dispatch routine</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>IoCallDriver was called above DISPATCH_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x12</p></td>
<td align="left"><p>Driver dispatch routine address</p></td>
<td align="left"><p>IRQL before calling driver dispatch routine</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>IoCallDriver was called above DISPATCH_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0A</p></td>
<td align="left"><p>Address of device object</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The driver passed <strong>IoInitializeTimer</strong> a device object with an already-initialized timer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0C</p></td>
<td align="left"><p>Address of I/O status block</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The driver passed an I/O status block to an IRP, but this block is allocated on a stack which has already unwound past that point.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0D</p></td>
<td align="left"><p>Address of user event object</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The driver passed a user event to an IRP, but this event is allocated on a stack which has already unwound past that point.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0E</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>Address of IRP</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The driver called <strong>IoCompleteRequest</strong> with IRQL &gt; DISPATCH_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0F</p></td>
<td align="left"><p>Address of the device object to which the IRP is being sent</p></td>
<td align="left"><p>Pointer to the IRP</p></td>
<td align="left"><p>Pointer to file object</p></td>
<td align="left"><p>The driver sent a create request with a file object that has been closed, or that had its open canceled.</p></td>
</tr>
</tbody>
</table>

 

In addition to the errors mentioned in the previous table, there are a number of **I/O Verification** errors that will cause Driver Verifier to halt the system, but which are not actually bug checks.

These errors cause messages to be displayed on the blue screen, in a crash dump file, and in a kernel debugger. These messages will appear differently in each of these locations. When these errors occur, the hexadecimal bug check code 0xC9 and the bug check string DRIVER\_VERIFIER\_IOMANAGER\_VIOLATION do not appear on the blue screen or in the debugger, although they will appear in a crash dump file.

On the blue screen, the following data will be displayed:

-   The message **IO SYSTEM VERIFICATION ERROR**.

-   The message **WDM DRIVER ERROR** *XXX*, where *XXX* is a hexadecimal code representing the specific error. (See the table below for a list of the I/O error codes and their meanings.)

-   The name of the driver which caused the error.

-   The address in the driver's code where the error was detected (Parameter 2).

-   A pointer to the IRP (Parameter 3).

-   A pointer to the device object (Parameter 4).

If a kernel-mode crash dump has been enabled, the following information will appear in the crash dump file:

-   The message **BugCheck 0xC9 (DRIVER\_VERIFIER\_IOMANAGER\_VIOLATION)**.

-   The hexadecimal I/O error code. (See the table below for a list of the I/O error codes and their meanings.)

-   The address in the driver's code where the error was detected.

-   A pointer to the IRP.

-   A pointer to the device object.

If a kernel debugger is attached to the system which has caused this violation, the following information will be sent to the debugger:

-   The message **WDM DRIVER ERROR**, along with an assessment of the severity of the error.

-   The name of the driver which caused the error.

-   A descriptive string which explains the cause of this error. Often additional information is passed along, such as a pointer to the IRP. (See the table below for a list of these descriptive strings and what additional information is specified.)

-   A query for further action. Possible responses are **b** (break), **i** (ignore), **z** (zap), **r** (remove), or **d** (disable). Instructing the operating system to continue allows you to see what would happen "down the line" if this error had not occurred. Of course, this often will lead to additional bug checks. The "zap" option will actually remove the breakpoint that caused this error to be discovered.

**Note**   No other bug checks can be ignored in this manner. Only this kind of **I/O Verification** errors can be ignored, and even these errors can only be ignored if a kernel debugger is attached.

 

The following table lists those **I/O Verification** errors that can appear.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">I/O Error Code</th>
<th align="left">Severity</th>
<th align="left">Cause of Error</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x200</p></td>
<td align="left"><p>Unknown</p></td>
<td align="left"><p>This code covers all unknown <strong>I/O Verification</strong> errors.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x201</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>A device is deleting itself while there is another device beneath it in the driver stack. This may be because the caller has forgotten to call <strong>IoDetachDevice</strong> first, or the lower driver may have incorrectly deleted itself.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x202</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>A driver has attempted to detach from a device object that is not attached to anything. This may occur if detach was called twice on the same device object. (Device object specified.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x203</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>A driver has called <strong>IoCallDriver</strong> without setting the cancel routine in the IRP to <strong>NULL</strong>. (IRP specified.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x204</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>The caller has passed in <strong>NULL</strong> as a device object. This is fatal. (IRP specified.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x205</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>The caller is forwarding an IRP that is currently queued beneath it. The code handling IRPs returning STATUS_PENDING in this driver appears to be broken. (IRP specified.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x206</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>The caller has incorrectly forwarded an IRP (control field not zeroed). The driver should use <strong>IoCopyCurrentIrpStackLocationToNext</strong> or <strong>IoSkipCurrentIrpStackLocation</strong>. (IRP specified.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x207</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>The caller has manually copied the stack and has inadvertently copied the upper layer&#39;s completion routine. The driver should use <strong>IoCopyCurrentIrpStackLocationToNext</strong>. (IRP specified.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x208</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>This IRP is about to run out of stack locations. Someone may have forwarded this IRP from another stack. (IRP specified.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x209</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>The caller is completing an IRP that is currently queued beneath it. The code handling IRPs returning STATUS_PENDING in this driver appears to be broken. (IRP specified.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x20A</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>The caller of <strong>IoFreeIrp</strong> is freeing an IRP that is still in use. (Original IRP and IRP in use specified.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x20B</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>The caller of <strong>IoFreeIrp</strong> is freeing an IRP that is still in use. (IRP specified.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x20C</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>The caller of <strong>IoFreeIrp</strong> is freeing an IRP that is still queued against a thread. (IRP specified.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x20D</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>The caller of <strong>IoInitializeIrp</strong> has passed an IRP that was allocated with <strong>IoAllocateIrp</strong>. This is illegal and unnecessary, and has caused a quota leak. Check the documentation for <strong>IoReuseIrp</strong> if this IRP is being recycled.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x20E</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>A PNP IRP has an invalid status. (Any PNP IRP must have its status initialized to STATUS_NOT_SUPPORTED.) (IRP specified.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x20F</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>A Power IRP has an invalid status. (Any Power IRP must have its status initialized to STATUS_NOT_SUPPORTED.) (IRP specified.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x210</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>A WMI IRP has an invalid status. (Any WMI IRP must have its status initialized to STATUS_NOT_SUPPORTED.) (IRP specified.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x211</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>The caller has forwarded an IRP while skipping a device object in the stack. The caller is probably sending IRPs to the PDO instead of to the device returned by <strong>IoAttachDeviceToDeviceStack</strong>. (IRP specified.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x212</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>The caller has trashed or has not properly copied the IRP&#39;s stack. (IRP specified.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x213</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>The caller has changed the status field of an IRP it does not understand. (IRP specified.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x214</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>The caller has changed the information field of an IRP it does not understand. (IRP specified.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x215</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>A non-successful non-STATUS_NOT_SUPPORTED IRP status for IRP_MJ_PNP is being passed down stack. (IRP specified.) Failed PNP IRPs must be completed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x216</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>The previously-set IRP_MJ_PNP status has been converted to STATUS_NOT_SUPPORTED. (IRP specified.) This failure status is reserved for use by the operating system. Drivers cannot fail a PnP IRP with this value.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x217</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>The driver has not handled a required IRP. The driver must update the status of the IRP to indicate whether or not it has been handled. (IRP specified.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x218</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>The driver has responded to an IRP that is reserved for other device objects elsewhere in the stack. (IRP specified.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x219</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>A non-successful non-STATUS_NOT_SUPPORTED IRP status for IRP_MJ_POWER is being passed down stack. (IRP specified.) Failed POWER IRPs must be completed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x21A</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>The previously-set IRP_MJ_POWER status has been converted to STATUS_NOT_SUPPORTED. (IRP specified.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x21B</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>A driver has returned a suspicious status. This is probably due to an uninitialized variable bug in the driver. (IRP specified.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x21C</p></td>
<td align="left"><p>Warning</p></td>
<td align="left"><p>The caller has copied the IRP stack but not set a completion routine. This is inefficient -- use <strong>IoSkipCurrentIrpStackLocation</strong> instead. (IRP specified.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x21D</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>An IRP dispatch handler has not properly detached from the stack below it upon receiving a remove IRP. (Device object, dispatch routine, and IRP specified.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x21E</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>An IRP dispatch handler has not properly deleted its device object upon receiving a remove IRP. (Device object, dispatch routine, and IRP specified.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x21F</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>A driver has not filled out a dispatch routine for a required IRP major function. (IRP specified.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x220</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>IRP_MJ_SYSTEM_CONTROL has been completed by someone other than the ProviderId. This IRP should either have been completed earlier or should have been passed down. (IRP specified, along with the device object where it was targeted.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x221</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>An IRP dispatch handler for a PDO has deleted its device object, but the hardware has not been reported as missing in a bus relations query. (Device object, dispatch routine, and IRP specified.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x222</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>A Bus Filter&#39;s IRP dispatch handler has detached upon receiving a remove IRP when the PDO is still alive. Bus Filters must clean up in <strong>FastIoDetach</strong> callbacks. (Device object, dispatch routine, and IRP specified.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x223</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>An IRP dispatch handler for a bus filter has deleted its device object, but the PDO is still present. Bus filters must clean up in <strong>FastIoDetach</strong> callbacks. (Device object, dispatch routine, and IRP specified.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x224</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>An IRP dispatch handler has returned a status that is inconsistent with the IRP&#39;s <strong>IoStatus.Status</strong> field. (Dispatch handler routine, IRP, IRP&#39;s IoStatus.Status, and returned Status specified.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x225</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>An IRP dispatch handler has returned a status that is illegal (0xFFFFFFFF). This is probably due to an uninitialized stack variable. To debug this error, use the <strong><a href="ln--list-nearest-symbols-.md" data-raw-source="[ln (List Nearest Symbols)](ln--list-nearest-symbols-.md)">ln (List Nearest Symbols)</a></strong> command with the specified address.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x226</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>An IRP dispatch handler has returned without passing down or completing this IRP, or someone forgot to return STATUS_PENDING. (IRP specified.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x227</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>An IRP completion routine is in pageable code. (This is never permitted.) (Routine and IRP specified.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x228</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>A driver&#39;s completion routine has not marked the IRP pending if the <strong>PendingReturned</strong> field was set in the IRP passed to it. This may cause Windows to hang, especially if an error is returned by the stack. (Routine and IRP specified.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x229</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>A cancel routine has been set for an IRP that is currently being processed by drivers lower in the stack, possibly stomping their cancel routine. (Routine and IRP specified.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x22A</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>The physical device object (PDO) has not responded to a required IRP. (IRP specified.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x22B</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>The physical device object (PDO) has forgotten to fill out the device relation list with the PDO for the <strong>TargetDeviceRelation</strong> query. (IRP specified.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x22C</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>The code implementing the <strong>TargetDeviceRelation</strong> query has not called <strong>ObReferenceObject</strong> on the PDO. (IRP specified.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x22D</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>The caller has completed a IRP_MJ_PNP it didn&#39;t understand instead of passing it down. (IRP specified.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x22E</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>The caller has completed a successful IRP_MJ_PNP instead of passing it down. (IRP specified.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x22F</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>The caller has completed an untouched IRP_MJ_PNP (instead of passing the IRP down), or non-PDO has failed the IRP using illegal value of STATUS_NOT_SUPPORTED. (IRP specified.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x230</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>The caller has completed an IRP_MJ_POWER it didn&#39;t understand instead of passing it down. (IRP specified.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x231</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>The caller has completed a successful IRP_MJ_POWER instead of passing it down. (IRP specified.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x232</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>The caller has completed an untouched IRP_MJ_POWER (instead of passing the IRP down), or non-PDO has failed the IRP using illegal value of STATUS_NOT_SUPPORTED. (IRP specified.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x233</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>The version field of the query capabilities structure in a query capabilities IRP was not properly initialized. (IRP specified.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x234</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>The size field of the query capabilities structure in a query capabilities IRP was not properly initialized. (IRP specified.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x235</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>The address field of the query capabilities structure in a query capabilities IRP was not properly initialized to -1. (IRP specified.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x236</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>The UI Number field of the query capabilities structure in a query capabilities IRP was not properly initialized to -1. (IRP specified.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x237</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>A driver has sent an IRP that is restricted for system use only. (IRP specified.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x238</p></td>
<td align="left"><p>Warning</p></td>
<td align="left"><p>The caller of <strong>IoInitializeIrp</strong> has passed an IRP that was allocated with <strong>IoAllocateIrp</strong>. This is illegal, unnecessary, and negatively impacts performance in normal use. If this IRP is being recycled, see <strong>IoReuseIrp</strong> in the Windows Driver Kit.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x239</p></td>
<td align="left"><p>Warning</p></td>
<td align="left"><p>The caller of <strong>IoCompleteRequest</strong> is completing an IRP that has never been forwarded via a call to <strong>IoCallDriver</strong> or <strong>PoCallDriver</strong>. This may be a bug. (IRP specified.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x23A</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>A driver has forwarded an IRP at an IRQL that is illegal for this major code. (IRP specified.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x23B</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>The caller has changed the status field of an IRP it does not understand. (IRP specified.)</p></td>
</tr>
</tbody>
</table>

 

The following table lists additional **I/O Verification** errors that can appear in Windows XP and later. Some of these errors will only be revealed if **Enhanced I/O Verification** is activated. In Windows Vista and later, the **Enhanced I/O Verification** settings are included as part of **I/O Verification**.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">I/O Error Code</th>
<th align="left">Severity</th>
<th align="left">Cause of Error</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x23C</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>A driver has completed an IRP without setting the cancel routine in the IRP to <strong>NULL</strong>. (IRP specified.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x23D</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>A driver has returned STATUS_PENDING but did not mark the IRP pending via a call to <strong>IoMarkIrpPending</strong>. (IRP specified.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x23E</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>A driver has marked an IRP pending but didn&#39;t return STATUS_PENDING. (IRP specified.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x23F</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>A driver has not inherited the DO_POWER_PAGABLE bit from the stack it has attached to. (Device object specified.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x240</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>A driver is attempting to delete a device object that has already been deleted via a prior call to <strong>IoDeleteDevice</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x241</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>A driver has detached its device object during a surprise remove IRP. (IRP and device object specified.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x242</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>A driver has deleted its device object during a surprise remove IRP. (IRP and device object specified.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x243</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>A driver has failed to clear the DO_DEVICE_INITIALIZING flag at the end of <strong>AddDevice</strong>. (Device object specified.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x244</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>A driver has not copied either the DO_BUFFERED_IO or the DO_DIRECT_IO flag from the device object it is attaching to. (Device object specified.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x245</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>A driver has set both the DO_BUFFERED_IO and the DO_DIRECT_IO flags. These flags are mutually exclusive. (Device object specified.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x246</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>A driver has failed to copy the <strong>DeviceType</strong> field from the device object it is attaching to. (Device object specified.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x247</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>A driver has failed an IRP that cannot legally be failed. (IRP specified.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x248</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>A driver has added a device object that is not a PDO to a device relations query. (IRP and device object specified.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x249</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>A driver has enumerated two child PDOs that returned identical Device IDs. (Both device objects specified.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x24A</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>A driver has mistakenly called a file I/O function with IRQL not equal to PASSIVE_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x24B</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>A driver has completed an IRP_MN_QUERY_DEVICE_RELATIONS request of type <strong>TargetDeviceRelation</strong> as successful, but did not properly fill out the request or forward the IRP to the underlying hardware stack. (Device object specified.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x24C</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>A driver has returned STATUS_PENDING but did not mark the IRP pending by a call to <strong>IoMarkIrpPending</strong>. (IRP specified.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x24D</p></td>
<td align="left"><p>Fatal error</p></td>
<td align="left"><p>A driver has passed an invalid device object to a function that requires a PDO. (Device object specified.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x300</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>A driver has returned a suspicious status. This is probably due to an uninitialized variable bug in the driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x301</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>A driver has forwarded an IRP at IRQL &gt; DISPATCH_LEVEL. (IRQL value specified)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x302</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>A driver has forwarded an IRP at IRQL &gt;= APC_LEVEL.</p>
<p>The I/O Manager will need to queue an APC to complete this request. The APC will not be able to run because the caller is already at APC level, so the caller is likely to deadlock. (IRQL value specified)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x306</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>The driver is completing an IRP_MJ_PNP (major) and IRP_MN_REMOVE_DEVICE (minor) request with a failure status code.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x307</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>The driver issued an I/O request with an event that was already signaled and received a STATUS_PENDING response. This can result in unwinding before the I/O is complete.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x310</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>The driver is reinitializing an IRP that is still in use.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x311</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>The driver is reinitializing an IRP that was created with IoMakeAssociatedIrp, IoBuildAsynchronousFsdRequest, IoBuildSynchronousFsdRequest, IoBuildDeviceIoControlRequest.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x312</p></td>
<td align="left"><p>Non-fatal error</p></td>
<td align="left"><p>The caller provided the IRP Status Information field with a value that is greater than the output section of the system buffer.</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

See the description of each code in the Parameters section for a description of the cause.

Resolution
----------

This bug check can only occur when Driver Verifier has been instructed to monitor one or more drivers. If you did not intend to use Driver Verifier, you should deactivate it. You might consider removing the driver which caused this problem as well.

If you are the driver writer, use the information obtained through this bug check to fix the bugs in your code.

For full details on Driver Verifier, see the Windows Driver Kit.

 

 




