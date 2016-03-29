---
title: Data Type Template Inheritance
description: Data Type Template Inheritance
ms.assetid: c2ecc091-8fdc-4666-9cdf-629903f13f6f
keywords: ["templates WDK GDL , data types", "data types WDK GDL , template inheritance", "templates WDK GDL , inheritance", "inheritance WDK GDL"]
---

# Data Type Template Inheritance


A data type template can inherit properties from a previously defined data type template. All recognized properties that are appropriate to the base template are inherited. Inherited properties cannot be redefined in the derived template.

Derived templates can be inherited by other templates to any level that you want. To specify a template to inherit from, simply name it by using the \*Inherits directive. The base template must be a data type template.

The templates that serve as base templates do not need to be completely defined. The \*Virtual: **TRUE** directive is used to inform the parser that a template can be partially defined. (The base-most template must, however, contain the **\*DataType** directive.) The derived template can then complete the definition of the data type. If the derived template cannot complete the definition of the data type, it must explicitly declare itself to be **Virtual**. The **Virtual** directive is not inherited. Virtual templates cannot be referenced by using the **\*ElementType** or **\*ValueType** directives. They can be referenced only through the **\*Inherits** directive.

**Note**   The parser filter automatically creates a default value for the **\*ArraySize** directive if it is missing when the **\*ElementType** directive is supplied in a COMPOSITE data type. As a result, **\*ArraySize** can be defined before **\*ElementType** (by defining **\*ArraySize** in a template that is subsequently inherited by the template that defines **\*ElementType**), but the reverse is not allowed (that is, **\*ElementType** cannot be defined before **\*ArraySize**).

 

### Schemas

Schemas are not emitted for incomplete data type templates. To avoid redundant schema definitions, schemas are not emitted for templates that are derived from a template that already has a schema. This restriction eliminates multiple definitions of the same primitive data type that would result if multiple variants of a single primitive data type are defined without the aid of inheritance. The **Virtual** directive does not affect whether the schema is emitted. The average user does not need to understand the details of when a schema is emitted. The parser filter takes care of this automatically.

### Binding

The properties that are defined or inherited in the base template that is referenced by the **\*Inherits:** directive are directly inherited by the derived template. When a derived or base template is referenced by the **\*ElementType** directive from another data type template or the **\*ValueType** directive from an attribute template, the named template is bound. There is no complex binding algorithm such as used to bind members of a construct template. Such an algorithm would not make sense because the values have no names or instance names that are needed to implement indirect binding.

### Example

Data type inheritance is used to factor out properties that are common to several data type templates. In the following example, base templates define the properties that are common to several array data types. Note that two levels of inheritance are used.

```
*Template:  GENERIC_ARRAY  *%  Basemost Template
{
    *Type:  DATATYPE
    *Virtual:  TRUE
    *DataType:   ARRAY
    *RequiredDelimiter: ","
    *OptionalDelimiter: "<20 09>"
}
*Template:  LIST_OF_TYPE  *%  first level derived Template
{
    *Inherits:  GENERIC_ARRAY
    *ArrayLabel: "LIST"
    *ArraySize: [*]
    *Virtual:  TRUE
}

*Template:  DT_INT_ARRAY  *%  first level derived Template
{
    *Inherits:  GENERIC_ARRAY
    *ElementType:  INTEGER
    *Virtual:  TRUE
}

*% ===================
*%  Second-level templates derived from LIST_OF_TYPE
*% ===================

*Template:  COLORS_LIST  
{
    *Inherits:  LIST_OF_TYPE
    *ElementType:  COLORS
    *ElementTags: (colors)
}
*Template:  STD_VAR_LIST
{
    *Inherits:  LIST_OF_TYPE
    *ElementType:  STD_VAR
    *ElementTags: (Standard_Variable)
}

*% ===================
*%  Second-level templates derived from DT_INT_ARRAY
*% ===================

*Template:  DT_POINT
{
    *Inherits:  DT_INT_ARRAY
    *ArrayLabel: "POINT"          
    *ElementTags: (X_pos, Y_pos)
    *ArraySize: 2
}
*Template:  DT_PAIR_OF_INTS
{
    *Inherits:  DT_INT_ARRAY
    *ArrayLabel: "PAIR"
    *ElementTags: (width, height)
    *ArraySize: 2
}
*Template:  RECTANGLE
{
    *Inherits:  DT_INT_ARRAY
    *ArrayLabel: "rect"
    *ElementTags: (left, top, right, bottom)
    *ArraySize: 4
}
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Data%20Type%20Template%20Inheritance%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




