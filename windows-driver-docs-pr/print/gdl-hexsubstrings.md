---
title: GDL HexSubStrings
description: GDL HexSubStrings
ms.assetid: 7451fd1f-a765-486a-bd90-bc01eac2c388
keywords:
- constructs WDK GDL , strings
- GDL WDK , strings
- strings WDK GDL , HexSubString
- HexSubString WDK GDL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDL HexSubStrings


A *HexSubString* is a way to represent non-displayable characters within a quoted string. A HexSubString is introduced by the less than symbol (&lt;) and is terminated by the greater than symbol (&gt;).

Within the HexSubString context, the only characters that are allowed are the hexadecimal digits, whitespace and linebreak sequences, and continuation linebreaks. All whitespace and linebreak characters that occur within the HexSubString context are ignored. Each HexSubString must contain an even number of hexadecimal digits, because two hexadecimal digits are needed to define a single byte.

If you want to create a quoted string that ends with the percent sign (%), the percent character must be represented with the HexSubString "&lt;25&gt;".

The HexSubString context can appear only within a quoted string context. Comments can appear within a HexSubString context.

 

 




