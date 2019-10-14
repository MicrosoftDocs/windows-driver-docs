---
title: SCSI Miniport Driver's DriverEntry Routine
description: SCSI Miniport Driver's DriverEntry Routine
ms.assetid: b143bb19-2c9e-4e43-841f-a3c47c7f1a1b
keywords:
- DriverEntry WDK storage
ms.date: 10/08/2019
ms.localizationpriority: medium
---

# SCSI Miniport Driver's DriverEntry Routine

A **DriverEntry** routine is the initial entry point for most Microsoft Windows kernel-mode drivers and for every SCSI miniport driver. A miniport driver's [**DriverEntry**](driverentry-of-scsi-miniport-driver.md) routine is called with two input arguments of type PVOID and must do the following:

1. Initialize a [HW_INITIALIZATION_DATA (SCSI)](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/srb/ns-srb-_hw_initialization_data) structure on the stack with zeros.

2. Set the **HwInitializationDataSize** member to **sizeof**(HW_INITIALIZATION_DATA).

3. Set driver-specific and HBA-specific values in the HW_INITIALIZATION_DATA members, including the miniport driver's entry points. The following entry points must be set:

   - [*HwScsiFindAdapter*](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff557300(v=vs.85))
   - [*HwScsiInitialize*](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff557302(v=vs.85))
   - [*HwScsiStartIo*](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff557323(v=vs.85))
   - [*HwScsiResetBus*](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff557318(v=vs.85))

    The following entry points can be set to a driver-supplied routine or must be set to **NULL**:

  - [*HwScsiInterrupt*](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff557312(v=vs.85)) (**NULL** if the miniport driver uses polling exclusively)
  - [*HwScsiDmaStarted*](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff557291(v=vs.85)) (**NULL** if the HBA uses PIO or is a bus master)
  - [*HwScsiAdapterState*](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff557278(v=vs.85)) (**NULL** if the miniport driver runs only on NT-based operating system platforms or if it is designed to also run on x86-only Windows platforms but the HBA has neither a BIOS nor x86-real-mode driver)
  - [*HwScsiAdapterControl*](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff557274(v=vs.85)) (**NULL** if the miniport driver does not support Plug and Play)

4. In an a legacy miniport driver, set up any driver-determined context data that the miniport driver's *HwScsiFindAdapter* routine will use.

5. Call [**ScsiPortInitialize**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/srb/nf-srb-scsiportinitialize) with the pointers that were input to the **DriverEntry** routine, the address of the filled-in HW_INITIALIZATION_DATA, and the address of the context data, if any.
