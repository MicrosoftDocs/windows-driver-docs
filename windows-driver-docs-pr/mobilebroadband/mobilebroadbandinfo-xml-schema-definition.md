---
title: MobileBroadbandInfo XML schema definition
description: MobileBroadbandInfo XML schema definition
ms.assetid: 4d4a8f0a-99e5-429b-bc56-fdc4818b0a91
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MobileBroadbandInfo XML schema definition

[!include[MBAE deprecation warning](mbae-deprecation-warning.md)]

The following is the namespace of the MobileBroadbandInfo XML schema:

``` syntax
http://schemas.microsoft.com/windows/2010/12/DeviceMetadata/MobileBroadbandInfo
```

The following is a definition of the MobileBroadbandInfo schema.

``` syntax
<?xml version="1.0" encoding ="UTF-8" ?>

<xs:schema
    targetNamespace="http://schemas.microsoft.com/windows/2010/12/DeviceMetadata/MobileBroadbandInfo"
    xmlns:tns="http://schemas.microsoft.com/windows/2010/12/DeviceMetadata/MobileBroadbandInfo"
    xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified" blockDefault="#all">

  <!-- root node -->
  <xs:element name="MobileBroadbandInfo" type="tns:MobileBroadbandInfoType"/>

  <!-- Tethering Enumeration Type -->
  <xs:simpleType name="TetheringAllowedType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="Never"/>
      <xs:enumeration value="Always"/>
      <xs:enumeration value="EntitlementCheckRequired"/>
    </xs:restriction>  
  </xs:simpleType>  

  <!-- mobile broadband information -->
  <xs:complexType name="MobileBroadbandInfoType">
    <xs:sequence>
      <xs:element name="NetworkConfiguration" type="tns:NetworkConfigType" minOccurs="0"/>
      <xs:element name="ProvisioningEngine" type="tns:ProvisioningEngineType" minOccurs="0"/>
      <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded"/>
    </xs:sequence>
  </xs:complexType>

  <!-- data for network configuration -->
  <xs:complexType name="NetworkConfigType">
    <xs:sequence>
      <xs:element name="MobileBroadbandProfiles" type="tns:MobileBroadbandProfilesType" minOccurs="0"/>
      <xs:element name="AllowStandardUserPinUnlock" type="xs:boolean" minOccurs="0"/>
      <xs:element name="AllowTethering" type="tns:TetheringAllowedType" minOccurs="0"/>
      <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded"/>
    </xs:sequence>
  </xs:complexType>

  <!-- mobile broadband profiles -->
  <xs:complexType name="MobileBroadbandProfilesType">
    <xs:sequence>
      <xs:element name="Purchase" type="tns:FileType" minOccurs="0"/>
      <xs:element name="Internet" type="tns:FileType" minOccurs="0"/>
      <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded"/>
    </xs:sequence>
  </xs:complexType>

  <!-- file name without path -->
  <!-- allowed characters: unicode letters, unicode digits, ascii period, ascii dash, ascii underscore, ascii space -->
  <xs:simpleType name="FileType">
    <xs:restriction base="xs:string">
      <xs:whiteSpace value="preserve"/>
      <xs:pattern value="[\p{L}\p{N}\.\-_ ]+" />  <!-- XML schema always implicitly anchors the entire regular expression -->
      <xs:minLength value="1"/>
      <xs:maxLength value="260"/>
    </xs:restriction>
  </xs:simpleType>

  <!-- data for the provisioning engine -->
  <xs:complexType name="ProvisioningEngineType">
    <xs:sequence>
      <xs:element name="TrustedCertificates" type="tns:TrustedCertificateListType" minOccurs="0"/>
      <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded"/>
    </xs:sequence>
  </xs:complexType>

  <!-- list of trusted provisioning signing certificates -->
  <xs:complexType name="TrustedCertificateListType">
    <xs:sequence>
      <xs:element name="TrustedCertificate" type="tns:TrustedCertificateType" minOccurs="0" maxOccurs="256"/>
      <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded"/>
    </xs:sequence>
  </xs:complexType>

  <!-- a single trusted provisioning signing certificate -->
  <xs:complexType name="TrustedCertificateType">
    <xs:sequence>
      <xs:element name="SubjectName" type="xs:string" />
      <xs:element name="IssuerName" type="xs:string" />
      <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
  </xs:complexType>

</xs:schema>
```

 

 





