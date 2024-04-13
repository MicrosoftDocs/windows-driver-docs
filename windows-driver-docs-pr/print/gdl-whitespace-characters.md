---
title: GDL Whitespace Characters
description: GDL Whitespace Characters
keywords:
- constructs WDK GDL , whitespace characters
- continuation linebreak WDK GDL
- linebreak sequence WDK GDL
- parser WDK GDL , handling whitespace
- GDL WDK , whitespace characters
ms.date: 04/20/2017
---

# GDL Whitespace Characters


*Whitespace characters* are defined to be space, tab, or a continuation linebreak. A *continuation linebreak* is a linebreak sequence immediately followed by the plus sign (+). (A *linebreak sequence* is "\\n\\r", "\\r\\n", "\\n", or "\\r" expressed as C-strings.)

Whitespace is interpreted literally within a [quoted string](gdl-quoted-strings.md) and within an arbitrary value context. Whitespace that occurs elsewhere is considered non-literal. The GDL parser consolidates non-literal whitespace; that is, any number of consecutive non-literal whitespace characters is replaced by one whitespace character. Literal whitespace is not consolidated.

 

 




