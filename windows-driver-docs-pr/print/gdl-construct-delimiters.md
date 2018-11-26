---
title: GDL Construct Delimiters
description: GDL Construct Delimiters
ms.assetid: 6f759534-3dc2-4e04-afe0-3f377790be21
keywords:
- constructs WDK GDL , delimiters
- GDL WDK , constructs
- parser WDK GDL , handling construct delimiters
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDL Construct Delimiters


The *construct delimiter* characters are the curly braces: { and }. Construct delimiter characters additionally behave like linebreaks, so you must follow or precede a construct delimiter with a linebreak sequence.

The following two code examples show the use of construct delimiters. The first example has the value spread over several lines.

```cpp
*Person: FlorenceF
{
 *Company:Contoso Pharmaceuticals
 {
 *Location: Redmond, WA
 }
}
```

The second example combines the value into one line but still uses the curly braces to delimit the parts of the value.

```cpp
*Person: FlorenceF{*Company:Contoso Pharmaceuticals{*Location: Redmond, WA}}
```

 

 




