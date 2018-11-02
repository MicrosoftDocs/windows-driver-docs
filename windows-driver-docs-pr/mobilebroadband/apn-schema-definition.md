---
title: APN schema definition
description: APN schema definition
ms.assetid: ae552bb5-702e-443f-8a97-c143859b127d
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





