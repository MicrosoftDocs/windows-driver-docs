---
title: GDL Schemas
description: GDL Schemas
ms.assetid: 1020bec8-3b34-4391-9e75-9ffcd8b07785
keywords:
- GDL WDK , schemas
- schemas WDK GDL
- schemas WDK GDL , examples
- constructs WDK GDL , examples
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDL Schemas


The GDL parser enables you to create and implement a data-driven schema. When a schema is supplied, the parser performs validates the schema and converts the data.

A *schema* describes the structure and format of the data in the associated GDL source file. The schema can be defined within the GDL source data file itself or it can be a separate file that the GDL source data file references. The schema defines the data entries that can appear within each construct and the number of times each attribute can be defined. For example, you might define a construct to describe a person. You might want the construct to include the person's name, birthdate, height, weight, home address, and some employment information.

The GDL data might look something like the following code example.

```cpp
*Person: person_ID
{
  *Name:
  *Birthdate:
  *Height:
  *Weight:
  *HomeAddress:
  *EmploymentInfo:
} 
```

Because \*HomeAddress and \*EmploymentInfo represent logical groupings of information, they can also be defined as constructs, as the following code example shows.

```cpp
*HomeAddress:
{
  *StreetAddress:
  *Apt_Number:
  *City:
  *State:
  *Zip:
}

*EmploymentInfo:
{
  *Employer:
  *Address:
  *Position:
  *Salary:
  *StartDate:
}
```

GDL constructs, such as those shown in the preceding example, do not define any syntax rules for their structure and content. For example, there could be two instances of the \*Person construct, one that specifies \*Weight in kilograms and the other that specifies \*Weight in pounds. These multiple instances can cause inconsistencies.

The GDL schema provides a method to formally specify the structure and content that the incoming data must conform to. The parser will validate the data against this schema and warn if the data or the structure of the data does not conform to the schema. You can specify whether entries are required or optional (like Apt) or whether entries can be multiply defined. For example, \*Apt\_Number might be optional and a single person can hold two jobs.

The schema allows the definition of entries to be shared and inherited. For example, the schema definition for \*Address in \*EmploymentInfo can be shared by \*HomeAddress. The schema allows new definitions to be derived from existing definitions. The two Address constructs do not need to be identical because they can be variants that are derived from a common inherited definition.

The schema can be used to specify the format of a given attribute value. For example, the schema can require that the date value be specified in the MM-DD-YYYY format. You can also have the parser decompose complex value expressions into their constituent components and display them in the snapshot. For example, your client application might want the date decomposed into three separate fields, as the following code example shows.

```cpp
*Date:
{
  *Month: Jan
  *Day: 1
  *Year: 2001
}
```

The ability of the schema to support inheritance has additional implications. Inheritance naturally enables you to extend the schema while maintaining compatibility. If there is a schema that is derived from another schema, a data file that conforms to the derived schema will automatically also conform to the original schema. This inheritance enables vendors to customize their schema (and by implication their data files) while retaining compatibility with a master schema (and all of the applications that require conformance to the master schema). In practice, the vendor must only reference the file that defines the master schema and create new definitions that inherit from the definitions in the master schema. The vendor does not need to make a private copy of the master schema or modify the master schema in any way. This situation ensures that the vendor does not need to take any action if the master schema is subsequently modified.

As the preceding example demonstrates, inheritance enables you to factor out common patterns and avoid needless duplication of definitions and the accompanying maintenance. As a result, the schemas and the data sets that they represent can be well thought-out and logically structured.

For more information about how to use inheritance-based schemas, see [GDL Templates](gdl-template-structure.md).

 

 




