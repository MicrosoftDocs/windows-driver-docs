---
title: Differentiating the SKU for Windows 7 Display Drivers
description: Differentiating the SKU for Windows 7 Display Drivers
ms.assetid: 3cf72bd5-21bc-4a7f-8c2f-98f8e70d8248
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Differentiating the SKU for Windows 7 Display Drivers


All in-box display driver INF files in Windows Server 2008, Windows Vista SP1, and later versions must include a value that indicates that the drivers are for Windows Client editions only and that they do not install on Windows Server SKUs.

In Windows 7, Windows Vista SP1, Windows Server 2008, and Windows Server 2008 R2, the **Manufacturer** directive must be followed by a string in the following form:

```
NT<platform>...1 
```

In this string, platform is x86 or amd64.

The following example shows the **Manufacturer** directive, and the section that follows it for drivers for x86 systems:

```
[Manufacturer]
%ATI% = ATI.Mfg,NTx86...1

[ATI.Mfg.NTx86...1]
```

The following example shows the **Manufacturer** directive, and the section that follows it for drivers for x64 systems:

```
[Manufacturer]
%ATI% = ATI.Mfg,NTamd64...1

[ATI.Mfg.NTamd64...1]
```

For more information about the **Manufacturer** section, see [**INF Manufacturer Section**](https://msdn.microsoft.com/library/windows/hardware/ff547454).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Differentiating%20the%20SKU%20for%20Windows%207%20Display%20Drivers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




