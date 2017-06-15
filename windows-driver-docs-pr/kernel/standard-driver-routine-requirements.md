---
title: Standard Driver Routine Requirements
author: windows-driver-content
description: Standard Driver Routine Requirements
MS-HAID:
- 'DrvComps\_5bc157a8-bfbb-4602-b647-685b883dac84.xml'
- 'kernel.standard\_driver\_routine\_requirements'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 49b382ad-c282-41d2-b8b3-68eca4e12b9c
keywords: ["standard driver routines WDK kernel , requirements", "driver routines WDK kernel , requirements", "routines WDK kernel , requirements"]
---

# Standard Driver Routine Requirements


## <a href="" id="ddk-standard-driver-routine-requirements-kg"></a>


Keep the following points in mind when designing a kernel-mode driver:

-   Each driver must have a [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine, which initializes driver-wide data structures and resources. The I/O manager calls the **DriverEntry** routine when it loads the driver.

-   Every driver must have at least one dispatch routine that receives and processes I/O request packets (IRPs). Each driver must place a dispatch routine's entry point in its [**DRIVER\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff544174) structure, for each [IRP major function code](https://msdn.microsoft.com/library/windows/hardware/ff550710) that the driver can receive. A driver can have a separate dispatch routine for each IRP major function code, or it can have one or more dispatch routines that handle several function codes.

-   Every WDM driver must have an [*Unload*](https://msdn.microsoft.com/library/windows/hardware/ff564886) routine. The driver must place the *Unload* routine's entry point in the driver's driver object. The responsibilities of a [PnP driver's Unload routine](pnp-driver-s-unload-routine.md) are minimal, but a [non-PnP driver's unload routine](non-pnp-driver-s-unload-routine.md) is responsible for releasing any system resources that the driver is using.

-   Every WDM driver must have an [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine and define its entry point in the [*driver extension*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-driver-extension) of the driver object. An *AddDevice* routine is responsible for creating and initializing device objects for each PnP device the driver controls.

-   A driver can have a [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine, which the I/O manager calls to start I/O operations for IRPs the driver has queued to a system-supplied IRP queue. Any driver that does not have a *StartIo* routine must either set up and manage internal queues for the IRPs it receives, or it must complete every IRP within its dispatch routines. Higher-level drivers might not have a *StartIo* routine, if they simply pass IRPs to lower-level drivers directly from their dispatch routines.

-   Certain miniport drivers are exceptions to the preceding requirements. See the device-type-specific documentation in the Windows Driver Kit (WDK) for information about the requirements for miniport drivers.

-   Whether a driver has any other kind of standard routine depends on its functionality and on how that driver fits into the system (for example, whether it interoperates with system-supplied drivers). See the device-type specific documentation in the WDK for details.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Standard%20Driver%20Routine%20Requirements%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


