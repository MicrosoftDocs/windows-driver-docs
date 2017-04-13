---
title: GDL Whitespace Characters
author: windows-driver-content
description: GDL Whitespace Characters
ms.assetid: 703c41c0-3e12-465a-823f-c32990a52382
keywords: ["constructs WDK GDL , whitespace characters", "continuation linebreak WDK GDL", "linebreak sequence WDK GDL", "parser WDK GDL , handling whitespace", "GDL WDK , whitespace characters"]
---

# GDL Whitespace Characters


*Whitespace characters* are defined to be space, tab, or a continuation linebreak. A *continuation linebreak* is a linebreak sequence immediately followed by the plus sign (+). (A *linebreak sequence* is "\\n\\r", "\\r\\n", "\\n", or "\\r" expressed as C-strings.)

Whitespace is interpreted literally within a [quoted string](gdl-quoted-strings.md) and within an arbitrary value context. Whitespace that occurs elsewhere is considered non-literal. The GDL parser consolidates non-literal whitespace; that is, any number of consecutive non-literal whitespace characters is replaced by one whitespace character. Literal whitespace is not consolidated.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDL%20Whitespace%20Characters%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


