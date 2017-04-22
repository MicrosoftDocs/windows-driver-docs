---
title: GDL Schema Root Element
author: windows-driver-content
description: GDL Schema Root Element
ms.assetid: 6148f026-52fa-452d-aa81-564d6ee5288d
keywords:
- GDL WDK , elements
- GDL WDK , schemas
- SnapshotRoot element WDK GDL
- root element WDK GDL
- snapshots WDK GDL , structure
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GDL Schema Root Element


The XSD schema that is produced by the GDL parser defines a root element (&lt;SnapshotRoot&gt;) as follows:

```
    <element name="SnapshotRoot" type="gdl:GDL_RootType"/>

    <complexType name="GDL_RootType"  >
        <sequence>
            <any processContents="lax" minOccurs="0" maxOccurs="unbounded"/>
        </sequence>
    </complexType>
```

The XSD schema does not allow &lt;any&gt; elements to coexist with defined element types so the parser's schema leaves the definition of the root element very flexible. Although the XSD schema is intentionally left very general, the &lt;SnapshotRoot&gt; element can hold any number of &lt;GDL\_ATTRIBUTE&gt; or &lt;CONSTRUCT&gt; elements in any order. Because of the GDL language's emphasis on the most recently defined entry, the appearance of elements in the XML snapshot is typically the opposite of the entry's appearance in the GDL source file.

The &lt;SnapshotRoot&gt; element is the outermost element in the snapshot document and it contains all of the other elements in the snapshot. There is only one &lt;SnapshotRoot&gt; element in each snapshot.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDL%20Schema%20Root%20Element%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


