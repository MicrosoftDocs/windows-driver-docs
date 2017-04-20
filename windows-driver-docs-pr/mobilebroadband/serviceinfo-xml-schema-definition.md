---
title: ServiceInfo XML Schema Definition
description: ServiceInfo XML Schema Definition
ms.assetid: c5d6aa78-b494-4931-bdfc-6acaab5c570f
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# ServiceInfo XML Schema Definition


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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20ServiceInfo%20XML%20Schema%20Definition%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




