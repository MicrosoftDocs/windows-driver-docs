---
title: SCSI Miniport Drivers
author: windows-driver-content
description: SCSI Miniport Drivers
ms.assetid: d9268be8-a68d-4617-b323-349ce7c62f3f
keywords: ["SCSI miniport drivers WDK storage", "storage miniport drivers WDK , SCSI miniport drivers", "miniport drivers WDK storage , SCSI miniport drivers", "SCSI miniport drivers WDK storage , about SCSI miniport drivers", "HBA WDK SCSI"]
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20SCSI%20Miniport%20Drivers%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


