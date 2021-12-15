---
title: Writing AdapterControl Routines
description: Writing AdapterControl Routines
keywords: ["AdapterControl routines, writing", "adapter objects WDK kernel , writing AdapterControl routines", "DMA transfers WDK kernel , writing AdapterControl routines"]
ms.date: 06/16/2017
---

# Writing AdapterControl Routines





Most drivers of DMA devices have an [*AdapterControl*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_control) routine, which is responsible for initiating DMA operations. (Drivers that do not require *AdapterControl* routines include those that [use scatter/gather DMA](using-scatter-gather-dma.md) and those that [use common-buffer, bus-master DMA](using-common-buffer-bus-master-dma.md).)

When a driver calls [**AllocateAdapterChannel**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pallocate_adapter_channel), its *AdapterControl* routine is run immediately if the system DMA controller or bus-master adapter is available for a DMA operation, and if enough map registers are available. Otherwise, the *AdapterControl* routine is queued until these resources are available.

If the driver's *AdapterControl* routine returns **KeepObject** or **DeallocateObjectKeepRegisters** (thereby retaining the system DMA controller channel or bus-master adapter for additional transfer operations), the driver's [*DpcForIsr*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_dpc_routine) or [*CustomDpc*](/windows-hardware/drivers/ddi/wdm/nc-wdm-kdeferred_routine) routine is responsible for releasing the adapter object or map registers by calling [**FreeAdapterChannel**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pfree_adapter_channel) or [**FreeMapRegisters**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pfree_map_registers) before the DPC routine completes the current IRP and returns control.

 

