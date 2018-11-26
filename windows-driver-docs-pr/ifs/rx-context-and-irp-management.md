---
title: RX_CONTEXT and IRP Management
description: RX_CONTEXT and IRP Management
ms.assetid: 74ca681d-2599-442c-aebe-3556d6354f7f
keywords:
- RDBSS WDK file systems , IRPs
- Redirected Drive Buffering Subsystem WDK file systems , IRPs
- RX_CONTEXT structure
- data structures WDK file systems
- RDBSS WDK file systems , connection and file structures
- Redirected Drive Buffering Subsystem WDK file systems , connection and file structures
- connection structures WDK RDBSS
- file structures WDK RDBSS
- structures WDK RDBSS
- connection information WDK RDBSS
- IRPs WDK RDBSS
- I/O request packets WDK RDBSS
- context WDK RDBSS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# RX\_CONTEXT and IRP Management


## <span id="ddk_rx_context_and_irp_management_if"></span><span id="DDK_RX_CONTEXT_AND_IRP_MANAGEMENT_IF"></span>


The RX\_CONTEXT structure is one of the fundamental data structures used by RDBSS and network mini-redirectors to manage an I/O request packet (IRP). An RX\_CONTEXT structure describes an IRP while it is being processed and contains state information that allows global resources to be released as the IRP is completed. The RX\_CONTEXT data structure encapsulates an IRP for use by RDBSS, network mini-redirectors, and the file system. An RX\_CONTEXT structure includes a pointer to a single IRP and all of the context required to process the IRP.

An RX\_CONTEXT structure is sometimes referred to as an IRP Context or RxContext in the Windows Driver Kit (WDK) header files and other resources used for developing network mini-redirector drivers.

The RX\_CONTEXT is a data structure to which additional information provided by the various network mini redirectors is attached. From a design standpoint, this additional information can be handled in one of several ways:

-   Allow for context pointers to be defined as part of RX\_CONTEXT, which network mini-redirectors use to store away their information. This implies that every time an RX\_CONTEXT structure is allocated and destroyed, the network mini-redirector driver must perform a separate associated allocation or destruction of the memory block that contains the additional network mini-redirector information. Since RX\_CONTEXT structures are created and destroyed in large numbers, this is not an acceptable solution from a performance standpoint.

-   Another approach consists of over allocating the size of each RX\_CONTEXT structure by a pre-specified amount for each network mini redirector, which is then reserved for use by the mini redirector. Such an approach avoids the additional allocation and destruction but complicates the RX\_CONTEXT management code in RDBSS.

-   The third approach consists of allocating a pre-specified area, which is the same for all network mini redirectors as part of each RX\_CONTEXT. This is an unformatted area on top of which any desired structure can be imposed by the various network mini redirectors. Such an approach overcomes the disadvantages associated with previous approaches. This is the approach currently implemented in RDBSS.

The third approach is the scheme used by RDBSS. Consequently, developers of network mini-redirector drivers should try and define the associated private context to fit into this pre-specified area defined in the RX\_CONTEXT data structure. Network mini-redirector drivers that violate this rule will incur a significant performance penalty.

Many RDBSS routines and routines exported by a network mini-redirector make reference to RX\_CONTEXT structures in either the initiating thread or in some other thread used by the routine. Thus, the RX\_CONTEXT structures are reference counted to manage their use for asynchronous operations. When the reference count goes to zero, the RX\_CONTEXT structure can be finalized and released on the last dereference operation.

RDBSS provides a number of routines that are used to manipulate an RX\_CONTEXT structure and the associated IRP. These routines are used to allocate, initialize, and delete an RX\_CONTEXT structure. These routines are also used to complete the IRP associated with an RX\_CONTEXT and set up a cancel routine for an RX\_CONTEXT.

The following routines manipulate RX\_CONTEXT structures:

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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554340" data-raw-source="[&lt;strong&gt;RxCompleteRequest&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554340)"><strong>RxCompleteRequest</strong></a></p></td>
<td align="left"><p>This routine is used to complete an IRP associated with an RX_CONTEXT structure. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554348" data-raw-source="[&lt;strong&gt;RxCompleteRequest_Real&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554348)"><strong>RxCompleteRequest_Real</strong></a></p></td>
<td align="left"><p>This routine is used to complete an IRP associated with an RX_CONTEXT structure. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554367" data-raw-source="[&lt;strong&gt;RxCreateRxContext&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554367)"><strong>RxCreateRxContext</strong></a></p></td>
<td align="left"><p>This routine allocates a new RX_CONTEXT structure and initializes the data structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554393" data-raw-source="[&lt;strong&gt;RxDereferenceAndDeleteRxContext_Real&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554393)"><strong>RxDereferenceAndDeleteRxContext_Real</strong></a></p></td>
<td align="left"><p>This routine dereferences an RX_CONTEXT structure, and if the reference count goes to zero, then it deallocates and removes the specified RX_CONTEXT structure from the RDBSS in-memory data structures.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554502" data-raw-source="[&lt;strong&gt;RxInitializeContext&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554502)"><strong>RxInitializeContext</strong></a></p></td>
<td align="left"><p>This routine initializes a newly allocated RX_CONTEXT structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554643" data-raw-source="[&lt;strong&gt;RxPrepareContextForReuse&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554643)"><strong>RxPrepareContextForReuse</strong></a></p></td>
<td align="left"><p>This routine prepares an RX_CONTEXT structure for reuse by resetting all operation-specific allocations and acquisitions previously made. The parameters obtained from the IRP are not modified. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554701" data-raw-source="[&lt;strong&gt;RxResumeBlockedOperations_Serially&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554701)"><strong>RxResumeBlockedOperations_Serially</strong></a></p></td>
<td align="left"><p>This routine wakes up the next waiting thread, if any, on the serialized blocking I/O queue.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554722" data-raw-source="[&lt;strong&gt;RxSetMinirdrCancelRoutine&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554722)"><strong>RxSetMinirdrCancelRoutine</strong></a></p></td>
<td align="left"><p>The routine sets up a network mini-redirector cancel routine for an RX_CONTEXT structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff557377" data-raw-source="[&lt;strong&gt;__RxSynchronizeBlockingOperations&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557377)"><strong>__RxSynchronizeBlockingOperations</strong></a></td>
<td align="left"><p>This routine is used to synchronize blocking I/O to the same work queue. This routine is used internally by RDBSS to synchronize named pipe operations. This routine may be used by a network mini-redirector to synchronize operations on a separate queue that is maintained by the network mini-redirector.</p>
<p>The routine is only available on Windows Server 2003.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff557382" data-raw-source="[&lt;strong&gt;__RxSynchronizeBlockingOperationsMaybeDroppingFcbLock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557382)"><strong>__RxSynchronizeBlockingOperationsMaybeDroppingFcbLock</strong></a></td>
<td align="left"><p>This routine is used to synchronize blocking I/O to the same work queue. This routine is used internally by RDBSS to synchronize named pipe operations. This routine may be used by a network mini-redirector to synchronize operations on a separate queue that is maintained by the network mini-redirector.</p>
<p>The routine is only available on Windows XP and Windows 2000.</p></td>
</tr>
</tbody>
</table>

 

The following macros are defined in the *rxcontx.h* header file that call the routines listed in the previous table. These macros are normally used instead of calling these routines directly.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Macro</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>RxSynchronizeBlockingOperations</strong>(<em>RXCONTEXT</em>,<em>FCB</em>,<em>IOQUEUE</em>)</p></td>
<td align="left"><p>This macro synchronizes blocking I/O requests to the same work queue. On Windows Server 2003, this macro calls the <strong>__RxSynchronizeBlockingOperations</strong> routine with the <em>DropFcbLock</em> parameter set to <strong>FALSE</strong>.</p>
<p>On Windows XP and Windows 2000, this macro calls the <strong>__RxSynchronizeBlockingOperationsMaybeDroppingFcbLock</strong> routine with the <em>DropFcbLock</em> parameter set to <strong>FALSE</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>RxSynchronizeBlockingOperations</strong>(<em>RXCONTEXT</em>,<em>FCB</em>,<em>IOQUEUE</em>)</p></td>
<td align="left"><p>This macro synchronizes blocking I/O requests to the same work queue. On Windows Server 2003, this macro calls the <strong>__RxSynchronizeBlockingOperations</strong> routine with the <em>DropFcbLock</em> parameter set to <strong>TRUE</strong>.</p>
<p>On Windows XP and Windows 2000, this macro calls the <strong>__RxSynchronizeBlockingOperationsMaybeDroppingFcbLock</strong> routine with the <em>DropFcbLock</em> parameter set to <strong>TRUE</strong>.</p></td>
</tr>
</tbody>
</table>

 

 

 




