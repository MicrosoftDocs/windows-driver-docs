---
title: GetWithArgument Request and Response Schemas
author: windows-driver-content
description: The GetWithArgument request schema and corresponding response schema definition, and an example of each, are below.
ms.assetid: F68731BC-2907-4FA2-B5A4-0FAC0A9F663A
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GetWithArgument Request and Response Schemas


The GetWithArgument request schema and corresponding response schema definition, and an example of each, are below.

## GetWithArgument Request Schema


A GetWithArgument request is used to query the printer for one or more of its current values.

The response to this request is in the following section [GetWithArgument Response Schema](#getwithargument-response-schema).

``` syntax
<bidi:GetWithArgument xmlns:bidi='http://schemas.microsoft.com/windows/2005/03/printing/bidi'>
  <Query schema='\Printer.Resources:Data'>
    <BIDI_STRING>en-us</BIDI_STRING>
  </Query>
</bidi:GetWithArgument>
```

Formal Definition of the GetWithArgument Request Schema

``` syntax
<?xml version='1.0'?>  
<schema targetNamespace='http://schemas.microsoft.com/windows/2005/03/printing/bidi'  
    xmlns:bidi='http://schemas.microsoft.com/windows/2005/03/printing/bidi'   
    xmlns ='http://www.w3.org/2001/XMLSchema'>  
    <element name='GetWithArgument'>  
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
                        <attribute name='schema' type='bidi:PARTIAL_SCHEMA_STRING' use='required'/>  
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
    <simpleType name='PARTIAL_SCHEMA_STRING'>  
        <restriction base='string'>  
            <pattern value='\(\w+(\.\w+)*(\:\w+)?)?'/>  
        </restriction>  
    </simpleType>   
</schema>
```

## GetWithArgument Response Schema


This example is the response to the GetWithArgument request above. For queries that succeed, the result is the value of the particular schema. For queries that fail, the result is an error code.

``` syntax
<bidi:GetWithArgumentResponse xmlns:bidi="http://schemas.microsoft.com/windows/2005/03/printing/bidi">
  <Query schema="\Printer.Data:GetWithArgument">
    <Schema name="\Printer.Data:GetWithArgument">
      <BIDI_BLOB>Base64 Encoded XML resource file data to be used by Print Config<BIDI_BLOB>
    </Schema>
  </Query>
</bidi:GetWithArgumentResponse>
```

Formal Definition of the GetWithArgument Response Schema

``` syntax
<?xml version='1.0'?>  
<schema targetNamespace='http://schemas.microsoft.com/windows/2005/03/printing/bidi'  
    xmlns:bidi='http://schemas.microsoft.com/windows/2005/03/printing/bidi'   
    xmlns ='http://www.w3.org/2001/XMLSchema'>  
    <element name='GetWithArgumentResponse'>  
        <complexType>  
            <sequence maxOccurs='unbounded'>  
                <element name='Query'>  
                    <complexType>  
                        <choice>  
                            <sequence maxOccurs='unbounded'>  
                                <element name='Schema'>  
                                    <complexType>  
                                        <choice>  
                                            <element name='BIDI_STRING' type='string'/>  
                                            <element name='BIDI_TEXT'   type='string'/>  
                                            <element name='BIDI_ENUM'   type='string'/>  
                                            <element name='BIDI_INT'    type='integer'/>  
                                            <element name='BIDI_FLOAT'  type='float'/>  
                                            <element name='BIDI_BOOL'   type='boolean'/>  
                                            <element name='BIDI_BLOB'   type='base64Binary'/>  
                                            <element name='Error'       type='integer'/>  
                                        </choice>  
                                        <attribute name='name' type='bidi:SCHEMA_STRING' use='required'/>  
                                    </complexType>  
                                </element>  
                            </sequence>  
                            <element name='Error' type='integer'/>  
                        </choice>  
                        <attribute name='schema' type='bidi:PARTIAL_SCHEMA_STRING' use='required'/>  
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
    <simpleType name='PARTIAL_SCHEMA_STRING'>  
        <restriction base='string'>  
            <pattern value='\(\w+(\.\w+)*(\:\w+)?)?'/>  
        </restriction>  
    </simpleType>    
</schema>
```

## Related topics
[Bidirectional Communication Schema](bidirectional-communication-schema.md)  
[**SendRecvXMLStream**](https://msdn.microsoft.com/library/windows/hardware/dd144983)  
[**SendRecvXMLString**](https://msdn.microsoft.com/library/windows/hardware/dd144984)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GetWithArgument%20Request%20and%20Response%20Schemas%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


