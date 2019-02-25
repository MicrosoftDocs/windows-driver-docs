---
title: GDL Syntax
description: GDL Syntax
ms.assetid: 31f0c2f6-2a6b-4a3c-9da1-6fd586b8ae2a
keywords:
- GDL WDK , syntax
- parsing GDL data WDK
- parser WDK GDL , parsing data
- GDL WDK , attributes
- GDL WDK , constructs
- attributes WDK GDL
- constructs WDK GDL
- constructs WDK GDL , delimiters
- GDL WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDL Syntax


The GDL parser processes a stream of GDL entries. Each entry is delimited by a linebreak sequence or a construct delimiter. The GDL stream might exist in a single file or might be constructed by a sequence of files that are logically equivalent to a stream that is contained in a single file.

There are two types of GDL entries: attributes and constructs. *GDL attributes* are simple pairs of keywords and values. *GDL constructs* contain a GDL attribute followed by a collection of data entries called a *construct*. A collection of constructs is separated by a series of *construct delimiters.*

Whitespace characters can appear between GDL entries, and comments can appear in GDL streams.

GDL uses strings to represent data.

This section includes:

[GDL Attributes](gdl-attributes.md)

[GDL Contexts](gdl-contexts.md)

[GDL Constructs](gdl-constructs.md)

[GDL Whitespace Characters](gdl-whitespace-characters.md)

[GDL Comments](gdl-comments.md)

[GDL Strings](gdl-strings.md)

 

 




