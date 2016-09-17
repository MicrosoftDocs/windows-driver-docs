---
title: EnumSchema Request and Response Schemas
author: windows-driver-content
description: The EnumSchema request schema and corresponding response schema definition, and an example of each, are below.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 031FA2EA-A33B-409C-82FD-B4FE9D0A2E93
---

# EnumSchema Request and Response Schemas


The EnumSchema request schema and corresponding response schema definition, and an example of each, are below.

## The EnumSchema Request Schema


An EnumSchema request is used to obtain a list of the printer's properties.

All EnumSchema requests are exactly the same and consist of only a root element.

``` syntax
<bidi:EnumSchema xmlns:bidi="http://schemas.microsoft.com/windows/2005/03/printing/bidi"/>
```

Formal Definition of the EnumSchema Request Schema

``` syntax
<?xml version='1.0'?>
<schema targetNamespace="http://schemas.microsoft.com/windows/2005/03/printing/bidi" 
  xmlns:bidi="http://schemas.microsoft.com/windows/2005/03/printing/bidi" 
  xmlns ='http://www.w3.org/2001/XMLSchema'>
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

``` syntax
<bidi:EnumSchema xmlns:bidi="http://schemas.microsoft.com/windows/2005/03/printing/bidi">
  <Schema name='\Printer.Configuration.DuplexUnit:Installed' />
  <Schema name='\Printer.Configuration.HardDisk:Installed'/>
  <Schema name='\Printer.Configuration.HardDisk:Capacity'/>
  <Schema name='\Printer.Configuration.HardDisk:FreeSpace'/>
</bidi:EnumSchema>
```

Formal Definition of the EnumSchema Response Schema

``` syntax
<?xml version='1.0'?>
<schema targetNamespace="http://schemas.microsoft.com/windows/2005/03/printing/bidi" 
  xmlns:bidi="http://schemas.microsoft.com/windows/2005/03/printing/bidi" 
  xmlns ='http://www.w3.org/2001/XMLSchema'>
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
[**SendRecvXMLStream**](https://msdn.microsoft.com/library/windows/hardware/dd144983)  
[**SendRecvXMLString**](https://msdn.microsoft.com/library/windows/hardware/dd144984)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20EnumSchema%20Request%20and%20Response%20Schemas%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


