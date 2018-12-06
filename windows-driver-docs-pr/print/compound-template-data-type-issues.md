---
title: Compound Template Data Type Issues
description: Compound Template Data Type Issues
ms.assetid: 61f26465-c79d-42e3-94c8-26c2c61ecb98
keywords:
- templates WDK GDL , data types
- data types WDK GDL , problems with template data types
- data types WDK GDL , compound
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Compound Template Data Type Issues


When compound data types are created from other data types and parentheses are used to enclose one of the data types, all data types that enclose a parentheses-bracketed data type must also be enclosed by parentheses.

For example, assume that you define a list of GPD integers by using the following templates.

```cpp
*Template:  LIST_OF_INTS
{
    *Type:  DATATYPE
    *DataType:   ARRAY
    *ElementType:  INTEGER
    *RequiredDelimiter: ","
    *OptionalDelimiter: "<20 09>"
    *ElementTags: (int)
    *ArraySize: *
}
*Template:  LIST_OF_LIST_OF_INTS
{
    *Type:  DATATYPE
    *DataType:   ARRAY
    *ElementType:  LIST_OF_INTS
    *RequiredDelimiter: ":"
    *OptionalDelimiter: "<20 09>"
    *ElementTags: (IntList)
    *ArraySize: *
}
```

Then, the following values are valid and equivalent expressions of the LIST\_OF\_LIST\_OF\_INTS data type.

```cpp
*ListList: 1,2,3:10,11,12:20,21,22 
*ListList: (1,2,3:10,11,12:20,21,22)
*ListList: ((1,2,3):(10,11,12):(20,21,22))
```

However, the following value violates the nesting of parenthesis rule.

```cpp
*ListList: (1,2,3):(10,11,12):(20,21,22)
```

The preceding example will generate a syntax error because the parser filter assumes any parenthesis that it encounters belongs to the outermost context, the next parenthesis belongs to the next context, and so on.

 

 




