---
title: GDL Parser
author: windows-driver-content
description: GDL Parser
ms.assetid: abb0e9b7-db98-4f8c-af15-83cd1841e5c2
keywords: ["GDL WDK , parser", "parser WDK GDL , about", "printer drivers WDK , converting data into XML", "converting data into XML WDK GDL", "transforming data into XML WDK GDL", "parsing GDL data WDK", "snapshots WDK GDL , GDL parser", "parser WDK GDL"]
---

# GDL Parser


The GDL parser converts GDL data into an XML snapshot. For more information about controlling the parser, see [IPrintCoreHelperUni](details-of-the-iprintcorehelperuni-interface.md) interface.

GDL provides [standard parsing](standard-gdl-parsing.md) and [template-based parsing](gdl-template-structure.md).

The parser filter recognizes a variety of *data type primitives*. These data types can appear as the value of an attribute and are mapped to their nearest XML equivalent in the XML snapshot. Additionally, the parser filter recognizes compound data types that are created from the primitive data types. The data type templates are used to define data types, and the **\*ValueType** directive is used to associate a data type template with an attribute template.

For more information about standard parsing, see [Standard GDL Parsing](standard-gdl-parsing.md).

For more information about template data types, see [GDL Template Data Types](gdl-template-data-types.md).

For troubleshooting information about parsing, see [Troubleshooting GDL Parsing](troubleshooting-gdl-parsing.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDL%20Parser%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


