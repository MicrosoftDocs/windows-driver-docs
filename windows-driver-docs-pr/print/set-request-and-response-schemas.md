---
title: Set Request and Response Schemas
author: windows-driver-content
description: The Set request schema and corresponding response schema definition, and an example of each, are below.
ms.assetid: 88E7F06C-3232-48C3-A0D6-2BEFF4ABA188
---

# Set Request and Response Schemas


The Set request schema and corresponding response schema definition, and an example of each, are below.

## Set Request Schema


The Set request is used to write values to printer properties.

In this example, the request attempts to set two properties. The second is a deliberate mistake: the Memory property is not writable. For the response to this request, see Set Response Schema below.

``` syntax
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

``` syntax
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

``` syntax
<bidi:Set xmlns:bidi="http://schemas.microsoft.com/windows/2005/03/printing/bidi">
  <Query schema='\Printer.DeviceInfo:Location'/>
  <Query schema='\Printer.Configuration.Memory:Size'>
    <Error>ERROR_BIDI_SCHEMA_READ_ONLY</Error>
  </Query>
</bidi:Set>
```

Formal Definition of the Set Response Schema

``` syntax
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
[**SendRecvXMLStream**](https://msdn.microsoft.com/library/windows/hardware/dd144983)  
[**SendRecvXMLString**](https://msdn.microsoft.com/library/windows/hardware/dd144984)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Set%20Request%20and%20Response%20Schemas%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


