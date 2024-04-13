---
title: SCSI Miniport Driver's HwScsiAdapterState Routine
description: SCSI Miniport Driver's HwScsiAdapterState Routine
keywords:
- SCSI miniport drivers WDK storage , HwScsiAdapterState
- HwScsiAdapterState
ms.date: 04/20/2017
---

# SCSI Miniport Driver's HwScsiAdapterState Routine


## <span id="ddk_scsi_miniport_drivers_hwscsiadapterstate_routine_kg"></span><span id="DDK_SCSI_MINIPORT_DRIVERS_HWSCSIADAPTERSTATE_ROUTINE_KG"></span>


In NT-based operating systems, miniport drivers should set this entry point to **NULL** in the [**HW\_INITIALIZATION\_DATA (SCSI)**](/windows-hardware/drivers/ddi/srb/ns-srb-_hw_initialization_data) (see [SCSI Miniport Driver Routines](scsi-miniport-driver-routines.md)) only if either of the following conditions hold:

-   The miniport driver drives an HBA to be connected on an I/O bus commonly found only in high-end, RISC-based platforms. That is, an x86-based platform running an x86-only Microsoft Windows system would not have an I/O bus of a type to support the HBA.

-   The miniport driver drives an HBA that could be found in an x86-based platform running an x86-only Windows system, but the HBA has neither a BIOS nor an x86-only real-mode driver.

Otherwise, a miniport driver must have a *HwScsiAdapterState* routine to be portable across NT-based operating systems and x86-only Microsoft Windows systems.

A [**HwScsiAdapterState**](/previous-versions/windows/hardware/drivers/ff557278(v=vs.85)) routine is responsible for saving and restoring the state of its HBA, as requested by the x86-only system during transitions between x86 real and protected processor mode.

See [**HwScsiAdapterState**](/previous-versions/windows/hardware/drivers/ff557278(v=vs.85)) for more information.

 

