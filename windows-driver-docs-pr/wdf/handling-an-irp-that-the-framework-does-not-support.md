---
title: Handling an IRP that the Framework Does Not Support
description: Handling an IRP that the Framework Does Not Support
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
-   [**IRP\_MJ\_DIRECTORY\_CONTROL**](../ifs/irp-mj-directory-control.md)
-   [**IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](../kernel/irp-mj-file-system-control.md)
-   [**IRP\_MJ\_FLUSH\_BUFFERS**](../kernel/irp-mj-flush-buffers.md)
-   [**IRP\_MJ\_LOCK\_CONTROL**](../ifs/irp-mj-lock-control.md)
-   [**IRP\_MJ\_QUERY\_EA**](../ifs/irp-mj-query-ea.md)
-   [**IRP\_MJ\_QUERY\_INFORMATION**](../ifs/irp-mj-query-information.md)
-   [**IRP\_MJ\_QUERY\_QUOTA**](../ifs/irp-mj-query-quota.md)
-   [**IRP\_MJ\_QUERY\_SECURITY**](../ifs/irp-mj-query-security.md)
-   [**IRP\_MJ\_QUERY\_VOLUME\_INFORMATION**](../ifs/irp-mj-query-volume-information.md)
-   [**IRP\_MJ\_SET\_EA**](../ifs/irp-mj-set-ea.md)
-   [**IRP\_MJ\_SET\_INFORMATION**](../kernel/irp-mj-set-information.md)
-   [**IRP\_MJ\_SET\_QUOTA**](../ifs/irp-mj-set-quota.md)
-   [**IRP\_MJ\_SET\_SECURITY**](../ifs/irp-mj-set-security.md)
-   [**IRP\_MJ\_SET\_VOLUME\_INFORMATION**](../ifs/irp-mj-set-volume-information.md)

If the framework receives an IRP that contains one of these I/O function codes, the framework does not process the IRP. If your driver is a filter driver, the framework passes the IRP to the next-lower driver in the driver stack. If your driver is not a filter driver, the framework calls [**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest) to complete the IRP with a status value of STATUS\_INVALID\_DEVICE\_REQUEST.

If your driver must handle IRPs that contain any of these I/O function codes, the driver must call [**WdfDeviceInitAssignWdmIrpPreprocessCallback**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitassignwdmirppreprocesscallback) to register an [*EvtDeviceWdmIrpPreprocess*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess) event callback function for an I/O function code.

When the driver receives an IRP that contains an I/O function code that the driver has registered an [*EvtDeviceWdmIrpPreprocess*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess) callback function for, the framework passes the IRP to the callback function. The callback function must then process the IRP by following the [WDM rules for handling IRPs](../kernel/handling-irps.md). The driver must call [**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest) to complete the IRP, or it must call [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver) to pass the IRP to the next-lower driver.

For an example of an [*EvtDeviceWdmIrpPreprocess*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess) callback function that handles an IRP that the framework does not support, see the [Serial](sample-kmdf-drivers.md) sample driver.

 

