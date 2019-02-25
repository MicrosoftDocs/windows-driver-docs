---
title: System Header Files for Storage Drivers
description: System Header Files for Storage Drivers
ms.assetid: 2ee83fa4-41df-403e-86b8-b269f5dfbfed
keywords:
- storage drivers WDK , system header files
- header files WDK storage
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# System Header Files for Storage Drivers


## <span id="ddk_system_header_files_for_storage_drivers_kg"></span><span id="DDK_SYSTEM_HEADER_FILES_FOR_STORAGE_DRIVERS_KG"></span>


The system-supplied storage drivers include the header file *scsi.h*, which contains SCSI-compliant definitions for CDBs and other structures used by most SCSI-compliant drivers. This header file includes *srb.h*, which defines the interfaces provided by the system-supplied port drivers to next-lower storage class and filter drivers.

Operating system-independent SCSI miniport drivers, which can be designed to run both with all platforms of NT-based operating systems and with x86-only Microsoft Windows systems, include the system-supplied header files *miniport.h* and *scsi.h*, which includes *srb.h*.

Tape miniclass drivers include *minitape.h*.

Medium changer miniclass drivers include *mcd.h*.

Vendor-supplied class and filter drivers can also incorporate the sample files *classpnp.h* and *classpnp.c*. These files define a series of **Class**Xxx routines that simplify the design of class and filter drivers. However, *classpnp.h* and *classpnp.c* are only samples, and are not supported in any version of the Windows operating system. Be cautious about using these files in a production driver, because some of the structure and routine declarations in *classpnp.h* might not be current or might be incompatible with the versions of Windows your driver runs in.

 

 




