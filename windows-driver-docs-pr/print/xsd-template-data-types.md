---
title: XSD Template Data Types
description: XSD Template Data Types
ms.assetid: 96d3a75a-fa15-47bb-8331-e3994d25c42d
keywords:
- templates WDK GDL , data types
- data types WDK GDL , primitive
- XSD_DEFINED data type WDK GDL
- ArrayLabel directive WDK GDL
- XMLDataType directive WDK GDL
- XSDTypeDefinition directive WDK GDL
- ComplexType directive WDK GDL
- parser WDK GDL , escaping special XML characters
- escaping special XML characters WDK GDL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# XSD Template Data Types


The XSD\_DEFINED data type uses schemas for the definition of the data type. You can define any ComplexType or SimpleType.

\*DataType: XSD\_DEFINED creates a data type definition by using the standard &lt;xsd:complexType&gt; or &lt; xsd:simpleType&gt; XML elements. The instance data value will be output as the content of an XML element whose xsi:type is specified by the value of \*XMLDataType that appears in this template. This output enables you to use XSD to derive new simple or complex types and use them in GDL attributes.

The following directives are used to completely define the XSD\_DEFINED data type:

-   \*XMLDataType (Required). The name (NCName) that has been assigned to the XSD data type that this template is defining. This name is the value of the **name** attribute in the &lt;complexType&gt; or &lt;simpleType&gt; element that the \*XSDTypeDefinition directive defines. This name must be unique to all XSD\_DEFINED and ENUMERATOR types. To avoid conflicts with data types that the GDL parser defines, you should avoid names that begin with "GDL\_" and "GDLW\_". The XML standard defines the syntax for a NCName and might impose additional restrictions.

-   \*XSDTypeDefinition (Required). The well-formed XSD that defines the data type. Only the &lt;complexType&gt; or &lt;simpleType&gt; elements can appear at the context that is closest to the root. Multiple &lt;complexType&gt; or &lt;simpleType&gt; elements can appear as siblings at the root-most context if at most only one of them is actually referenced as the value type of a GDL attribute. The name of the type that is referenced as the value type of a GDL attribute is the one that appears in the \*XMLDataType directive. The remaining data types can only be referenced from within other &lt;complexType&gt; or &lt;simpleType&gt; definitions.

    Type definitions can also reference other type definitions that are defined in other templates. When you reference type definitions within a \*XSDTypeDefinition directive that were created by using the \*XSDTypeDefinition directive, you must use the gdl: namespace prefix.

    If the XSD occupies multiple lines or if it violates GDL syntax rules, it must be enclosed by &lt;Begin/EndValue&gt; delimiters. The XSD that is defined in this delimiters will be inserted into the XSD schema that the GDL parser generates. Note that the &lt;complexType&gt; definitions that will be referenced as the ValueType of a GDL attribute cannot declare any XML attributes. In the schema that the GDL parser produces, the XSD namespace is the default namespace, so element names like &lt;complexType&gt; or &lt;sequence&gt; or &lt;element&gt; do not need a namespace qualifier. The target namespace is associated with the gdl: prefix.

-   \*ComplexType? (**TRUE** | **FALSE**) (Optional). If this directive is **TRUE**, the GDL parser will reference this definition as &lt;complexContent&gt; when extending this data type; otherwise, the definition is referenced as &lt;simpleContent&gt;. If this directive is not specified, the parser will assume it is **FALSE**.

-   \*ArrayLabel (Optional). If this directive is specified, the parser filter expects the instance values of this type to be enclosed by parentheses, preceded by the specified array label.

The syntax of the value instance that is declared to be of this data type must adhere to the syntax that is defined by the XSD that the \*XSDTypeDefinition directive supplies. The parser will provide the start and end tag for the element, and the value instance data should supply only the element content. If the XML syntax conflicts with the basic GDL syntax rules, the value (or just the conflicting portion) must be enclosed within &lt;Begin/EndValue:&gt; constructs.

XML values with such incompatible syntaxes, or whose syntax is incompatible with the syntax that compound data types use, cannot appear as a member of a compound data type. Also note that the GDL parser will not escape special XML characters like opening or closing brackets (&lt; or &gt;) or an ampersand (&). The creator of the value instance is responsible for conforming to XML syntax for character data.

For example, consider the following template.

```cpp
*Template:  USAddress
{
    *Type:  DATATYPE
    *DataType:   XSD_DEFINED
    *ComplexType?: TRUE
    *XMLDataType: "USAddress"
    *XSDTypeDefinition:<BeginValue:XSD>
    <complexType name="USAddress">
        <sequence>
            <element name="name"   type="string"/>
            <element name="street" type="string"/>
            <element name="city"   type="string"/>
            <element name="state"  type="string"/>
            <element name="zip"    type="gdl:zipCode"/>
        </sequence>
    </complexType>

<simpleType name="zipCode">
 <restriction base="integer">
  <minInclusive value="10000"/>
  <maxInclusive value="99999"/>
 </restriction>
</simpleType><EndValue:XSD>
}
```

The preceding example defines an XSD-defined type named "USAddress" that can be referenced by a GDL attribute as its ValueType. This XSD example actually defines two data types: **USAddress** and **zipCode**. The **zipCode** type cannot be referenced by a GDL attribute and can be referenced only from within another XSD data type definition.

In the following example, the **zipCode** type is referenced in the declaration of the &lt;zip&gt; element. Note that it is referenced by using the gdl: namespace prefix. **zipCode** could also be referenced from a XSD data type definition in another template.

The preceding template definition will cause the creation of the following XML schema entry (it is the value of \*XSDTypeDefinition unchanged).

```cpp
    <complexType name="USAddress">
        <sequence>
            <element name="name"   type="string"/>
            <element name="street" type="string"/>
            <element name="city"   type="string"/>
            <element name="state"  type="string"/>
            <element name="zip"    type="gdl:zipCode"/>
        </sequence>
    </complexType>

    <simpleType name="zipCode">
        <restriction base="integer">
            <minInclusive value="10000"/>
            <maxInclusive value="99999"/>
        </restriction>
    </simpleType>
```

The parser automatically constructs another data type that defines a new type that is derived from the **USAddress** type, but that has additional XML attributes that might appear in the snapshot. If you use original data type, you would receive schema validation errors because the original type did not allow for any XML attributes to appear. With this approach, youdo not have to hard code parser-synthesized XML attributes in your templates, and if additional attributes are added to future versions of the snapshot, you would not need to modify the existing templates.

The following code example shows the additional data type definition.

```cpp
    <complexType name = "GDLW_USAddress">
        <complexContent>
            <extension base="gdl:USAddress">
                <attribute name="Name" type="string" use="optional"/>
                <attribute name="Personality" type="string" use="optional"/>
            </extension>
        </complexContent>
    </complexType>
```

**Note**   The **GDLW\_USAddress** data type is declared as &lt;complexContent&gt; because the template for **USAddress** set \*ComplexType?: **TRUE**.

 

Consider the following GDL entry.

```cpp
*Address: <BeginValue:XML> 
   <name>Alice Smith</name>
   <street>123 Maple Street</street>
   <city>Mill Valley</city>
   <state>CA</state>
   <zip>90952</zip>
<EndValue:XML>
```

And consider the ADDRESS template, which declares the \*Address GDL aAttribute to have a \*ValueType that is defined by the template **USAddress**, as the following code example shows.

```cpp
*Template:  ADDRESS
{
    *Name: "*Address"
    *Type:  ATTRIBUTE
    *ValueType:  USAddress
}
```

If the earlier GDL entry is interpreted by using the ADDRESS template, the resulting XML output would occur.

```cpp
    <GDL_ATTRIBUTE Name="*Address"  xsi:type="GDLW_USAddress" >
    <name>Ben Smith</name>
    <street>123 Maple Street</street>
    <city>Mill Valley</city>
    <state>CA</state>
    <zip>90952</zip>
    </GDL_ATTRIBUTE>
```

The XML attribute xsi:type defines this instance of the ATTRIBUTE element to hold an XSD-defined data type named **GDLW\_USAddress**. The entire value of the GDL attribute instance is inserted as element content into the &lt;GDL\_ATTRIBUTE&gt; element in the XML snapshot without any modification. Thus, the value must be valid XML and must follow all XML syntax rules, like representation of special characters.

 

 




