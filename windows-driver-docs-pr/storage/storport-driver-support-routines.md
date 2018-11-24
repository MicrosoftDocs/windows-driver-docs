---
title: Storport driver support routines
description: Describes the Storport miniport driver routines and differences between the design of the SCSI port driver and that of the Storport driver.
ms.assetid: 
keywords:
- Storport driver support routines
- storage WDK
- storage support routines
ms.date: 06/11/2018
ms.localizationpriority: medium
---

# Storport driver support routines

A miniport driver that works with the Storport driver must contain implementations of the routine descriptions listed in this section, and it must expose them through an [HW_INITIALIZATION_DATA](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/ns-storport-_hw_initialization_data) structure during the miniport driver's initialization phase. 

The Storport miniport driver routines are in most respects equivalent to their SCSI port counterparts (see [SCSI Miniport Driver Routines](https://docs.microsoft.com/windows-hardware/drivers/storage/required-and-optional-scsi-miniport-driver-routines) for more information). However, there are important differences between the design of the SCSI port driver and that of the Storport driver, and these routines must accommodate those differences. 

For instance, miniport drivers that work with the Storport driver must always be prepared to receive another I/O request after the [HwStorStartIo](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nc-storport-hw_startio) routine has completed. A miniport driver that works with SCSI port is not required to do this. The SCSI port version does not receive a new I/O request until it explicitly signals the port driver, using the [StorPortNotification](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nf-storport-storportnotification) function, that it is prepared to handle another request. 

If the Storport version of the miniport driver cannot handle a request at the time it is submitted, it has a set of queue management functions, not available to the SCSI port version, that allow it to deal with the overload. Like the SCSI port version, the Storport version of the miniport driver completes the request with [SRB_STATUS_BUSY](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nf-storport-storportdevicebusy), but unlike the SCSI port version, it can also mark the device queue as busy using the StorPortDeviceBusy routine. Similar functions allow the miniport driver to pause and resume processing on an adapter-wide basis.

For more information about the support routines provided by the Storport driver, see [Storport Driver Support Routines].

For more information about the Storport driver, see [Storage Port Drivers](https://docs.microsoft.com/windows-hardware/drivers/storage/storage-port-drivers). 

The following are Storport driver support routines:

| Routine  |Description   |
|---|---|
|[HW_MESSAGE_SIGNALED_INTERRUPT_ROUTINE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nc-storport-hw_message_signaled_interrupt_routine)| Handles a message signaled interrupt (MSI). |
|[HW_ADAPTER_CONTROL](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nc-storport-hw_adapter_control)|A miniport driver's **HwStorAdapterControl** routine is called to perform synchronous operations to control the state or behavior of an adapter, such as stopping or restarting the HBA for power management.|
|[HW_BUILDIO](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nc-storport-hw_buildio)|The **HwStorBuildIo** routine processes the SRB with unsynchronized access to shared system data structures before passing it to [HwStorStartIo](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nc-storport-hw_startio).|
|[HW_DPC_ROUTINE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nc-storport-hw_dpc_routine)|The **HwStorDpcRoutine** routine is a routine that is deferred for execution at DISPATCH IRQL by means of the deferred procedure call (DPC) mechanism.|
|[HW_FIND_ADAPTER](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nc-storport-hw_find_adapter)|The **HwStorFindAdapter** routine uses the supplied configuration to determine whether a specific HBA is supported and, if it is, to return configuration information about that adapter.|
|[HW_INITIALIZE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nc-storport-hw_initialize)|The HwStorInitialize routine initializes the miniport driver after a system reboot or power failure occurs.|
|[HW_INTERRUPT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nc-storport-hw_interrupt)|The Storport driver calls the **HwStorInterrupt** routine after the HBA generates an interrupt request.|
|[HW_PASSIVE_INITIALIZE_ROUTINE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nc-storport-hw_passive_initialize_routine)|The **HwStorPassiveInitializeRoutine** callback routine is called after the **HwStorInitialize** routine when the current IRQL is at PASSIVE_LEVEL.|
|[HW_RESET_BUS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nc-storport-hw_reset_bus)|The **HwStorResetBus** routine is called by the port driver to clear error conditions.|
|[HW_STARTIO](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nc-storport-hw_startio)|The Storport driver calls the **HwStorStartIo** routine one time for each incoming I/O request.|
|[HW_TIMER](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nc-storport-hw_timer)|The **HwStorTimer** routine is called after the interval that is specified when the miniport driver called [StorPortNotification](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nf-storport-storportnotification) with the *[RequestTimerCall](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nf-storport-storportnotification)* NotificationType value.|
|[]()||
