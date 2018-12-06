---
title: Installing in Windows
description: Installing in Windows
ms.assetid: 790caffd-ebb0-4ba1-b31c-b03d3c83bc59
keywords:
- audio adapters WDK , system components
- adapter drivers WDK audio , system components
- Port Class audio adapters WDK , system components
ms.date: 10/26/2017
ms.localizationpriority: medium
---

# Installing in Windows


In the following example of an INF device-driver-installation section, the two directives add the system-driver information that installs the core system components for an audio adapter in Windows:

```inf
  [XYZ-Audio-Device.Registration.NTX86]
  Include=ks.inf, wdmaudio.inf
  Needs=KS.Registration, WDMAUDIO.Registration
```

For information about the **Include** and **Needs** directives, see [**INF DDInstall Section**](https://msdn.microsoft.com/library/windows/hardware/ff547344).

 

 




