---
title: FLT_PARAMETERS for IRP_MJ_CREATE union
description: The following union component is used when the MajorFunction field of the FLT_IO_PARAMETER_BLOCK structure for the operation is IRP_MJ_CREATE.
keywords: ["FLT_PARAMETERS for IRP_MJ_CREATE union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FLT_PARAMETERS
api_location:
- fltkernel.h
api_type:
- HeaderDef
ms.date: 11/05/2019
---

# FLT_PARAMETERS for IRP_MJ_CREATE union

The following union component is used when the **MajorFunction** field of the [FLT_IO_PARAMETER_BLOCK](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure for the operation is [**IRP_MJ_CREATE**](irp-mj-create.md).

## Syntax

```ManagedCPlusPlus
typedef union _FLT_PARAMETERS {
  ...    ;
  struct {
    PIO_SECURITY_CONTEXT     SecurityContext;
    ULONG                    Options;
    USHORT POINTER_ALIGNMENT FileAttributes;
    USHORT                   ShareAccess;
    USHORT POINTER_ALIGNMENT EaLength;
    PVOID                    EaBuffer;
    LARGE_INTEGER            AllocationSize;
  } Create;
  ...    ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

## Members

The **Create** structure of FLT_PARAMETERS contains the following members.

**SecurityContext**

Pointer to an [IO_SECURITY_CONTEXT](/windows-hardware/drivers/ddi/content/wdm/ns-wdm-_io_security_context) structure that represents the security context of an IRP_MJ_CREATE request, where:

- **SecurityContext->AccessState** is a pointer to an [ACCESS_STATE](/windows-hardware/drivers/ddi/wdm/ns-wdm-_access_state) structure that contains the object's subject context, granted access types, and remaining desired access types.

- **SecurityContext->DesiredAccess** is an [ACCESS_MASK](../kernel/access-mask.md) structure that specifies access rights requested for the file. For more information, see the *DesiredAccess* parameter to [**FltCreateFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcreatefile).

**Options**  
Bitmask of flags that specify the options to be applied when creating or opening the file, as well as the action to be taken if the file already exists. The low 24 bits of this member correspond to the *CreateOptions* parameter to [**FltCreateFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcreatefile). The high 8 bits correspond to the *CreateDisposition* parameter to **FltCreateFile**.

**FileAttributes**  
Bitmask of attributes to be applied when creating or opening the file. For more information, see the *FileAttributes* parameter to [**FltCreateFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcreatefile).

**ShareAccess**  
Bitmask of share access rights requested for the file. If this parameter is zero, exclusive access is being requested. For more information, see the *ShareAccess* parameter to [**FltCreateFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcreatefile).

**EaLength**  
Length, in bytes, of the buffer that the **EaBuffer** member points to. For more information, see the *EaLength* parameter to [**FltCreateFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcreatefile).

**EaBuffer**  
Pointer to a caller-supplied, [FILE_FULL_EA_INFORMATION](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_full_ea_information)-structured buffer that contains extended attribute (EA) information to be applied to the file. For more information, see the *EaBuffer* parameter to [**FltCreateFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcreatefile).

**AllocationSize**  
Optionally specifies the initial allocation size, in bytes, for the file. A nonzero value has no effect unless the file is being created, overwritten, or superseded. For more information, see the *AllocationSize* parameter to [**FltCreateFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcreatefile).

## Remarks

The [FLT_PARAMETERS](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) structure for the [IRP_MJ_CREATE](irp-mj-create.md) operation contains the parameters for an IRP-based **Create** operation represented by a callback data ([FLT_CALLBACK_DATA](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)) structure. It is contained in an [FLT_IO_PARAMETER_BLOCK](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure.

IRP_MJ_CREATE is an IRP-based operation.

## Requirements

| Header | *fltkernel.h* (include Fltkernel.h)

## See also

[ACCESS_MASK](../kernel/access-mask.md)

[ACCESS_STATE](/windows-hardware/drivers/ddi/wdm/ns-wdm-_access_state)

[FILE_FULL_EA_INFORMATION](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_full_ea_information)

[FLT_CALLBACK_DATA](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)

[FLT_IO_PARAMETER_BLOCK](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block)

[FLT_IS_FASTIO_OPERATION](/windows-hardware/drivers/ddi/index)

[FLT_PARAMETERS](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters)

[**FltCreateFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcreatefile)

[IRP_MJ_CREATE](irp-mj-create.md)
