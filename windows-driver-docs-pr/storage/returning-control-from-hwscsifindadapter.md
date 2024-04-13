---
title: Returning Control from HwScsiFindAdapter
description: Returning Control from HwScsiFindAdapter
keywords:
- HwScsiFindAdapter
- SCSI miniport drivers WDK storage , HwScsiFindAdapter
- return values WDK SCSI
- status values WDK SCSI
ms.date: 04/20/2017
---

# Returning Control from HwScsiFindAdapter

When a legacy miniport driver's [*HwScsiFindAdapter*](/previous-versions/windows/hardware/drivers/ff557300(v=vs.85)) routine returns control, [**ScsiPortInitialize**](/windows-hardware/drivers/ddi/srb/nf-srb-scsiportinitialize) returns to the **DriverEntry** routine if the call(s) to *HwScsiFindAdapter* indicated that the miniport driver could not support an HBA. Otherwise, **ScsiPortInitialize** claims resources in the registry and sets up necessary system resources, such as interrupt and adapter objects, on behalf of the miniport driver. Then, it calls the miniport driver's *HwScsiInitialize* routine, described in [SCSI Miniport Driver's HwScsiInitialize Routine](scsi-miniport-driver-s-hwscsiinitialize-routine.md).

When a Plug and Play miniport driver's *HwScsiFindAdapter* routine returns control, the Plug and Play manager is allowed to unload the miniport driver if the call(s) to *HwScsiFindAdapter* indicated that the miniport driver could not support an HBA. Otherwise, the port driver connects interrupts (other resources having been claimed and set up before the *HwScsiFindAdapter* call) and calls the miniport driver's [*HwScsiInitialize*](/previous-versions/windows/hardware/drivers/ff557302(v=vs.85)) routine, which initializes the HBA.

Currently, in addition to the values it sets in the [PORT_CONFIGURATION_INFORMATION](/windows-hardware/drivers/ddi/srb/ns-srb-_port_configuration_information), the port driver also checks the registry for user-set values that disable any or all of the following:

- Synchronous transfers on the HBA: The port driver ORs the default **SrbFlags** that it maintains for the HBA with SRB_FLAGS_DISABLE_SYNCH_TRANSFER.

- Bus-disconnect operations on the HBA: The port driver ORs the default **SrbFlags** with SRB_FLAGS_DISABLE_DISCONNECT.

- Tagged queuing: The port driver sets the **TaggedQueuing** Boolean that it maintains for the HBA to **FALSE**.

- Internal queuing of requests on the HBA: The port driver sets to **FALSE** the **MultipleRequestPerLu** Boolean that it maintains about the HBA.

Any of the immediately preceding "disable" values in the registry overrides whatever the *HwScsiFindAdapter* routine sets in the PORT_CONFIGURATION_INFORMATION buffer. Note that temporarily disabling synchronous transfers, bus-disconnect operations, tagged queuing, and HBA internal request queuing can simplify using a debugger to trace request handling in a miniport driver that is under development.

Note also that the NT-based operating system port driver uses values from the PORT_CONFIGURATION_INFORMATION provided by a miniport driver's *HwScsiFindAdapter* routine or from other sources (such as the registry for a legacy miniport driver) to fill in the IO_SCSI_CAPABILITIES data for use by storage class drivers, as described in [Storage Class Drivers](introduction-to-storage-class-drivers.md).
