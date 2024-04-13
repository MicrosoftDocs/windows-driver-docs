---
title: Restrictions on Miniport Drivers that Manage the Boot Drive
description: Restrictions on Miniport Drivers that Manage the Boot Drive
keywords:
- storage miniport drivers WDK , boot drives
- miniport drivers WDK storage , boot drives
- boot drives WDK storage
- disk dump drivers WDK storage
- dump mode WDK storage
ms.date: 04/20/2017
---

# Restrictions on Miniport Drivers that Manage the Boot Drive


A storage miniport driver that manages an adapter for a boot device is subject to special restrictions during a system crash. While dumping the system's memory image to disk, the miniport driver must operate within a different environment. The usual communication between the miniport driver, the port driver, and disk class driver is interrupted. The kernel does disk I/O by direct calls to the disk dump port driver, *diskdump.sys* (*dumpata.sys* for ATA controllers), bypassing file systems, and the normal I/O stack. The disk dump driver, in turn, calls the boot device's miniport driver to handle all I/O operations, and the disk dump driver intercepts all of the miniport driver's calls to the port driver.

The disk dump driver provides the same set of support routines that the port driver provides, so the miniport driver should be able to use disk dump driver routines in the same way that it uses port routines.

However, miniport drivers that manage adapters in the disk dump path are subject to the following limitations while in dump mode:

### <span id="mem_usage"></span><span id="MEM_USAGE"></span>Memory usage

Miniport drivers must make frugal use of memory during a system crash. The amount of noncached memory that the miniport driver can allocate for its device and driver extensions is extremely limited. The miniport driver should not attempt to allocate more than 32 kilobytes of memory.

### <span id="accessibility"></span><span id="ACCESSIBILITY"></span>Accessibility of the boot device

The boot device must be accessible before the miniport returns from initialization routine ([**HwStorInitialize**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_initialize) for StorPort and [*HwScsiInitialize*](/previous-versions/windows/hardware/drivers/ff557302(v=vs.85)) for SCSI Port). The operating system might send commands to the boot device at any point after the initialization routine completes.

### <span id="bus_resets"></span><span id="BUS_RESETS"></span>Bus resets

Miniport drivers should disregard requests to reset the bus ([**HwStorResetBus**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_reset_bus) for StorPort and [*HwScsiResetBus*](/previous-versions/windows/hardware/drivers/ff557318(v=vs.85)) for SCSI Port ).

### <span id="dpcs"></span><span id="DPCS"></span>Deferred Procedure Calls (DPCs)

StorPort miniport drivers must not attempt to initialize a DPC routine ([**HwStorDpcRoutine**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_dpc_routine)) with [**StorPortInitializeDpc**](/windows-hardware/drivers/ddi/storport/nf-storport-storportinitializedpc). Any processing normally queued for execution to a DPC routine during an interrupt request must, in this case, occur in the context of that request.

### <span id="multiple_requests"></span><span id="MULTIPLE_REQUESTS"></span>Multiple requests per logical unit

The disk dump port driver does not send multiple requests per logical unit. Therefore, it does not matter what value a miniport driver assigns to the **MultipleRequestPerLu** member of [**PORT\_CONFIGURATION\_INFORMATION**](/previous-versions/windows/hardware/drivers/ff563901(v=vs.85)).

### <span id="polling"></span><span id="POLLING"></span>Polling and time checking

Miniport drivers must not rely on time checking routines, such as [**ScsiPortQuerySystemTime**](/windows-hardware/drivers/ddi/srb/nf-srb-scsiportquerysystemtime) or [**StorPortQuerySystemTime**](/windows-hardware/drivers/ddi/storport/nf-storport-storportquerysystemtime) while running in dump mode. Best practices for miniport drivers exclude using the [**KeQuerySystemTime**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kequerysystemtime) routine, at any time, because miniport drivers should always use port driver library routines to check the time.

### <span id="irql"></span><span id="IRQL"></span>Interrupt request level

The runtime port driver calls [**HwStorFindAdapter**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_find_adapter) and [*HwScsiFindAdapter*](/previous-versions/windows/hardware/drivers/ff557300(v=vs.85)) at PASSIVE IRQL. However, the dump driver calls all miniport routines at IRQL higher than PASSIVE. Therefore, miniport drivers in the dump path must avoid operations, such as registry accesses, that must be performed at PASSIVE IRQL.

### <span id="target_and_lun"></span><span id="TARGET_AND_LUN"></span>Target IDs and logical unit numbers (LUNs)

Miniport drivers must not use a different target ID and LUN for the boot device during the dump process.

Storage miniport drivers in the boot or dump path must detect whether they are running in dump mode. There are two ways that the operating system signals a storage miniport driver that the miniport driver is running in dump mode or the operating system is changing to a hibernation state:

-   The operating system passes **NULL** arguments to the miniport driver's *DriverEntry* routine.

-   The disk dump port driver passes a string of "dump=1" in the *ArgumentString* parameter when it calls the [**HwStorFindAdapter**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_find_adapter) or [*HwScsiFindAdapter*](/previous-versions/windows/hardware/drivers/ff557300(v=vs.85)) routine.

When you look in the debugger for an image of a storage miniport driver in dump mode, the driver name will have a prefix of "dump\_". If the miniport driver is in hibernation mode, the driver name will have a prefix of "hiber\_".

