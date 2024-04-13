---
title: Capability Override Settings to Disable OpenGL
description: This software device setting for all in-box display INFs ensures that no in-box drivers are exposed to possible interoperability issues with out-of-box OpenGL ICDs.
ms.date: 04/20/2017
---

# Capability override settings to disable OpenGL

This software device setting for all in-box display INFs ensures that no in-box drivers are exposed to possible interoperability issues with out-of-box OpenGL ICDs.

For example:

``` syntax
[R200_SoftwareDeviceSettings]
HKR,, CapabilityOverride,                       %REG_DWORD%,    0x8
```
