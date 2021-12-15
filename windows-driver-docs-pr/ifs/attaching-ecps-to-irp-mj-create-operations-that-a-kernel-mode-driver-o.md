---
title: Attach ECPs to IRP_MJ_CREATE operations that a kernel-mode driver originated
description: Attaching ECPs to IRP_MJ_CREATE operations that a kernel-mode driver originated
ms.date: 09/02/2021
---

# Attaching ECPs to IRP_MJ_CREATE operations that a kernel-mode driver originated

You must follow these steps to set up ECPs and attach the ECPs to an [**IRP_MJ_CREATE**](./irp-mj-create.md) operation on a file:

1. Call [**FltAllocateExtraCreateParameterList**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocateextracreateparameterlist) or [**FsRtlAllocateExtraCreateParameterList**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlallocateextracreateparameterlist) to allocate memory for an [**ECP_LIST**](/previous-versions/windows/hardware/drivers/ff540148(v=vs.85)) structure. The operating system does not automatically free **ECP_LIST** structures. Instead, after the **ECP_LIST** structure is allocated, the minifilter driver must eventually call [**FltFreeExtraCreateParameterList**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfreeextracreateparameterlist) or [**FsRtlFreeExtraCreateParameterList**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlfreeextracreateparameterlist) to free **ECP_LIST**.

2. Call [**FltAllocateExtraCreateParameter**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocateextracreateparameter) or [**FsRtlAllocateExtraCreateParameter**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlallocateextracreateparameter) to allocate paged memory pool for an ECP context structure and to generate a pointer to that structure.

3. Call [**FltInsertExtraCreateParameter**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltinsertextracreateparameter) or [**FsRtlInsertExtraCreateParameter**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlinsertextracreateparameter) to insert ECP context structures into the [**ECP_LIST**](/previous-versions/windows/hardware/drivers/ff540148(v=vs.85)) structure.

4. Call [**IoInitializeDriverCreateContext**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-ioinitializedrivercreatecontext) to initialize an [**IO_DRIVER_CREATE_CONTEXT**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_io_driver_create_context) structure.

5. Define the [**IO_DRIVER_CREATE_CONTEXT**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_io_driver_create_context) structure. In this definition, point the **ExtraCreateParameter** member of **IO_DRIVER_CREATE_CONTEXT** to the [ECP_LIST](/previous-versions/windows/hardware/drivers/ff540148(v=vs.85)) structure.

6. Call [**FltCreateFileEx2**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcreatefileex2) or [**IoCreateFileEx**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iocreatefileex) to attach the ECPs to the [**IRP_MJ_CREATE**](./irp-mj-create.md) operation on the file. In this call, pass a pointer to the [**IO_DRIVER_CREATE_CONTEXT**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_io_driver_create_context) structure to the *DriverContext* parameter.

7. Call [**FltFreeExtraCreateParameterList**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfreeextracreateparameterlist) or [**FsRtlFreeExtraCreateParameterList**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlfreeextracreateparameterlist) to free the [**ECP_LIST**](/previous-versions/windows/hardware/drivers/ff540148(v=vs.85)) structure.
