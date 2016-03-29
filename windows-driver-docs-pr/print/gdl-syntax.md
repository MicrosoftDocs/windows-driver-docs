---
title: GDL Syntax
description: GDL Syntax
ms.assetid: 31f0c2f6-2a6b-4a3c-9da1-6fd586b8ae2a
keywords: ["GDL WDK , syntax", "parsing GDL data WDK", "parser WDK GDL , parsing data", "GDL WDK , attributes", "GDL WDK , constructs", "attributes WDK GDL", "constructs WDK GDL", "constructs WDK GDL , delimiters", "GDL WDK"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDL%20Syntax%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




