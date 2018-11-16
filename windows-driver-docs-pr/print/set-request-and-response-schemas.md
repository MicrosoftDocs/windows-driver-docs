---
title: Set Request and Response Schemas
description: The Set request schema and corresponding response schema definition, and an example of each, are below.
ms.assetid: 88E7F06C-3232-48C3-A0D6-2BEFF4ABA188
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Set Request and Response Schemas


The Set request schema and corresponding response schema definition, and an example of each, are below.

## Set Request Schema


The Set request is used to write values to printer properties.

In this example, the request attempts to set two properties. The second is a deliberate mistake: the Memory property is not writable. For the response to this request, see Set Response Schema below.

```xml
<bidi:Set xmlns:bidi="http://schemas.microsoft.com/windows/2005/03/printing/bidi">
  <Query schema='\Printer.DeviceInfo:Location'>
    <BIDI_STRING>supply room</BIDI_STRING>
  </Query>
  <Query schema='\Printer.Configuration.Memory:Size'>
    <BIDI_INT>4096</BIDI_INT>
  </Query>
</bidi:Set>
```

Formal Definition of the Set Request Schema

```xml
<?xml version='1.0'?>
<schema targetNamespace="http://schemas.microsoft.com/windows/2005/03/printing/bidi" 
     xmlns:bidi="http://schemas.microsoft.com/windows/2005/03/printing/bidi" 
     xmlns ='http://www.w3.org/2001/XMLSchema'>
  <element name='Set'>
    <complexType>
      <sequence maxOccurs='unbounded'>
        <element name='Query'>
          <complexType>
            <choice>
              <element name='BIDI_STRING' type='string'/>
              <element name='BIDI_TEXT'   type='string'/>
              <element name='BIDI_ENUM'   type='string'/>
              <element name='BIDI_INT'    type='integer'/>
              <element name='BIDI_FLOAT'  type='float'/>
              <element name='BIDI_BOOL'   type='boolean'/>
              <element name='BIDI_BLOB'   type='base64Binary'/>
            </choice>
            <attribute name='schema' type='bidi:SCHEMA_STRING' use='required'/>
            <anyAttribute namespace='##other' processContents='skip'/>
          </complexType>
          </element>
      </sequence>
      <anyAttribute namespace='##other' processContents='skip'/>
    </complexType>
  </element>
  <simpleType name='SCHEMA_STRING'>
    <restriction base='string'>
      <pattern value='\\\w+(\.\w+)*\:\w+'/>
    </restriction>
  </simpleType>
</schema>
```

## Set Response Schema


This is the response to the Set request above. Note that when the write operation succeeds, the original query value is returned without any value. If the operation fails, an error code is returned.

```xml
<bidi:Set xmlns:bidi="http://schemas.microsoft.com/windows/2005/03/printing/bidi">
  <Query schema='\Printer.DeviceInfo:Location'/>
  <Query schema='\Printer.Configuration.Memory:Size'>
    <Error>ERROR_BIDI_SCHEMA_READ_ONLY</Error>
  </Query>
</bidi:Set>
```

Formal Definition of the Set Response Schema

```xml
<?xml version='1.0'?>
<schema targetNamespace="http://schemas.microsoft.com/windows/2005/03/printing/bidi" 
     xmlns:bidi="http://schemas.microsoft.com/windows/2005/03/printing/bidi" 
     xmlns ='http://www.w3.org/2001/XMLSchema'>
  <element name='Set'>
    <complexType>
      <sequence maxOccurs='unbounded'>
        <element name='Query'>
          <complexType>
            <sequence minOccurs='0' maxOccurs='1'>
              <element name='Error' type='integer'/>
            </sequence>
            <attribute name='schema' type='bidi:SCHEMA_STRING' use='required'/>
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

[SendRecvXMLStream](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/bidispl/nf-bidispl-ibidispl2-sendrecvxmlstream)  

[SendRecvXMLString](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/bidispl/nf-bidispl-ibidispl2-sendrecvxmlstring)  
