---
title: GDL Quoted Strings
author: windows-driver-content
description: GDL Quoted Strings
ms.assetid: 52d6f1bf-0b8c-4aa7-8cc8-1a18def224be
keywords: ["constructs WDK GDL , strings", "GDL WDK , strings", "strings WDK GDL , quoted strings", "quoted strings WDK GDL"]
---

# GDL Quoted Strings


A *quoted string* begins and ends with the double quotation character ("). Any characters that appear between will be treated literally as part of the quoted string with the following exceptions:

-   A percent sign plus a double quotation mark (%") is treated as a literal double quotation character (").

-   A percent sign plus a less than symbol (%&lt;) is treated as a literal less than symbol (&lt;).

-   A percent sign followed by any other character is treated as a literal percent sign (%).

-   The less than symbol (&lt;) introduces a [HexSubString](gdl-hexsubstrings.md) context.

-   Quoted strings can appear within a nested context; only the HexSubString context is recognized within a uoted string.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDL%20Quoted%20Strings%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


