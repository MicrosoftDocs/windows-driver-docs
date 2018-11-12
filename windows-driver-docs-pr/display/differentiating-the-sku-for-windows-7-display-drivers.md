---
title: Differentiating the SKU for Windows 7 Display Drivers
description: Differentiating the SKU for Windows 7 Display Drivers
ms.assetid: 3cf72bd5-21bc-4a7f-8c2f-98f8e70d8248
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Differentiating the SKU for Windows 7 Display Drivers


All in-box display driver INF files in Windows Server 2008, Windows Vista SP1, and later versions must include a value that indicates that the drivers are for Windows Client editions only and that they do not install on Windows Server SKUs.

In Windows 7, Windows Vista SP1, Windows Server 2008, and Windows Server 2008 R2, the **Manufacturer** directive must be followed by a string in the following form:

```inf
NT<platform>...1 
```

In this string, platform is x86 or amd64.

The following example shows the **Manufacturer** directive, and the section that follows it for drivers for x86 systems:

```inf
[Manufacturer]
%ATI% = ATI.Mfg,NTx86...1

[ATI.Mfg.NTx86...1]
```

The following example shows the **Manufacturer** directive, and the section that follows it for drivers for x64 systems:

```inf
[Manufacturer]
%ATI% = ATI.Mfg,NTamd64...1

[ATI.Mfg.NTamd64...1]
```

For more information about the **Manufacturer** section, see [**INF Manufacturer Section**](https://msdn.microsoft.com/library/windows/hardware/ff547454).

 

 





