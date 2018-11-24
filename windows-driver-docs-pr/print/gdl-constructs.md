---
title: GDL Constructs
description: GDL Constructs
ms.assetid: e579bff0-4e28-4e9e-bef2-f6748c3849e5
keywords:
- GDL WDK , constructs
- constructs WDK GDL
- child entries WDK GDL
- parent construct WDK GDL
- ancestor construct WDK GDL
- syntactical constructs WDK GDL
- logical constructs WDK GDL
- unions WDK GDL
- constructs WDK GDL , syntactical constructs
- constructs WDK GDL , logical constructs
- constructs WDK GDL , unions
- constructs WDK GDL , delimiters
- constructs WDK GDL , examples
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDL Constructs


A *GDL construct* is simply a [GDL attribute](gdl-attributes.md) followed by a construct body. Logically, a construct represents a collection of data, much like a C structure does.

A *construct body* is zero, one, or more GDL entries enclosed by [construct delimiter characters](gdl-construct-delimiters.md). The construct body must be introduced by the left curly brace ({), and terminated by the right curly brace (}).

The GDL entries that are enclosed by the construct delimiter characters are referred to as the *contents* of the construct. The enclosed GDL entries are also referred as *children*, *child entries*, *child elements*, or *members* of the construct. Because the child entries can also be constructs, you can create arbitrarily deep nestings of constructs; however, only the immediate descendants of the parent construct are called *child entries*.

Conversely, the construct that immediately encloses the child entries is sometimes referred as the *parent construct*. Two GDL entries that share the same parent construct are called *Siblings*. A construct whose body contains the parent of an entry or the parent of a parent of an entry (and so on) is called an *ancestor construct*.

The attribute that precedes the construct body is called the *construct head*, or sometimes just the *construct*. The keyword component of the construct head is called the *construct type*. If multiple sibling constructs are defined, each with the same keyword, they are considered to belong to the same construct type. The value component of the construct head is called the *construct instance name*, or the *construct tag*. The construct tag is expected to be a [symbol](gdl-arbitrary-value-contexts.md). The construct tag is syntactically optional but is required in some cases.

Constructs can be either *syntactical* or *logical*. Constructs can consist of unions.

An arbitrary amount of whitespace and linebreak sequences can precede or follow the [construct delimiter characters](gdl-construct-delimiters.md). However, for the sake of readability, a C-style indentation convention is typically used.

The following code example shows a GDL construct.

```cpp
*ConstructType: ConstructTag
{   *%  Begin Construct Delimiter
*%  this is the Construct Body
*ChildAttribute: child attribute value
*ChildConstruct: ChildConstructTag
{
 *%  Body of Child construct could hold more constructs.
}
*AnotherChildConstruct: ChildConstructTag2
{
 *% Contents of *AnotherChildConstruct
 *% since both child constructs share the same Parent construct, they are
 *% Sibling Constructs.
 *DescendantAttribute:  this attribute is a descendant of  *ConstructType: ConstructTag
}
}   *%  End Construct Delimiter
```

This section includes:

[GDL Construct Delimiters](gdl-construct-delimiters.md)

[Syntactical and Logical Constructs in GDL](syntactical-and-logical-constructs-in-gdl.md)

[GDL Construct Unions](gdl-construct-unions.md)

[GDL Whitespace Characters](gdl-whitespace-characters.md)

[GDL Comments](gdl-comments.md)

[GDL Strings](gdl-strings.md)

 

 




