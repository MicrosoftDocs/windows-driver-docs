---
title: Defining Accelerator Capabilities
description: Defining Accelerator Capabilities
ms.assetid: 1f590cfd-74b8-4a08-848d-fcbb2c0c9486
keywords:
- DirectX Video Acceleration WDK Windows 2000 display , accelerator capabilities
- Video Acceleration WDK DirectX , accelerator capabilities
- VA WDK DirectX , accelerator capabilities
- restricted profiles WDK DirectX VA
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Defining Accelerator Capabilities


## <span id="ddk_defining_accelerator_capabilities_gg"></span><span id="DDK_DEFINING_ACCELERATOR_CAPABILITIES_GG"></span>


An accelerator can be used in restricted operation, in which case it conforms to a [restricted profile](restricted-profiles.md), or it can be used in nonrestricted operation, in which case it does not conform to a restricted profile.

### <span id="Restricted_Operation"></span><span id="restricted_operation"></span><span id="RESTRICTED_OPERATION"></span>Restricted Operation

The capabilities of an accelerator are defined according to which restricted profile it supports. An accelerator may support one or more restricted profiles.

Some restricted profiles are defined as subsets of the capabilities of other restricted profiles (for example, the MPEG2\_A profile is a subset of the capabilities of the MPEG2\_B profile). Accelerators that support a particular restricted profile must also support any restricted profile that is a subset of the profile being supported. For example, accelerators that support the MPEG2\_B profile must also support the MPEG2\_A profile.

### <span id="Nonrestricted_Operation"></span><span id="nonrestricted_operation"></span><span id="NONRESTRICTED_OPERATION"></span>Nonrestricted Operation

If in DirectX VA an accelerator is used without strict conformance to a restricted profile, the **wRestrictedMode** member of the [**DXVA\_ConnectMode**](https://msdn.microsoft.com/library/windows/hardware/ff563138) structure must be set to 0xFFFF to indicate this lack of restriction.

All defined values of the **bDXVA\_Func** variable are allowed.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Defining%20Accelerator%20Capabilities%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




