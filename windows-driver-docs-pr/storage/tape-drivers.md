---
title: Tape Drivers
author: windows-driver-content
description: Tape Drivers
ms.assetid: d6d8ac92-0713-401c-9551-fc8e08e903f4
keywords: ["tape drivers WDK storage", "storage tape drivers WDK", "storage drivers WDK , tape drivers", "tape drivers WDK storage , about tape drivers", "storage tape drivers WDK , about tape drivers"]
---

# Tape Drivers


## <span id="ddk_tape_drivers_kg"></span><span id="DDK_TAPE_DRIVERS_KG"></span>


This section contains the following information:

[Using the Tape Class Driver](using-the-tape-class-driver.md)

[Required and Optional Tape Miniclass Routines](required-and-optional-tape-miniclass-routines.md)

[Storing Tape Miniclass Context in Optional Extensions](storing-tape-miniclass-context-in-optional-extensions.md)

[Processing Tape Device Control Requests](processing-tape-device-control-requests.md)

NT-based operating systems provide a generic tape class driver that handles operating system-specific and device-independent tape tasks. The tape class driver is provided as a kernel-mode DLL. To support a new tape device or family of tape devices, a driver writer creates a device-specific tape miniclass driver that links dynamically to the system-supplied tape class driver.

If a tape miniclass driver calls only routines in the tape class driver, the miniclass driver can be portable across Microsoft operating systems that support Win32 applications and provide a tape class driver that uses the tape miniclass interface. A tape miniclass driver includes the header file *minitape.h*.

An existing tape miniclass driver must be modified to support one new entry point, TapeMiniGetMediaTypes, in order to build and run under Windows 2000 and later operating systems. No other modifications are required. The system-supplied tape class driver, together with the system-supplied storage port driver, handles Plug and Play and power management requests on behalf of a tape miniclass driver.

This section describes the support provided by the operating system-specific tape class driver and provides guidelines for writing a new tape miniclass driver. See [Tape Class Driver Routines](https://msdn.microsoft.com/library/windows/hardware/ff567959) and [Tape Miniclass Driver Routines](https://msdn.microsoft.com/library/windows/hardware/ff567970) for details on the routines in the tape class and tape miniclass drivers. See [Device Configurations and Layered Drivers](https://msdn.microsoft.com/library/windows/hardware/ff543100) for a description of the storage device driver layers.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Tape%20Drivers%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


