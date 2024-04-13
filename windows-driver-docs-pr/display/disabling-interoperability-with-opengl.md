---
title: Disabling Interoperability with OpenGL
description: Disabling Interoperability with OpenGL
keywords:
- INF files WDK display , interoperability
- interoperability WDK display
- OpenGL WDK display
ms.date: 04/20/2017
---

# Disabling Interoperability with OpenGL


To ensure that no Microsoft Direct3D display drivers are exposed to possible interoperability issues with OpenGL installable client drivers (ICDs), you must set the following entry in an add-registry section of the INF:

```inf
[Xxx_SoftwareDeviceSettings]
...
HKR,, CapabilityOverride,    %REG_DWORD%, 0x8
```

 

 





