---
title: FLT_PARAMETERS for IRP_MJ_QUERY_SECURITY union
description: Union component used when the MajorFunction field of the FLT_IO_PARAMETER_BLOCK structure for the operation is IRP_MJ_QUERY_SECURITY.
keywords: ["FLT_PARAMETERS for IRP_MJ_QUERY_SECURITY union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FLT_PARAMETERS
api_location:
- fltkernel.h
api_type:
- HeaderDef
ms.date: 03/13/2023
ms.topic: reference
---

# FLT_PARAMETERS for IRP_MJ_QUERY_SECURITY union

Union component used when the **MajorFunction** field of the [**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure for the operation is [**IRP_MJ_QUERY_SECURITY**](irp-mj-query-security.md).

## Syntax

``` C
typedef union _FLT_PARAMETERS {
  ...    ;
  struct {
    SECURITY_INFORMATION    SecurityInformation;
    ULONG POINTER_ALIGNMENT Length;
    PVOID                   SecurityBuffer;
    PDML                    MdlAddress;
  } QuerySecurity;
  ...    ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

## Members

- **QuerySecurity**: Structure containing the following members.

- **SecurityInformation**: Pointer to a caller-supplied [**SECURITY_INFORMATION**](security-information.md) value that specifies the security information to be queried. One of the following:

  | SecurityInformation Value | Meaning |
  | ------------------------- | ------- |
  | OWNER_SECURITY_INFORMATION | The owner identifier of the object is being queried. Requires READ_CONTROL access. |
  | GROUP_SECURITY_INFORMATION | The primary group identifier of the object is being queried. Requires READ_CONTROL access. |
  | DACL_SECURITY_INFORMATION | The discretionary access control list (DACL) of the object is being queried. Requires READ_CONTROL access. |
  | SACL_SECURITY_INFORMATION | The system ACL (SACL) of the object is being queried. Requires ACCESS_SYSTEM_SECURITY access. |

- **Length**: Length, in bytes, of the buffer that **SecurityBuffer** points to.

- **SecurityBuffer**: Pointer to a caller-supplied output buffer that receives a copy of the security descriptor of the specified object. The calling process must have the right to view the specified aspects of the object's security status. The [**SECURITY_DESCRIPTOR**](/previous-versions/windows/hardware/drivers/ff556610(v=vs.85)) structure is returned in self-relative format. This member is optional and can be NULL if a MDL is provided in **MdlAddress**. See **Remarks**.

- **MdlAddress**: Address of a memory descriptor list (MDL) that describes the buffer that **SecurityBuffer** points to. This member is optional and can be **NULL** if a buffer is provided in **SecurityBuffer**. See **Remarks**.

## Remarks

The [**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) structure for [**IRP_MJ_QUERY_SECURITY**](irp-mj-query-security.md) operations contains the parameters for an IRP-based query-security-information operation represented by a callback data ([**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)) structure. It is contained in an [**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure.

If both a **SecurityBuffer** and **MdlAddress** buffer are provided, it is recommended that minifilters use the MDL. The memory that **SecurityBuffer** points to is valid when it is a user mode address being accessed within the context of the calling process, or if it is a kernel mode address.

If a minifilter changes the value of **MdlAddress**, then after its post operation callback, Filter Manager will free the MDL currently stored in **MdlAddress** and restore the previous value of **MdlAddress**.

On Windows XP and later, the object that the **TargetFileObject** member of the FLT_IO_PARAMETER_BLOCK structure points to can represent a named data stream. For more information about named data streams, see [**FILE_STREAM_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_stream_information).

IRP_MJ_QUERY_SECURITY is an IRP-based operation.

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Header | *Fltkernel.h* (include *Fltkernel.h*) |

## See also

[**FILE_STREAM_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_stream_information)

[**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)

[**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block)

[**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters)

[**IRP_MJ_QUERY_SECURITY**](irp-mj-query-security.md)

[**SECURITY_DESCRIPTOR**](/previous-versions/windows/hardware/drivers/ff556610(v=vs.85))

[**SECURITY_INFORMATION**](security-information.md)
