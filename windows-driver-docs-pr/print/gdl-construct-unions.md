---
title: GDL Construct Unions
description: GDL Construct Unions
ms.assetid: 0ca237fe-7f47-4b9c-8963-676a2afd1140
keywords: ["constructs WDK GDL , unions", "logical constructs WDK GDL", "constructs WDK GDL , logical constructs", "constructs WDK GDL , examples", "sibling constructs WDK GDL", "unions WDK GDL", "parser WDK GDL , handling unions", "GDL WDK , unions"]
---

# GDL Construct Unions


If multiple constructs with the same construct type and construct tag are defined in the GDL source file, the logical representation of that construct (the [logical construct](syntactical-and-logical-constructs-in-gdl.md)) will contain the union of the contents of the original constructs that are defined in the GDL source file.

The construct type and the construct tag together uniquely specify or define a logical construct (within the context of its parent). Unlike XML, when two *sibling* constructs are defined, each with the same construct type and the construct tag, the result is one logical construct. In fact, the constructs do not need to even be syntactical siblings, they can be logical siblings. (*Syntactical siblings* explicitly reside in the same construct body, and *logical siblings* are both children of the same logical construct.)

The contents of the logical construct is a union of the contents of the siblings. What appears in the snapshot are the logical constructs, not the constructs as they are originally syntactically defined in the GDL source file. In the following code example, there are two sibling constructs, both with Construct Type: \*Person and with Construct Tag: FlorenceF.

```
*Person: FlorenceF
{
*Name: Florence Flipo
*Company:Contoso Pharmaceuticals
{
*Location: Redmond, WA
}
}
*Person: FlorenceF
{
*Position: CEO
*Company:Contoso Pharmaceuticals
{
*NumberOfEmployees: 43,000
}
}
```

According to the preceding rule, the two siblings define a single logical construct that contains the union of both siblings.

```
*Person: FlorenceF
{
*Name: Florence Flipo
*Company:Contoso Pharmaceuticals
{
*Location: Redmond, WA
}
*Position: CEO
*Company:Contoso Pharmaceuticals
{
*NumberOfEmployees: 43,000
}
}
```

Note that the merge in the preceding example has created two new sibling constructs that have the same Construct Type: \*Company and Construct Tag: Contoso Pharmaceuticals.

If the same rule was applied again (recursively), the following code would result.

```
*Person: FlorenceF
{
*Name: Florence Flipo
*Company:Contoso Pharmaceuticals
{
*Location: Redmond, WA
*NumberOfEmployees: 43,000
}
*Position: CEO
}
```

Any of the preceding three GDL fragments, when they are parsed, produces the same internal representation. The internal representation most closely resembles the last fragment.

When [attributes](gdl-attributes.md) with the same [keyword](gdl-keywords.md) are multiply defined, no merge takes place. Each definition still exists in the internal representation. The template directive **\*Additive** is used to specify what value or values are transferred to the snapshot.

The GDL parser takes the syntactical representation of the GDL stream and creates an internal logical representation of the GDL commands. The internal representation of these commands is then converted to XML and becomes a snapshot.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDL%20Construct%20Unions%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




