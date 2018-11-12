---
title: Bug Check 0x10D WDF_VIOLATION
description: The WDF_VIOLATION bug check has a value of 0x0000010D. This indicates that Kernel-Mode Driver Framework (KMDF) detected that Windows found an error in a framework-based driver.
ms.assetid: 2d8c9730-cd24-4f8c-8f8b-252644737847
keywords: ["Bug Check 0x10D WDF_VIOLATION", "WDF_VIOLATION"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- WDF_VIOLATION
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x10D: WDF\_VIOLATION


The WDF\_VIOLATION bug check has a value of 0x0000010D. This indicates that Kernel-Mode Driver Framework (KMDF) detected that Windows found an error in a framework-based driver.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## WDF\_VIOLATION Parameters


Parameter 1 indicates the specific error code of the bug check. Parameter 4 is reserved.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter 1</th>
<th align="left">Parameter 2</th>
<th align="left">Parameter 3</th>
<th align="left">Cause of Error</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x1</p></td>
<td align="left"><p>Pointer to a WDF_POWER_ROUTINE_TIMED_OUT_DATA structure</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A framework-based driver has timed out during a power operation. This typically means that the device stack did not set the DO_POWER_PAGABLE bit and a driver attempted a pageable operation after the paging device stack was powered down.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x2</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>An attempt is being made to acquire a lock that is currently being held.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x3</p></td>
<td align="left"><p>WDFREQUEST handle</p></td>
<td align="left"><p>The number of outstanding references that remain on both buffers</p></td>
<td align="left"><p>Windows Driver Framework Verifier has encountered a fatal error. In particular, an I/O request was completed, but a framework request object cannot be deleted because there are outstanding references to the input buffer, the output buffer, or both.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x4</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The caller&#39;s address</p></td>
<td align="left"><p>A <strong>NULL</strong> parameter was passed to a function that required a non-<strong>NULL</strong> value.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x5</p></td>
<td align="left"><p>The handle value passed in</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A framework object handle of the incorrect type was passed to a framework object method.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x6</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>See table below.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x7</p></td>
<td align="left"><p>The handle of the framework object</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A driver attempted to delete a framework object incorrectly by calling <strong>WdfObjectDereference</strong> to delete a handle instead of calling <strong>WdfObjectDelete</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x8</p></td>
<td align="left"><p>The handle of the DMA transaction object</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>An operation occurred on a DMA transaction object while it was not in the correct state.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x9</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Currently unused.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xA</p></td>
<td align="left"><p>A pointer to a WDF_QUEUE_FATAL_ERROR_DATA structure</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A fatal error has occurred while processing a request that is currently in the queue.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xB</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>See table below.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xC</p></td>
<td align="left"><p>WDFDEVICE handle</p></td>
<td align="left"><p>Pointer to new PnP IRP</p></td>
<td align="left"><p>A new state-changing PnP IRP arrived while the driver was processing another state-changing PnP IRP.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xD</p></td>
<td align="left"><p>WDFDEVICE handle</p></td>
<td align="left"><p>Pointer to power IRP</p></td>
<td align="left"><p>A device&#39;s power policy owner received a power IRP that it did not request. There might be multiple power policy owners, but only one is allowed. A KMDF driver can change power policy ownership by calling <strong>WdfDeviceInitSetPowerPolicyOwnership</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xE</p></td>
<td align="left"><p>IRQL at which the event callback function was called.</p></td>
<td align="left"><p>IRQL at which the event callback function returned.</p></td>
<td align="left"><p>An event callback function did not return at the same IRQL at which it was called. The callback function changed the IRQL directly or indirectly (for example, by acquiring a spinlock, which raises IRQL to DISPATCH_LEVEL, but not releasing the spinlock).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xF</p></td>
<td align="left"><p>Address of an event callback function.</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>An event callback function entered a critical region, but it did not leave the critical region before returning.</p></td>
</tr>
</tbody>
</table>

 

**Parameter 1 is equal to 0x6**

If Parameter 1 is equal to 0x6, then a fatal error was made in handling a WDF request. In this case, Parameter 2 further specifies the type of fatal error that has been made, as defined by the enumeration WDF\_REQUEST\_FATAL\_ERROR.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter 2</th>
<th align="left">Parameter 3</th>
<th align="left">Cause of Error</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x1</p></td>
<td align="left"><p>The address of the IRP</p></td>
<td align="left"><p>No more I/O stack locations are available to format the underlying IRP.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x2</p></td>
<td align="left"><p>The WDF request handle value</p></td>
<td align="left"><p>An attempt was made to format a framework request object that did not contain an IRP.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x3</p></td>
<td align="left"><p>The WDF request handle value</p></td>
<td align="left"><p>The driver attempted to send a framework request that has already been sent to an I/O target.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x4</p></td>
<td align="left"><p>A pointer to a WDR_REQUEST_FATAL_ERROR_INFORMATION_LENGTH_MISMATCH_DATA structure that contains a pointer to the IRP, a WDF request handle value, an IRP major function, and the number of bytes attempted to be written</p></td>
<td align="left"><p>The driver has completed a framework request, but has written more bytes to the output buffer than are specified in the IRP.</p></td>
</tr>
</tbody>
</table>

 

**Parameter 1 is equal to 0xB**

If Parameter 1 is equal to 0xB, then an attempt to acquire or release a lock was invalid. In this case, Parameter 3 further specifies the error that has been made.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter 2</th>
<th align="left">Parameter 3</th>
<th align="left">Cause of Error</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>The handle value</p></td>
<td align="left"><p>0x0</p></td>
<td align="left"><p>A handle passed to <strong>WdfObjectAcquireLock</strong> or <strong>WdfObjectReleaseLock</strong> represents an object that does not support synchronization locks.</p></td>
</tr>
<tr class="even">
<td align="left"><p>A WDF spin lock handle</p></td>
<td align="left"><p>0x1</p></td>
<td align="left"><p>The spin lock is being released by a thread that did not acquire it.</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

See the description of each code in the Parameters section for an explanation of the cause.

Resolution
----------

The [**!analyze**](-analyze.md) debug extension displays information about the bug check and can be very helpful in gathering information, such as the faulting code module.

Typically, the WDF dump file will yield further information on the driver that caused this bug check. Use this command to look at the log file.

```dbgcmd
kd> !wdfkd.wdflogdump <WDF_Driver_Name>
```

If Parameter 1 is equal to **0x2**, examine the caller's stack to determine the lock in question.

If Parameter 1 is equal to **0x3**, the driver's Kernel-Mode Driver Framework error log will include details about the outstanding references.

If Parameter 1 is equal to **0x4**, use the [**ln debugger**](ln--list-nearest-symbols-.md) command with the value of *Parameter 3* as its argument to determine which function requires a non-**NULL** parameter.

If Parameter 1 is equal to **0x7**, use the **!wdfkd.wdfhandle***Parameter 2* extension command to determine the handle type.

If Parameter 1 is equal to **0xA**, then the WDF\_QUEUE\_FATAL\_ERROR\_DATA structure will indicate either the problematic request or the queue handle. It will also indicate the NTSTATUS, if not STATUS\_SUCCESS, when available.

 

 




