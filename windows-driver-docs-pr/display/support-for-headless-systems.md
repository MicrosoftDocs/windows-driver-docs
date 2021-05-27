---
title: Support for headless systems
description: Windows 8 supports booting without any graphics hardware.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Support for headless systems


Windows 8 supports booting without any graphics hardware. This is accomplished by using a stub display output if no display devices are found. This stub display is implemented as part of the in-box Microsoft Basic Display Driver (MSBDD).

Because the stub display is used when no PnP driver is available, no third-party drivers are required. It works for both normal operation and for system crashes, so no hardware or firmware support is required to fake a display device.

On architectures in which VGA has been the norm, MSBDD requires positive confirmation that VGA is not present; otherwise, it assumes that VGA hardware is available and that the system is not headless. System firmware should set the VGA Not Present flag in the IAPC\_BOOT\_ARCH field of FADT and if there is any VBIOS, it should implement an empty mode list through the VESA BIOS Extensions (VBE). These mechanisms should indicate that VGA is not present even if the system implements a VBIOS with int 10h mode 12h support for compatibility with previous versions of Windows. In the absence of VBE support, the Basic Display Driver uses a display that is initialized by the boot loader, so a headless system should not represent a working display through UEFI GOP.

 

 





