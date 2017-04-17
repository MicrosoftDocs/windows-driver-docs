---
title: GDL Arbitrary Value Contexts
author: windows-driver-content
description: GDL Arbitrary Value Contexts
ms.assetid: 6de79b2b-5f0f-4d6c-8a95-d9ef2266c2ef
keywords: ["GDL WDK , contexts", "contexts WDK GDL , arbitrary value contexts", "arbitrary value contexts WDK GDL", "values WDK GDL , contexts"]
---

# GDL Arbitrary Value Contexts


An *arbitrary value context* is used to define values that contain any arbitrary sequence of characters even if they violate the GDL syntax rules.

The arbitrary value context is introduced when the "&lt;BeginValue:*symbol*&gt;" character sequence is encountered and terminates when the "&lt;EndValue:*symbol*&gt;" character sequence is encountered. *symbol* is any valid symbol token that you choose. The same symbol must appear in both the BeginValue and EndValue invocation. No whitespaces can appear in the BeginValue and EndValue tags.

An arbitrary value context can be defined in any value context except within a comment or a quoted string. The arbitrary value context can appear within a nested context. No contexts are recognized within the arbitrary value context, but any sequence of bytes can be defined within.

An arbitrary value context symbol is a token that consists of characters from the set \[A-Z, a-z, 0-9, \_ \]. There is no limit to the length of a symbol.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDL%20Arbitrary%20Value%20Contexts%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


