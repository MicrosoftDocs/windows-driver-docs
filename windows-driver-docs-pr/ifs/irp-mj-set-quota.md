---
title: IRP\_MJ\_SET\_QUOTA
description: IRP\_MJ\_SET\_QUOTA
ms.assetid: 256c349b-48cb-4a9f-a60a-89503d8f3f58
keywords: ["IRP_MJ_SET_QUOTA Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_SET_QUOTA
api_type:
- NA
---

# IRP\_MJ\_SET\_QUOTA


## When Sent


The IRP\_MJ\_SET\_QUOTA request is sent by the I/O Manager. It can be sent, for example, when a user-mode application has called a Microsoft Win32 method such as **IDiskQuotaControl::SetQuotaState**.

## Operation: File System Drivers


IRP\_MJ\_SET\_QUOTA and IRP\_MJ\_QUERY\_QUOTA existed in Windows NT 4.0 but were not used by file systems. On Windows 2000 and later systems, they are used for disk quota support in NTFS. Support for these IRPs by new file systems is optional.

## Operation: File System Filter Drivers


The filter driver should pass this IRP down to the next-lower driver on the stack, unless it needs to explicitly override quota behavior.

## Parameters


A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174) with the given IRP to get a pointer to its own [**stack location**](https://msdn.microsoft.com/library/windows/hardware/ff550659) in the IRP, shown in the following list as *IrpSp*. (The IRP is shown as *Irp*.) The driver can use the information that is set in the following members of the IRP and the IRP stack location in processing a set quota information request:

<a href="" id="deviceobject"></a>*DeviceObject*  
Pointer to the target device object.

<a href="" id="deviceobject--flags"></a>*DeviceObject-&gt;Flags*  
If the DO\_BUFFERED\_IO flag is set, the caller has requested METHOD\_BUFFERED I/O. Otherwise, the caller has requested METHOD\_NEITHER I/O.

<a href="" id="irp--associatedirp-systembuffer"></a>*Irp-&gt;AssociatedIrp.SystemBuffer*  
Pointer to a system-supplied buffer to be used as an intermediate system buffer, if the DO\_BUFFERED\_IO flag is set in *DeviceObject-&gt;Flags*. Otherwise, this member is set to **NULL**.

<a href="" id="irp--iostatus"></a>*Irp-&gt;IoStatus*  
Pointer to an [**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671) structure that receives the final completion status and information about the requested operation.

<a href="" id="irp--userbuffer"></a>*Irp-&gt;UserBuffer*  
Pointer to a caller-supplied buffer that contains the quota entries to be added or modified for the volume.

<a href="" id="irpsp--fileobject"></a>*IrpSp-&gt;FileObject*  
Pointer to the file object that is associated with *DeviceObject*.

The *IrpSp-&gt;FileObject* parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE\_OBECT structure. The **RelatedFileObject** field of the FILE\_OBJECT structure is not valid during the processing of IRP\_MJ\_SET\_QUOTA and should not be used.

<a href="" id="irpsp--majorfunction"></a>*IrpSp-&gt;MajorFunction*  
Specifies IRP\_MJ\_SET\_QUOTA.

<a href="" id="irpsp--parameters-setquota-length"></a>*IrpSp-&gt;Parameters.SetQuota.Length*  
Specifies the length, in bytes, of the buffer pointed to by *Irp-&gt;UserBuffer*.

## See also


[**FILE\_QUOTA\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540342)

[**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659)

[**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671)

[**IoCheckQuotaBufferValidity**](https://msdn.microsoft.com/library/windows/hardware/ff548279)

[**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174)

[**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694)

[**IRP\_MJ\_QUERY\_QUOTA**](irp-mj-query-quota.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20IRP_MJ_SET_QUOTA%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





