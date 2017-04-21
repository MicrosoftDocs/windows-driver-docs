---
title: '\ String\ section changes for localized strings'
description: This INF requirement ensures that pseudo-localized builds work. The requirement is to delineate localizable versus non-localizable strings within the strings section
ms.assetid: F0A0C309-9FA3-4941-AF35-15CD63DB25E3
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# \[String\] section changes for localized strings


This INF requirement ensures that pseudo-localized builds work. The requirement is to delineate localizable versus non-localizable strings within the strings section.

The following example has no preface of what is localized or not; this should not be used:

``` syntax
[Strings]

REG_MULTI_SZ   = 0x00010000
REG_DWORD      = 0x00010001

MSFT = "Microsoft"
IHV  = "Contoso, Ltd"
```

The following example should be used instead; note the new lines:

``` syntax
[Strings]

;Localizable
MSFT = "Microsoft"
IHV  = "Contoso, Ltd"


;Non-Localizable
REG_MULTI_SZ   = 0x00010000
REG_DWORD      = 0x00010001
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20[String]%20section%20changes%20for%20localized%20strings%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




