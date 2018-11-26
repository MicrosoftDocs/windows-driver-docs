---
title: GDL Exercise 1 Implementing a GDL Schema
description: GDL Exercise 1 Implementing a GDL Schema
ms.assetid: 0adfef5a-4211-45e9-bb65-8174822efdc5
keywords:
- GDL WDK , examples
- examples WDK GDL
- tutorials WDK GDL
- GDL WDK , tutorials
- schemas WDK GDL , implementing GDL schemas
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDL Exercise 1: Implementing a GDL Schema


### <a href="" id="exercise"></a> Exercise

Implement a schema that creates three categories of attributes and does not impose restrictions on where constructs can be located.

These attributes must be divided into the following categories:

-   Attributes that can appear at the root level and within constructs.

-   Attributes that can appear only at the root level.

-   Attributes that can appear only within constructs.

Do not define any keywords in your schema; just include the framework for the future keywords.

**Note**   By using templates, you can create a virtual schema--that is, a schema that does not define any GDL entries. The base schema that is defined in this way exerts its influence no matter how this schema is extended in the future.

 

### <a href="" id="solution"></a> Solution

The following code example demonstrates one way to complete this exercise.

```cpp
*Template:  ATTRIBUTE
{
    *Type:  ATTRIBUTE
    *Virtual:  TRUE
}
*Template:  ROOT_ATTRIB
{
    *Inherits: ATTRIBUTE
    *Virtual:  TRUE
}
*Template:     CONSTRUCT_ATTRIB  *%  May not appear at Root level
{
    *Inherits: ATTRIBUTE
    *Virtual:  TRUE
}
*Template:     FREEFLOAT
{
    *Inherits: ATTRIBUTE
    *Virtual:  TRUE
}
*Template:  CONSTRUCTS
{
    *Type: CONSTRUCT
    *Members:  ( CONSTRUCTS, FREEFLOAT, CONSTRUCT_ATTRIB)
    *Virtual:  TRUE
}

*Template:  ROOT
{
            *Type: CONSTRUCT
            *AllowNewMembers: FALSE
            *Name:  "root"
            *Instances:  <ANY>
            *Members:  (ROOT_ATTRIB, FREEFLOAT, CONSTRUCTS)
}
```

**Note**   You can place the templates in the preceding example in a MasterTemplate.gdl file for use by the next exercise.

 

 

 




