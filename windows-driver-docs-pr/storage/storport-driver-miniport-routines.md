---
title: Storport driver miniport routines
author: windows-driver-content
description: Describes the Storport miniport driver routines and differences between the design of the SCSI port driver and that of the Storport driver.
ms.assetid: 
keywords:
- Storport driver support routines
- storage WDK
- storage support routines
ms.author: windowsdriverdev
ms.date: 06/11/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---


# Storport driver miniport routines

A miniport driver that works with the Storport driver must contain implementations of the routine descriptions listed in this section, and it must expose them through an [HW_INITIALIZATION_DATA](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/ns-storport-_hw_initialization_data) structure during the miniport driver's initialization phase. 

The Storport miniport driver routines are in most respects equivalent to their SCSI port counterparts (see [SCSI Miniport Driver Routines](https://technet.microsoft.com/en-us/ff565312(v=vs.96)) for more information). However, there are important differences between the design of the SCSI port driver and that of the Storport driver, and these routines must accommodate those differences. 

For instance, miniport drivers that work with the Storport driver must always be prepared to receive another I/O request after the [HwStorStartIo](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nc-storport-hw_startio) routine has completed. A miniport driver that works with SCSI port is not required to do this. The SCSI port version does not receive a new I/O request until it explicitly signals the port driver, using the [StorPortNotification](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nf-storport-storportnotification) function, that it is prepared to handle another request. 

If the Storport version of the miniport driver cannot handle a request at the time it is submitted, it has a set of queue management functions, not available to the SCSI port version, that allow it to deal with the overload. Like the SCSI port version, the Storport version of the miniport driver completes the request with **SRB_STATUS_BUSY**, but unlike the SCSI port version, it can also mark the device queue as busy using the [StorPortDeviceBusy](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nf-storport-storportdevicebusy) routine. Similar functions allow the miniport driver to pause and resume processing on an adapter-wide basis.

For more information about the support routines provided by the Storport driver, see [Storport driver support routines](storport-driver-support-routines.md).

For more information about the Storport driver, see [Storage Port Drivers](storage-port-drivers.md). 

The following are miniport driver routines:
| Routine  |Description   |
|---|---|
|[HW_MESSAGE_SIGNALED_INTERRUPT_ROUTINE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nc-storport-hw_message_signaled_interrupt_routine)|The **HwMSInterruptRoutine** routine handles a message signaled interrupt (MSI).|
|[HW_ADAPTER_CONTROL]()||
|[HW_BUILDIO]()||
|[HW_DPC_ROUTINE]()||
|[HW_FIND_ADAPTER]()||
|[HW_INITIALIZE]()||
|[HW_INTERRUPT]()||
|[HW_PASSIVE_INITIALIZE_ROUTINE]()||
|[HW_RESET_BUS]()||
|[HW_STARTIO]()||
|[HW_TIMER]()||
|[]()||
|[]()||
|[]()||
|[]()||
|[]()||
|[]()||
