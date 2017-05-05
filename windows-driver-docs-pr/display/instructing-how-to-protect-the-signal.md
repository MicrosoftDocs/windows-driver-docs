---
title: Instructing How to Protect the Signal
description: Instructing How to Protect the Signal
ms.assetid: d55a3660-5b7c-43e9-b1c5-b61f8b997a1a
keywords:
- copy protection WDK COPP , signal protection
- video copy protection WDK COPP , signal protection
- COPP WDK DirectX VA , signal protection
- protected video WDK COPP , signal protection
- signal protection WDK COPP
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Instructing How to Protect the Signal


**This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.**

The COPP command can provide instructions about how to protect the signal that goes through the physical connector associated with the DirectX VA COPP device. To set signal protection, the video miniport driver's [*COPPCommand*](https://msdn.microsoft.com/library/windows/hardware/ff539642) function receives a pointer to a [**DXVA\_COPPCommand**](https://msdn.microsoft.com/library/windows/hardware/ff563141) structure with the **guidCommandID** member set to the DXVA\_COPPSetSignaling GUID and the **CommandData** member set to a pointer to a [**DXVA\_COPPSetSignalingCmdData**](https://msdn.microsoft.com/library/windows/hardware/ff563146) structure that specifies how to protect the signal.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Instructing%20How%20to%20Protect%20the%20Signal%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




