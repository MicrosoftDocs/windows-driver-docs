---
title: GDL Schema Construct Element
description: GDL Schema Construct Element
ms.assetid: 46653504-4ce7-455c-a22a-a6032cbd6a3e
keywords:
- GDL WDK , elements
- GDL WDK , schemas
- construct element WDK GDL
- snapshots WDK GDL , structure
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDL Schema Construct Element


The XSD schema that is produced by the GDL parser defines a construct element as follows:

```cpp
    <complexType name="GDL_ConstructType">
        <sequence>
            <any processContents="lax" minOccurs="0" maxOccurs="unbounded"/>
        </sequence>
        <attribute name="Name" type="string" use="required"/>
        <attribute name="Instance" type="string" use="required"/>
        <attribute name="Constrained" type="boolean" use="optional"/>
    </complexType>
```

The preceding definition is similar to the definition of the [&lt;SnapshotRoot&gt; element](gdl-schema-root-element.md). And construct elements, like the root element, can hold construct (&lt;CONSTRUCT&gt;) and attribute (&lt;GDL\_ATTRIBUTE&gt;) elements. However, &lt;GDL\_ConstructType&gt; can have three additional XML attributes: **Name**, **Instance**, and **Constrained**. **Name** and **Instance** and required and hold the Name and Instance GDL constructs, respectively. **Constrained** is optional and holds a Boolean value that indicates if the option is constrained or not. This attribute appears only for &lt;CONSTRUCT&gt; elements that correspond to \*Option constructs.

For example, consider the following GDL entry.

```cpp
*Feature:  PaperSize
{
   *Option:  Letter
   {
   }
}
```

The preceding entry results in the following XML snapshot.

```cpp
     <CONSTRUCT Name="*Feature" Instance="PaperSize">
        <CONSTRUCT Name="*Option" Instance="Letter" Constrained="FALSE" >
        </CONSTRUCT>
    </CONSTRUCT>
```

A particular option is marked constrained depending on the supplied configuration and the set of constraints that are defined in the GDL instance data.

 

 




