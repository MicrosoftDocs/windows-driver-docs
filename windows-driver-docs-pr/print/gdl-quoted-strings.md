---
title: GDL Quoted Strings
description: GDL Quoted Strings
ms.assetid: 52d6f1bf-0b8c-4aa7-8cc8-1a18def224be
keywords:
- constructs WDK GDL , strings
- GDL WDK , strings
- strings WDK GDL , quoted strings
- quoted strings WDK GDL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDL Quoted Strings


A *quoted string* begins and ends with the double quotation character ("). Any characters that appear between will be treated literally as part of the quoted string with the following exceptions:

-   A percent sign plus a double quotation mark (%") is treated as a literal double quotation character (").

-   A percent sign plus a less than symbol (%&lt;) is treated as a literal less than symbol (&lt;).

-   A percent sign followed by any other character is treated as a literal percent sign (%).

-   The less than symbol (&lt;) introduces a [HexSubString](gdl-hexsubstrings.md) context.

-   Quoted strings can appear within a nested context; only the HexSubString context is recognized within a uoted string.

 

 




