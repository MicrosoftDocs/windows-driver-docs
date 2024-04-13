---
title: Completing the IRP
description: Completing the IRP
keywords:
- IRP dispatch routines WDK file system , completing IRPs
- completing I/O requests WDK file system
ms.date: 02/23/2023
---

# Completing the IRP

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

Every dispatch routine receives a pointer to the IRP's target device object in its **DeviceObject** parameter. If the legacy filter driver has a control device object (CDO), the dispatch routine should check whether **DeviceObject** points to the filter driver's CDO before performing any processing on the IRP.

File system filter drivers aren't required to support any I/O operations that are sent specifically to the CDO. (For more information about commonly supported operations, see [The Filter Driver's Control Device Object](the-filter-driver-s-control-device-object.md).) However, the CDO must complete every IRP that is sent to it.

To *complete* an IRP, a dispatch routine must perform all of the following steps:

1. Set **Irp->IoStatus.Status** to an appropriate NTSTATUS value.

2. Call [**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest) to return the IRP to the I/O Manager.

3. Return the same status value as in step 1 to the caller.

Completing an IRP is sometimes referred to as "succeeding" or "failing" the IRP:

- *Succeeding* an IRP means to complete it with a success or informational NTSTATUS value such as STATUS_SUCCESS.

- *Failing* an IRP means to complete it with an error or warning NTSTATUS value such as STATUS_INVALID_DEVICE_REQUEST or STATUS_BUFFER_OVERFLOW.

NTSTATUS values are defined in ntstatus.h. These values fall into four categories: success, informational, warning, and error. For more information, see [Using NTSTATUS Values](../kernel/using-ntstatus-values.md).

Although STATUS_PENDING is a success NTSTATUS value, it's a programming error to complete an IRP with STATUS_PENDING.
