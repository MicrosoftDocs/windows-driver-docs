---
title: XML Structure of GDL Snapshots
author: windows-driver-content
description: XML Structure of GDL Snapshots
ms.assetid: 46051e45-da46-488c-9d70-2299954445be
keywords: ["GDL WDK , snapshots", "snapshots WDK GDL , structure", "parser WDK GDL , snapshots", "GDL WDK , data tree", "data tree WDK GDL", "GDL WDK , entries"]
---

# XML Structure of GDL Snapshots


The XML snapshot is a subset of the GDL data tree that contains those switch and case branches that satisfy the client-supplied configuration. The data tree is the tree that is formed by all of the GDL data entries, some of which might have configuration dependencies. For more information about configuration dependencies, see [Creating GDL Configuration-Dependent Data](creating-gdl-configuration-dependent-data.md).

In addition to emitting an XML snapshot, the GDL parser can also generate a separate XSD schema that describes the overall structure of the snapshot. This schema also contains the definition of enumeration data types that the GDL templates define. These definitions enable clients to perform schema validation of all primitive data types in the snapshot if desired. If the schema validation is not performed, enumerations will not be checked for validity when the DOM tree is loaded; this check is not necessary because the GDL parser performs its own enumeration validity checks.

To be a valid XML document, the napshot contains a single root element: &lt;SnapshotRoot&gt;. This element represents the root context of the GDL tree. The &lt;SnapshotRoot&gt; element can contain child &lt;CONSTRUCT&gt; or &lt;GDL\_ATTRIBUTE&gt; elements. The &lt;CONSTRUCT&gt; element is used to represent a GDL construct, and the &lt;GDL\_ATTRIBUTE&gt; element is used to represent a GDL attribute.

Each &lt;CONSTRUCT&gt; element can contain other &lt;CONSTRUCT&gt; and &lt;GDL\_ATTRIBUTE&gt; elements. The &lt;GDL\_ATTRIBUTE&gt; element holds only the value that is associated with that attribute and does not contain any &lt;CONSTRUCT&gt; or &lt;GDL\_ATTRIBUTE&gt; elements. The &lt;GDL\_ATTRIBUTE&gt; value can appear directly as the character data content of the &lt;GDL\_ATTRIBUTE&gt; element for non-compound data types or can be represented by one or more child elements if the value is defined as a GDL compound data type.

If the GDL parser cannot associate an attribute with a template that defines the data type of the attribute's value, or if the value that is found does not conform to the declared data type, the corresponding &lt;GDL\_ATTRIBUTE&gt; element in the XML snapshot will contain a &lt;CDATA&gt; section that contains the original value as specified in the GDL file.

GDL supports the following types of schema elements for snapshots.

-   [Root](gdl-schema-root-element.md)

-   [Construct](gdl-schema-construct-element.md)

-   [Attribute](gdl-schema-attribute-element.md)

The following topics describe additional data types that are used in the XML snapshot schema:

[Enumerations and XSD-Defined Data Types](enumerations-and-xsd-defined-data-types.md)

[Data Type Wrappers](data-type-wrappers.md)

For more information about namespaces in the XML snapshot schema, see [XML Snapshot Namespaces](xml-snapshot-namespaces.md).

For information about character data in XML snapshots, see the following topics:

[XML Schema Linebreak Translations](xml-schema-linebreak-translations.md)

[Unicode Representations in XML Snapshots](unicode-representations-in-xml-snapshots.md)

[XML Restrictions on Allowed Characters in Snapshots](xml-restrictions-on-allowed-characters-in-snapshots.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20XML%20Structure%20of%20GDL%20Snapshots%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


