---
title: Receiving Asynchronous I/O Request Packets on the IEEE 1394 Bus
description: The computer itself is a node on the IEEE 1394 bus, and therefore can receive asynchronous I/O requests.
ms.assetid: 7b8eaf40-7fdc-4c25-86a7-8377d2d51877
keywords:
- receiving asynchronous I/O requests
- allocating address ranges
- addresses WDK IEEE 1394 bus
- backing store WDK IEEE 1394 bus
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Receiving Asynchronous I/O Request Packets on the IEEE 1394 Bus


The computer itself is a node on the IEEE 1394 bus, and therefore can receive asynchronous I/O requests. Drivers can allocate ranges of addresses in the computer's IEEE 1394 address space, and receive requests from external nodes, by submitting the REQUEST\_ALLOCATE\_ADDRESS\_RANGE request to the bus driver.

When the driver allocates the address range, it can specify which types of transactions a device may send to the allocated addresses, by specifying one or more of ACCESS\_FLAGS\_TYPE\_READ, ACCESS\_FLAGS\_TYPE\_WRITE, or ACCESS\_FLAGS\_TYPE\_LOCK in the **u.AllocateAddressRange.fulAccessType** member of the request's IRB. Requests that are not one of the specified types automatically fail.

Two different drivers may allocate the same address range. By default, the bus driver automatically demultiplexes the requests, and the driver only sees the requests on the allocated addresses that come from the driver's device. Drivers can request that they receive all packets sent to the addresses by all nodes on the bus, by specifying the ACCESS\_FLAGS\_TYPE\_BROADCAST flag in **u.AllocateAddressRange.fulAccessType**.

-   [Which addresses are allocated?](#ddk-receiving-asynchronous-i-o-request-packets-on-the-ieee-1394-bus-kg)
-   [Allocation and backing store](#allocation-and-backing-store)
-   [Client driver's notification routine for receive asynchronous I/O requests](#client-drivers-notification-routine-for-receive-asynchronous-io-requests)
-   [Asynchronous receive in the pre-notification case](#asynchronous-receive-in-the-pre-notification-case)

## Which addresses are allocated?


The bus driver supports two different strategies for allocating address ranges. If the driver requires a specific range of addresses, beginning at a hard-coded address, it can specify the hard-coded address in the **u.AllocateAddressRange.Required1394Offset** member of the request's IRB, and the length of the address range in **u.AllocateAddressRange.nLength**. The bus driver will allow two different drivers to allocate the same address twice. If the same driver tries to allocate an address range beginning at the same address twice, the bus driver returns the request with a status code of STATUS\_SUCCESS, but the request itself is ignored.

Otherwise, the driver can allow the bus driver to choose the allocated addresses. The bus driver keeps track of all address ranges allocated by drivers, and will only return previously unallocated addresses.

The bus driver does not allocate the address contiguously. The addresses are segmented according to the MDL provided as backing store. Each segment in the MDL corresponds to one segment in the address range. A driver that needs the allocated addresses to be contiguous can allocate contiguous memory from nonpaged pool.

If the driver needs to guarantee that every segment is smaller than a specific size, they can specify that size in **u.AllocateAddressRange.MaxSegmentSize**. Drivers that do not need to specify a maximum segment size set **u.AllocateAddressRange.MaxSegmentSize** to zero.

The bus driver returns the address ranges in the memory location pointed to by the **u.AllocateAddressRange.p1394AddressRange** member of the IRB. The device driver must allocate an array that is large enough to hold each ADDRESS\_RANGE structure, even in the worst case segmentation scenario. If the driver does not specify a segment size, or its maximum segment size is bigger than PAGE\_SIZE, then the driver can determine the worst case by using the ADDRESS\_AND\_SIZE\_TO\_SPAN\_PAGES macro on the buffer used for backing store. If the maximum segment size is smaller than PAGE\_SIZE, the driver must allocate an array of size **u.AllocateAddressRange.nLength**/**u.AllocateAddressRange.MaxSegmentSize** + 2.

When the bus driver returns the allocated addresses, it records the actual number of address ranges allocated in **u.AllocateAddressRange.hAddressRange**.

## Allocation and backing store


The bus driver receives all asynchronous packet requests on behalf of the driver. At the driver's behest, it can transparently handle the request, or it can dispatch the request to the driver. By setting options when it allocates the addresses, the driver can choose how the bus driver handles each request.

1.  The driver provides backing store for the address range, and the bus driver transparently handles all read, write, and lock requests by using the backing store.

    When the driver allocates addresses, it can supply an MDL in **u.AllocateAddressRange.Mdl** to serve as backing store. The bus driver maps the MDL onto the range of addresses it allocates for the driver, and handles all requests by reading or writing from the MDL. If the host controller supports it, the transaction is handled entirely by the host controller's DMA hardware. When possible, the device driver should allow the bus driver to choose the range of addresses allocated: the bus driver will choose 1394 addresses that support automatic DMA for each transaction.

    The driver must specify NOTIFY\_FLAGS\_NEVER for **u.AllocateAddressRange.fulNotificationOptions**.

    Here's an example:

    ```cpp
    pIRB->u.AllocateAddressRange.Mdl = an MDL previously allocated by the driver.
    pIRB->u.AllocateAddressRange.fulNotificationOptions = NOTIFY_FLAGS_NEVER
     
    ```

    For this option alone, the driver can also allocate address ranges while at raised IRQL. The driver can submit the request directly to the port driver, bypassing the usual IRP method of communication, by calling the port driver's physical mapping routine. The device driver passes the IRB to the port driver's physical mapping routine. The port driver will then allocate the address range asynchronously; when the port driver finishes, it calls the device driver's notification routine, passed in **u.AllocateAddressRange.Callback**, and passes **u.AllocateAddressRange.Context** as the parameter. The notification routine is called at DISPATCH\_LEVEL.

    The device driver can get a pointer to the port driver's physical mapping routine by submitting the GET\_LOCAL\_HOST\_INFO request to the bus driver, with **nLevel** = GET\_PHYS\_ADDR\_ROUTINE. The bus driver returns a GET\_LOCAL\_HOST\_INFO4 structure, which contains the physical mapping routine, and a context parameter that the device driver passes along with the IRB to the physical mapping routine.

    Here is an example of how the driver can set up the request for the physical mapping routine. The physical mapping routine does not change, so the driver would normally only submit this request once.

    ```cpp
    GET_LOCAL_HOST_INFO5 PhysMapInfo;
    pGetInfoIRB->FunctionNumber = GET_LOCAL_HOST_INFO;
    pGetInfoIRB->GET_PHYS_ADDR_ROUTINE;
     
    /* Driver submits the request. */
     
    ```

    Continuing the example, here is how the driver can use the physical mapping routine to submit the request at an elevated IRQL.

    ```cpp
    VOID AllocationCompletionRoutine(PVOID Context);
    /* Driver fills out the members of the IRB, including these: */
    pIRB->u.AllocateAddressRange.Mdl = an MDL previously allocated by the driver.
    pIRB->u.AllocateAddressRange.fulNotificationOptions = NOTIFY_FLAGS_NEVER
    pIRB->Callback = AllocationCompletionRoutine;
    pIRB->Context = information specific to this allocation the driver wants passed to its callback.
     
    /* Driver submits the request to the physical mapping routine. */
    PhysMapInfo.PhysAddrMappingRoutine(PhysMapInfo.Context, pIRB);
     
    /* 
    The bus driver does the allocation asynchronously. When it&#39;s done, it will signal the driver by executing AllocationCompletionRoutine(pIRB->u.AllocateAddressRange.Context);
    */
     
    ```

2.  The driver provides backing store for the address range. The bus driver notifies the driver after it completes each I/O transaction.

    The driver can provide either a single MDL, or a linked list of MDLs, as backing store. If the driver provides a single MDL, the bus driver pumps data into or out of the MDL in response to the asynchronous request. Once it completes the transaction, it signals the device driver by calling the driver-supplied notification callback.

    The device driver supplies the notification routine in the **u.AllocateAddressRange.Callback** member of the IRB. The driver must set at least one of the NOTIFY\_FLAGS\_AFTER\_XXX flags. When the bus driver calls the routine, it passes a NOTIFICATION\_INFO structure, which specifies the MDL backing store (in **Mdl**), the byte offset within the MDL where the transaction began (in **ulOffset**), and the length in bytes of the range of addresses affected (in **nLength**). The notification routine is called at DISPATCH\_LEVEL. Any context information for this request that the driver passes in **u.AllocateAddressRange.Context** is passed by the bus driver in the **Context** member of NOTIFICATION\_INFO.

    Using only one MDL, there is some risk of synchronization problems: the device may write to the address range faster than the driver can read from it. To avoid such a clash, for addresses to which the device only has write access the driver can provide a linked list of MDLs, in **u.AllocateAddressRange.FifoSListHead**, and a spin lock in **u.AllocateAddressRange.FifoSpinLock**. When the bus driver receives each asynchronous request packet, it holds the spin lock and pops off the first element on the list to fulfill the request. It then calls the driver's notification routine.

    In the NOTIFICATION\_INFO structure, the bus driver provides the MDL it used to handle the transaction (in **Mdl**), the byte offset of the first address affected (in **ulOffset**), and the length of the ranges of addresses affected (in **nLength**). It also provides the ADDRESS\_FIFO of the MDL (in **Fifo**). Before the driver returns from its notification routine, it should either use **Fifo** to push the element back on the list, or provide another MDL of the same size; otherwise, the bus driver will run out of MDLs to use in handling write requests from the device.

    Here is an extended example of using this type of notification. Globally, the driver creates an interlocked, singly-linked list, and a spin lock. The driver needs to access the linked list and the spin lock at raised IRQLs, so they must be in nonpaged memory. Typically, drivers keep them in their device extensions.

    ```cpp
    PSLIST_HEADER FifoSListHead;
    KSPIN_LOCK FifoSpinLock;
     
    ExInitializeSListHead(FifoSListHead);
    KeInitializeSpinLock(FifoSpinLock);
     
    ```

    When the driver submits the request, it can set up the relevant IRB members as follows:

    ```cpp
    VOID DriverNotificationRoutine(PNOTIFICATION_INFO NotificationInfo);
     
    pIRB->u.AllocateAddressRange.Mdl = NULL;
    pIRB->u.AllocateAddressRange.fulAccessType = ACCESS_FLAGS_READ;
    pIRB->u.AllocateAddressRange.fulNotificationOptions = NOTIFY_FLAGS_AFTER_WRITE;
    pIRB->u.AllocateAddressRange.FifoSListHead = FifoSListHead;
    pIRB->u.AllocateAddressRange.FifoSpinLock = FifoSpinLock;
    pIRB->u.AllocateAddressRange.Callback = DriverNotificationRoutine;
    pIRB->u.AllocateAddressRange.Context = context information specific to this request -- the bus driver will pass this as the Context member of the NOTIFICATION_INFO it passes to NotificationRoutine.
     
    ```

    In the callback, the driver either needs to allocate a new MDL and push it onto the list, or push the original MDL back on the list. For the latter, the bus driver passes the original ADDRESS\_FIFO for the current MDL. Here is an example of the driver pushing the current MDL back on the list:

    ```cpp
    ExInterlockedPushEntrySList(FifoSListHead, NotificationInfo->Fifo->FifoList, FifoSpinLock);
     
    ```

    If the driver specifies a single MDL as backing store in the original allocation request, the driver may return one or more address ranges.

3.  The bus driver signals the driver each time a request arrives, and hands off the packet to the driver.

    The driver provides a callback in the **u.AllocateAddressRange.Callback** member of the IRB. The NOTIFY\_FLAGS\_AFTER\_XXX flags are ignored, and all packets are handed to the driver to handle.

    The driver must set the **Mdl**, **FifoSListHead**, and **FifoSpinLock** members of **u.AllocateAddressRange** to **NULL**. Here is an example of the settings for a driver that wishes to be notified when it receives asynchronous request packets of all three types.

    ```cpp
    VOID DriverNotificationRoutine( IN PNOTIFICATION_INFO NotificationInfo );
     
    pIRB->u.AllocateAddressRange.Callback = DriverNotificationRoutine;
    pIRB->u.AllocateAddressRange.Context = information specific to this address range.
    pIRB->u.AllocateAddressRange.Mdl = NULL;
    pIRB->u.AllocateAddressRange.FifoSListHead = NULL;
    pIRB->u.AllocateAddressRange.FifoSpinLock = NULL;
     
    ```

    The bus driver allocates a single contiguous range of addresses.

    The bus driver passes a NOTIFICATION\_INFO structure to the driver's callback routine. The device driver must create its own response packet (see the IEEE 1394 specification for details), and it must allocate its own buffer to contain the response packet it creates. The response packet must be from nonpaged pool or from a buffer that has been probed and locked.

    Within NOTIFICATION\_INFO, the bus driver provides an uninitialized MDL in the **ResponseMdl** member. It also provides pointers to memory locations where it expects the device driver to enter a pointer to the response packet (in **ResponsePacket**), and the response packet length (in **ResponseLength**). The driver can also provide a kernel event object. The bus driver signals the kernel event object once it completes the transaction.

    Here is an example of how the device driver can fill in the necessary information in its notification routine.

    ```cpp
    /* Suppose the driver creates its response packet in PVOID ResponsePacket, of length ResponseLength. It has created a kernel event ResponseEvent. */
    MmInitializeMdl(NotificationInfo->ResponseMdl, ResponsePacket, ResponseLength);
    MmBuildMdlFForNonPagedPool(Notification->ResponseMdl);
    *(NotificationInfo->ResponsePacket) = ResponsePacket.
    *(NotificationInfo->ResponseLength) = ResponseLength;
    *(NotificationInfo)->ResponseEvent = Event;
     
    ```

## Client driver's notification routine for receive asynchronous I/O requests


The client driver must perform the following tasks in the driver's asynchronous receive notification routine:

-   Verify the members of the [**NOTIFICATION\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff537437) structure that is passed to the client driver.
-   For successful read/lock requests (where you return data through the response packet), the client driver must:
    -   Allocate memory by calling [**WdfMemoryCreate**](https://msdn.microsoft.com/library/windows/hardware/ff548706) ([**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520) for WDM-based client drivers) for the response packet data.
    -   Fill that buffer with the data to be returned.
    -   Initialize the **ResponseMdl** member and reference the buffer. You can call [**MmInitializeMdl**](https://msdn.microsoft.com/library/windows/hardware/ff554568) and [**MmBuildMdlForNonPagedPool**](https://msdn.microsoft.com/library/windows/hardware/ff554498).
    -   Set **\*NotificationInfo-&gt;ResponsePacket** to point to the buffer.
    -   Set **\*NotificationInfo-&gt;ResponseLength** to the size of the response data being returned, that is 4 for a quadlet read request).
    -   Allocate memory by calling [**WdfMemoryCreate**](https://msdn.microsoft.com/library/windows/hardware/ff548706) ([**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520) for WDM-based client drivers) for the response event.
    -   Set **\*NotificationInfo-&gt;ResponseEvent** to point to the event buffer.
    -   Schedule a work item to wait on the event, and free the response packet and event data buffers after the response event is signaled.
    -   Set **NotificationInfo-&gt;ResponseCode** to RCODE\_RESPONSE\_COMPLETE.

## Asynchronous receive in the pre-notification case


The legacy 1394 bus driver fails to complete asynchronous receive transactions by using the pre-notification mechanism. For more information, see [Knowledge Base: IEEE 1394 Async Receive Response not sent using Pre-Notification (2635883)](http://support.microsoft.com/kb/2635883).

For the new 1394 bus driver, the expected behavior of the client driver's notification callback routine in the pre-notification case is as follows:

-   If **Mdl** and **Fifo** members of the [**NOTIFICATION\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff537437) structure are NULL, then pre-notification is being performed.
-   The **ResponseMdl**, **ResponsePacket**, **ResponseLength**, and **ResponseEvent** members of the [**NOTIFICATION\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff537437) structure must not be NULL.
-   The **fulNotificationOptions** member of the [**NOTIFICATION\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff537437) structure must indicate the action (read, write, lock) that triggered the notification. Only one flag (NOTIFY\_FLAGS\_AFTER\_READ , NOTIFY\_FLAGS\_AFTER\_WRITE , or NOTIFY\_FLAGS\_AFTER\_LOCK) can be set each time your notification routine is invoked.
-   You can identify the type of request by inspecting the **RequestPacket-&gt;AP\_tCode** member of the ASYNC\_PACKET structure. The member indicates the TCODE that specifies the request type, such as block or quadlet read/write, type of lock request. The ASYNC\_PACKET structure is declared in 1394.h.
-   The **ResponsePacket** and **ResponseEvent** members of [**NOTIFICATION\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff537437) contain pointers to pointers. Therefore, you must reference the pointers to your response packet and response event appropriately.
-   The **ResponseLength** member of [**NOTIFICATION\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff537437) is a pointer to a ULONG variable. Therefore, you must dereference the member appropriately when setting the response data length for requests such as for read & lock requests).
-   The 1394 client driver is responsible for allocating memory for the response packet and response event (from nonpaged pool), and releasing that memory after the response has been delivered. It is recommended that a work item is queued and the work item should wait on response event. That event is signaled by the 1394 bus driver after the response has been delivered. The client driver can then release the memory within the work item.
-   The **ResponseCode** member in the [**NOTIFICATION\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff537437) structure must be set to one of the RCODE values defined in 1394.h. If **ResponseCode** is set to any value other than RCODE\_RESPONSE\_COMPLETE, the 1394 bus driver sends an error response packet. In the case of a read or lock request, the request does not return any data. In Windows 7, can leak memory, for more information see [Knowledge Base: Memory Leak in IEEE 1394 Bus Driver Performing Asynchronous Notification Callbacks (2023232)](http://support.microsoft.com/kb/2023232).
-   For read and lock requests, the **ResponsePacket** member of the [**NOTIFICATION\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff537437) structure must point to the data to be returned in the asynchronous response packet.

The following code examples shows the work item implementation and the client driver's notification routine.

```cpp
VOID
kmdf1394_NotifyRoutineWorkItem (
                                 IN WDFWORKITEM  WorkItem)
{
    NTSTATUS                 ntStatus;
    PNOTIFY_WORKITEM_CONTEXT notifyContext = GetNotifyWorkitemContext(WorkItem);

    Enter();

    ASSERT(notifyContext);

    ntStatus = KeWaitForSingleObject(
                                     &notifyContext->responseEvent,
                                     Executive,
                                     KernelMode,
                                     FALSE,
                                     NULL);
    if (!NT_SUCCESS(ntStatus)) 
    {
        DoTraceLevelMessage(TRACE_LEVEL_ERROR, 
                            TRACE_FLAG_ASYNC, 
                            "Wait on notify response event failed: %!STATUS!\n",
                            ntStatus);
    }

    WdfObjectDelete (WorkItem);

    Exit();
}

VOID 
kmdf1394_NotificationCallback (
    IN PNOTIFICATION_INFO   NotifyInfo)
{
    PASYNC_PACKET           asyncPacket = (PASYNC_PACKET)NotifyInfo->RequestPacket;
    PASYNC_ADDRESS_DATA     asyncAddressData = NotifyInfo->Context;
    PULONG                  responseQuadlet;
    WDF_WORKITEM_CONFIG     workItemConfig;
    WDFWORKITEM             workItem;
    WDF_OBJECT_ATTRIBUTES   attributes;
    PNOTIFY_WORKITEM_CONTEXT notifyContext;
    NTSTATUS                ntStatus;

    Enter();

    DoTraceLevelMessage(TRACE_LEVEL_INFORMATION, 
                        TRACE_FLAG_ASYNC, 
                        "NotifyInfo Mdl %p ulOffset %08x nLength %08x fulNotificationOptions %08x Context %p RCode %x Pkt %p\n", 
                        NotifyInfo->Mdl, 
                        NotifyInfo->ulOffset, 
                        NotifyInfo->nLength, 
                        NotifyInfo->fulNotificationOptions, 
                        NotifyInfo->Context,
                        NotifyInfo->ResponseCode,
                        asyncPacket);

    if (NotifyInfo->Mdl)
    {
        // Post-Notification
        switch (NotifyInfo->fulNotificationOptions)
        {
            case NOTIFY_FLAGS_AFTER_LOCK:
                NotifyInfo->ResponseCode = RCODE_TYPE_ERROR;
                break;

            case NOTIFY_FLAGS_AFTER_WRITE:
                NotifyInfo->ResponseCode = RCODE_TYPE_ERROR;
                break;

            case NOTIFY_FLAGS_AFTER_READ:
                // Don&#39;t touch ResponseCode if no error
                // NotifyInfo->ResponseCode = RCODE_RESPONSE_COMPLETE;
                break;

            default: 
                NotifyInfo->ResponseCode = RCODE_TYPE_ERROR;
                break;
        }
    }
    else
    {
        // Pre-Notification
        if (asyncPacket)
        {
            if ( !NotifyInfo->ResponseMdl ||
                    !NotifyInfo->ResponsePacket ||
                    !NotifyInfo->ResponseLength ||
                    !NotifyInfo->ResponseEvent )
            {
                DoTraceLevelMessage(TRACE_LEVEL_ERROR, 
                                    TRACE_FLAG_ASYNC, 
                                    "Pre-Notification failure: missing Response field(s)!\n");
                DoTraceLevelMessage(TRACE_LEVEL_ERROR, 
                                    TRACE_FLAG_ASYNC, 
                                    "ResponseMdl %p\tResponsePacket %p\tResponseLength %p\tResponseEvent %p\n",
                                    NotifyInfo->ResponseMdl, NotifyInfo->ResponsePacket,
                                    NotifyInfo->ResponseLength, NotifyInfo->ResponseEvent);
                if (NotifyInfo->ResponsePacket != NULL)
                {
                    DoTraceLevelMessage(TRACE_LEVEL_ERROR, 
                                        TRACE_FLAG_ASYNC, 
                                        "\t*ResponsePacket %p\n",
                                        *NotifyInfo->ResponsePacket);
                }
                NotifyInfo->ResponseCode = RCODE_TYPE_ERROR;
            }
            else if ( NULL == asyncAddressData )
            {
                DoTraceLevelMessage(TRACE_LEVEL_ERROR, 
                                    TRACE_FLAG_ASYNC, 
                                    "Pre-Notification failure: missing Notify Context!\n");
                NotifyInfo->ResponseCode = RCODE_TYPE_ERROR;
            }
            else
            {
                DoTraceLevelMessage(TRACE_LEVEL_INFORMATION, 
                                    TRACE_FLAG_ASYNC, 
                                    "AddrData %p DevExt %p Buffer %p Len %x hAddrRange %!HANDLE! Mdl %p\n", 
                                    asyncAddressData, 
                                    asyncAddressData->DeviceExtension, 
                                    asyncAddressData->Buffer, 
                                    asyncAddressData->nLength, 
                                    asyncAddressData->hAddressRange, 
                                    asyncAddressData->pMdl);

                switch (asyncPacket->AP_tCode)
                {
                    case TCODE_LOCK_REQUEST:
                        NotifyInfo->ResponseCode = RCODE_TYPE_ERROR;
                        break;

                    case TCODE_WRITE_REQUEST_QUADLET:
                    case TCODE_WRITE_REQUEST_BLOCK:
                        NotifyInfo->ResponseCode = RCODE_TYPE_ERROR;
                        break;

                    case TCODE_READ_REQUEST_BLOCK:
                        NotifyInfo->ResponseCode = RCODE_DATA_ERROR;
                        break;

                    case TCODE_READ_REQUEST_QUADLET:
                        // only implementing Quadlet Read for now

                        // Create a WdfWorkItem, with notifyResponse as its context, 
                        // to handle waiting for the Response Event & cleaning up all the response stuff

                        WDF_WORKITEM_CONFIG_INIT (&workItemConfig, kmdf1394_NotifyRoutineWorkItem);

                        WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE(&attributes, NOTIFY_WORKITEM_CONTEXT);

                        attributes.ParentObject = WdfObjectContextGetObject(asyncAddressData->DeviceExtension);

                        ntStatus = WdfWorkItemCreate( &workItemConfig,
                            &attributes,
                            &workItem);

                        if (!NT_SUCCESS (ntStatus)) 
                        {
                            DoTraceLevelMessage(TRACE_LEVEL_ERROR, 
                                                TRACE_FLAG_ASYNC, 
                                                "Failed to create workitem %x\n", 
                                                ntStatus);

                            NotifyInfo->ResponseCode = RCODE_DATA_ERROR;
                            break;
                        }

                        notifyContext = GetNotifyWorkitemContext(workItem);

                        notifyContext->asyncAddressData = asyncAddressData;

                        // NotifyInfo->ResponsePacket
                        // memory location that the driver fills in with
                        // a pointer to the beginning of its response packet

                        // parent this memory object to the workitem so both can be cleaned up together
                        WDF_OBJECT_ATTRIBUTES_INIT (&attributes);
                        attributes.ParentObject = workItem;

                        ntStatus = WdfMemoryCreate(
                                                   &attributes,
                                                   NonPagedPool,
                                                   POOLTAG_KMDF_VDEV,
                                                   sizeof(ULONG),
                                                   &notifyContext->responseMemory,
                                                   &responseQuadlet);

                        if (!NT_SUCCESS(ntStatus) || !responseQuadlet)
                        {
                            DoTraceLevelMessage(TRACE_LEVEL_ERROR, 
                                                TRACE_FLAG_ASYNC, 
                                                "Failed to allocate Reponse Data Memory: %!STATUS!\n",
                                                ntStatus);

                            WdfObjectDelete (workItem);

                            NotifyInfo->ResponseCode = RCODE_DATA_ERROR;
                            break;
                        } 

                        RtlFillMemory(responseQuadlet, sizeof(ULONG), 0x8F);    // dummy data for testing

                        // NotifyInfo->ResponseMdl
                        // initialize MDL for a nonpageable buffer,
                        // and fill the buffer with the response packet
                        MmInitializeMdl(NotifyInfo->ResponseMdl,
                                        responseQuadlet,
                                        sizeof(ULONG));
                        MmBuildMdlForNonPagedPool(NotifyInfo->ResponseMdl);

                        // do what it looks like the New (KMDF) stack expects,
                        // which is that NotifyInfo->ResponsePacket points to the
                        // data following the Async Packet header
                        *NotifyInfo->ResponsePacket = (PVOID)&responseQuadlet;

                        // NotifyInfo->ResponseEvent
                        // memory location that the driver fills in with
                        // the kernel event the bus driver should use to signal
                        // that it has completed sending the response packet
                        KeInitializeEvent(&notifyContext->responseEvent, NotificationEvent, FALSE);

                        *NotifyInfo->ResponseEvent = &notifyContext->responseEvent;

                        // NotifyInfo->ResponseLength
                        // memory location that the driver fills in with
                        // the length of its response packet
                        *NotifyInfo->ResponseLength = sizeof(ULONG);

                        // NotifyInfo->ResponseCode
                        // specifies the result of the driver&#39;s response to the request
                        NotifyInfo->ResponseCode = RCODE_RESPONSE_COMPLETE;

                        // Enqueue the work item to clean up after notification completion
                        WdfWorkItemEnqueue (workItem);

                        DoTraceLevelMessage(TRACE_LEVEL_INFORMATION, 
                                            TRACE_FLAG_ASYNC, 
                                            "Pre-Notification: Read Quadlet: Notify Response Handle %!HANDLE! Data %08x Event %p\n", 
                                            notifyContext->responseMemory, 
                                            *responseQuadlet, 
                                            &notifyContext->responseEvent);

                        break;

                    default: 
                        NotifyInfo->ResponseCode = RCODE_TYPE_ERROR;
                        break;
                } // switch (asyncPacket->AP_tCode)
            } // else [pre-notification params OK]
        } // if (asyncPacket)
        else
        {
            DoTraceLevelMessage(TRACE_LEVEL_ERROR, 
                                TRACE_FLAG_ASYNC, 
                                "Pre-Notification failure: no RequestPacket!\n");
            NotifyInfo->ResponseCode = RCODE_DATA_ERROR;
        }
    }

    ExitS( NotifyInfo->ResponseCode | RCODE_STATUS_MASK );
    return;
} // kmdf1394_NotificationCallback
```

 

 




