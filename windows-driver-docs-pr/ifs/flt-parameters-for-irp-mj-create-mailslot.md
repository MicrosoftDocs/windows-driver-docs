---
title: FLT_PARAMETERS for IRP_MJ_CREATE_MAILSLOT Union
description: The following union component is used when the MajorFunction field of the FLT_IO_PARAMETER_BLOCK structure for the operation is IRP_MJ_CREATE_MAILSLOT.
keywords:
- FLT_PARAMETERS for IRP_MJ_CREATE_MAILSLOT union File System Drivers
- FLT_PARAMETERS union File System Drivers
- PFLT_PARAMETERS union pointer File System Drivers
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

# FLT_PARAMETERS for IRP_MJ_CREATE_MAILSLOT union

The following structure within the [FLT_PARAMETERS](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) union is used when the **MajorFunction** field of the [FLT_IO_PARAMETER_BLOCK](/windows-hardware/drivers/ddi/content/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure is [IRP_MJ_CREATE_MAILSLOT](irp-mj-create-mailslot.md).

## Syntax

``` C
typedef union _FLT_PARAMETERS {
  ...    ;
  struct {
    PIO_SECURITY_CONTEXT     SecurityContext;
    ULONG                    Options;
    USHORT POINTER_ALIGNMENT Reserved;
    USHORT                   ShareAccess;
    PVOID                    Parameters;
  } CreateMailslot;
  ...    ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

## Members

The **CreateMailslot** structure of FLT_PARAMETERS contains the following members.

- **SecurityContext**: Pointer to an [IO_SECURITY_CONTEXT](/windows-hardware/drivers/ddi/content/wdm/ns-wdm-_io_security_context) structure that represents the security context of an IRP_MJ_CREATE_MAILSLOT request, where:

- **SecurityContext->AccessState** is a pointer to an [ACCESS_STATE](/windows-hardware/drivers/ddi/wdm/ns-wdm-_access_state) structure that contains the object's subject context, granted access types, and remaining desired access types.

- **SecurityContext->DesiredAccess** is an [ACCESS_MASK](../kernel/access-mask.md) structure that specifies access rights requested for the mailslot. For more information, see the *DesiredAccess* parameter of [**FltCreateMailslotFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcreatemailslotfile).

- **Options**: Bitmask of flags that specify the options to be applied when creating or opening the mailslot, as well as the action to be taken if the mailslot already exists. The low 24 bits of this member correspond to the *CreateOptions* parameter for **FltCreateMailslotFile**. The high 8 bits correspond to the *CreateDisposition* parameter for **FltCreateMailslotFile**.

- **Reserved**: Reserved; do not use.

- **ShareAccess**: Bitmask of share access rights requested for the mailslot file. If this parameter is zero, exclusive access is being requested. For more information, see the *ShareAccess* parameter to [**FltCreateMailslotFile**](/windows-hardware/drivers/ddi/content/fltkernel/nf-fltkernel-fltcreatemailslotfile).

- **Parameters**: Pointer to a [MAILSLOT_CREATE_PARAMETERS](/windows-hardware/drivers/ddi/wdm/ns-wdm-_mailslot_create_parameters) structure containing information about the mailslot that is being created or opened.

## Remarks

[FLT_PARAMETERS](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) contains a **CreateMailslot** structure when the I/O operation is IRP_MJ_CREATE_MAILSLOT. The I/O operation is represented by a [FLT_CALLBACK_DATA](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data) structure, with the operation parameters contained within the [FLT_IO_PARAMETER_BLOCK](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure that the callback data's *Iopb* parameter points to.

A file system minifilter driver that has registered a callback routine for IRP_MJ_CREATE_MAILSLOT operations should perform any needed processing and return.

Note that, other than the last longword field, the fields in the **CreateMailslot** structure must match those for the **Create** structure.

IRP_MJ_CREATE_MAILSLOT is an IRP-based operation.

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Header | *Fltkernel.h* (include *Fltkernel.h*) |

## See also

[ACCESS_MASK](../kernel/access-mask.md)

[ACCESS_STATE](/windows-hardware/drivers/ddi/content/wdm/ns-wdm-_access_state)

[FLT_CALLBACK_DATA](/windows-hardware/drivers/ddi/content/fltkernel/ns-fltkernel-_flt_callback_data)

[FLT_IO_PARAMETER_BLOCK](/windows-hardware/drivers/ddi/content/fltkernel/ns-fltkernel-_flt_io_parameter_block)

[FLT_PARAMETERS](/windows-hardware/drivers/ddi/content/fltkernel/ns-fltkernel-_flt_parameters)

[**FltCreateMailslotFile**](/windows-hardware/drivers/ddi/content/fltkernel/nf-fltkernel-fltcreatemailslotfile)

[IRP_MJ_CREATE_MAILSLOT](irp-mj-create-mailslot.md)

[MAILSLOT_CREATE_PARAMETERS](/windows-hardware/drivers/ddi/wdm/ns-wdm-_mailslot_create_parameters)
