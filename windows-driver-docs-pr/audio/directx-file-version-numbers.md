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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DirectX File Version Numbers


## <span id="directx_file_version_numbers"></span><span id="DIRECTX_FILE_VERSION_NUMBERS"></span>


VxDs that support DirectX should meet the DirectX setup requirements for driver version numbers and driver capabilities. See the DirectX 8.0 Programmer's Reference. These requirements do not apply to WDM or Windows NT 4.0 drivers.

Use the following procedure to check the driver version numbers:

-   Use the Setup application provided with any DX-supported game to install the device driver. Record the version numbers for all installed files, including all .drv, .dll, .vxd, and .exe files in the driver-installation package.

-   Confirm that all internal version numbers correspond to external (string) version numbers and that the numbers follow the version-numbering rules (see [Version Numbers for Audio Drivers](version-numbers-for-audio-drivers.md)).

-   Use Windows Explorer to view the directory containing the files. Right-click each file and click **Properties** to verify that the copyright information is correct. In particular, verify that your driver does not specify "Microsoft" as the vendor name.

 

 




