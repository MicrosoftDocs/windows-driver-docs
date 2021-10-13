---
title: SCSI Miniport Driver's DriverEntry Routine
description: SCSI Miniport Driver's DriverEntry Routine
keywords:
- DriverEntry WDK storage
ms.date: 10/08/2019
ms.localizationpriority: medium
---

# SCSI Miniport Driver's DriverEntry Routine

A **DriverEntry** routine is the initial entry point for most Microsoft Windows kernel-mode drivers and for every SCSI miniport driver. A miniport driver's [**DriverEntry**](driverentry-of-scsi-miniport-driver.md) routine is called with two input arguments of type PVOID and must do the following:

1. Initialize a [HW_INITIALIZATION_DATA (SCSI)](/windows-hardware/drivers/ddi/srb/ns-srb-_hw_initialization_data) structure on the stack with zeros.

2. Set the **HwInitializationDataSize** member to **sizeof**(HW_INITIALIZATION_DATA).

3. Set driver-specific and HBA-specific values in the HW_INITIALIZATION_DATA members, including the miniport driver's entry points. The following entry points must be set:

   - [*HwScsiFindAdapter*](/previous-versions/windows/hardware/drivers/ff557300(v=vs.85))
   - [*HwScsiInitialize*](/previous-versions/windows/hardware/drivers/ff557302(v=vs.85))
   - [*HwScsiStartIo*](/previous-versions/windows/hardware/drivers/ff557323(v=vs.85))
   - [*HwScsiResetBus*](/previous-versions/windows/hardware/drivers/ff557318(v=vs.85))

    The following entry points can be set to a driver-supplied routine or must be set to **NULL**:

  - [*HwScsiInterrupt*](/previous-versions/windows/hardware/drivers/ff557312(v=vs.85)) (**NULL** if the miniport driver uses polling exclusively)
  - [*HwScsiDmaStarted*](/previous-versions/windows/hardware/drivers/ff557291(v=vs.85)) (**NULL** if the HBA uses PIO or is a bus master)
  - [*HwScsiAdapterState*](/previous-versions/windows/hardware/drivers/ff557278(v=vs.85)) (**NULL** if the miniport driver runs only on NT-based operating system platforms or if it is designed to also run on x86-only Windows platforms but the HBA has neither a BIOS nor x86-real-mode driver)
  - [*HwScsiAdapterControl*](/previous-versions/windows/hardware/drivers/ff557274(v=vs.85)) (**NULL** if the miniport driver does not support Plug and Play)

4. In an a legacy miniport driver, set up any driver-determined context data that the miniport driver's *HwScsiFindAdapter* routine will use.

5. Call [**ScsiPortInitialize**](/windows-hardware/drivers/ddi/srb/nf-srb-scsiportinitialize) with the pointers that were input to the **DriverEntry** routine, the address of the filled-in HW_INITIALIZATION_DATA, and the address of the context data, if any.
