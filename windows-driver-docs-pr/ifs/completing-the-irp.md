---
title: Completing the IRP
author: windows-driver-content
description: Completing the IRP
ms.assetid: 3174b36c-feb5-497c-a6e4-0d070c658899
keywords: ["IRP dispatch routines WDK file system , completing IRPs", "completing I/O requests WDK file system"]
---

# Completing the IRP


## <span id="ddk_handling_the_control_device_object_case_if"></span><span id="DDK_HANDLING_THE_CONTROL_DEVICE_OBJECT_CASE_IF"></span>


Every dispatch routine receives a pointer to the IRP's target device object in its *DeviceObject* parameter. If the filter driver has a control device object (CDO), the dispatch routine should check whether the *DeviceObject* pointer points to the filter driver's CDO before performing any processing on the IRP.

File system filter drivers are not required to support any I/O operations that are sent specifically to the CDO. (For more information about commonly supported operations, see [The Filter Driver's Control Device Object](the-filter-driver-s-control-device-object.md).) However, the CDO must complete every IRP that is sent to it.

To *complete* an IRP, a dispatch routine must perform all of the following steps:

1.  Set **Irp-&gt;IoStatus.Status** to an appropriate NTSTATUS value.

2.  Call [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) to return the IRP to the I/O Manager.

3.  Return the same status value as in step 1 to the caller.

Completing an IRP is sometimes referred to as "succeeding" or "failing" the IRP:

-   To *succeed* an IRP means to complete it with a success or informational NTSTATUS value such as STATUS\_SUCCESS.

-   To *fail* an IRP means to complete it with an error or warning NTSTATUS value such as STATUS\_INVALID\_DEVICE\_REQUEST or STATUS\_BUFFER\_OVERFLOW.

NTSTATUS values are defined in ntstatus.h. These values fall into four categories: success, informational, warning, and error. For more information, see [Using NTSTATUS Values](https://msdn.microsoft.com/library/windows/hardware/ff565436).

**Note**   Although STATUS\_PENDING is a success NTSTATUS value, it is a programming error to complete an IRP with STATUS\_PENDING.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Completing%20the%20IRP%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


