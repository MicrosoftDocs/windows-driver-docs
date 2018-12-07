---
title: Completing the IRP
description: Completing the IRP
ms.assetid: 3174b36c-feb5-497c-a6e4-0d070c658899
keywords:
- IRP dispatch routines WDK file system , completing IRPs
- completing I/O requests WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 

 




