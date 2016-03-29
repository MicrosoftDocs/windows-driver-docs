---
title: Bidirectional Communication Schema
description: Bidirectional Communication Schema
ms.assetid: b15b1aff-623e-4159-ab0f-ce386a1377eb
keywords: ["bidirectional communication schema WDK print", "bidi communication schema WDK print", "property WDK bidi communication", "value WDK bidi communication"]
---

# Bidirectional Communication Schema


The bidirectional (bidi) communication schema is a hierarchy of printer attributes, some of which are properties and others that are values (or value entries).

-   A *property* is a node in the schema hierarchy. A property can have one or more children, and these children can be other properties or values. A property can contain a list of values or other properties. It can represent a feature, a compound feature, or a print system attribute (such as the driver name).

-   A *value* is a leaf in the schema hierarchy that represents either a single data item or a list of related data items. A value has a name, a data type, and a data value. A value cannot have child elements. A value can be referenced by its name, but only when the name is associated with the schema path to the property that is the parent of the value.

For example, the following query can be used to access the *Installed* value under the Staple property.

```
"\Printer.Finishing.Staple:Installed"
```

The bidi schema can be extended in Windows Vista by creating a bidi extension file. This file is an XML file that defines new schemas specific to a particular driver. The schemas in a bidi extension file are a subset of the standard print schema and are defined by using constructs of the XSD file (Bidi Extension Framework).

For a complete listing of the schema properties and values, see [Bidirectional Communication Schema Hierarchy](bidirectional-communication-schema-hierarchy.md). To learn how to construct queries, see [Constructing a Bidi Communication Schema Query](constructing-a-bidi-communication-schema-query.md). For details of the properties and values in the Bidi Communication Schema, see [Bidi Communication Schema Reference](bidi-communications-schema-reference.md).

A convenient way to install a bidi extension file is to make the file a *dependent file* of the printer driver. For more information about dependent files, see [Printer INF File Entries](printer-inf-file-entries.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Bidirectional%20Communication%20Schema%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




