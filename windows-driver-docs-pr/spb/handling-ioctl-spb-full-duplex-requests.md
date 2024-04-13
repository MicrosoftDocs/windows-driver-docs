---
title: Handling IOCTL_SPB_FULL_DUPLEX Requests
description: Some buses, such as SPI, enable read and write transfers to simultaneously occur between the bus controller and a device on the bus.
ms.date: 09/14/2021
---

# Handling IOCTL_SPB_FULL_DUPLEX Requests

Some buses, such as SPI, enable read and write transfers to simultaneously occur between the bus controller and a device on the bus. To support these full-duplex transfers, the definition of the simple peripheral bus (SPB) I/O request interface includes, as an option, the [IOCTL_SPB_FULL_DUPLEX](./spb-ioctls.md#ioctl_spb_full_duplex-control-code) I/O control code (IOCTL). Only SPB controller drivers for bus controllers that implement full-duplex transfers in hardware should support the **IOCTL_SPB_FULL_DUPLEX** IOCTL.

If an SPB controller driver supports I/O requests for full-duplex transfers, the driver should use the **IOCTL_SPB_FULL_DUPLEX** IOCTL for these requests, and should follow the implementation guidelines that are presented in this topic. The purpose of these guidelines is to encourage uniform behavior across all hardware platforms that support **IOCTL_SPB_FULL_DUPLEX** requests. Drivers for SPB-connected peripheral devices can then rely on these requests to produce similar results regardless of what platform that they run on.

## Buffer Requirements

An [IOCTL_SPB_FULL_DUPLEX](./spb-ioctls.md#ioctl_spb_full_duplex-control-code) request is formatted the same as an [IOCTL_SPB_EXECUTE_SEQUENCE](./spb-ioctls.md#ioctl_spb_execute_sequence-control-code) request, but with these constraints:

* The [SPB_TRANSFER_LIST](/windows-hardware/drivers/ddi/spb/ns-spb-spb_transfer_list) structure in the request must contain exactly two entries. The first entry describes a buffer that contains data to write to the device. The second entry describes a buffer used to hold data read from the device.
* Each [SPB_TRANSFER_LIST_ENTRY](/windows-hardware/drivers/ddi/spb/ns-spb-spb_transfer_list_entry) structure in the transfer list must specify a **DelayInUs** value of zero.

During a full-duplex transfer, the read and write transfers start in unison. The first byte of write data is transmitted over the bus at the same time as the first byte of read data.

The write and read buffers in the **IOCTL_SPB_FULL_DUPLEX** request are not required to be the same length.

If the read buffer is shorter than the write buffer, the full-duplex bus transfer continues until the entire contents of write buffer are written to the device. After the read buffer is full, the bus controller discards all additional data received from the device until the full-duplex bus transfer completes.

If the write buffer is shorter than the read buffer, the full-duplex bus transfer continues until the read buffer is full. After the entire contents of the write buffer are written to the device, the bus controller writes zeros to the device until the full-duplex bus transfer completes.

If the **IOCTL_SPB_FULL_DUPLEX** request completes successfully, the SPB controller driver sets the **Status** member of the I/O status block to STATUS_SUCCESS, and sets the **Information** member to the total number of bytes transferred (bytes read plus bytes written) during the full-duplex transfer. The count value in the **Information** member should never exceed the sum of the read buffer size and the write buffer size.

If the read buffer is shorter than the write buffer, the count value in the **Information** member should not include the bytes of data that the bus controller reads from the device (and discards) after the read buffer is full. For example, if a full-duplex transfer with a 1-byte write buffer and a 4-byte read buffer completes successfully, the count value should be 5, not 8. Similarly, if the write buffer is shorter than the read buffer, the count value should not include the zeros written to the device after the write buffer is emptied.

## Parameter Checking

Although the [IOCTL_SPB_EXECUTE_SEQUENCE](./spb-ioctls.md#ioctl_spb_execute_sequence-control-code) and **IOCTL_SPB_FULL_DUPLEX** requests have similar formats, they are handled differently by the SPB framework extension (SpbCx). For the **IOCTL_SPB_EXECUTE_SEQUENCE** request, SpbCx validates the parameter values in the request, and captures the request's buffers in the process context of the request originator. SpbCx passes **IOCTL_SPB_EXECUTE_SEQUENCE** requests to the SPB controller driver through the driver's [EvtSpbControllerIoSequence](/windows-hardware/drivers/ddi/spbcx/nc-spbcx-evt_spb_controller_sequence) callback function, which is dedicated to these requests.

In contrast, SpbCx treats the **IOCTL_SPB_FULL_DUPLEX** request as a custom, driver-defined IOCTL request. SpbCx passes **IOCTL_SPB_FULL_DUPLEX** requests to the SPB controller driver through the driver's [EvtSpbControllerIoOther](/windows-hardware/drivers/ddi/spbcx/nc-spbcx-evt_spb_controller_other) callback function, which also handles any custom IOCTL requests that the driver supports. SpbCx does no parameter checking or buffer capture for these requests. The driver is responsible for any parameter checking or buffer capture that might be required for the IOCTL requests that the driver receives through its *EvtSpbControllerIoOther* function. To enable buffer capture, the driver must supply an [EvtIoInCallerContext](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_io_in_caller_context) callback function when the driver registers its *EvtSpbControllerIoOther* function. For more information, see [Using the SPB_TRANSFER_LIST Structure for Custom IOCTLs](./using-the-spb-transfer-list-structure.md).

Typically, the SPB controller driver validates the parameter values in an **IOCTL_SPB_FULL_DUPLEX** request in the *EvtSpbControllerIoOther* function instead of in the *EvtIoInCallerContext* function. The following code example shows how the driver might implement parameter checking. In this example, the driver verifies that the following parameter requirements are satisfied:

* The transfer list in the request contains exactly two entries.
* The first entry in the transfer list is for a write buffer, and the second is for a read buffer.
* The **DelayInUs** value for both entries is zero.

```cpp
//
// Validate the transfer count.
//

SPB_REQUEST_PARAMETERS params;
SPB_REQUEST_PARAMETERS_INIT(&params);
SpbRequestGetParameters(SpbRequest, &params);

if (params.SequenceTransferCount != 2)
{
    //
    // The full-duplex request must have 
    // exactly two transfer descriptors.
    //
    
    status = STATUS_INVALID_PARAMETER;        
    goto exit;
}

//
// Retrieve the write and read transfer descriptors.
//

const ULONG fullDuplexWriteIndex = 0;
const ULONG fullDuplexReadIndex = 1;

SPB_TRANSFER_DESCRIPTOR writeDescriptor;
SPB_TRANSFER_DESCRIPTOR readDescriptor;
PMDL pWriteMdl;
PMDL pReadMdl;

SPB_TRANSFER_DESCRIPTOR_INIT(&writeDescriptor);
SPB_TRANSFER_DESCRIPTOR_INIT(&readDescriptor);

SpbRequestGetTransferParameters(
    SpbRequest, 
    fullDuplexWriteIndex, 
    &writeDescriptor,
    &pWriteMdl);

SpbRequestGetTransferParameters(
    SpbRequest, 
    fullDuplexReadIndex, 
    &readDescriptor,
    &pReadMdl);
    
//
// Validate the transfer direction of each descriptor.
//

if ((writeDescriptor.Direction != SpbTransferDirectionToDevice) ||
    (readDescriptor.Direction != SpbTransferDirectionFromDevice))
{
    //
    // For full-duplex I/O, the direction of the first transfer
    // must be SpbTransferDirectionToDevice, and the direction
    // of the second must be SpbTransferDirectionFromDevice.
    //
    
    status = STATUS_INVALID_PARAMETER;
    goto exit;
}

//
// Validate the delay for each transfer descriptor.
//

if ((writeDescriptor.DelayInUs != 0) || (readDescriptor.DelayInUs != 0))
{
    //
    // The write and read buffers for full-duplex I/O are transferred
    // simultaneously over the bus. The delay parameter in each transfer
    // descriptor must be set to 0.
    //
    
    status = STATUS_INVALID_PARAMETER;
    goto exit;
}

MyDriverPerformFullDuplexTransfer(
    pDevice, 
    pRequest,
    writeDescriptor,
    pWriteMdl,
    readDescriptor,
    pReadMdl);
```

After checking the parameter values, the preceding code example calls a driver-internal routine, named `MyDriverPerformFullDuplexTransfer`, to initiate the full-duplex I/O transfer.
