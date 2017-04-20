---
title: APN schema definition
description: APN schema definition
ms.assetid: ae552bb5-702e-443f-8a97-c143859b127d
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# APN schema definition

**Note**  
The XML document must be saved by using UTF-8 encoding.

The following is a definition of the APN schema.

``` syntax
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="OperatorList">
    <xs:complexType>
      <xs:sequence>
        <xs:element ref="Operator" maxOccurs="unbounded"/>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
  <xs:element name="Operator">
    <xs:complexType>
      <xs:sequence>
        <xs:element ref="HardwareIdList"/>
        <xs:element ref="ConnectionInfoList"/>
        <xs:element ref="TrustedCertificateList" minOccurs="0"/>
      </xs:sequence>
      <xs:attribute name="name" type="xs:string" use="required"/>
      <xs:attribute name="AccountExperienceURL" type="xs:anyURI" use="optional"/>
      <xs:attribute name="OperatorGUID" type="GUID" use="optional"/>
    </xs:complexType>
  </xs:element>
  <xs:element name="HardwareIdList">
    <xs:complexType>
      <xs:sequence>
        <xs:element ref="HardwareId" maxOccurs="unbounded"/>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
  <xs:element name="HardwareId">
    <xs:complexType>
      <xs:attribute name="id" type="xs:string" use="required"/>
    </xs:complexType>
  </xs:element>
  <xs:element name="ConnectionInfoList">
    <xs:complexType>
      <xs:sequence>
        <xs:element ref="ConnectionInfo" maxOccurs="unbounded"/>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
  <xs:element name="ConnectionInfo">
    <xs:complexType>
      <xs:attribute name="AccessString" use="optional">
        <!--The AccessString element identifies the APN or dial string to be used to establish a data connection -->
        <xs:simpleType>
          <xs:restriction base="xs:string">
            <xs:minLength value="0"/>
            <xs:maxLength value="100"/>
          </xs:restriction>
        </xs:simpleType>
      </xs:attribute>
      <xs:attribute name="Username" use="optional">
        <!--The UserName element specifies the user name for logon -->
        <xs:simpleType>
          <xs:restriction base="xs:string">
            <xs:minLength value="0"/>
            <xs:maxLength value="255"/>
            <xs:whiteSpace value="collapse"/>
          </xs:restriction>
        </xs:simpleType>
      </xs:attribute>
      <xs:attribute name="Password" use="optional">
        <xs:simpleType>
          <xs:restriction base="xs:string">
            <xs:minLength value="0"/>
            <xs:maxLength value="255"/>
            <xs:whiteSpace value="collapse"/>
          </xs:restriction>
        </xs:simpleType>
      </xs:attribute>
      <xs:attribute name="FriendlyName" use="optional">
        <xs:simpleType>
          <xs:restriction base="xs:string">
            <xs:minLength value="0"/>
            <xs:maxLength value="255"/>
            <xs:whiteSpace value="collapse"/>
          </xs:restriction>
        </xs:simpleType>
      </xs:attribute>
      <xs:attribute name="Purchase" type="xs:boolean" use="required"/>
      <xs:attribute name="Internet" type="xs:boolean" use="required"/>
      <xs:attribute name="AutoConnectOrder" type="xs:positiveInteger" use="optional"/>
      <xs:attribute name="Compression" use="optional">
        <xs:simpleType>
          <xs:restriction base="xs:token">
            <xs:enumeration value="DISABLE"/>
            <xs:enumeration value="ENABLE"/>
          </xs:restriction>
        </xs:simpleType>
      </xs:attribute>
      <xs:attribute name="AuthProtocol" use="optional">
        <xs:simpleType>
          <xs:restriction base="xs:token">
            <xs:enumeration value="NONE"/>
            <xs:enumeration value="PAP"/>
            <xs:enumeration value="CHAP"/>
            <xs:enumeration value="MsCHAPv2"/>
          </xs:restriction>
        </xs:simpleType>
      </xs:attribute>
    </xs:complexType>
  </xs:element>
  <xs:element name="TrustedCertificateList">
    <xs:complexType>
      <xs:sequence>
        <xs:element ref="TrustedCertificate" maxOccurs="unbounded"/>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
  <xs:element name="TrustedCertificate">
    <xs:complexType>
      <xs:attribute name="SubjectName" type="xs:string" use="required"/>
      <xs:attribute name="IssuerName" type="xs:string" use="required"/>
    </xs:complexType>
  </xs:element>
  <xs:simpleType name="GUID">
    <xs:restriction base="xs:token">
      <xs:pattern value="\{[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\}"/>
    </xs:restriction>
  </xs:simpleType>
</xs:schema>
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20APN%20schema%20definition%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




