---
title: DDI Changes for Direct3D Version 9 Drivers
description: DDI Changes for Direct3D Version 9 Drivers
ms.assetid: b702c02d-3be6-46e8-9e53-5d33e5e3fc70
keywords:
- Direct3D version 10.1 WDK Windows 7 display , DDI changes for Direct3D version 9 drivers
- Direct3D version 9 drivers WDK Windows 7 display
- Direct3D version 9 drivers WDK Windows 7 display , DDI changes
- XR_BIAS WDK Windows 7 display , Direct3D version 9 DDI
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DDI Changes for Direct3D Version 9 Drivers


This section applies only to Windows 7 and later operating systems.

XR\_BIAS is the only new extended format ability that Windows 7 makes available to user-mode display drivers that only support the Direct3D version 9 DDI.

Such a user-mode display driver can indicate that it supports the D3DDDIFMT\_A2B10G10R10\_XR\_BIAS format value from the [**D3DDDIFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff544312) enumeration. The driver indicates such support by creating an entry in the array of populated [**FORMATOP**](https://msdn.microsoft.com/library/windows/hardware/ff566438) structures in the **pData** member of the [**D3DDDIARG\_GETCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff543148) structure that the driver returns from a call to its [**GetCaps**](https://msdn.microsoft.com/library/windows/hardware/ff566762) function with the D3DDDICAPS\_GETFORMATDATA value set in the **Type** member of D3DDDIARG\_GETCAPS. This entry should indicate, in the **Operations** member of **FORMATOP**, all of the typical operations that the runtime can perform on surfaces with the D3DDDIFMT\_A2B10G10R10\_XR\_BIAS format. For example, the driver should set the FORMATOP\_\*\_RENDERTARGET bits in **Operations**. The driver must also set the FORMATOP\_DISPLAYMODE and FORMATOP\_3DACCELERATION bits in **Operations**.

If the driver returns a [**FORMATOP**](https://msdn.microsoft.com/library/windows/hardware/ff566438) entry for the D3DDDIFMT\_A2B10G10R10\_XR\_BIAS format, the driver can subsequently receive calls to its [**CreateResource**](https://msdn.microsoft.com/library/windows/hardware/ff540688) function to create resources with the D3DDDIFMT\_A2B10G10R10\_XR\_BIAS format set in the **Format** member of the [**D3DDDIARG\_CREATERESOURCE**](https://msdn.microsoft.com/library/windows/hardware/ff542963) structure.

The driver only receives requests to create resources with the D3DDDIFMT\_A2B10G10R10\_XR\_BIAS format for full-screen flipping chains. The Desktop Windows Manager (DWM) handles windowed presentation of XR\_BIAS in shader code. The driver should treat D3DDDIFMT\_A2B10G10R10\_XR\_BIAS-format resources as the D3DDDIFMT\_A2B10G10R10 format in all operations except scan out, For example, the driver can treat D3DDDIFMT\_A2B10G10R10\_XR\_BIAS-format resources as the D3DDDIFMT\_A2B10G10R10 format for blending, filtering, and format-conversion operations. The only difference is how XR\_BIAS affects scan-out. For more information about scan-out, see [BGRA Scan-Out Support](bgra-scan-out-support.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20DDI%20Changes%20for%20Direct3D%20Version%209%20Drivers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




