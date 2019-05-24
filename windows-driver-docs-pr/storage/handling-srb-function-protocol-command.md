---
title: Handling SRB_FUNCTION_PROTOCOL_COMMAND
description: Handling SRB_FUNCTION_PROTOCOL_COMMAND
ms.assetid: 12e9791b-8ddf-4d42-9d89-243bc38eeeb7
keywords:
- SCSI miniport drivers WDK storage , HwScsiStartIo
- HwScsiStartIo
- SRB_FUNCTION_PROTOCOL_COMMAND
ms.date: 05/23/2019
ms.localizationpriority: medium
---

# Handling SRB_FUNCTION_PROTOCOL_COMMAND

A miniport driver handles SRB_FUNCTION_PROTOCOL_COMMAND requests when the HBA is to provide dedicated support for a user-mode application. Supporting this request allows a set of driver-defined ("private") protocol commands to be sent directly to the miniport driver.

For SRBs with the **Function** member set to SRB_FUNCTION_PROTOCOL_COMMAND, the **DataBuffer** member contains a pointer to a system-defined [STORAGE_PROTOCOL_COMMAND](https://docs.microsoft.com/windows/desktop/api/winioctl/ns-winioctl-_storage_protocol_command) structure.

**VISHAL: WHAT DOES MINIPORT NEED TO DO WHEN IT RECEIVES SRB_FUNCTION_PROTOCOL_COMMAND???**

* **what error conditions does it look for? does it return error codes - which ones?**
* **what else does it need to do?**

**VISHAL: Should I link to both SCSI and STOR versions of StartIo and SRB in See Also Section??**

## See Also

[IOCTL_STORAGE_PROTOCOL_COMMAND (*winioctl.h*)](https://docs.microsoft.com/windows/desktop/api/winioctl/ni-winioctl-ioctl_storage_protocol_command)

[IOCTL_STORAGE_PROTOCOL_COMMAND (*ntddstor.h*)](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddstor/ni-ntddstor-ioctl_storage_protocol_command)

[HwScsiStartIo](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/srb/nc-srb-phw_startio)

[HwStorStartIo](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nc-storport-hw_startio)

[SRB_IO_CONTROL](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddscsi/ns-ntddscsi-_srb_io_control)

[SCSI_REQUEST_BLOCK](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/srb/ns-srb-_scsi_request_block)

[STORAGE_REQUEST_BLOCK](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/srb/ns-srb-_storage_request_block)