---
title: AttachmentService WSDL
description: AttachmentService WSDL
ms.assetid: 1a886bd8-5eb4-4990-9d39-bacbbbbe3d3d
keywords: ["WSDBIT tool WDK , WSDL", "WSDAPI Basic Interoperability Tool WDK , WSDL", "AttachmentService service WDK WSDBIT", "WSDBIT tool WDK , services", "WSDAPI Basic Interoperability Tool WDK , services"]
---

# AttachmentService WSDL


The following code sample shows the AttachmentService WSDL.

```
<wsdl:definitions 
 targetNamespace="http://schemas.example.org/AttachmentService" 
 xmlns:tns="http://schemas.example.org/AttachmentService"
 xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" 
 xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" 
 xmlns:wsdp="http://schemas.xmlsoap.org/ws/2005/05/devprof" 
 xmlns:wsp="http://schemas.xmlsoap.org/ws/2004/09/policy" 
 xmlns:wsoap12="http://schemas.xmlsoap.org/wsdl/soap12/"
 xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"
 xmlns:wsx="http://schemas.xmlsoap.org/ws/2004/09/mex"
    xmlns:wsf="http://schemas.xmlsoap.org/ws/2004/09/transfer">

 <wsp:Policy wsu:Id="Attachment">
 <wsdp:Profile />
 <wsdp:OptimizedMimeSerialization />
 </wsp:Policy>

 <wsdl:types>
 <xs:schema 
   targetNamespace="http://schemas.example.org/AttachmentService"
   xmlns:tns="http://schemas.example.org/AttachmentService" 
   xmlns:xs="http://www.w3.org/2001/XMLSchema"
   elementFormDefault="qualified" 
   blockDefault="#all" >
 <xs:element name="OneWayAttachment" type="tns:AttachmentType" />
 <xs:complexType name="AttachmentType" >
 <xs:sequence>
 <xs:element name="Param" type="xs:base64Binary" />
 <xs:any minOccurs="0" maxOccurs="unbounded" 
 namespace="##other" processContents="lax" />
 </xs:sequence>
 <xs:anyAttribute namespace="##other"
 processContents="lax" />
 </xs:complexType>
 <xs:element name="TwoWayAttachmentRequest"    
 type="tns:AttachmentType" />
 <xs:element name="TwoWayAttachmentResponse"
 type="tns:AttachmentType" />
 </xs:schema>
 </wsdl:types>

 <wsdl:message name="OneWayAttachmentMessageIn">
 <wsdl:part name="parameters" element="tns:OneWayAttachment" />
 </wsdl:message>
 <wsdl:message name="TwoWayAttachmentMessageIn">
 <wsdl:part name="parameters" element="tns:TwoWayAttachmentRequest" />
 </wsdl:message>
 <wsdl:message name="TwoWayAttachmentMessageOut">
 <wsdl:part name="parameters" element="tns:TwoWayAttachmentResponse" />
 </wsdl:message>

 <wsdl:portType name="AttachmentService">
        <wsdl:operation name="OneWayAttachment">
            <wsdl:input
                message="tns:OneWayAttachmentMessageIn"
                    wsa:Action="http://schemas.example.org/AttachmentService/OneWayAttachment"/>
        </wsdl:operation>
        <wsdl:operation name="TwoWayAttachment">
            <wsdl:input
                message="tns:TwoWayAttachmentMessageIn"
                wsa:Action="http://schemas.example.org/AttachmentService/TwoWayAttachmentRequest"/>
            <wsdl:output
                message="tns:TwoWayAttachmentMessageOut"
                wsa:Action="http://schemas.example.org/AttachmentService/TwoWayAttachmentResponse"/>
        </wsdl:operation>

 </wsdl:portType>

 <wsdl:binding name="AttachmentServiceSoap12Binding" type="tns:AttachmentService">
 <wsoap12:binding style="document"
 transport="http://schemas.xmlsoap.org/soap/http" />
 <wsp:PolicyReference URI="#Attachment" wsdl:required="true" />
        <wsdl:operation name="OneWayAttachment">
            <wsoap12:operation
                soapAction="http://schemas.example.org/AttachmentService/OneWayAttachment"/>
            <wsdl:input>
                <wsoap12:body use="literal" />
            </wsdl:input>
        </wsdl:operation>
        <wsdl:operation name="TwoWayAttachment">
            <wsoap12:operation
                soapAction="http://schemas.example.org/AttachmentService/TwoWayAttachmentRequest"/>
            <wsdl:input>
                <wsoap12:body use="literal" />
            </wsdl:input>
            <wsdl:output>
                <wsoap12:body use="literal" />
            </wsdl:output>
        </wsdl:operation>

 </wsdl:binding>

 <wsdl:service name="AttachmentService">
 <wsdl:port 
 name="AttachmentPort"
 binding="tns:AttachmentServiceSoap12Binding">
 <wsoap12:address
 location="http://localhost/WebService/Attachment.asmx" />
 </wsdl:port>
 </wsdl:service>

</wsdl:definitions>
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20AttachmentService%20WSDL%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




