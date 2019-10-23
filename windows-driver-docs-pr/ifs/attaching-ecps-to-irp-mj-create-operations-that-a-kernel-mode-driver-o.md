---
title: Attach ECPs to IRP_MJ_CREATE Operations that a Kernel-Mode Driver Originated
description: Attaching ECPs to IRP_MJ_CREATE Operations that a Kernel-Mode Driver Originated
ms.assetid: 87daa861-b0d5-4877-bf16-fad120108de6
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Attaching ECPs to IRP\_MJ\_CREATE Operations that a Kernel-Mode Driver Originated


You must follow these steps to set up ECPs and attach the ECPs to an [**IRP\_MJ\_CREATE**](https://docs.microsoft.com/windows-hardware/drivers/ifs/irp-mj-create) operation on a file:

1.  Call the [**FltAllocateExtraCreateParameterList**](https://docs.microsoft.com/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocateextracreateparameterlist) or [**FsRtlAllocateExtraCreateParameterList**](https://msdn.microsoft.com/library/windows/hardware/ff545632) routine to allocate memory for an [ECP\_LIST](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff540148(v=vs.85)) structure. The operating system does not automatically free ECP\_LIST structures. Instead, after the ECP\_LIST structure is allocated, the minifilter driver must eventually call the [**FltFreeExtraCreateParameterList**](https://docs.microsoft.com/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfreeextracreateparameterlist) or [**FsRtlFreeExtraCreateParameterList**](https://msdn.microsoft.com/library/windows/hardware/ff546005) routine to free ECP\_LIST.

2.  Call the [**FltAllocateExtraCreateParameter**](https://docs.microsoft.com/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocateextracreateparameter) or [**FsRtlAllocateExtraCreateParameter**](https://msdn.microsoft.com/library/windows/hardware/ff545609) routine to allocate paged memory pool for an ECP context structure and to generate a pointer to that structure.

3.  Call the [**FltInsertExtraCreateParameter**](https://docs.microsoft.com/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltinsertextracreateparameter) or [**FsRtlInsertExtraCreateParameter**](https://msdn.microsoft.com/library/windows/hardware/ff546179) routine to insert ECP context structures into the [ECP\_LIST](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff540148(v=vs.85)) structure.

4.  Call the [**IoInitializeDriverCreateContext**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddk/nf-ntddk-ioinitializedrivercreatecontext) routine to initialize an [**IO\_DRIVER\_CREATE\_CONTEXT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_io_driver_create_context) structure.

5.  Define the [**IO\_DRIVER\_CREATE\_CONTEXT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_io_driver_create_context) structure. In this definition, point the **ExtraCreateParameter** member of **IO\_DRIVER\_CREATE\_CONTEXT** to the [ECP\_LIST](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff540148(v=vs.85)) structure.

6.  Call the [**FltCreateFileEx2**](https://docs.microsoft.com/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcreatefileex2) or [**IoCreateFileEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iocreatefileex) routine to attach the ECPs to the [**IRP\_MJ\_CREATE**](https://docs.microsoft.com/windows-hardware/drivers/ifs/irp-mj-create) operation on the file. In this call, pass a pointer to the [**IO\_DRIVER\_CREATE\_CONTEXT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_io_driver_create_context) structure to the *DriverContext* parameter.

7.  Call the [**FltFreeExtraCreateParameterList**](https://docs.microsoft.com/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfreeextracreateparameterlist) or [**FsRtlFreeExtraCreateParameterList**](https://msdn.microsoft.com/library/windows/hardware/ff546005) routine to free the [ECP\_LIST](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff540148(v=vs.85)) structure.

 

 




