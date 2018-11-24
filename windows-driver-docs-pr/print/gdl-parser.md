---
title: GDL Parser
description: GDL Parser
ms.assetid: abb0e9b7-db98-4f8c-af15-83cd1841e5c2
keywords:
- GDL WDK , parser
- parser WDK GDL , about
- printer drivers WDK , converting data into XML
- converting data into XML WDK GDL
- transforming data into XML WDK GDL
- parsing GDL data WDK
- snapshots WDK GDL , GDL parser
- parser WDK GDL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDL Parser


The GDL parser converts GDL data into an XML snapshot. For more information about controlling the parser, see [IPrintCoreHelperUni](details-of-the-iprintcorehelperuni-interface.md) interface.

GDL provides [standard parsing](standard-gdl-parsing.md) and [template-based parsing](gdl-template-structure.md).

The parser filter recognizes a variety of *data type primitives*. These data types can appear as the value of an attribute and are mapped to their nearest XML equivalent in the XML snapshot. Additionally, the parser filter recognizes compound data types that are created from the primitive data types. The data type templates are used to define data types, and the **\*ValueType** directive is used to associate a data type template with an attribute template.

For more information about standard parsing, see [Standard GDL Parsing](standard-gdl-parsing.md).

For more information about template data types, see [GDL Template Data Types](gdl-template-data-types.md).

For troubleshooting information about parsing, see [Troubleshooting GDL Parsing](troubleshooting-gdl-parsing.md).

 

 




