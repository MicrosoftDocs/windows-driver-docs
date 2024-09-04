---
title: Storport Driver Miniport Routines
description: Describes the Storport miniport driver routines and differences between the design of the SCSI port driver and that of the Storport driver.
keywords:
- Storport driver support routines
- storage WDK
- storage support routines
ms.date: 09/04/2024
---

# Storport driver miniport routines

A miniport driver that works with the Storport driver must contain implementations of the routine descriptions listed in this section, and it must expose them through a [**HW_INITIALIZATION_DATA**](/windows-hardware/drivers/ddi/storport/ns-storport-_hw_initialization_data-r1) structure during the miniport driver's initialization phase.

The Storport miniport driver routines are in most respects equivalent to their [SCSI port counterparts](scsi-miniport-driver-routines.md). However, there are important differences between the design of the SCSI port driver and that of the Storport driver, and the miniport routines must accommodate those differences.

For instance:

* A Storport miniport driver must always be prepared to receive another I/O request after its [**HwStorStartIo**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_startio) routine completes.
* A SCSI miniport driver doesn't have this requirement. It doesn't receive a new I/O request until it explicitly signals the port driver when it can handle another request by calling [**StorPortNotification**](/windows-hardware/drivers/ddi/storport/nf-storport-storportnotification).

If the Storport miniport driver can't immediately handle a submitted request, it has a set of queue management functions that allow it to deal with the overload. These queue management functions aren't available to the SCSI miniport driver. Like the SCSI miniport driver, the Storport miniport driver completes the request with **SRB_STATUS_BUSY**. But unlike the SCSI port version, it can also mark the device queue as busy using the [**StorPortDeviceBusy**](/windows-hardware/drivers/ddi/storport/nf-storport-storportdevicebusy) routine. Similar functions allow the Storport miniport driver to pause and resume processing on an adapter-wide basis.

For more information about the support routines provided by the Storport driver, see [Storport driver support routines](storport-driver-support-routines.md).

For more information about the Storport driver, see [Storage Port Drivers](storage-port-drivers.md).

## List of Storport miniport driver routines

| Routine | Description |
| ------- | ----------- |
| [HW_MESSAGE_SIGNALED_INTERRUPT_ROUTINE](/windows-hardware/drivers/ddi/storport/nc-storport-hw_message_signaled_interrupt_routine) | Handles a message signaled interrupt (MSI). |
| [HW_ADAPTER_CONTROL](/windows-hardware/drivers/ddi/storport/nc-storport-hw_adapter_control) | Performs synchronous operations to control the state or behavior of an adapter, such as stopping or restarting the HBA for power management. |
| [HW_BUILDIO](/windows-hardware/drivers/ddi/storport/nc-storport-hw_buildio) | Processes the SRB with unsynchronized access to shared system data structures before passing it to **HwStorStartIo**. |
| [HW_DPC_ROUTINE](/windows-hardware/drivers/ddi/storport/nc-storport-hw_dpc_routine) | Routine that is deferred for execution at DISPATCH IRQL with the deferred procedure call (DPC) mechanism. |
| [HW_FIND_ADAPTER](/windows-hardware/drivers/ddi/storport/nc-storport-hw_find_adapter) | Uses the supplied configuration to determine whether a specific HBA is supported and, if it is, to return configuration information about that adapter. |
| [HW_INITIALIZE](/windows-hardware/drivers/ddi/storport/nc-storport-hw_initialize) | Initializes the miniport driver after a system reboot or power failure occurs. |
| [HW_INTERRUPT](/windows-hardware/drivers/ddi/storport/nc-storport-hw_interrupt) | The Storport driver calls the **HwStorInterrupt** routine after the HBA generates an interrupt request. |
| [HW_PASSIVE_INITIALIZE_ROUTINE](/windows-hardware/drivers/ddi/storport/nc-storport-hw_passive_initialize_routine) | Called after the **HwStorInitialize** routine when the current IRQL is at PASSIVE_LEVEL. |
| [HW_RESET_BUS](/windows-hardware/drivers/ddi/storport/nc-storport-hw_reset_bus) | Called by the port driver to clear error conditions. |
| [HW_STARTIO](/windows-hardware/drivers/ddi/storport/nc-storport-hw_startio) | The Storport driver calls the **HwStorStartIo** routine one time for each incoming I/O request. |
| [HW_TIMER](/windows-hardware/drivers/ddi/storport/nc-storport-hw_timer) | Called after the interval that is specified when the miniport driver called **StorPortNotification** with the **RequestTimerCall** *NotificationType* value. |
| [HW_TRACING_ENABLED](/windows-hardware/drivers/ddi/storport/nc-storport-hw_tracing_enabled) | Enables the Storport to notify a miniport that event tracing is enabled. |
| [HW_UNIT_CONTROL](/windows-hardware/drivers/ddi/storport/nc-storport-hw_unit_control) | Called to perform synchronous operations to control the state of storage unit device. The miniport driver is notified to start a unit or handle a power state transition for a unit device. |
| [HW_WORKITEM](/windows-hardware/drivers/ddi/storport/nc-storport-hw_workitem) | A miniport-provided callback function for processing a Storport work item request. |
