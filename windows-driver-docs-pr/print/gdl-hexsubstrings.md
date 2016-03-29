---
title: GDL HexSubStrings
description: GDL HexSubStrings
ms.assetid: 7451fd1f-a765-486a-bd90-bc01eac2c388
keywords: ["constructs WDK GDL , strings", "GDL WDK , strings", "strings WDK GDL , HexSubString", "HexSubString WDK GDL"]
---

# GDL HexSubStrings


A *HexSubString* is a way to represent non-displayable characters within a quoted string. A HexSubString is introduced by the less than symbol (&lt;) and is terminated by the greater than symbol (&gt;).

Within the HexSubString context, the only characters that are allowed are the hexadecimal digits, whitespace and linebreak sequences, and continuation linebreaks. All whitespace and linebreak characters that occur within the HexSubString context are ignored. Each HexSubString must contain an even number of hexadecimal digits, because two hexadecimal digits are needed to define a single byte.

If you want to create a quoted string that ends with the percent sign (%), the percent character must be represented with the HexSubString "&lt;25&gt;".

The HexSubString context can appear only within a quoted string context. Comments can appear within a HexSubString context.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDL%20HexSubStrings%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




