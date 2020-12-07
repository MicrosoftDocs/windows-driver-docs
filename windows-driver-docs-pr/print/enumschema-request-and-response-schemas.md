---
title: EnumSchema Request and Response Schemas
description: The EnumSchema request schema and corresponding response schema definition, and an example of each, are below.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EnumSchema Request and Response Schemas


The EnumSchema request schema and corresponding response schema definition, and an example of each, are below.

## The EnumSchema Request Schema


An EnumSchema request is used to obtain a list of the printer's properties.

All EnumSchema requests are exactly the same and consist of only a root element.

```xml
<bidi:EnumSchema xmlns:bidi="https://schemas.microsoft.com/windows/2005/03/printing/bidi"/>
```

Formal Definition of the EnumSchema Request Schema

```xml
<?xml version='1.0'?>
<schema targetNamespace="https://schemas.microsoft.com/windows/2005/03/printing/bidi" 
  xmlns:bidi="https://schemas.microsoft.com/windows/2005/03/printing/bidi" 
  xmlns ='https://www.w3.org/2001/XMLSchema'>
  <element name='EnumSchema'>
    <complexType>
      <anyAttribute namespace='##other' processContents='skip'/>
    </complexType>
  </element>
</schema>
```

## The EnumSchema Response Schema


The EnumSchema response has a &lt;Schema&gt; element for each property.

In this example, the printer has only a few accessible properties.

```xml
<bidi:EnumSchema xmlns:bidi="https://schemas.microsoft.com/windows/2005/03/printing/bidi">
  <Schema name='\Printer.Configuration.DuplexUnit:Installed' />
  <Schema name='\Printer.Configuration.HardDisk:Installed'/>
  <Schema name='\Printer.Configuration.HardDisk:Capacity'/>
  <Schema name='\Printer.Configuration.HardDisk:FreeSpace'/>
</bidi:EnumSchema>
```

Formal Definition of the EnumSchema Response Schema

```xml
<?xml version='1.0'?>
<schema targetNamespace="https://schemas.microsoft.com/windows/2005/03/printing/bidi" 
  xmlns:bidi="https://schemas.microsoft.com/windows/2005/03/printing/bidi" 
  xmlns ='https://www.w3.org/2001/XMLSchema'>
  <element name='EnumSchema'>
    <complexType>
      <sequence maxOccurs='unbounded'>
        <element name='Schema'>
          <complexType>
            <attribute name='name' type='bidi:SCHEMA_STRING' use='required'/>
          </complexType>
        </element>
      </sequence>
    </complexType>
  </element>
  <simpleType name='SCHEMA_STRING'>
    <restriction base='string'>
      <pattern value='\\\w+(\.\w+)*\:\w+'/>
    </restriction>
  </simpleType>
</schema>
```

## Related topics

[Bidirectional Communication Schema](bidirectional-communication-schema.md)  

[SendRecvXMLStream](/windows-hardware/drivers/ddi/bidispl/nf-bidispl-ibidispl2-sendrecvxmlstream)  

[SendRecvXMLString](/windows-hardware/drivers/ddi/bidispl/nf-bidispl-ibidispl2-sendrecvxmlstring)
