---
title: Sdv-map.h
description: Sdv-map.h
ms.assetid: c230fb86-fe65-416b-bd3e-a0ab7270576d
keywords: ["output files WDK Static Driver Verifier", "Sdv-map.h WDK Static Driver Verifier", "header files WDK Static Driver Verifier", "driver entry points WDK Static Driver Verifier", "entry points WDK Static Driver Verifier", "Sdv-map.h WDK Static Driver Verifier , about Sdv-map.h", "scanning DriverEntry routine WDK Static Driver Verifier"]
---

# Sdv-map.h


Sdv-map.h is a header file that lists the driver entry points that SDV detected in the driver.

SDV creates an Sdv-map.h file in the driver's sources directory when you use a **staticdv /scan** command to scan the driver's source code. SDV uses the function role type declarations to identify the entry points. If you do not use a **staticdv /scan** command, SDV creates an Sdv-map.h file when you use a **staticdv /rule** or **staticdv /config** command to run an SDV analysis.

If this file is inaccurate or incomplete, you can correct it, approve it, and then rescan and rerun the verification.

This section includes:

[Understanding Sdv-map.h](understanding-the-sdv-map-h-file.md)

[Sdv-map.h Format](format-of-the-sdv-map-h-file.md)

[Approving Sdv-map.h](approving-the-sdv-map-h-file.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Sdv-map.h%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




