---
title: Converting a Windows NT 4.0 SCSI Miniport for Plug and Play
description: Converting a Windows NT 4.0 SCSI Miniport for Plug and Play
ms.assetid: 46e5eb41-ff41-4054-856b-cc32f286e543
keywords:
- SCSI miniport drivers WDK storage , PnP
- PnP WDK SCSI
- Plug and Play WDK SCSI
- converting SCSI miniport drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Converting a Windows NT 4.0 SCSI Miniport for Plug and Play


## <span id="ddk_converting_a_windows_nt_4_0_scsi_miniport_for_plug_and_play_kg"></span><span id="DDK_CONVERTING_A_WINDOWS_NT_4_0_SCSI_MINIPORT_FOR_PLUG_AND_PLAY_KG"></span>


Even if a miniport driver has enabled Plug and Play in the registry, the driver will fault during initialization unless it honors certain restrictions in the use of the *HwContext* pointer and resources supplied by the port driver. A miniport driver might also fault during initialization if it depends on a predictable initialization order of drivers.

To run successfully under Plug and Play, a Microsoft Windows

NT 4.0 miniport driver's source code might need to be modified as described in the following sections.

 

 




