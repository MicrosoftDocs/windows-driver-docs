---
title: Use Only Supplied Resources in a Plug and Play SCSI Miniport
description: Use Only Supplied Resources in a Plug and Play SCSI Miniport
ms.assetid: 26c688dc-b6af-4a0c-8401-d53e653d90b3
keywords:
- SCSI miniport drivers WDK storage , PnP
- PnP WDK SCSI
- Plug and Play WDK SCSI
- converting SCSI miniport drivers
- resource restrictions WDK SCSI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Use Only Supplied Resources in a Plug and Play SCSI Miniport


## <span id="ddk_use_only_supplied_resources_in_a_plug_and_play_scsi_miniport_kg"></span><span id="DDK_USE_ONLY_SUPPLIED_RESOURCES_IN_A_PLUG_AND_PLAY_SCSI_MINIPORT_KG"></span>


One of the goals for a Plug and Play system is to reduce or eliminate the number of drivers that detect their devices by accessing known memory locations. This includes drivers that determine their resources by reading the configuration space for their HBA.

In Plug and Play, devices on enumerable buses are detected by the driver for the bus. This allows the bus driver to handle any resource conflicts, provide special-case fixes for broken bus and bridge parts, and so forth.

Consequently, a SCSI miniport driver must use only the resources provided by the port driver (if any) in Microsoft Windows 2000 and later systems. The miniport driver is allowed to scan the bus for an HBA only if the port driver passes in zero-value access ranges. If the miniport driver attempts to use resources that are not assigned to it, the [**ScsiPortGetDeviceBase**](https://msdn.microsoft.com/library/windows/hardware/ff564629) call will fail. Calls to read and write device registers or ports that have not been properly mapped also might fail.

 

 




