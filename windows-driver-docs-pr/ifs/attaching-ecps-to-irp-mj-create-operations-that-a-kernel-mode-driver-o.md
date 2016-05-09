---
title: Attaching ECPs to IRP\_MJ\_CREATE Operations that a Kernel-Mode Driver Originated
author: windows-driver-content
description: Attaching ECPs to IRP\_MJ\_CREATE Operations that a Kernel-Mode Driver Originated
ms.assetid: 87daa861-b0d5-4877-bf16-fad120108de6
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Attaching%20ECPs%20to%20IRP_MJ_CREATE%20Operations%20that%20a%20Kernel-Mode%20Driver%20Originated%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


