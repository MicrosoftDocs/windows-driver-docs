---
title: FLT_PARAMETERS for IRP_MJ_SET_SECURITY Union
description: Union component used when the MajorFunction field of the FLT_IO_PARAMETER_BLOCK structure for the operation is IRP_MJ_SET_SECURITY.
keywords: ["FLT_PARAMETERS for IRP_MJ_SET_SECURITY union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
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

# FLT_PARAMETERS for IRP_MJ_SET_SECURITY union

Union component used when the **MajorFunction** field of the [**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure for the operation is [**IRP_MJ_SET_SECURITY**](irp-mj-set-security.md).

## Syntax

``` C
typedef union _FLT_PARAMETERS {
  ...    ;
  struct {
    SECURITY_INFORMATION SecurityInformation;
    PSECURITY_DESCRIPTOR SecurityDescriptor;
  } SetSecurity;
  ...    ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

## Members

- **SetSecurity**: Structure containing the following members.

- **SecurityInformation**: Pointer to a [**SECURITY_INFORMATION**](security-information.md) value that specifies which security information is to be set in the security descriptor. This value can be one of the following.

  | SecurityInformation Value | Meaning |
  | ------------------------- | ------- |
  | DACL_SECURITY_INFORMATION | The discretionary access control list (DACL) of the object is being set. Requires WRITE_DAC access. |
  | GROUP_SECURITY_INFORMATION | The primary group identifier of the object is being set. Requires WRITE_OWNER access. |
  | OWNER_SECURITY_INFORMATION | The owner identifier of the object is being set. Requires WRITE_OWNER access. |
  | SACL_SECURITY_INFORMATION | The system ACL (SACL) of the object is being set. Requires ACCESS_SYSTEM_SECURITY access.

- **SecurityDescriptor**: Pointer to a [**SECURITY_DESCRIPTOR**](/previous-versions/windows/hardware/drivers/ff556610(v=vs.85)) structure that contains the values of the security information to be assigned to the object.

## Remarks

The [**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) structure for [**IRP_MJ_SET_SECURITY**](irp-mj-set-security.md) operations contains the parameters for a set-security-information operation represented by a callback data ([**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)) structure. It is contained in an FLT_IO_PARAMETER_BLOCK structure.

IRP_MJ_SET_SECURITY is an IRP-based operation.

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Header | *Fltkernel.h* (include *Fltkernel.h*) |

## See also

[**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)

[**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block)

[**FLT_IS_FASTIO_OPERATION**](/windows-hardware/drivers/ddi/index)

[**FLT_IS_FS_FILTER_OPERATION**](/previous-versions/ff544648(v=vs.85))

[**FLT_IS_IRP_OPERATION**](/previous-versions/ff544654(v=vs.85))

[**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters)

[**IRP_MJ_SET_SECURITY**](irp-mj-set-security.md)

[**SECURITY_DESCRIPTOR**](/previous-versions/windows/hardware/drivers/ff556610(v=vs.85))

[**SECURITY_INFORMATION**](security-information.md)
