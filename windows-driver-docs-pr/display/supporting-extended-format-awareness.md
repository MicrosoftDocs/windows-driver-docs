---
title: Supporting Extended Format Awareness
description: Supporting Extended Format Awareness
ms.assetid: b473ebf2-75a0-4e3f-8190-d1a557ae6da0
keywords: ["Direct3D version 10.1 WDK Windows 7 display", "Direct3D version 10.1 WDK Windows 7 display , extended format awareness", "extended format awareness WDK Windows 7 display"]
---

# Supporting Extended Format Awareness


This section applies only to Windows 7 and later operating systems.

Several new formats are defined for the version of Direct3D 10.1 that Windows 7 provides. Also, Windows 7 Direct3D 10.1 provides the DXGI\_FORMAT\_R8G8B8A8\_TYPELESS existing format family with the ability to cast between members. Direct3D 10.1 and later versions expose this extended format support through a new version and hardware capability discovery mechanism. Direct3D 10.0 does not support extended formats even if the graphics hardware has Direct3D 10.1 capabilities.

The following are new Direct3D 10.1 features to support extended format awareness:

-   New XR formats for high color scan-out

-   Re-adding BGR formats that are missing from Direct3D version 10

-   Enabling creation of differently-formatted views of fully-typed members of the DXGI\_FORMAT\_R8G8B8A8\_TYPELESS, DXGI\_FORMAT\_R10G10B10A2\_TYPELESS and DXGI\_FORMAT\_R16G16B16\_A16\_TYPELESS families, which contain all the Direct3D version 10 scan-out formats

-   Scan-out and present support for BGRA and BGRA\_SRGB

Windows 7 also provides its version of Direct3D 9 with a new swap-chain flag that permits the XR interpretation of a 10:10:10:2 back buffer to communicate to the DWM.

The following sections describe the new features for Direct3D:

[Version Discovery Support](version-discovery-support.md)

[Details of the Extended Format](details-of-the-extended-format.md)

[Fully-Typed Back Buffers Casting](fully-typed-back-buffers-casting.md)

[BGRA Scan-Out Support](bgra-scan-out-support.md)

[Extended Format Aware Requirements](extended-format-aware-requirements.md)

[DDI Changes for Direct3D Version 9 Drivers](ddi-changes-for-direct3d-version-9-drivers.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Supporting%20Extended%20Format%20Awareness%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




