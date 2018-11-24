---
title: Supporting Plug and Play in a SCSI Miniport Driver
description: Supporting Plug and Play in a SCSI Miniport Driver
ms.assetid: c8b148ac-b1ab-4870-8818-5ef1c2d68599
keywords:
- SCSI miniport drivers WDK storage , PnP
- PnP WDK SCSI
- Plug and Play WDK SCSI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Plug and Play in a SCSI Miniport Driver


## <span id="ddk_supporting_plug_and_play_in_a_scsi_miniport_driver_kg"></span><span id="DDK_SUPPORTING_PLUG_AND_PLAY_IN_A_SCSI_MINIPORT_DRIVER_KG"></span>


Although Microsoft Windows 2000 and later operating systems are Plug and Play operating systems, by default SCSI miniport drivers are run as legacy drivers. The HBA for a legacy miniport driver cannot be removed from the system while it is running, nor are legacy miniport drivers automatically detected when added to a running system. These limitations might be acceptable for certain HBAs, but SCSI miniport drivers for PC Card/CardBus HBAs and HBAs in laptops should support Plug and Play.

A Plug and Play miniport driver must implement an *HwScsiAdapterControl* routine to stop and manage power to the HBA. No additional routines are required of a Plug and Play miniport driver to accommodate changes in driver initialization.

The SCSI port driver creates PDOs for target devices and the FDO for the miniport driver, and handles requests to add, start or unload the device on behalf of the miniport driver. For general information about Plug and Play drivers, see [Plug and Play](https://msdn.microsoft.com/library/windows/hardware/ff547125).

 

 




