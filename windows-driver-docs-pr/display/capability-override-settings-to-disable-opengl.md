---
title: Capability override settings to disable OpenGL
description: This software device setting for all in-box display INFs ensures that no in-box drivers are exposed to possible interoperability issues with out-of-box OpenGL ICDs.
ms.assetid: 70903938-4A89-45A3-B1AD-B823C5735AB1
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Capability override settings to disable OpenGL


This software device setting for all in-box display INFs ensures that no in-box drivers are exposed to possible interoperability issues with out-of-box OpenGL ICDs.

For example:

``` syntax
[R200_SoftwareDeviceSettings]
HKR,, CapabilityOverride,                       %REG_DWORD%,    0x8
```

 

 





