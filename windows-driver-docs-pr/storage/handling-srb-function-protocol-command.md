---
title: Handling SRB_FUNCTION_PROTOCOL_COMMAND
description: Handling SRB_FUNCTION_PROTOCOL_COMMAND
keywords:
- SCSI miniport drivers WDK storage , HwScsiStartIo
- HwScsiStartIo
- SRB_FUNCTION_PROTOCOL_COMMAND
ms.date: 05/23/2019
---

# Handling SRB_FUNCTION_PROTOCOL_COMMAND

A miniport driver handles SRB_FUNCTION_PROTOCOL_COMMAND requests when the HBA is to provide dedicated support for a user-mode application. Supporting this request allows a set of driver-defined ("private") protocol commands to be sent directly to the miniport driver.

For SRBs with the **Function** member set to SRB_FUNCTION_PROTOCOL_COMMAND, the **DataBuffer** member contains a pointer to a system-defined [STORAGE_PROTOCOL_COMMAND](/windows-hardware/drivers/ddi/ntddstor/ns-ntddstor-_storage_protocol_command) structure.

The miniport should do the following:

* Translate the command information provided in the STORAGE_PROTOCOL_COMMAND structure into the appropriate protocol-specific bus command. The protocol is identified by **\*Data->Buffer.ProtocolType**.

* For WRITE-type requests, transfer the data to which **DataToDeviceBufferOffset** points to the device.

* For READ-type requests, transfer data from the device to the buffer that **DataFromDeviceBufferOffset** points to.

* Set **ReturnStatus** to reflect the status of the request, and optionally set **ErrorCode**.

## See Also

[IOCTL_STORAGE_PROTOCOL_COMMAND (*winioctl.h*)](/windows/win32/api/winioctl/ni-winioctl-ioctl_storage_protocol_command)

[IOCTL_STORAGE_PROTOCOL_COMMAND (*ntddstor.h*)](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_protocol_command)

[HwStorStartIo](/windows-hardware/drivers/ddi/storport/nc-storport-hw_startio)

[SRB_IO_CONTROL](/windows-hardware/drivers/ddi/ntddscsi/ns-ntddscsi-_srb_io_control)

[SCSI_REQUEST_BLOCK](/windows-hardware/drivers/ddi/srb/ns-srb-_scsi_request_block)

[STORAGE_PROTOCOL_COMMAND](/windows-hardware/drivers/ddi/ntddstor/ns-ntddstor-_storage_protocol_command)

[STORAGE_REQUEST_BLOCK](/windows-hardware/drivers/ddi/srb/ns-srb-_storage_request_block)
