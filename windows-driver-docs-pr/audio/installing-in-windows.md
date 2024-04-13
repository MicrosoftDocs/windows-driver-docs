---
title: Installing in Windows
description: Installing in Windows
keywords:
- audio adapters WDK , system components
- adapter drivers WDK audio , system components
- Port Class audio adapters WDK , system components
ms.date: 10/26/2017
---

# Installing in Windows


In the following example of an INF device-driver-installation section, the two directives add the system-driver information that installs the core system components for an audio adapter in Windows:

```inf
  [XYZ-Audio-Device.Registration.NTX86]
  Include=ks.inf, wdmaudio.inf
  Needs=KS.Registration, WDMAUDIO.Registration
```

For information about the **Include** and **Needs** directives, see [**INF DDInstall Section**](../install/inf-ddinstall-section.md).

 

