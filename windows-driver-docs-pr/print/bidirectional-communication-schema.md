---
title: Bidirectional Communication Schema
description: Bidirectional Communication Schema
ms.assetid: b15b1aff-623e-4159-ab0f-ce386a1377eb
keywords:
- bidirectional communication schema WDK print
- bidi communication schema WDK print
- property WDK bidi communication
- value WDK bidi communication
ms.date: 06/11/2018
ms.localizationpriority: medium
---

# Bidirectional Communication Schema


The bidirectional (bidi) communication schema is a hierarchy of printer attributes, some of which are properties and others that are values (or value entries).

-   A *property* is a node in the schema hierarchy. A property can have one or more children, and these children can be other properties or values. A property can contain a list of values or other properties. It can represent a feature, a compound feature, or a print system attribute (such as the driver name).

-   A *value* is a leaf in the schema hierarchy that represents either a single data item or a list of related data items. A value has a name, a data type, and a data value. A value cannot have child elements. A value can be referenced by its name, but only when the name is associated with the schema path to the property that is the parent of the value.

For example, the following query can be used to access the *Installed* value under the Staple property.

`\Printer.Finishing.Staple:Installed`

The bidi schema can be extended in by creating a bidi extension file. This file is an XML file that defines new schemas specific to a particular driver. The schemas in a bidi extension file are a subset of the standard print schema and are defined by using constructs of the XSD file (Bidi Extension Framework).

For a complete listing of the schema properties and values, see [Bidirectional Communication Schema Hierarchy](bidirectional-communication-schema-hierarchy.md). To learn how to construct queries, see [Constructing a Bidi Communication Schema Query](constructing-a-bidi-communication-schema-query.md). For details of the properties and values in the Bidi Communication Schema, see [Bidi Communication Schema Reference](bidi-communications-schema-reference.md).

A convenient way to install a bidi extension file is to make the file a *dependent file* of the printer driver. For more information about dependent files, see [Printer INF File Entries](printer-inf-file-entries.md).
