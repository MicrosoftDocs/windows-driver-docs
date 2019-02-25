---
title: GDL Schema Root Element
description: GDL Schema Root Element
ms.assetid: 6148f026-52fa-452d-aa81-564d6ee5288d
keywords:
- GDL WDK , elements
- GDL WDK , schemas
- SnapshotRoot element WDK GDL
- root element WDK GDL
- snapshots WDK GDL , structure
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDL Schema Root Element


The XSD schema that is produced by the GDL parser defines a root element (&lt;SnapshotRoot&gt;) as follows:

```cpp
    <element name="SnapshotRoot" type="gdl:GDL_RootType"/>

    <complexType name="GDL_RootType"  >
        <sequence>
            <any processContents="lax" minOccurs="0" maxOccurs="unbounded"/>
        </sequence>
    </complexType>
```

The XSD schema does not allow &lt;any&gt; elements to coexist with defined element types so the parser's schema leaves the definition of the root element very flexible. Although the XSD schema is intentionally left very general, the &lt;SnapshotRoot&gt; element can hold any number of &lt;GDL\_ATTRIBUTE&gt; or &lt;CONSTRUCT&gt; elements in any order. Because of the GDL language's emphasis on the most recently defined entry, the appearance of elements in the XML snapshot is typically the opposite of the entry's appearance in the GDL source file.

The &lt;SnapshotRoot&gt; element is the outermost element in the snapshot document and it contains all of the other elements in the snapshot. There is only one &lt;SnapshotRoot&gt; element in each snapshot.

 

 




