---
title: Driver DLL for display adapter or chipset has properly formatted file version
description: This topic describes the proper formatting for display driver DLLs.
ms.assetid: E39B2A48-D3F8-4EA5-BCF3-23B1053E8D96
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Driver DLL for display adapter or chipset has properly formatted file version


This topic describes the proper formatting for display driver DLLs.

The file version of the display driver DLLs must be of the form A.BB.CC.DDDD:

-   The A field must be set to 9 for WDDM 1.2 drivers on Windows 8.
-   The A field must be set to 8 for WDDM 1.1 drivers on Windows 7.
-   The A field must be set to 7 for WDDM 1.0 drivers on Windows Vista.
-   The A field must be set to 6 for XDDM drivers on Windows Vista.

For Windows 7 and earlier (WDDM 1.1 and earlier) drivers the BB field must be set to the DDI version that the driver supports:

-   DirectX 9 drivers (which expose any of the D3DDEVCAPS2\_\* caps) must set BB to 14.
-   DirectX 10 drivers must set BB to 15.
-   Direct3D 11-DDI driver on Direct3D 10 hardware must set BB to 16.
-   Direct3D 11-DDI driver on Direct3D 11 hardware must set BB to 17.

For Windows 8 (WDDM 1.2) drivers the BB field must be set to the highest DirectX feature level supported by the driver on the graphics hardware covered by the driver:

-   A Feature Level 9 driver must set BB to 14.
-   A Feature Level 10 driver must set BB to 15.
-   A Feature Level 11 driver must set BB to 17.
-   A Feature Level 11\_1 driver must set BB to 18.

Because for WDDM 1.2 drivers, BB is set to reflect feature level supported, irrespective of hardware DX level, 16 is not used, as it was specific to D3D11-DDI on DX10 hardware for WDDM 1.1 drivers.

The CC field can be equal to any value between 01 and 9999.

The DDDD field can be set to any numerical value between 0 and 9999.

For example:

-   Windows Vista DirectX 9.0-compatible WDDM drivers can use the range 7.14.01.0000 to 7.14.9999.9999.
-   Windows 7 DirectX 10.0-compatible WDDM 1.1 drivers can use the range 8.15.01.0000 to 8.15.9999.9999.
-   Windows 8 WDDM 1.2 drivers on DX10 hardware would be 9.15.01.0000 to 9.15.9999.9999.

**Recommendation** (this will become a requirement in a future release): We highly recommend that the DriverVer in the display driver .INF file also conform to the above DLL version-numbering requirement, except that for Windows 8, WDDM 1.2 drivers, the BB field in the INF DriverVer must be set for the highest DirectX feature level that is supported by the driver on the graphics hardware listed in the INF.

 

 





