---
title: Email Filter Instructions Schema
description: Email Filter Instructions Schema
ms.assetid: 12e0a664-72fc-4c1a-9fa0-e87b4e3cce3e
keywords: ["Email Filter Instructions Schema"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Email Filter Instructions Schema


You can use the following schema for post-scan filtering for email destinations.

```
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:emlf="http://schemas.microsoft.com/windows/2007/10/imaging/postscan/filter/email"
        xmlns:xs="http://www.w3.org/2001/XMLSchema"
        targetNamespace="http://schemas.microsoft.com/windows/2007/10/imaging/postscan/filter/email"
        elementFormDefault="qualified">
    <xs:annotation>
        <xs:documentation>
            WSD Enterprise Scanning - Email filter Instructions schema
            Copyright 2007 Microsoft Corp. All rights reserved
        </xs:documentation>
    </xs:annotation>

    <xs:annotation>
        <xs:documentation>
            Define the XML Elements that represent the Filter configuration for the SMTP Email filter.
        </xs:documentation>
    </xs:annotation>
    <xs:attribute name="CanAddAddresses" type="xs:boolean" default="false" />
    <xs:element name="EmailConfig" type="emlf:EmailConfigType" />
    <xs:complexType name="EmailConfigType">
        <xs:sequence>
            <xs:element name="SendToScanUser" type="emlf:BoolExtType" minOccurs="0" />
            <xs:element name="SendToAddresses" type="emlf:SendToAddressesType" minOccurs="0" />
            <xs:any namespace="##other" minOccurs="0" maxOccurs="unbounded"/>
        </xs:sequence>
        <xs:anyAttribute namespace="##other" processContents="lax"/>
    </xs:complexType>
    <xs:complexType name="SendToAddressesType">
        <xs:sequence>
            <xs:element name="EmailAddress" type="emlf:String255ExtType" maxOccurs="unbounded" />
            <xs:any namespace="##other" minOccurs="0" maxOccurs="unbounded"/>
        </xs:sequence>
<xs:attribute ref="emlf:CanAddAddresses"/>
        <xs:anyAttribute namespace="##other" processContents="lax"/>
    </xs:complexType>

    <xs:annotation>
        <xs:documentation>Extensions to basic element types to allow IHV extensibility</xs:documentation>
    </xs:annotation>
    <xs:complexType name="BoolExtType">
        <xs:simpleContent>
            <xs:extension base="xs:boolean">
                <xs:anyAttribute namespace="##other" processContents="lax"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
    <xs:complexType name="String255ExtType">
        <xs:simpleContent>
            <xs:extension base="emlf:String255BaseType">
                <xs:anyAttribute namespace="##other" processContents="lax"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
    <xs:simpleType name="String255BaseType">
        <xs:restriction base="xs:string">
            <xs:maxLength value="255"/>
            <xs:whiteSpace value="preserve"/>
        </xs:restriction>
    </xs:simpleType>
</xs:schema>
```

The DSM Email Filter Instruction Schema supports the following element:

[EmailConfig](emailconfig.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Email%20Filter%20Instructions%20Schema%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




