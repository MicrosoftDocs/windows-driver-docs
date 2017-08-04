---
title: '[Version] section directives'
description: This topic describes [Version] section directives in the INF.
ms.assetid: 76AC10DC-AECC-4C35-8BEE-4B2E8B06FEE0
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# \[Version\] section directives


This topic describes *\[Version\]* section directives in the INF.

All inbox drivers must not reference the Layout.inf file.

All inbox drivers must not reference any catalog files.

For example:

``` syntax
[Version]
Signature="$Windows NT$"
Provider=%MSFT%
ClassGUID={4D36E968-E325-11CE-BFC1-08002BE10318}
Class=Display
DriverVer=11/22/2004, 6.14.10.7000

Note: 
no line item for LayoutFile=layout.inf
no line item for CatalogFile=delta.cat
```

WHQL display drivers must not reference the Layout.inf file.

For example:

``` syntax
[Version]
Signature="$Windows NT$"
Provider=%IHV%
ClassGUID={4D36E968-E325-11CE-BFC1-08002BE10318}
Class=Display
DriverVer=11/22/2004, 6.14.10.7000

Note: 
no line item for LayoutFile=layout.inf
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20[Version]%20section%20directives%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




