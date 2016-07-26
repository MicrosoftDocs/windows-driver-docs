---
title: Accessing and Modifying Files
description: Accessing and Modifying Files
ms.assetid: DD5A527F-5F8D-4892-A2D5-C0279913B6A3
---

# Accessing and Modifying Files


The following guidelines apply to driver package components when they access or modify files:

-   Files should be modified only by using [INF directives](inf-directives.md) within an INF file. For example, use the INF [**CopyFiles**](inf-copyfiles-directive.md) directive to copy files and the INF [**RenFiles**](inf-renfiles-directive.md) directive to rename files.

-   Files that appear in an INF [**CopyFiles**](inf-copyfiles-directive.md) directive must not also appear in an INF [**RenFiles**](inf-renfiles-directive.md) or [**DelFiles**](inf-delfiles-directive.md) directive in the INF file.

**Important**  The INF [**RenFiles**](inf-renfiles-directive.md) and [**DelFiles**](inf-delfiles-directive.md) directives must be used carefully. You should not use these directives in the INF file for a Plug and Play (PnP) function driver.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Accessing%20and%20Modifying%20Files%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




