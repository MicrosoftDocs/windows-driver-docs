---
title: ServiceInfo XML Schema Definition
description: ServiceInfo XML Schema Definition
ms.assetid: c5d6aa78-b494-4931-bdfc-6acaab5c570f
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ServiceInfo XML Schema Definition

[!include[MBAE deprecation warning](mbae-deprecation-warning.md)]

The following is the namespace of the ServiceInfo XML schema:

``` syntax
http://schemas.microsoft.com/windows/2010/05/DeviceMetadata/ServiceInfo
```

The following is a definition of the ServiceInfo schema.

``` syntax
<?xml version="1.0" encoding ="UTF-8" ?>
  <xs:schema targetNamespace="http://schemas.microsoft.com/windows/2010/05/DeviceMetadata/ServiceInfo"
             xmlns:tns="http://schemas.microsoft.com/windows/2010/05/DeviceMetadata/ServiceInfo"
             xmlns:xs="http://www.w3.org/2001/XMLSchema"
             elementFormDefault="qualified"
             blockDefault="#all">

    <xs:element name="ServiceInfo" type="tns:ServiceInfoType" />

    <xs:complexType name="ServiceInfoType">
      <xs:sequence>
        <xs:element name="ServiceCategoryList" type="tns:ServiceCategoryListType" />
        <xs:element name="ServiceName" type="tns:ServiceNameType" minOccurs="0" />
        <xs:element name="ServiceDescription1" type="tns:ServiceDescriptionType" minOccurs="0" />
        <xs:element name="ServiceDescription2" type="tns:ServiceDescriptionType" minOccurs="0" />
        <xs:element name="ServiceNumber" type ="tns:ServiceNumberType" />
        <xs:element name="ServiceProvider" type="tns:ProviderNameType" />
        <xs:element name="ServiceIconFile" type="tns:ServiceIconFileType" minOccurs="0" />
        <xs:element name="ServiceSpecificExtension" type="tns:ServiceSpecificExtensionType" minOccurs="0" />
        <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
      </xs:sequence>
    </xs:complexType>

    <xs:complexType name="ServiceCategoryListType">
      <xs:sequence>
        <xs:element name="ServiceCategory" type="tns:ServiceCategoryType" maxOccurs="unbounded" />
        <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
      </xs:sequence>
    </xs:complexType>

    <xs:simpleType name="ServiceCategoryType">
      <xs:union memberTypes="tns:ServiceCategoryTypeEnumeration xs:string" />
    </xs:simpleType>

    <xs:simpleType name="ServiceCategoryTypeEnumeration">
      <xs:restriction base="xs:string" >
        <xs:enumeration value="Network" />
        <xs:enumeration value="Network.MobileBroadband" />
        <xs:enumeration value="Other" />
      </xs:restriction>
    </xs:simpleType>

    <xs:simpleType name="ServiceNameType">
      <xs:restriction base="xs:string">
        <xs:minLength value="0" />
        <xs:maxLength value="200" />
      </xs:restriction>
    </xs:simpleType>

    <xs:simpleType name="ServiceNumberType">
      <xs:union memberTypes="tns:GUIDType xs:string" />
    </xs:simpleType>

    <xs:simpleType name="ProviderNameType">
      <xs:restriction base="xs:string">
        <xs:minLength value="1" />
        <xs:maxLength value="20" />
      </xs:restriction>
    </xs:simpleType>

    <xs:simpleType name="ServiceDescriptionType">
      <xs:restriction base="xs:string">
        <xs:minLength value="1" />
        <xs:maxLength value="1024" />
      </xs:restriction>
    </xs:simpleType>

    <xs:simpleType name="ServiceIconFileType">
      <xs:restriction base="xs:string">
        <xs:pattern value=".+\.ico" />
      </xs:restriction>
    </xs:simpleType>

    <xs:simpleType name="GUIDType">
      <xs:restriction base="xs:string">
        <xs:pattern value="[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}" />
      </xs:restriction>
    </xs:simpleType>

    <xs:complexType name="ServiceSpecificExtensionType">
      <xs:simpleContent>
        <xs:extension base="xs:string">
          <xs:attribute name="namespace" type="xs:anyURI" use="required" />
        </xs:extension>
      </xs:simpleContent>
    </xs:complexType>

</xs:schema>
```

 

 





