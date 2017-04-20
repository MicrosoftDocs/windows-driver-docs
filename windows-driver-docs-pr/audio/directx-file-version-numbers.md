---
title: DirectX File Version Numbers
description: DirectX File Version Numbers
ms.assetid: 60f840d2-384c-49be-bf05-c16613b4858c
keywords:
- DirectX file version numbers WDK audio
- version numbers WDK audio
- audio miniport drivers WDK , version numbers
- miniport drivers WDK audio , version numbers
- audio drivers WDK , version numbers
- driver version numbers WDK audio
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DirectX File Version Numbers


## <span id="directx_file_version_numbers"></span><span id="DIRECTX_FILE_VERSION_NUMBERS"></span>


VxDs that support DirectX should meet the DirectX setup requirements for driver version numbers and driver capabilities. See the DirectX 8.0 Programmer's Reference. These requirements do not apply to WDM or Windows NT 4.0 drivers.

Use the following procedure to check the driver version numbers:

-   Use the Setup application provided with any DX-supported game to install the device driver. Record the version numbers for all installed files, including all .drv, .dll, .vxd, and .exe files in the driver-installation package.

-   Confirm that all internal version numbers correspond to external (string) version numbers and that the numbers follow the version-numbering rules (see [Version Numbers for Audio Drivers](version-numbers-for-audio-drivers.md)).

-   Use Windows Explorer to view the directory containing the files. Right-click each file and click **Properties** to verify that the copyright information is correct. In particular, verify that your driver does not specify "Microsoft" as the vendor name.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20DirectX%20File%20Version%20Numbers%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


