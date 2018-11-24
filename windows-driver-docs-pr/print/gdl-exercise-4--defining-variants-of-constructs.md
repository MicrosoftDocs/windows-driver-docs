---
title: GDL Exercise 4 Defining Variants of Constructs
description: GDL Exercise 4 Defining Variants of Constructs
ms.assetid: b923b5f8-6e60-44a0-a38e-8bfa315281c5
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

# GDL Exercise 4: Defining Variants of Constructs


### <a href="" id="exercise"></a> Exercise

Modify the construct \*PFeature from [Exercise 3](gdl-exercise-3--creating-root-level-constructs.md) by defining two variants: \*PFeature: PaperSize and \*PFeature InputTray.

The POption that is contained in \*PFeature: PaperSize has the following attributes: **\*Name**, **\*Command**, **\*Papersize**.

The POption that is contained in \*PFeature: InputTray has the following attributes: **\*Name**, **\*Command**, and **\*Capacity:** *\# of sheets*.

Create a template to abstract the common properties of these two types of \*POptions.

### <a href="" id="solution"></a> Solution

The following template satisfies the conditions.

```cpp
*Template:  COMMAND_TYPE
{
    *Type:  DATATYPE
    *DataType:   FILTER_TYPE
    *ElementType:  XML_STRING
    *FilterTypeName: "COMMAND_STRING"
}
*Template:  ACOMMAND
{
    *Name:  "*Command"
    *Type:  ATTRIBUTE
    *ValueType:  COMMAND_TYPE
}
```

The following derived option template further defines properties of the virtual template POPTION.

```cpp
*Template:  GENERIC_OPTION
{
    *Inherits: POPTION
    *Members:  (NAME, ACOMMAND)
    *Instances:  <ANY>
}
*Template:  XML_INT4
{
    *Type:  DATATYPE
    *DataType:   XML_TYPE
    *XMLDataType: "int"
}
*Template:  INTEGER
{
    *Type:  DATATYPE
    *DataType:   FILTER_TYPE
    *ElementType:  XML_INT4
    *FilterTypeName: "HEX_OR_INT"
}
*Template:  XML_FLOAT
{
    *Type:  DATATYPE
    *DataType:   XML_TYPE
    *XMLDataType: "float"
}
*Template:  PAIR_OF_FLOAT
{
    *Type:  DATATYPE
    *DataType:   ARRAY
    *ElementType:  XML_FLOAT
    *RequiredDelimiter: ","
    *OptionalDelimiter: "<20 09>"
    *ArrayLabel: "PAIR"
    *ElementTags: (width, height)
    *ArraySize: 2
}
*Template:  LEN_UNITS
{
    *Type:  DATATYPE
    *DataType:   ENUMERATOR
    *XMLDataType: "LengthUnits"
    *EnumeratorList: (inches, mm, microns, pixels)
}
*Template:  PAGE_DIM
{
    *Type:  DATATYPE
    *DataType:   COMPOSITE
    *ElementType: (PAIR_OF_FLOAT, LEN_UNITS)
    *RequiredDelimiter: ","
    *OptionalDelimiter: "<20 09>"
    *ElementTags: (dimensions, units)
}
*Template:  PAPERDIMENSIONS
{
    *Name: "*PaperSize"
    *Type:  ATTRIBUTE
    *ValueType:  PAGE_DIM
}
```

The following derived option template further specializes properties of the template GENERIC\_OPTION.

```cpp
*Template:  PAPERSIZE_OPTION
{
    *Name:  "*POption"  *%  Isolate branch from Base Templates
    *Inherits: GENERIC_OPTION
    *Members:  (PAPERDIMENSIONS)
    *Instances:  <ANY>
}


*Template:  PAPERSIZE_FEATURE
{
    *Inherits: PFEATURE
    *Members:  (PAPERSIZE_OPTION)
    *Instances:  PaperSize
}

*Template:  TRAY_CAPACITY
{
    *Name: "*Capacity"
    *Type:  ATTRIBUTE
    *ValueType:  INTEGER
}
```

The following derived option template further specializes properties of the template GENERIC\_OPTION.

```cpp
*Template:  INPUTTRAY_OPTION
{
    *Name:  "*POption"   *%  Isolate branch from Base Templates
    *Inherits: GENERIC_OPTION
    *Members:  (TRAY_CAPACITY)
    *Instances:  <ANY>
}

*Template:  INPUTTRAY_FEATURE
{
    *Inherits: PFEATURE
    *Members:  (INPUTTRAY_OPTION)
    *Instances:  InputTray
}
```

 

 




