---
title: GDL Schema Construct Element
author: windows-driver-content
description: GDL Schema Construct Element
ms.assetid: 46653504-4ce7-455c-a22a-a6032cbd6a3e
keywords: ["GDL WDK , elements", "GDL WDK , schemas", "construct element WDK GDL", "snapshots WDK GDL , structure"]
---

# GDL Schema Construct Element


The XSD schema that is produced by the GDL parser defines a construct element as follows:

```
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

```
*Feature:  PaperSize
{
   *Option:  Letter
   {
   }
}
```

The preceding entry results in the following XML snapshot.

```
     <CONSTRUCT Name="*Feature" Instance="PaperSize">
        <CONSTRUCT Name="*Option" Instance="Letter" Constrained="FALSE" >
        </CONSTRUCT>
    </CONSTRUCT>
```

A particular option is marked constrained depending on the supplied configuration and the set of constraints that are defined in the GDL instance data.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDL%20Schema%20Construct%20Element%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


