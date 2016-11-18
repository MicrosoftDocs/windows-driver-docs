---
title: SimpleService WSDL
description: SimpleService WSDL
ms.assetid: 4fb5fcb7-9821-47c8-ae0d-3e73f8ee30c5
keywords: ["WSDBIT tool WDK , WSDL", "WSDAPI Basic Interoperability Tool WDK , WSDL", "SimpleService service WDK WSDBIT", "WSDBIT tool WDK , services", "WSDAPI Basic Interoperability Tool WDK , services"]
---

# SimpleService WSDL


The following code sample shows the SimpleService WSDL.

```
<wsdl:definitions
    targetNamespace="http://schemas.example.org/SimpleService"
    xmlns:tns="http://schemas.example.org/SimpleService"
    xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing"
    xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
    xmlns:wsdp="http://schemas.xmlsoap.org/ws/2006/02/devprof"
    xmlns:wsp="http://schemas.xmlsoap.org/ws/2004/09/policy"
    xmlns:wsoap12="http://schemas.xmlsoap.org/wsdl/soap12/"
    xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"
    xmlns:wsx="http://schemas.xmlsoap.org/ws/2004/09/mex"
    xmlns:wsf="http://schemas.xmlsoap.org/ws/2004/09/transfer">
 
    <wsp:Policy wsu:Id="Simple">
        <wsdp:Profile />
    </wsp:Policy>
 
    <wsdl:types>
        <xs:schema
            targetNamespace="http://schemas.example.org/SimpleService"
            xmlns:tns="http://schemas.example.org/SimpleService"
            xmlns:xs="http://www.w3.org/2001/XMLSchema"
            elementFormDefault="qualified"
            blockDefault="#all">


            <!-- ========================================================== -->
            <!-- OneWay message -->
            <!-- This verifies sending a simple value one-way to the service -->

            <xs:element name="OneWay" type="tns:OneWayType" />
            <xs:complexType name="OneWayType">
                <xs:sequence>
                    <xs:element name="Param" type="xs:int" />
                    <xs:any minOccurs="0" maxOccurs="unbounded"
                        namespace="##other" processContents="lax" />
                </xs:sequence>
                <xs:anyAttribute namespace="##other" processContents="lax" />
            </xs:complexType>


            <!-- ========================================================== -->
            <!-- TwoWay message -->
            <!-- This verifies sending a pair of values to a service and
                 receiving a sum in response -->

            <xs:element name="TwoWayRequest" type="tns:TwoWayType" />
            <xs:complexType name="TwoWayType">
                <xs:sequence>
                    <xs:element name="X" type="xs:int" />
                    <xs:element name="Y" type="xs:int" />
                    <xs:any minOccurs="0" maxOccurs="unbounded"
                        namespace="##other" processContents="lax" />
                </xs:sequence>
                <xs:anyAttribute namespace="##other" processContents="lax" />
            </xs:complexType>
            <xs:element name="TwoWayResponse" type="tns:TwoWayResponseType" />
            <xs:complexType name="TwoWayResponseType">
                <xs:sequence>
                    <xs:element name="Sum" type="xs:int" />
                    <xs:any minOccurs="0" maxOccurs="unbounded"
                        namespace="##other" processContents="lax" />
                </xs:sequence>
                <xs:anyAttribute namespace="##other" processContents="lax" />
            </xs:complexType>

            <!-- ========================================================== -->
            <!-- TypeCheck message -->
            <!-- This verifies handling of specific types by sending them
                 to the service and verifying the service echoes them back
                 correctly -->

            <xs:element name="TypeCheckRequest" type="tns:TypeCheckType" />
            <xs:complexType name="TypeCheckType">
                <xs:sequence>
                    <xs:element name="BoolCheck" type="xs:boolean" />
                    <xs:element name="DecimalCheck" type="xs:decimal" />
                    <xs:element name="FloatCheck" type="xs:float" />
                    <xs:element name="UriListCheck" type="tns:UriListType" />
                    <xs:any minOccurs="0" maxOccurs="unbounded"
                        namespace="##other" processContents="lax" />
                </xs:sequence>
                <xs:anyAttribute namespace="##other" processContents="lax" />
            </xs:complexType>
            <xs:element name="TypeCheckResponse" type="tns:TypeCheckResponseType" />
            <xs:complexType name="TypeCheckResponseType">
                <xs:sequence>
                    <xs:element name="BoolCheck" type="xs:boolean" />
                    <xs:element name="DecimalCheck" type="xs:decimal" />
                    <xs:element name="FloatCheck" type="xs:float" />
                    <xs:element name="UriListCheck" type="tns:UriListType" />
                    <xs:any minOccurs="0" maxOccurs="unbounded"
                        namespace="##other" processContents="lax" />
                </xs:sequence>
                <xs:anyAttribute namespace="##other" processContents="lax" />
            </xs:complexType>

            <xs:simpleType name="UriListType" >
                <xs:list itemType="xs:anyURI" />
            </xs:simpleType>

            <!-- ========================================================== -->
            <!-- AnyCheck message -->
            <!-- This verifies handling of extensible sections by sending
                 arbitrary data and verifying the service echoes it back
                 correctly -->

            <xs:element name="AnyCheckRequest" type="tns:AnyCheckType" />
            <xs:complexType name="AnyCheckType">
                <xs:sequence>
                    <xs:any minOccurs="0" maxOccurs="unbounded"
                        namespace="##other" processContents="lax" />
                </xs:sequence>
                <xs:anyAttribute namespace="##other" processContents="lax" />
            </xs:complexType>
            <xs:element name="AnyCheckResponse" type="tns:AnyCheckResponseType" />
            <xs:complexType name="AnyCheckResponseType">
                <xs:sequence>
                    <xs:any minOccurs="0" maxOccurs="unbounded"
                        namespace="##other" processContents="lax" />
                </xs:sequence>
                <xs:anyAttribute namespace="##other" processContents="lax" />
            </xs:complexType>

        </xs:schema>
    </wsdl:types>

    <wsdl:message name="OneWayMessageIn">
        <wsdl:part name="parameters" element="tns:OneWay" />
    </wsdl:message>

    <wsdl:message name="TwoWayMessageIn">
        <wsdl:part name="parameters" element="tns:TwoWayRequest" />
    </wsdl:message>
    <wsdl:message name="TwoWayMessageOut">
        <wsdl:part name="parameters" element="tns:TwoWayResponse" />
    </wsdl:message>

    <wsdl:message name="TypeCheckMessageIn">
        <wsdl:part name="parameters" element="tns:TypeCheckRequest" />
    </wsdl:message>
    <wsdl:message name="TypeCheckMessageOut">
        <wsdl:part name="parameters" element="tns:TypeCheckResponse" />
    </wsdl:message>

    <wsdl:message name="AnyCheckMessageIn">
        <wsdl:part name="parameters" element="tns:AnyCheckRequest" />
    </wsdl:message>
    <wsdl:message name="AnyCheckMessageOut">
        <wsdl:part name="parameters" element="tns:AnyCheckResponse" />
    </wsdl:message>

 
    <wsdl:portType name="SimpleService">
        <wsdl:operation name="OneWay">
            <wsdl:input
                message="tns:OneWayMessageIn"
                wsa:Action="http://schemas.example.org/SimpleService/OneWay"/>
        </wsdl:operation>
        <wsdl:operation name="TwoWay">
            <wsdl:input
                message="tns:TwoWayMessageIn"
                wsa:Action="http://schemas.example.org/SimpleService/TwoWayRequest"/>
            <wsdl:output
                message="tns:TwoWayMessageOut"
                wsa:Action="http://schemas.example.org/SimpleService/TwoWayResponse"/>
        </wsdl:operation>
        <wsdl:operation name="TypeCheck">
            <wsdl:input
                message="tns:TypeCheckMessageIn"
                wsa:Action="http://schemas.example.org/SimpleService/TypeCheckRequest"/>
            <wsdl:output
                message="tns:TypeCheckMessageOut"
                wsa:Action="http://schemas.example.org/SimpleService/TypeCheckResponse"/>
        </wsdl:operation>
        <wsdl:operation name="AnyCheck">
            <wsdl:input
                message="tns:AnyCheckMessageIn"
                wsa:Action="http://schemas.example.org/SimpleService/AnyCheckRequest"/>
            <wsdl:output
                message="tns:AnyCheckMessageOut"
                wsa:Action="http://schemas.example.org/SimpleService/AnyCheckResponse"/>
        </wsdl:operation>
    </wsdl:portType>
 
    <wsdl:binding name="SimpleServiceSoap12Binding" type="tns:SimpleService">
        <wsoap12:binding style="document" transport="http://schemas.xmlsoap.org/soap/http" />
        <wsp:PolicyReference URI="#Simple" wsdl:required="true" />
        <wsdl:operation name="OneWay">
            <wsoap12:operation
                soapAction="http://schemas.example.org/SimpleService/OneWay" />
                <wsdl:input>
                    <wsoap12:body use="literal" />
                </wsdl:input>
            </wsdl:operation>
        <wsdl:operation name="TwoWay">
            <wsoap12:operation
                soapAction="http://schemas.example.org/SimpleService/TwoWayRequest" />
            <wsdl:input>
                <wsoap12:body use="literal" />
            </wsdl:input>
            <wsdl:output>
                <wsoap12:body use="literal" />
            </wsdl:output>
        </wsdl:operation>
        <wsdl:operation name="TypeCheck">
            <wsoap12:operation
                soapAction="http://schemas.example.org/SimpleService/TypeCheckRequest" />
            <wsdl:input>
                <wsoap12:body use="literal" />
            </wsdl:input>
            <wsdl:output>
                <wsoap12:body use="literal" />
            </wsdl:output>
        </wsdl:operation>
        <wsdl:operation name="AnyCheck">
            <wsoap12:operation
                soapAction="http://schemas.example.org/SimpleService/AnyCheckRequest" />
            <wsdl:input>
                <wsoap12:body use="literal" />
            </wsdl:input>
            <wsdl:output>
                <wsoap12:body use="literal" />
            </wsdl:output>
        </wsdl:operation>
    </wsdl:binding>
 
    <wsdl:service name="SimpleService">
        <wsdl:port
            name="SimplePort"
            binding="tns:SimpleServiceSoap12Binding">
            <wsoap12:address location="http://localhost/WebService/Simple.asmx" />
        </wsdl:port>
    </wsdl:service>
 
</wsdl:definitions> 
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20SimpleService%20WSDL%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




