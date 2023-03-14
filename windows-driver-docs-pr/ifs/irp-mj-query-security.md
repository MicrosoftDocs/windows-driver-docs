---
title: IRP_MJ_QUERY_SECURITY (FS and filter drivers)
description: IRP_MJ_QUERY_SECURITY
keywords: ["IRP_MJ_QUERY_SECURITY Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_QUERY_SECURITY
api_type:
- NA
ms.date: 03/13/2023
ms.topic: reference
---

# IRP_MJ_QUERY_SECURITY (FS and filter drivers)

## When Sent

The I/O Manager sends the IRP_MJ_QUERY_SECURITY request. It can be sent, for example, when a user-mode application has called a Win32 function such as [**GetSecurityInfo**](/windows/win32/api/aclapi/nf-aclapi-getsecurityinfo).

## Operation: File System Drivers

The file system driver should extract and decode the file object to determine whether it represents a user file or directory open. If it does, the driver should process the query and complete the IRP. Otherwise, the driver should complete the IRP as appropriate without processing the query.

## Operation: Legacy File System Filter Drivers

The filter driver should pass this IRP down to the next-lower driver on the stack.

## Parameters

A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation) for the given IRP to get a pointer to its own stack location in the IRP. In the following parameters, **Irp** points to the [**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp) and **IrpSp** points to the [**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location). The driver can use the information that is set in the following members of the IRP and the IRP stack location to process a query security request:

- **DeviceObject** is a pointer to the target device object.

- **Irp->IoStatus** points to an [**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block) structure that receives the final completion status and information about the requested operation.

- **Irp->UserBuffer** points to a caller-supplied output buffer that receives a copy of the security descriptor of the specified object. The calling process must have the right to view the specified aspects of the object's security status. The [**SECURITY_DESCRIPTOR**](/previous-versions/windows/hardware/drivers/ff556610(v=vs.85)) structure is returned in self-relative format.

- **IrpSp->FileObject** points to the file object that is associated with *DeviceObject*.

  On Windows XP and later, the file object can represent a named data stream. For more information about named data streams, see [**FILE_STREAM_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_stream_information).

  The **IrpSp->FileObject** parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE_OBJECT structure. The **RelatedFileObject** field of the FILE_OBJECT structure isn't valid during the processing of IRP_MJ_QUERY_SECURITY and shouldn't be used.

- **IrpSp->MajorFunction** is set to IRP_MJ_QUERY_SECURITY.

- **IrpSp->Parameters.QuerySecurity.Length** is the size, in bytes, of the buffer pointed to by the **Irp->UserBuffer** parameter.

- **IrpSp->Parameters.QuerySecurity.SecurityInformation** points to the [**SECURITY_INFORMATION**](security-information.md) structure for the operation. This value can be a valid combination of the following bits.

  | SecurityInformation Value | Meaning |
  | ------------------------- | ------- |
  | OWNER_SECURITY_INFORMATION | Indicates that the owner identifier of the object is being queried. Requires READ_CONTROL access. |
  | GROUP_SECURITY_INFORMATION | Indicates that the primary group identifier of the object is being queried. Requires READ_CONTROL access. |
  | DACL_SECURITY_INFORMATION | Indicates that the discretionary access control list (DACL) of the object is being queried. Requires READ_CONTROL access. |
  | SACL_SECURITY_INFORMATION | Indicates that the system ACL (SACL) of the object is being queried. Requires ACCESS_SYSTEM_SECURITY access. |

## See also

[**FILE_STREAM_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_stream_information)

[**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location)

[**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block)

[**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation)

[**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp)

[**IRP_MJ_SET_SECURITY**](irp-mj-set-security.md)

[**SECURITY_DESCRIPTOR**](/previous-versions/windows/hardware/drivers/ff556610(v=vs.85))

[**SECURITY_INFORMATION**](security-information.md)
