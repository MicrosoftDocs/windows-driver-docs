---
title: Defining Accelerator Capabilities
description: Defining Accelerator Capabilities
ms.assetid: 1f590cfd-74b8-4a08-848d-fcbb2c0c9486
keywords:
- DirectX Video Acceleration WDK Windows 2000 display , accelerator capabilities
- Video Acceleration WDK DirectX , accelerator capabilities
- VA WDK DirectX , accelerator capabilities
- restricted profiles WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





