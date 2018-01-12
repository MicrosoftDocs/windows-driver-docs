---
title: IRP\_MJ\_FLUSH\_BUFFERS
description: IRP\_MJ\_FLUSH\_BUFFERS
ms.assetid: 13df0d84-0320-4d7e-9acc-8f913ba6afaa
keywords: ["IRP_MJ_FLUSH_BUFFERS Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_FLUSH_BUFFERS
api_type:
- NA
---

# IRP\_MJ\_FLUSH\_BUFFERS


## When Sent


The IRP\_MJ\_FLUSH\_BUFFERS request is sent by the I/O Manager and other operating system components, as well as other kernel-mode drivers, when buffered data needs to be flushed to disk. It can be sent, for example, when a user-mode application has called a Microsoft Win32 function such as **FlushFileBuffers**. (For file system drivers and file system filter drivers, calling [**CcFlushCache**](https://msdn.microsoft.com/library/windows/hardware/ff539082) is usually preferable to sending an IRP.)

All file system and filter drivers that maintain internal buffers for data must handle this IRP so that changes to file data or metadata can be preserved across system shutdowns.

## Operation: File System Drivers


The file system driver should flush to disk any important data or metadata associated with the file object and complete the IRP. For more information about how to handle this IRP, study the FASTFAT sample.

## Operation: File System Filter Drivers


The filter driver should flush to disk any important data or metadata associated with the file object and pass this IRP down to the next-lower driver on the stack.

## Parameters


A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174) with the given IRP to get a pointer to its own [**stack location**](https://msdn.microsoft.com/library/windows/hardware/ff550659) in the IRP, shown in the following list as *IrpSp*. (The IRP is shown as *Irp*.) The driver can use the information that is set in the following members of the IRP and the IRP stack location in processing a flush buffers request:

<a href="" id="deviceobject"></a>*DeviceObject*  
Pointer to the target device object.

<a href="" id="irp--iostatus"></a>*Irp-&gt;IoStatus*  
Pointer to an [**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671) structure that receives the final completion status and information about the requested operation.

<a href="" id="irpsp--fileobject"></a>*IrpSp-&gt;FileObject*  
Pointer to the file object that is associated with *DeviceObject*.

The *IrpSp-&gt;FileObject* parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE\_OBECT structure. The **RelatedFileObject** field of the FILE\_OBJECT structure is not valid during the processing of IRP\_MJ\_FLUSH\_BUFFERS and should not be used.

<a href="" id="irpsp--majorfunction"></a>*IrpSp-&gt;MajorFunction*  
Specifies IRP\_MJ\_FLUSH\_BUFFERS.

## See also


[**CcFlushCache**](https://msdn.microsoft.com/library/windows/hardware/ff539082)

[**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659)

[**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671)

[**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174)

[**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694)

[**IRP\_MJ\_FLUSH\_BUFFERS (WDK Kernel Reference)**](https://msdn.microsoft.com/library/windows/hardware/ff550760)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20IRP_MJ_FLUSH_BUFFERS%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





