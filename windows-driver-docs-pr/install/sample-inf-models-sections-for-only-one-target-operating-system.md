---
title: Sample INF Models Sections for Only One Target Operating System
description: Sample INF Models Sections for Only One Target Operating System
ms.assetid: 4cad05f6-ec88-4bc8-b69a-0d6b06dfeec0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Sample INF Models Sections for Only One Target Operating System


It is possible to use decorated [**INF *Models* sections**](inf-models-section.md) to limit the range of applicable target operating systems.

The following example shows an [**INF Manufacturer section**](inf-manufacturer-section.md) with various [**INF *Models* sections**](inf-models-section.md) that will prevent Windows from installing a device on x86-based systems not running Windows Vista.

```cpp
[Manufacturer]
%Msft% = Msft, NTx86.6.0, NT.6.1

;For Windows Vista only

[Msft.NTx86.6.0]
%NetVMini.DeviceDesc%    = NetVMini.ndi, root\NetVMini ; Root enumerated 
%NetVMini.DeviceDesc%    = NetVMini.ndi, {b85b7c50-6a01-11d2-b841-00c04fad5171}\NetVMini ; Toaster Bus enumerated 

;For Windows 7 and later

[Msft.NT.6.1]
```

In this example, the [**INF Manufacturer section**](inf-manufacturer-section.md) has the following [**INF *Models* sections**](inf-models-section.md):

-   A complete INF *Models* section for Windows Vista on x86-based systems that include device descriptions and hardware identifiers (IDs). Windows will select and use this section when it installs the device on x86-based systems that are running Windows Vista.

-   An empty INF *Models* section for Windows 7 and later versions of Windows on any hardware platform. Windows will select this section for device installation on these platforms. However, because the section contains no specific device descriptions or hardware IDs, Windows will not install any devices through this INF file.

 

 





