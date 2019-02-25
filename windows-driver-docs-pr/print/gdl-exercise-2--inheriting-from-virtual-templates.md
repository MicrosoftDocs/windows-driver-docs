---
title: GDL Exercise 2 Inheriting from Virtual Templates
description: GDL Exercise 2 Inheriting from Virtual Templates
ms.assetid: 89878438-bea4-4d6f-bf3b-88d5bef0e6ab
keywords:
- GDL WDK , examples
- examples WDK GDL
- tutorials WDK GDL
- GDL WDK , tutorials
- schemas WDK GDL , implementing GDL schemas
- templates WDK GDL , inheritance
- templates WDK GDL , examples
- inheritance WDK GDL
- virtual templates WDK GDL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDL Exercise 2: Inheriting from Virtual Templates


### <a href="" id="exercise"></a> Exercise

Define a data type that accepts a Unicode string that is encoded by using 2 bytes to represent 1 Unicode character. Then, define non-virtual templates that inherit from the previously defined virtual templates. Do not modify the schema that you created in [Exercise 1](gdl-exercise-1--implementing-a-gdl-schema.md). Create a sample GDL data file and verify the schema is applied correctly. Create a sample GDL data file that does not conform to the schema and verify the errors are detected.

### <a href="" id="solution"></a> Solution

The following two templates define the Unicode data type.

```cpp
*Include: MasterTemplate.gdl
 
*Template:  XML_STRING
{
    *Type:  DATATYPE
    *DataType:   XML_TYPE
    *XMLDataType: "string"
}
```

```cpp
*Template:  NORMAL_STRING
{
    *Type:  DATATYPE
    *DataType:   FILTER_TYPE
    *ElementType:  XML_STRING
    *FilterTypeName: "NORMAL_STRING"
}
```

The following template inherits from the templates that are defined in Exercise 1. There is a construct named \*Command and three types of attributes: **\*Name** (which appears at the root level), **\*CommandName** (which can appear within a \*Command construct), and **\*UniName** (which can appear within both contexts).

```cpp
*Template:  COMMAND
{
    *Name:  "*Command"
    *Inherits: CONSTRUCTS
    *Instances:  <ANY>
}
*Template:  ROOT_NAME
{
    *Name:  "*Name"
    *Inherits: ROOT_ATTRIB
    *ValueType:  NORMAL_STRING
}
*Template:  CMD_NAME
{
    *Name:  "*CommandName"
    *Inherits: CONSTRUCT_ATTRIB
    *ValueType:  NORMAL_STRING
}
*Template:  UNIVERSAL_NAME
{
    *Name:  "*UniName"
    *Inherits: FREEFLOAT
    *ValueType:  NORMAL_STRING
}
```

The following GDL file conforms to the given schema.

```cpp
*Name: "can only appear at root level"
*UniName:  "can appear anywhere"
*Command: X
{
    *CommandName:  "May only appear within a command"
    *UniName:  "can appear anywhere, even in a command"
    *Command: nested
    {
        *CommandName:  "nested commands are ok."
        *UniName:  "template defined a recursive nesting" 100 %
    }
}
```

The following GDL file does not conform to the given schema.

```cpp
*CommandName:  "Error! May only appear within a command"
*Command: X
{
    *Name: "Error! can only appear at root level"
}
```

 

 




