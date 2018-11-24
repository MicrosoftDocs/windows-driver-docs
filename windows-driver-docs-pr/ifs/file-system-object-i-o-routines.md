---
title: File System Object I/O Routines
description: File System Object I/O Routines
ms.assetid: 0514e396-76b9-458b-9a98-e539d7e90274
keywords:
- mini-redirectors WDK , object I/O routines
- I/O WDK network redirectors
- low-I/O routines WDK network redirectors
- file system object I/O WDK
- file objects WDK mini-redirectors
- objects WDK mini-redirectors
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# File System Object I/O Routines


The file system object I/O routines represent the traditional file I/O calls for read, write, and other file operations. These routines are often called "low I/O routines" in the network mini-redirector. RDBSS calls these routines in response to receiving a specific IRP

The low I/O routines are passed in as an array of routine pointers as part of the MINIRDR\_DISPATCH structure passed to the [**RxRegisterMinirdr**](https://msdn.microsoft.com/library/windows/hardware/ff554693) routine that is used to register the network mini-redirector at startup (in the **DriverEntry** routine). The value of the array entry is the low I/O operation to perform.

These low I/O or file system object I/O routines are normally called asynchronously by RDBSS. So a network mini-redirector must make certain that any low I/O routines that are implemented can be safely called asynchronously. It is also possible for a network mini-redirector to ignore the request for an asynchronous call and implement a routine to only operate synchronously. However, for certain calls that may take time to complete (read and write, for example), implementing these as synchronous operations can significantly reduce I/O performance for the entire operating system.

All the file system object I/O routines expect a pointer to an RX\_CONTEXT structure to be passed in as a parameter. Before calling these routines, RDBSS sets the value of a number of members in the **LowIoContext** structure of the RX\_CONTEXT. Some of the members in the **LowIoContext** structure are set for all routines, while some members are only set for specific routines. The RX\_CONTEXT data structure contains the IRP that is being processed and has a **LowIoContext.Operation** member that specifies the low I/O operation to perform. It is possible for several of the low I/O routines to point to the same routine in a network mini-redirector because this **LowIoContext.Operation** member can be used to differentiate the low I/O operation requested. For example, all the I/O calls related to file locks could call the same low I/O routine in the network mini-redirector which uses the **LowIoContext.Operation** member to differentiate the lock or unlock operation requested.

Other file I/O routines other than the low I/O routines are based on synchronous calls, although this is subject to change in future releases of the Windows operating system.

While in the LowIo path, the **LowIoContext.ResourceThreadId** member of the RX\_CONTEXT is guaranteed to indicate the owning thread that initiated the operation in RDBSS. The **LowIoContext.ResourceThreadId** member can be used to release the FCB resource on behalf of another thread. When an asynchronous routine completes, the FCB resource that was acquired from the initial thread can be released.

If an **MrxLowIoSubmit\[LOWIO\_OP\_XXX\]** routine is likely to take a long time to complete, the network mini-redirector driver should release the FCB resource before initiating the network communication. The FCB resource can be released by calling [**RxReleaseFcbResourceForThreadInMRx**](https://msdn.microsoft.com/library/windows/hardware/ff554694).

The following table lists the routines that can be implemented by a network mini-redirector for file system object I/O (low I/O) operations.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Routine</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff550703" data-raw-source="[&lt;strong&gt;MRxLowIOSubmit[LOWIO_OP_EXCLUSIVELOCK]&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550703)"><strong>MRxLowIOSubmit[LOWIO_OP_EXCLUSIVELOCK]</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector open an exclusive lock on a file object. RDBSS issues this call in response to receiving an IRP_MJ_LOCK_CONTROL with a minor code of IRP_MN_LOCK and IrpSp-&gt;Flags has the SL_EXCLUSIVE_LOCK bit set.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff550709" data-raw-source="[&lt;strong&gt;MRxLowIOSubmit[LOWIO_OP_FSCTL]&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550709)"><strong>MRxLowIOSubmit[LOWIO_OP_FSCTL]</strong></a></td>
<td align="left"><p>RDBSS calls this routine to pass a file system control request to the network mini-redirector. RDBSS issues this call in response to receiving an IRP_MJ_FILE_SYSTEM_CONTROL.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff550715" data-raw-source="[&lt;strong&gt;MRxLowIOSubmit[LOWIO_OP_IOCTL]&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550715)"><strong>MRxLowIOSubmit[LOWIO_OP_IOCTL]</strong></a></td>
<td align="left"><p>RDBSS calls this routine to pass an I/O system control request to the network mini-redirector. RDBSS issues this call in response to receiving an IRP_MJ_DEVICE_CONTROL or IRP_MJ_INTERNAL_DEVICE_CONTROL..</p></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff550721" data-raw-source="[&lt;strong&gt;MRxLowIOSubmit[LOWIO_OP_NOTIFY_CHANGE_DIRECTORY]&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550721)"><strong>MRxLowIOSubmit[LOWIO_OP_NOTIFY_CHANGE_DIRECTORY]</strong></a></td>
<td align="left"><p>RDBSS calls this routine to issue a request to the network mini-redirector for a directory change notification operation. RDBSS issues this call in response to receiving an IRP_MJ_DIRECTORY_CONTROL.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff550724" data-raw-source="[&lt;strong&gt;MRxLowIOSubmit[LOWIO_OP_READ]&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550724)"><strong>MRxLowIOSubmit[LOWIO_OP_READ]</strong></a></td>
<td align="left"><p>RDBSS calls this routine to issue a read request to the network mini-redirector. RDBSS issues this call in response to receiving an IRP_MJ_READ.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff550734" data-raw-source="[&lt;strong&gt;MRxLowIOSubmit[LOWIO_OP_SHAREDLOCK]&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550734)"><strong>MRxLowIOSubmit[LOWIO_OP_SHAREDLOCK]</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network redirector open a shared lock on a file object. RDBSS issues this call in response to receiving an IRP_MJ_LOCK_CONTROL with a minor code of IRP_MN_LOCK and IrpSp-&gt;Flags does not have the SL_EXCLUSIVE_LOCK bit set.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff550740" data-raw-source="[&lt;strong&gt;MRxLowIOSubmit[LOWIO_OP_UNLOCK]&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550740)"><strong>MRxLowIOSubmit[LOWIO_OP_UNLOCK]</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector remove a single lock on a file object. RDBSS issues this call in response to receiving an IRP_MJ_LOCK_CONTROL with a minor code of IRP_MN_UNLOCK_SINGLE.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff550745" data-raw-source="[&lt;strong&gt;MRxLowIOSubmit[LOWIO_OP_UNLOCK_MULTIPLE]&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550745)"><strong>MRxLowIOSubmit[LOWIO_OP_UNLOCK_MULTIPLE]</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that the network mini-redirector remove multiple locks held on a file object. RDBSS issues this call in response to receiving an IRP_MJ_LOCK_CONTROL with a minor code of IRP_MN_UNLOCK_ALL or IRP_MN_UNLOCK_ALL_BY_KEY. The byte ranges to be unlocked are specified in the <strong>LowIoContext.ParamsFor.Locks.LockList</strong> member of the RX_CONTEXT.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff550746" data-raw-source="[&lt;strong&gt;MRxLowIOSubmit[LOWIO_OP_WRITE]&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550746)"><strong>MRxLowIOSubmit[LOWIO_OP_WRITE]</strong></a></td>
<td align="left"><p>RDBSS calls this routine to issue a write request to the network mini-redirector. RDBSS issues this call in response to receiving an IRP_MJ_WRITE.</p></td>
</tr>
</tbody>
</table>

 

 

 




