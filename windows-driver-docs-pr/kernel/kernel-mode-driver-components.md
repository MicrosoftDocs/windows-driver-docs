---
title: Kernel-Mode Driver Components
author: windows-driver-content
description: Kernel-Mode Driver Components
MS-HAID:
- 'DrvComps\_781d63af-c743-4ad0-9712-807dbf6f860d.xml'
- 'kernel.kernel\_mode\_driver\_components'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 79be2948-cc74-4f0b-8ffa-1e57f44d7b0c
keywords: ["kernel-mode drivers WDK , components", "kernel-mode drivers WDK , standard driver routines", "standard driver routines WDK kernel", "driver routines WDK kernel", "routines WDK kernel"]
---

# Kernel-Mode Driver Components


## <a href="" id="ddk-kernel-mode-driver-components-kg"></a>


This section introduces the standard routines contained in kernel-mode drivers. Some of these *standard driver routines* are required; others are optional. The section also introduces *driver objects*, which contain pointers to each driver's standard routines.

Some drivers interact with a system-supplied port driver or class driver that defines much of the driver's required functionality. For example, a SCSI miniport driver primarily interacts with the SCSI port driver. For such drivers, see the class-specific documentation for details of required and optional driver support.

This section includes:

[Introduction to Standard Driver Routines](introduction-to-standard-driver-routines.md)

[Standard Driver Routine Requirements](standard-driver-routine-requirements.md)

[Introduction to Driver Objects](introduction-to-driver-objects.md)

[Writing a DriverEntry Routine](writing-a-driverentry-routine.md)

[Writing a Reinitialize Routine](writing-a-reinitialize-routine.md)

[Writing an AddDevice Routine](writing-an-adddevice-routine.md)

[Writing Dispatch Routines](writing-dispatch-routines.md)

[Writing an Unload Routine](writing-an-unload-routine.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Kernel-Mode%20Driver%20Components%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


