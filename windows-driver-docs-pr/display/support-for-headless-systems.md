---
title: Support for headless systems
description: Windows 8 supports booting without any graphics hardware. This is accomplished by using a stub display output if no display devices are found. This stub display is implemented as part of the in-box Microsoft Basic Display Driver (MSBDD).
ms.assetid: 6351F6F9-6666-4040-A82A-3813ACCE8DEA
---

# Support for headless systems


Windows 8 supports booting without any graphics hardware. This is accomplished by using a stub display output if no display devices are found. This stub display is implemented as part of the in-box Microsoft Basic Display Driver (MSBDD).

Because the stub display is used when no PnP driver is available, no third-party drivers are required. It works for both normal operation and for system crashes, so no hardware or firmware support is required to fake a display device.

On architectures in which VGA has been the norm, MSBDD requires positive confirmation that VGA is not present; otherwise, it assumes that VGA hardware is available and that the system is not headless. System firmware should set the VGA Not Present flag in the IAPC\_BOOT\_ARCH field of FADT and if there is any VBIOS, it should implement an empty mode list through the VESA BIOS Extensions (VBE). These mechanisms should indicate that VGA is not present even if the system implements a VBIOS with int 10h mode 12h support for compatibility with previous versions of Windows. In the absence of VBE support, the Basic Display Driver uses a display that is initialized by the boot loader, so a headless system should not represent a working display through UEFI GOP.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Support%20for%20headless%20systems%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




