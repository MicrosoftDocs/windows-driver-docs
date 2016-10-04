---
title: Files and Your Build Environment
author: windows-driver-content
description: Files and Your Build Environment
MS-HAID:
- 'di\_c1ee6950-1553-461d-b05e-12776df4769c.xml'
- 'hid.files\_and\_your\_build\_environment'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 0c85a599-65bb-45e5-a2f8-eefd47e82025
keywords: ["property sheets WDK DirectInput , files", "game controllers WDK DirectInput , files", "control panels WDK DirectInput , files", "property sheets WDK DirectInput , build environments", "game controllers WDK DirectInput , build environments", "control panels WDK DirectInput , build environments", "build environments WDK DirectInput", "files WDK DirectInput"]
---

# Files and Your Build Environment


## <a href="" id="ddk-files-and-your-build-environment-di"></a>


At a minimum, you will need the Direct X Direct Development Kit (DDK) header file Dicpl.h. This file provides you with the necessary interface, structures, class definitions, and errors. It is recommended that you use DirectInput's **IDirectInputJoyConfig8** interface for all registry access to assure that your property sheet also works on Windows NT 4.0 and later. If you plan to use DirectInput in your property page, you must also used the associated DirectX SDK files. All structures in the DirectInput control panel are packed on 8-byte boundaries. Verify that your property sheet packs structures on 8-byte boundaries.

**Note**   When testing your control panel, make sure to test it on a system whose primary display is set to a resolution of 640 x 480 pixels. Make sure that all the controls are still visible at this reduced resolution.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Files%20and%20Your%20Build%20Environment%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


