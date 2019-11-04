---
title: FLT_PARAMETERS for IRP_MJ_CREATE_NAMED_PIPE union
description: The following union component is used when the MajorFunction field of the FLT_IO_PARAMETER_BLOCK structure for the operation is IRP_MJ_CREATE_NAMED_PIPE.
ms.assetid: cbe7e523-3ae2-424b-a2e2-edaeb64c15c5
keywords: ["FLT_PARAMETERS for IRP_MJ_CREATE_NAMED_PIPE union File System Drivers", "FLT_PARAMETERS union File System Drivers", "PFLT_PARAMETERS union pointer File System Drivers"]
topic_type:
- apiref
api_name:
- FLT_PARAMETERS
api_location:
- fltkernel.h
api_type:
- HeaderDef
ms.date: 11/05/2019
ms.localizationpriority: medium
---

# FLT_PARAMETERS for IRP_MJ_CREATE_NAMED_PIPE union

The following structure within the [FLT_PARAMETERS](https://docs.microsoft.com/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) union is used when the **MajorFunction** field of the [FLT_IO_PARAMETER_BLOCK](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure is [IRP_MJ_CREATE_NAMED_PIPE](irp-mj-create-named-pipe.md).

## Syntax

```ManagedCPlusPlus
typedef union _FLT_PARAMETERS {
  ...    ;
  struct {
    PIO_SECURITY_CONTEXT     SecurityContext;
    ULONG                    Options;
    USHORT POINTER_ALIGNMENT Reserved;
    USHORT                   ShareAccess;
    PVOID                    Parameters;
  } CreatePipe;
  ...    ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

## Members

The **CreatePipe** structure of FLT_PARAMETERS contains the following members.

**SecurityContext**  
Pointer to an [IO_SECURITY_CONTEXT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/ns-wdm-_io_security_context) structure that represents the security context of an IRP_MJ_CREATE_NAMED_PIPE request, where:

- **SecurityContext->AccessState** is a pointer to an [ACCESS_STATE](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/ns-wdm-_access_state) structure that contains the object's subject context, granted access types, and remaining desired access types.

- **SecurityContext->DesiredAccess** is an [ACCESS_MASK](https://docs.microsoft.com/windows-hardware/drivers/kernel/access-mask) structure that specifies access rights requested for the named pipe. For more information, see the *DesiredAccess* parameter of [**FltCreateNamedPipeFile**](https://docs.microsoft.com/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcreatenamedpipefile).

**Options**  
Bitmask of flags that specify the options to be applied when creating or opening the named pipe, as well as the action to be taken if the pipe already exists. The low 24 bits of this member correspond to the *CreateOptions* parameter for **FltCreateNamedPipeFile**. The high 8 bits correspond to the *CreateDisposition* parameter to **FltCreateNamedPipeFile**.

**Reserved**  
Reserved; do not use.

**ShareAccess**  
Bitmask of share access rights requested for the named pipe file. If this parameter is zero, exclusive access is being requested. For more information, see the *ShareAccess* parameter to [**FltCreateNamedPipeFile**](https://docs.microsoft.com/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcreatenamedpipefile).

**Parameters**  
Pointer to a [NAMED_PIPE_CREATE_PARAMETERS](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/ns-wdm-_named_pipe_create_parameters.md) structure containing information about the named pipe that is being created or opened.

## Remarks

The [FLT_PARAMETERS](https://docs.microsoft.com/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) structure for the [IRP_MJ_CREATE_NAMED_PIPE](irp-mj-create-named-pipe.md) operation contains the parameters for an IRP-based **CreatePipe** operation represented by a callback data ([FLT_CALLBACK_DATA](https://docs.microsoft.com/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)) structure. It is contained in an [FLT_IO_PARAMETER_BLOCK](https://docs.microsoft.com/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure.

Note that, other than the last longword field, the fields in the **CreatePipe** structure must match those for the **Create** structure.

IRP_MJ_CREATE_NAMED_PIPE is an IRP-based operation.

## Requirements

|   |   |
| - | - |
| Header| Fltkernel.h (include Fltkernel.h) |

## See also

[ACCESS_MASK](https://docs.microsoft.com/windows-hardware/drivers/kernel/access-mask)

[ACCESS_STATE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/ns-wdm-_access_state)

[FLT_CALLBACK_DATA](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/ns-fltkernel-_flt_callback_data)

[FLT_IO_PARAMETER_BLOCK](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/ns-fltkernel-_flt_io_parameter_block)

[FLT_PARAMETERS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/ns-fltkernel-_flt_parameters)

[**FltCreateNamedPipeFile**](https://docs.microsoft.com/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcreatenamedpipefile)

[IRP_MJ_CREATE_NAMED_PIPE](irp-mj-create-named-pipe.md)

[NAMED_PIPE_CREATE_PARAMETERS](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/ns-wdm-_named_pipe_create_parameters.md)
