---
title: GDL Exercise 3 Creating Root-Level Constructs
description: GDL Exercise 3 Creating Root-Level Constructs
ms.assetid: 3c7ad284-b77c-4ad3-8334-2fe5b026e340
keywords:
- GDL WDK , examples
- examples WDK GDL
- tutorials WDK GDL
- GDL WDK , tutorials
- constructs WDK GDL , creating constructs
- creating GDL constructs WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDL Exercise 3: Creating Root-Level Constructs


### <a href="" id="exercise"></a> Exercise

Modify the schema of [Exercise 1](gdl-exercise-1--implementing-a-gdl-schema.md) to introduce a construct named \*PFeature that can be found only at the root level.

Use the following conditions:

-   \*PFeature can have any instance name.

-   \*PFeature members are the attributes named **\*Name** and **\*DefaultOption**.

-   \*PFeature has a construct member named **\*Poption** that should be declared as virtual.

### <a href="" id="solution"></a> Solution

The following template satisfies the preceding conditions.

```cpp
*Template:  POPTION
{
    *Name:  "*POption"
    *Type: CONSTRUCT
    *Virtual:  TRUE
}

*Template:  NAME
{
    *Name:  "*Name"
    *Type:  ATTRIBUTE
    *ValueType:  NORMAL_STRING
}

*Template:  SYMBOL
{
    *Type:  DATATYPE
    *DataType:   FILTER_TYPE
    *ElementType:  XML_STRING
    *FilterTypeName: "SYMBOLNAME"
}
*Template:  DEFAULT_OPT
{
    *Name: "*DefaultOption"
    *Type:  ATTRIBUTE
    *ValueType:  SYMBOL
}

*Template:  PFEATURE 
{
    *Name:  "*PFeature"
    *Type: CONSTRUCT
    *Members:  (POPTION, NAME, DEFAULT_OPT)
    *Instances:  <ANY>
}
*Template:  ROOT2
{
    *Inherits: ROOT
    *Members:  (PFEATURE)
}
```

 

 




