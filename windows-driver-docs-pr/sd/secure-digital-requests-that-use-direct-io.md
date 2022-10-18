---
title: Secure Digital Requests That Use Direct I/O (Windows Drivers)
description: Learn more about Securing Digital Requests That Use Direct I/O.
ms.date: 10/17/2022
---

# Secure Digital Requests That Use Direct I/O

The following code example illustrates how a driver uses a command request to retrieve the contents of a device's function basic register (FBR). Since the amount of data retrieved is small, the example uses a direct I/O command (called CMD52 in the SD specification), which instructs the bus driver to transmit the data across the CMD line. To see a code example that illustrates how to use extended I/O (called CMD53 in the SD specification), see [Secure Digital Requests That Use Extended I/O](secure-digital-requests-that-use-extended-io.md).

```cpp
    const SDCMD_DESCRIPTOR ReadIoDirectDesc =
    {SDCMD_IO_RW_DIRECT, SDCC_STANDARD, SDTD_READ,
    SDTT_CMD_ONLY, SDRT_5};
    
    PSDBUS_REQUEST_PACKET sdrp = NULL;
    SD_RW_DIRECT_ARGUMENT sdIoArgument;
    
    sdrp = ExAllocatePool(NonPagedPool, 
        sizeof(SDBUS_REQUEST_PACKET));
    if (!sdrp) {
        return STATUS_INSUFFICIENT_RESOURCES;
    }
    RtlZeroMemory(sdrp, sizeof(SDBUS_REQUEST_PACKET));
    sdrp->RequestFunction = SDRF_DEVICE_COMMAND;
    sdrp->Parameters.DeviceCommand.CmdDesc = ReadIoDirectDesc;
    
    // Set up the argument and command descriptor
    
    sdIoArgument.u.AsULONG = 0;
    sdIoArgument.u.bits.Address = Offset;
    
    // Function # must be initialized by SdBus GetProperty call
    
    sdIoArgument.u.bits.Function = pDevExt->FunctionNumber;
    sdrp->Parameters.DeviceCommand.Argument = sdIoArgument.u.AsULONG;
    
    // Submit the request
    
    status = SdBusSubmitRequest(pDevExt->BusInterface.Context, sdrp);
    
    if (NT_SUCCESS(status)) {
        // for direct I/O, the data comes in the response
        *Data = sdrp->ResponseData.AsUCHAR[0];
    }
    ExFreePool(sdrp);
```

To read the FBR, the code example performs the following steps:

1. **Initialize the Descriptor**

   The first step in sending a device-command request is to define an SD command descriptor, [**SDCMD\_DESCRIPTOR**](/windows-hardware/drivers/ddi/sddef/ns-sddef-_sdcmd_descriptor). Typically, a descriptor is defined as a constant data structure. The descriptor in the code example defines a read operation with the following elements:

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
   <td><p>The operation defined by the descriptor reads a single byte of data from the FBR, so the code example uses a direct I/O command (CMD52), which instructs the card to report the requested data across the CMD line and not the DAT lines. The code example indicates a direct I/O command by assigning a value of SDCMD_IO_RW_DIRECT to this member.</p></td>
   </tr>
   <tr class="even">
   <td><p><a href="/windows-hardware/drivers/ddi/sddef/ne-sddef-sd_command_class"><strong>SD_COMMAND_CLASS</strong></a></p></td>
   <td><p>Read operations belong to the standard command set (command codes 0 to 63), so the value assigned to this member of the descriptor is SDCC_STANDARD.</p></td>
   </tr>
   <tr class="odd">
   <td><p><a href="/windows-hardware/drivers/ddi/sddef/ne-sddef-sd_transfer_direction"><strong>SD_TRANSFER_DIRECTION</strong></a></p></td>
   <td><p>Read operations require a transfer from the device to the host, so the value assigned to this member of the descriptor is SDTD_READ.</p></td>
   </tr>
   <tr class="even">
   <td><p><a href="/windows-hardware/drivers/ddi/sddef/ne-sddef-sd_transfer_type"><strong>SD_TRANSFER_TYPE</strong></a></p></td>
   <td><p>This operation reads a small amount of data from a register over the CMD line. The card does not have to send data over the DAT lines, therefore, this member is assigned a value of SDTT_CMD_ONLY.</p></td>
   </tr>
   <tr class="odd">
   <td><p><a href="/windows-hardware/drivers/ddi/sddef/ne-sddef-sd_response_type"><strong>SD_RESPONSE_TYPE</strong></a></p></td>
   <td><p>The descriptor specifies a response type of SDRT_5, which means that the card must notify the host that the operation has completed with an interrupt request. For an explanation of the R5 response, see the <em>MultiMedia Card Association</em> specification.</p></td>
   </tr>
   </tbody>
   </table>

1. **Initialize the Request Packet** by completing the following steps:

   1. **Define the Request Function**:

      After creating an SD descriptor, the code example initializes the request packet, [**SDBUS\_REQUEST\_PACKET**](/previous-versions/windows/hardware/drivers/ff537931(v=vs.85).md). The **RequestFunction** member of the request packet specifies whether the request contains a device command (value of SDRF\_DEVICE\_COMMAND) or a property operation (value of SDRF\_GET\_PROPERTY or SDRF\_SET\_PROPERTY). The code example initiates a device command, so it sets the **RequestFunction** member to SDRF\_DEVICE\_COMMAND.

   1. **Load the Command Descriptor**: Next, the code example stores the newly initialized descriptor in the **Parameters.DeviceCommand.CmdDesc** member of the request packet.

   1. **Initialize the Read/Write Argument**:

        The request packet contains an [**SD\_RW\_DIRECT\_ARGUMENT**](/windows-hardware/drivers/ddi/sddef/ns-sddef-sd_rw_direct_argument) structure that holds the location of the data that the bus driver retrieves. This structure also stores the number of the function whose I/O space from which the bus driver reads. The example code retrieves the function number from the device extension, which implies that the driver previously retrieved the information from the card (probably when it started the device) with an SDRF\_GET\_PROPERTY request and stored it in the device extension.

1. **Submit the Request**

   After initializing the descriptor and the request packet, the code example uses the synchronous request routine, [**SdBusSubmitRequest**](/windows-hardware/drivers/ddi/ntddsd/nf-ntddsd-sdbussubmitrequest), to submit the request. The request routine passes in the request packet and the interface context information that the system provided to the driver when it opened the SD interface. Because this is a synchronous request, the driver must be running at IRQL less than DISPATCH\_LEVEL.

1. **Results of the Command**

   Because the code example uses direct I/O, no data buffer is required other than the **ResponseData** field in the SD request packet.
