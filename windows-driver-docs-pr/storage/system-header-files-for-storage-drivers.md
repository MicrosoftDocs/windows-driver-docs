---
title: System Header Files for Storage Drivers
author: windows-driver-content
description: System Header Files for Storage Drivers
ms.assetid: 2ee83fa4-41df-403e-86b8-b269f5dfbfed
keywords: ["storage drivers WDK , system header files", "header files WDK storage"]
---

# System Header Files for Storage Drivers


## <span id="ddk_system_header_files_for_storage_drivers_kg"></span><span id="DDK_SYSTEM_HEADER_FILES_FOR_STORAGE_DRIVERS_KG"></span>


The system-supplied storage drivers include the header file *scsi.h*, which contains SCSI-compliant definitions for CDBs and other structures used by most SCSI-compliant drivers. This header file includes *srb.h*, which defines the interfaces provided by the system-supplied port drivers to next-lower storage class and filter drivers.

Operating system-independent SCSI miniport drivers, which can be designed to run both with all platforms of NT-based operating systems and with x86-only Microsoft Windows systems, include the system-supplied header files *miniport.h* and *scsi.h*, which includes *srb.h*.

Tape miniclass drivers include *minitape.h*.

Medium changer miniclass drivers include *mcd.h*.

Vendor-supplied class and filter drivers can also incorporate the sample files *classpnp.h* and *classpnp.c*. These files define a series of **Class**Xxx routines that simplify the design of class and filter drivers. However, *classpnp.h* and *classpnp.c* are only samples, and are not supported in any version of the Windows operating system. Be cautious about using these files in a production driver, because some of the structure and routine declarations in *classpnp.h* might not be current or might be incompatible with with the versions of Windows your driver runs in.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20System%20Header%20Files%20for%20Storage%20Drivers%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


