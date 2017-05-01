---
title: Driver DLL for display adapter or chipset has properly formatted file version
description: This topic describes the proper formatting for display driver DLLs.
ms.assetid: E39B2A48-D3F8-4EA5-BCF3-23B1053E8D96
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

-   Windows Vista DirectX 9.0â€“compatible WDDM drivers can use the range 7.14.01.0000 to 7.14.9999.9999.
-   Windows 7 DirectX 10.0â€“compatible WDDM 1.1 drivers can use the range 8.15.01.0000 to 8.15.9999.9999.
-   Windows 8 WDDM 1.2 drivers on DX10 hardware would be 9.15.01.0000 to 9.15.9999.9999.

**Recommendation** (this will become a requirement in a future release): We highly recommend that the DriverVer in the display driver .INF file also conform to the above DLL version-numbering requirement, except that for Windows 8, WDDM 1.2 drivers, the BB field in the INF DriverVer must be set for the highest DirectX feature level that is supported by the driver on the graphics hardware listed in the INF.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Driver%20DLL%20for%20display%20adapter%20or%20chipset%20has%20properly%20formatted%20file%20version%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




