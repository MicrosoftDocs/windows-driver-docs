---
title: Making SCSI Port Miniport Drivers Work with Storport
description: Making SCSI Port Miniport Drivers Work with Storport
ms.assetid: d2e8daaf-47e2-4a6c-9992-517dc107d4bd
keywords:
- Storport drivers WDK , SCSI Port miniport drivers
- SCSI Port drivers WDK storage , Storport drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Making SCSI Port Miniport Drivers Work with Storport


## <span id="ddk_making_scsi_port_miniport_drivers_work_with_storport_kg"></span><span id="DDK_MAKING_SCSI_PORT_MINIPORT_DRIVERS_WORK_WITH_STORPORT_KG"></span>


The Storport-miniport driver interface is designed to be as similar to the SCSI Port-miniport driver interface as possible, in order to facilitate the adaptation of SCSI Port miniport drivers to work with the Storport driver. In order to make a SCSI Port miniport driver work with Storport, you must take the following basic steps:

1.  Change all instances of the **\#include** &lt;*scsi.h*&gt; directive with the **\#include** &lt;*storport.h*&gt; directive.

    If both the *scsi.h* and *storport.h* header files are included, a compile time error will occur.

2.  Replace s*csiport.lib* with *storport.lib* in your build scripts, that is, in the sources or **makefile** file.

3.  Make certain that all expanded structures are properly initialized.

    The sizes of both the [**HW\_INITIALIZATION\_DATA (SCSI)**](https://msdn.microsoft.com/library/windows/hardware/ff557456) structure and the [**PORT\_CONFIGURATION\_INFORMATION (SCSI)**](https://msdn.microsoft.com/library/windows/hardware/ff563900) structure have changed, so make certain the new members are properly initialized.

The Storport header file, *storport.h,* currently retains both SCSI Port-prefixed commands and StorPort-prefixed commands to facilitate porting from the SCSI Port.

This section provides more detailed instructions for driver writers who wish to modify a miniport driver that is designed to work with SCSI Port, so that it can work with Storport. The following topics are covered:

[Requirements for Using Storport with an Adapter](requirements-for-using-storport-with-an-adapter.md)

[Hardware Initialization with Storport](hardware-initialization-with-storport.md)

[Setting Port Configuration Information with Storport](setting-port-configuration-information-with-storport.md)

 

 




