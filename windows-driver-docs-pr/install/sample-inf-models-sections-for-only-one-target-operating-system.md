---
title: Sample INF Models Sections for Only One Target Operating System
description: Sample INF Models Sections for Only One Target Operating System
ms.assetid: 4cad05f6-ec88-4bc8-b69a-0d6b06dfeec0
---

# Sample INF Models Sections for Only One Target Operating System


It is possible to use decorated [**INF *Models* sections**](inf-models-section.md) to limit the range of applicable target operating systems.

The following example shows an [**INF Manufacturer section**](inf-manufacturer-section.md) with various [**INF *Models* sections**](inf-models-section.md) that will prevent Windows from installing a device on x86-based systems not running Windows Vista.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Sample%20INF%20Models%20Sections%20for%20Only%20One%20Target%20Operating%20System%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




