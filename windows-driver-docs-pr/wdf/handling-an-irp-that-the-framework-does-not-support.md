---
title: Handling an IRP that the Framework Does Not Support
description: Handling an IRP that the Framework Does Not Support
ms.assetid: 0481f335-f63b-4f93-8eb4-523a70082302
keywords:
- unsupported WDM IRPs WDK KMDF
- IRPs WDK KMDF , unsupported
- WDM IRPs WDK KMDF , unsupported
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling an IRP that the Framework Does Not Support


\[Applies to KMDF only\]

The framework does not support I/O requests that have the following major IRP codes:

-   IRP\_MJ\_CREATE\_MAILSLOT
-   IRP\_MJ\_CREATE\_NAMED\_PIPE
-   IRP\_MJ\_DEVICE\_CHANGE
-   [**IRP\_MJ\_DIRECTORY\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff548658)
-   [**IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550751)
-   [**IRP\_MJ\_FLUSH\_BUFFERS**](https://msdn.microsoft.com/library/windows/hardware/ff550760)
-   [**IRP\_MJ\_LOCK\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff549251)
-   [**IRP\_MJ\_QUERY\_EA**](https://msdn.microsoft.com/library/windows/hardware/ff549279)
-   [**IRP\_MJ\_QUERY\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff549283)
-   [**IRP\_MJ\_QUERY\_QUOTA**](https://msdn.microsoft.com/library/windows/hardware/ff549293)
-   [**IRP\_MJ\_QUERY\_SECURITY**](https://msdn.microsoft.com/library/windows/hardware/ff549298)
-   [**IRP\_MJ\_QUERY\_VOLUME\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff549318)
-   [**IRP\_MJ\_SET\_EA**](https://msdn.microsoft.com/library/windows/hardware/ff549346)
-   [**IRP\_MJ\_SET\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff550799)
-   [**IRP\_MJ\_SET\_QUOTA**](https://msdn.microsoft.com/library/windows/hardware/ff549401)
-   [**IRP\_MJ\_SET\_SECURITY**](https://msdn.microsoft.com/library/windows/hardware/ff549407)
-   [**IRP\_MJ\_SET\_VOLUME\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff549415)

If the framework receives an IRP that contains one of these I/O function codes, the framework does not process the IRP. If your driver is a filter driver, the framework passes the IRP to the next-lower driver in the driver stack. If your driver is not a filter driver, the framework calls [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) to complete the IRP with a status value of STATUS\_INVALID\_DEVICE\_REQUEST.

If your driver must handle IRPs that contain any of these I/O function codes, the driver must call [**WdfDeviceInitAssignWdmIrpPreprocessCallback**](https://msdn.microsoft.com/library/windows/hardware/ff546043) to register an [*EvtDeviceWdmIrpPreprocess*](https://msdn.microsoft.com/library/windows/hardware/ff540925) event callback function for an I/O function code.

When the driver receives an IRP that contains an I/O function code that the driver has registered an [*EvtDeviceWdmIrpPreprocess*](https://msdn.microsoft.com/library/windows/hardware/ff540925) callback function for, the framework passes the IRP to the callback function. The callback function must then process the IRP by following the [WDM rules for handling IRPs](https://msdn.microsoft.com/library/windows/hardware/ff546847). The driver must call [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) to complete the IRP, or it must call [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) to pass the IRP to the next-lower driver.

For an example of an [*EvtDeviceWdmIrpPreprocess*](https://msdn.microsoft.com/library/windows/hardware/ff540925) callback function that handles an IRP that the framework does not support, see the [Serial](sample-kmdf-drivers.md) sample driver.

 

 





