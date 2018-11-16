---
title: SCSI Miniport Drivers
description: SCSI Miniport Drivers
ms.assetid: d9268be8-a68d-4617-b323-349ce7c62f3f
keywords:
- SCSI miniport drivers WDK storage
- storage miniport drivers WDK , SCSI miniport drivers
- miniport drivers WDK storage , SCSI miniport drivers
- SCSI miniport drivers WDK storage , about SCSI miniport drivers
- HBA WDK SCSI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SCSI Miniport Drivers


## <span id="ddk_scsi_miniport_drivers_kg"></span><span id="DDK_SCSI_MINIPORT_DRIVERS_KG"></span>


This section contains the following information:

[Supporting Plug and Play in a SCSI Miniport Driver](supporting-plug-and-play-in-a-scsi-miniport-driver.md)

[Registry Entries for Plug and Play SCSI Miniport Drivers](registry-entries-for-plug-and-play-scsi-miniport-drivers.md)

[Restrictions on SCSI Miniport Drivers that Manage the Boot Drive](restrictions-on-scsi-miniport-drivers-that-manage-the-boot-drive.md)

[Error Handling in SCSI Miniport Drivers](error-handling-in-scsi-miniport-drivers.md)

[Required and Optional SCSI Miniport Driver Routines](required-and-optional-scsi-miniport-driver-routines.md)

SCSI miniport drivers for NT-based operating systems are HBA-specific but operating system-independent. That is, each miniport driver links itself with the system-supplied SCSI port driver, which is a dynamic-link library (DLL), and calls only the port driver's **ScsiPort***Xxx* routines to communicate with the system and its HBA. Such SCSI miniport drivers run on other Microsoft operating systems that support Microsoft Win32 applications and also export the **ScsiPort***Xxx* routines. For more information about the **ScsiPort***Xxx* routines, see [SCSI Port Library Routines](https://msdn.microsoft.com/library/windows/hardware/ff565375).

Note that any SCSI miniport driver that calls routines other than the **ScsiPort***Xxx* cannot run in both Microsoft operating system environments. To remain portable across Microsoft Windows systems, including NT-based operating systems, SCSI miniport drivers must call only the system-supplied **ScsiPort***Xxx*.

A SCSI miniport driver can be a Plug and Play driver, or it can run as a legacy driver that does not participate in Plug and Play operations such as resource redistribution or power management. The primary differences between a Plug and Play and a legacy miniport driver are the order in which initialization routines are called and enforcement of certain restrictions that were applied to miniport drivers in Microsoft Windows NT 4.0, but not enforced.

 

 




