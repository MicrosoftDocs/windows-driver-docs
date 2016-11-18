---
title: EventingService WSDL
description: EventingService WSDL
ms.assetid: 2071f4db-6a5a-4e9f-b53f-f50d4d99772a
keywords: ["WSDBIT tool WDK , WSDL", "WSDAPI Basic Interoperability Tool WDK , WSDL", "EventingService service WDK WSDBIT", "WSDBIT tool WDK , services", "WSDAPI Basic Interoperability Tool WDK , services"]
---

# EventingService WSDL


The following code sample shows the EventingService WSDL.

```
<wsdl:definitions 
 targetNamespace="http://schemas.example.org/EventingService" 
 xmlns:tns="http://schemas.example.org/EventingService"
 xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" 
 xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
 xmlns:wsdp="http://schemas.xmlsoap.org/ws/2005/05/devprof" 
 xmlns:wse="http://schemas.xmlsoap.org/ws/2004/08/eventing" 
 xmlns:wsp="http://schemas.xmlsoap.org/ws/2004/09/policy" 
 xmlns:wsoap12="http://schemas.xmlsoap.org/wsdl/soap12/"
    xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"
 xmlns:wsx="http://schemas.xmlsoap.org/ws/2004/09/mex"
 xmlns:wsf="http://schemas.xmlsoap.org/ws/2004/09/transfer" >

 <wsp:Policy wsu:Id="Eventing" >
 <wsdp:Profile />
 <wsdp:PushDelivery />
 <wsdp:DurationExpiration />
 <wsdp:ActionFilter />
 </wsp:Policy>

 <wsdl:types>
 <xs:schema 
   targetNamespace="http://schemas.example.org/EventingService"
   xmlns:tns="http://schemas.example.org/EventingService" 
   xmlns:xs="http://www.w3.org/2001/XMLSchema"
   elementFormDefault="qualified" 
   blockDefault="#all">

 <xs:element name="SimpleEvent" type="tns:SimpleEventType" />
 <xs:complexType name="SimpleEventType">
     <xs:sequence/>
 </xs:complexType>
 
 <xs:element name="IntegerEvent" type="tns:IntegerEventType" />
 <xs:complexType name="IntegerEventType">
 <xs:sequence>
 <xs:element name="Param" type="xs:int" />
 <xs:any minOccurs="0"
 maxOccurs="unbounded"
 namespace="##other"
 processContents="lax" />
 </xs:sequence>
 <xs:anyAttribute namespace="##other"
 processContents="lax" />
 </xs:complexType>
 </xs:schema>
 </wsdl:types>

 <wsdl:message name="SimpleEventMessageOut">
 <wsdl:part name="parameters" element="tns:SimpleEvent" />
 </wsdl:message>
 <wsdl:message name="IntegerEventMessageOut">
 <wsdl:part name="parameters" element="tns:IntegerEvent" />
 </wsdl:message>

   <wsdl:portType name="EventingService" wse:EventSource="true" >
        <wsdl:operation name="SimpleEvent">
            <wsdl:output
                message="tns:SimpleEventMessageOut"
                wsa:Action="http://schemas.example.org/EventingService/SimpleEvent"/>
        </wsdl:operation>
        <wsdl:operation name="IntegerEvent">
            <wsdl:output
                message="tns:IntegerEventMessageOut"
                wsa:Action="http://schemas.example.org/EventingService/IntegerEvent"/>
        </wsdl:operation>
    </wsdl:portType>

 <wsdl:binding name="EventingServiceSoap12Binding" type="tns:EventingService">
 <wsoap12:binding style="document"
 transport="http://schemas.xmlsoap.org/soap/http" />
 <wsp:PolicyReference URI="#Eventing" wsdl:required="true" />
        <wsdl:operation name="SimpleEvent">
            <wsoap12:operation
                soapAction="http://schemas.example.org/EventingService/SimpleEvent" />
            <wsdl:output>
                <wsoap12:body use="literal" />
            </wsdl:output>
        </wsdl:operation>
        <wsdl:operation name="IntegerEvent">
            <wsoap12:operation
                soapAction="http://schemas.example.org/EventingService/IntegerEvent" />
            <wsdl:output>
                <wsoap12:body use="literal" />
            </wsdl:output>
        </wsdl:operation>
 </wsdl:binding>

 <wsdl:service name="EventingService">
 <wsdl:port 
   name="EventingPort" 
   binding="tns:EventingServiceSoap12Binding">
 <wsoap12:address
 location="http://localhost/WebService/Eventing.asmx" />
 </wsdl:port>
 </wsdl:service>

</wsdl:definitions>
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20EventingService%20WSDL%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




