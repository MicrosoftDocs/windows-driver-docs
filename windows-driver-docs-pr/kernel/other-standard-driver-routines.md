---
title: Other Standard Driver Routines
author: windows-driver-content
description: Other Standard Driver Routines
MS-HAID:
- 'DrvComps\_322d7480-7564-4a03-a0d6-647e50ebdef1.xml'
- 'kernel.other\_standard\_driver\_routines'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 3dada9cc-7239-47de-8940-bc4cef8be4ca
keywords: ["driver objects WDK kernel", "standard driver routines WDK kernel , driver objects", "driver routines WDK kernel , driver objects", "routines WDK kernel , driver objects", "objects WDK driver objects"]
---

# Other Standard Driver Routines


## <a href="" id="ddk-other-standard-driver-routines-kg"></a>


As the [driver object illustration](introduction-to-driver-objects.md#driver-object-illustration) shows, kernel-mode drivers have other standard routines along with those for which they set entry points in their respective driver objects. Most standard driver routines and some of the configuration-dependent objects they use are defined by the I/O manager. The ISR, *SynchCritSection* routine, and those shown in the Driver Object figure with names containing the word "custom" are defined by the NT kernel.

Most drivers use the [device extension](device-extensions.md) of each device object they create to maintain device-specific state about their I/O operations and to store pointers to any system resources that they must allocate in order to have other standard routines. For example, the **DDCustomTimerDpc** routine shown in the Driver Object figure requires the driver to supply storage for kernel-defined timer and DPC objects.

The set of standard driver routines for lowest-level drivers shown on the left in the [driver object illustration](introduction-to-driver-objects.md#driver-object-illustration) is necessarily different from the set for higher-level drivers. Some of the routines shown in this figure are device-dependent or configuration-dependent requirements. Others are optional: you may choose to implement such a routine depending on the nature or configuration of the driver's devices, on the driver's design, and on the driver's position in a chain of layered drivers.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Other%20Standard%20Driver%20Routines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


