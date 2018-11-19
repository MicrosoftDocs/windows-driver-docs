---
title: Attach ECPs to IRP_MJ_CREATE Operations that a Kernel-Mode Driver Originated
description: Attaching ECPs to IRP_MJ_CREATE Operations that a Kernel-Mode Driver Originated
ms.assetid: 87daa861-b0d5-4877-bf16-fad120108de6
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Attaching ECPs to IRP\_MJ\_CREATE Operations that a Kernel-Mode Driver Originated


You must follow these steps to set up ECPs and attach the ECPs to an [**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff548630) operation on a file:

1.  Call the [**FltAllocateExtraCreateParameterList**](https://msdn.microsoft.com/library/windows/hardware/ff541741) or [**FsRtlAllocateExtraCreateParameterList**](https://msdn.microsoft.com/library/windows/hardware/ff545632) routine to allocate memory for an [ECP\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff540148) structure. The operating system does not automatically free ECP\_LIST structures. Instead, after the ECP\_LIST structure is allocated, the minifilter driver must eventually call the [**FltFreeExtraCreateParameterList**](https://msdn.microsoft.com/library/windows/hardware/ff542964) or [**FsRtlFreeExtraCreateParameterList**](https://msdn.microsoft.com/library/windows/hardware/ff546005) routine to free ECP\_LIST.

2.  Call the [**FltAllocateExtraCreateParameter**](https://msdn.microsoft.com/library/windows/hardware/ff541728) or [**FsRtlAllocateExtraCreateParameter**](https://msdn.microsoft.com/library/windows/hardware/ff545609) routine to allocate paged memory pool for an ECP context structure and to generate a pointer to that structure.

3.  Call the [**FltInsertExtraCreateParameter**](https://msdn.microsoft.com/library/windows/hardware/ff543305) or [**FsRtlInsertExtraCreateParameter**](https://msdn.microsoft.com/library/windows/hardware/ff546179) routine to insert ECP context structures into the [ECP\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff540148) structure.

4.  Call the [**IoInitializeDriverCreateContext**](https://msdn.microsoft.com/library/windows/hardware/ff548419) routine to initialize an [**IO\_DRIVER\_CREATE\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff548565) structure.

5.  Define the [**IO\_DRIVER\_CREATE\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff548565) structure. In this definition, point the **ExtraCreateParameter** member of **IO\_DRIVER\_CREATE\_CONTEXT** to the [ECP\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff540148) structure.

6.  Call the [**FltCreateFileEx2**](https://msdn.microsoft.com/library/windows/hardware/ff541939) or [**IoCreateFileEx**](https://msdn.microsoft.com/library/windows/hardware/ff548283) routine to attach the ECPs to the [**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff548630) operation on the file. In this call, pass a pointer to the [**IO\_DRIVER\_CREATE\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff548565) structure to the *DriverContext* parameter.

7.  Call the [**FltFreeExtraCreateParameterList**](https://msdn.microsoft.com/library/windows/hardware/ff542964) or [**FsRtlFreeExtraCreateParameterList**](https://msdn.microsoft.com/library/windows/hardware/ff546005) routine to free the [ECP\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff540148) structure.

 

 




