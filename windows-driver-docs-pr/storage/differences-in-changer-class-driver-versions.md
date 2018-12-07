---
title: Differences in Changer Class Driver Versions
description: Differences in Changer Class Driver Versions
ms.assetid: 4ae4d1b0-cf2f-4c81-b8ae-3a91fd479a89
keywords:
- changer drivers WDK storage , class drivers
- storage changer drivers WDK , class drivers
- class drivers WDK storage , changer drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Differences in Changer Class Driver Versions


## <span id="ddk_differences_in_changer_class_driver_versions_kg"></span><span id="DDK_DIFFERENCES_IN_CHANGER_CLASS_DRIVER_VERSIONS_KG"></span>


There are three key differences between the implementation of the changer class/miniclass driver pair in Windows XP and in Windows 2000:

1.  Different use of a [**DriverEntry of Changer Miniclass Drivers**](https://msdn.microsoft.com/library/windows/hardware/ff552647) routine in the miniclass driver.

    In Windows 2000, the changer class driver's **DriverEntry** routine performs various driver initialization tasks, including the initialization of entry points for I/O requests. In Windows XP and later operating systems, initialization takes place in the **DriverEntry** routine of the miniclass driver. See [Required Changer Miniclass Routines](required-changer-miniclass-routines.md) for further information about the tasks that a miniclass driver's **DriverEntry** routine is required to perform.

2.  Different means of accessing *classpnp.sys* library routines.

    Class drivers for disk, tape, CD-ROM, and changer devices make use of the *classpnp.sys* library, a system-supplied DLL that contains a collection of operating system-specific, device-independent routines.

    Most system-supplied storage class drivers provide a set of key routines similar to routines found in the *classpnp.sys* library. This is done so that their miniclass drivers can call class driver routines instead of making direct calls to *classpnp.sys.* This shields the miniclass drivers from changes to the *classpnp.sys* DDI.

    Windows 2000 changer miniclass drivers are an exception to this rule, because in Windows 2000 the changer class driver does not provide miniclass drivers with a facility for calling the *classpnp.sys* routines indirectly. Thus, in Windows 2000, changer miniclass drivers must either call the *classpnp.sys* routines directly or call equivalent routines in line. Miniclass drivers that call *classpnp.sys* routines directly must link to the *classpnp.sys* library statically, swelling the size of the driver. If a driver dynamically links to *classpnp.sys*, changes to this library in subsequent releases might cause the driver to malfunction.

    In Windows XP and later operating systems, several of the most important services formerly provided by direct calls to the *classpnp.sys* library are provided by the changer class driver. Therefore, in Windows XP and later operating systems, it is usually unnecessary for changer miniclass drivers to call *classpnp.sys* library routines directly.

3.  The Windows XP changer class driver provides routines not available in Windows 2000. The discussion that follows examines this difference.

In Windows 2000, the changer class driver provides the following routines for the miniclass driver to call:

-   [**ChangerClassAllocatePool**](https://msdn.microsoft.com/library/windows/hardware/ff551402) -- allocates pool memory.

-   [**ChangerClassFreePool**](https://msdn.microsoft.com/library/windows/hardware/ff551411) -- frees pool memory.

-   [**ChangerClassDebugPrint**](https://msdn.microsoft.com/library/windows/hardware/ff551406) -- prints debugging information.

In Windows XP and later operating systems, the changer class driver provides, two additional routines in addition to the routines previously listed.

-   [**ChangerClassInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff551413) -- The changer miniclass driver calls **ChangerClassInitialize** from within its **DriverEntry** routine to initialize the driver. **ChangerClassInitialize** performs many tasks formerly performed by the Windows 2000 changer class driver's **DriverEntry** routine.

-   [**ChangerClassSendSrbSynchronous**](https://msdn.microsoft.com/library/windows/hardware/ff551415) -- initializes and synchronously sends an SRB to an indicated target device.

 

 




