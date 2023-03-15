---
title: Secure Digital Requests That Use Extended I/O (Windows Drivers)
description: Learn more about Securing Digital Requests That Use Extended I/O.
ms.date: 03/03/2023
---

# Secure Digital Requests That Use Extended I/O

Secure Digital (SD) requests that read or write more than just a couple of bytes of data must use an extended I/O command (referred to as CMD53 in the SD specification). The extended I/O command instructs the bus driver to transmit data over the SD card's DAT lines. The characteristics of a data transfer depend on the capabilities of the SD controller. For instance, some controllers only allow programmable I/O (PIO); others permit direct memory access (DMA). For maximum compatibility across different SD controller types, device drivers should load the request packet with a pointer to an MDL that describes the data buffer. The device driver must construct its own MDL, unless a driver in a higher layer constructs the MDL and passes it down to the device driver.

The following code example shows how a driver could perform an extended I/O request using a data buffer described by an MDL. This code example is similar in format to the direct I/O code example described in [Secure Digital Requests That Use Direct I/O](secure-digital-requests-that-use-direct-io.md), therefore it might be helpful to study the direct I/O code example before studying the extended I/O code example.

The principle difference between the two examples is that the extended I/O code example illustrates how to use MDLs with an SD request. There are also slight differences in the way descriptors and request packets are defined for direct and extended I/O.

```cpp
    const SDCMD_DESCRIPTOR WriteIoExtendedDesc =
    {SDCMD_IO_RW_EXTENDED, SDCC_STANDARD,
    SDTD_WRITE, SDTT_SINGLE_BLOCK, SDRT_1};
    
    // first, get an MDL to map the data. Call IoAllocateMdl to
    // allocate an MDL and pass in a pointer to a buffer  
    // allocated from the non-paged pool.
    
    mdl = IoAllocateMdl(Data, Length, FALSE, FALSE, NULL);
    
    if (mdl == NULL) {
      return STATUS_INSUFFICIENT_RESOURCES;
    }
    
    MmBuildMdlForNonPagedPool (mdl);
    
    // next, allocate a request packet for the arguments of the command
     
    sdrp = ExAllocatePool(NonPagedPool, sizeof(SDBUS_REQUEST_PACKET));
    
    if (!sdrp) {
      IoFreeMdl(mdl);
      return STATUS_INSUFFICIENT_RESOURCES;
    }
    RtlZeroMemory(sdrp, sizeof(SDBUS_REQUEST_PACKET));
    sdrp->RequestFunction = SDRF_DEVICE_COMMAND;
    sdrp->Parameters.DeviceCommand.CmdDesc = 
    WriteIoExtendedDesc;
    
    // then, set up the argument and command descriptor
    sdIoArgument.u.AsULONG = 0;
    sdIoArgument.u.bits.Address = Offset;
    
    // retrieve function number, the driver previously initialized 
    // this value with the SdBus GetProperty call
    sdIoArgument.u.bits.Function = pDevExt->FunctionNumber;
    sdIoArgument.u.bits.WriteToDevice = 1;
    
    sdrp->Parameters.DeviceCommand.Argument = 
        sdIoArgument.u.AsULONG;
    
    sdrp->Parameters.DeviceCommand.Mdl = mdl;
    sdrp->Parameters.DeviceCommand.Length = Length;
    // finally, submit the request
    status = SdBusSubmitRequest(pDevExt->BusInterface.Context,sdrp);
    
    IoFreeMdl(mdl);
    ExFreePool(sdrp);
```

This code example includes the following steps:

1. **Initialize the Descriptor**

   The first step in sending a device-command request is to define an SD command descriptor, [**SDCMD\_DESCRIPTOR**](/windows-hardware/drivers/ddi/sddef/ns-sddef-_sdcmd_descriptor). The descriptor in the code example defines an extended I/O write operation with the following elements:

   <table>
   <thead>
   <tr class="header">
   <th>Element</th>
   <th>Description</th>
   </tr>
   </thead>
   <tbody>
   <tr class="odd">
   <td><p><a href="/windows-hardware/drivers/ddi/sddef/ns-sddef-_sdcmd_descriptor#members">SD_COMMAND_CODE</a></p></td>
   <td><p>The operation defined by the descriptor performs an extended I/O write, so the value of the command code is SDCMD_IO_RW_DIRECT.</p></td>
   </tr>
   <tr class="even">
   <td><p><a href="/windows-hardware/drivers/ddi/sddef/ne-sddef-sd_command_class"><strong>SD_COMMAND_CLASS</strong></a></p></td>
   <td><p>Extended I/O write operations belong to the standard command set (command codes 0 to 63), so the value assigned to this member of the descriptor is SDCC_STANDARD.</p></td>
   </tr>
   <tr class="odd">
   <td><p><a href="/windows-hardware/drivers/ddi/sddef/ne-sddef-sd_transfer_direction"><strong>SD_TRANSFER_DIRECTION</strong></a></p></td>
   <td><p>Write operations require a transfer from the host to the device, so the value assigned to this member of the descriptor is SDTD_WRITE.</p></td>
   </tr>
   <tr class="even">
   <td><p><a href="/windows-hardware/drivers/ddi/sddef/ne-sddef-sd_transfer_type"><strong>SD_TRANSFER_TYPE</strong></a></p></td>
   <td><p>The descriptor for an extended I/O write operation must include a transfer type. The code example specifies a single block write, SDTT_SINGLE_BLOCK, which indicates that the host writes one block of data to the device. The driver established the size of a block by a prior SET_BLOCKLEN command (not illustrated in this code example). For an explanation of the SET_BLOCKLEN command and the SDTT_SINGLE_BLOCK transfer type, see <em>The MultiMedia Card</em> specification, published by the MultiMedia Card Association (MMCA) technical committee.</p></td>
   </tr>
   <tr class="odd">
   <td><p><a href="/windows-hardware/drivers/ddi/sddef/ne-sddef-sd_response_type"><strong>SD_RESPONSE_TYPE</strong></a></p></td>
   <td><p>The descriptor specifies a response type of SDRT_1, which specifies a standard R1 response to the command and contains status data. For an explanation of the R1 response, see the <em>MultiMedia Card Association</em> specification.</p></td>
   </tr>
   </tbody>
   </table>

1. **Set Up the MDL**

   Call [**IoAllocateMdl**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocatemdl) to allocate an MDL and pass in a pointer to a buffer allocated from non-paged pool. Next, the [**MmBuildMdlForNonPagedPool**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmbuildmdlfornonpagedpool) routine takes the newly allocated MDL that specifies a virtual memory buffer in non-paged pool and updates it to describe the underlying physical pages. Callers of **MmBuildMdlForNonPagedPool** must be running at IRQL \<= DISPATCH\_LEVEL.

1. **Initialize the Request Packet** by completing the following steps:

   - **Define the Request Function**:

     After creating an SD descriptor, the code example initializes the request packet, [**SDBUS\_REQUEST\_PACKET**](/previous-versions/windows/hardware/drivers/ff537931(v=vs.85)). The **RequestFunction** member of the request packet specifies whether the request contains a device command (value of SDRF\_DEVICE\_COMMAND) or a property operation (value of SDRF\_GET\_PROPERTY or SDRF\_SET\_PROPERTY). The code example is sending a device command, so it sets the **RequestFunction** member to SDRF\_DEVICE\_COMMAND.

   - **Load the Command Descriptor**. Next, the code example stores the newly initialized descriptor in the **Parameters.DeviceCommand.CmdDesc** member of the request packet.

   - **Initialize the Read/Write Argument**:

     The request packet contains an [**SD\_RW\_DIRECT\_ARGUMENT**](/windows-hardware/drivers/ddi/sddef/ns-sddef-sd_rw_direct_argument) structure with the location to which the bus driver writes. This structure also stores the number of the function whose I/O space the bus driver reads from. The code example retrieves the function number from the device extension, which implies that the driver previously retrieved this information from the card (probably when it started the device with an SDRF\_GET\_PROPERTY request and stored it in the device extension.

1. **Submit the Request**

   After initializing the descriptor and the request packet, the example uses the synchronous request routine, [**SdBusSubmitRequest**](/windows-hardware/drivers/ddi/ntddsd/nf-ntddsd-sdbussubmitrequest) to submit the request. It passes in the request packet and the interface context information that the system provided to the driver when it opened the SD interface. Because this is a synchronous request, the driver must be running at IRQL less than DISPATCH\_LEVEL.

1. **Results of the Command**

   Because the code example uses a direct I/O command, no data buffer other than the **ResponseData** field in the SD request packet.

The code example allocates a data transfer buffer from non-paged pool. A driver can use **PagedPool** for a data transfer buffer, provided it locks down the pages. However, drivers must *always* allocate data transfer buffers from non-paged pool when doing SDRF\_GET\_PROPERTY and SDRF\_SET\_PROPERTY requests. Drivers must also allocate SD request packets from non-paged pool because the completion routine of the IRP that accompanies the SD request might run in a deferred procedure call (DPC).

For all kinds of requests, there are performance benefits to allocating buffers from non-paged pool when the buffers are small and the driver holds them briefly.
