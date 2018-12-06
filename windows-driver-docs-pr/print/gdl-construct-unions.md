---
title: GDL Construct Unions
description: GDL Construct Unions
ms.assetid: 0ca237fe-7f47-4b9c-8963-676a2afd1140
keywords:
- constructs WDK GDL , unions
- logical constructs WDK GDL
- constructs WDK GDL , logical constructs
- constructs WDK GDL , examples
- sibling constructs WDK GDL
- unions WDK GDL
- parser WDK GDL , handling unions
- GDL WDK , unions
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDL Construct Unions


If multiple constructs with the same construct type and construct tag are defined in the GDL source file, the logical representation of that construct (the [logical construct](syntactical-and-logical-constructs-in-gdl.md)) will contain the union of the contents of the original constructs that are defined in the GDL source file.

The construct type and the construct tag together uniquely specify or define a logical construct (within the context of its parent). Unlike XML, when two *sibling* constructs are defined, each with the same construct type and the construct tag, the result is one logical construct. In fact, the constructs do not need to even be syntactical siblings, they can be logical siblings. (*Syntactical siblings* explicitly reside in the same construct body, and *logical siblings* are both children of the same logical construct.)

The contents of the logical construct is a union of the contents of the siblings. What appears in the snapshot are the logical constructs, not the constructs as they are originally syntactically defined in the GDL source file. In the following code example, there are two sibling constructs, both with Construct Type: \*Person and with Construct Tag: FlorenceF.

```cpp
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

```cpp
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

```cpp
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

 

 




