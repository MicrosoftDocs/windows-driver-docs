---
title: PackageInfo XML schema definition
description: PackageInfo XML schema definition
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: b0e4f800-816a-4d8b-a68b-56dc468caf52
---

# PackageInfo XML schema definition


The following is the namespace of the PackageInfo XML schema:

``` syntax
http://schemas.microsoft.com/windows/DeviceMetadata/PackageInfo/2007/11/
http://schemas.microsoft.com/windows/2010/08/DeviceMetadata/PackageInfov2
```

The following is a definition of the PackageInfo schema.

``` syntax
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema targetNamespace="http://schemas.microsoft.com/windows/DeviceMetadata/PackageInfo/2007/11/"
           xmlns:v2=http://schemas.microsoft.com/windows/2010/08/DeviceMetadata/PackageInfov2
           xmlns:tns="http://schemas.microsoft.com/windows/DeviceMetadata/PackageInfo/2007/11/"
           xmlns:xs="http://www.w3.org/2001/XMLSchema"
           elementFormDefault="qualified"
           blockDefault="#all">

<xs:import namespace="http://schemas.microsoft.com/windows/2010/08/DeviceMetadata/PackageInfov2" schemaLocation="PackageInfov2.xsd" />

  <xs:element name="PackageInfo" type="tns:PackageInfoType" />

  <xs:complexType name="PackageInfoType">
    <xs:sequence>
      <xs:element name="MetadataKey" type="tns:MetadataKeyType" />
      <xs:element name="PackageStructure" type="tns:PackageStructureType" />
      <xs:element name="Relationships" type="tns:RelationshipsType" minOccurs="0" />
      <xs:element name="MetadataBuilderInformation" type="tns:MetadataBuilderInformationType" minOccurs="0" />
      <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="MetadataKeyType">
    <xs:sequence>
      <xs:choice>
        <xs:sequence>
         <xs:element name="HardwareIDList" type="tns:HardwareIDListType" />
         <xs:element name="ModelIDList" type="tns:ModelIDListType" minOccurs="0" />
        </xs:sequence>
        <xs:element name="ModelIDList" type="tns:ModelIDListType" />
      </xs:choice>
      <xs:element name="Locale" type="tns:LocaleType" />
      <xs:element name="LastModifiedDate" type="xs:dateTime" />
      <xs:element ref="v2:MultipleLocale" minOccurs="0" />
      <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="ModelIDListType">
    <xs:sequence>
      <xs:element name="ModelID" type="tns:GUIDType" maxOccurs="unbounded" />
    </xs:sequence>
  </xs:complexType>

  <xs:simpleType name="GUIDType">
    <xs:restriction base="xs:string">
      <xs:pattern value= "[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}" />
    </xs:restriction>
  </xs:simpleType>

  <xs:complexType name="HardwareIDListType">
    <xs:sequence>
      <xs:element name="HardwareID" type="tns:HardwareIDType" maxOccurs="unbounded" />
    </xs:sequence>
  </xs:complexType>

  <xs:simpleType name="HardwareIDType">
    <xs:restriction base="xs:string">
      <xs:minLength value="1" />
      <xs:maxLength value="207" />
      <xs:pattern value="^([a-zA-Z0-9!#$%&amp;()*+\-./:;&lt;=&gt;?@[\\\]^_`{|}~])*$" /> 
    </xs:restriction>
  </xs:simpleType>

  <xs:complexType name="LocaleType">
    <xs:simpleContent>
      <xs:extension base="xs:string">
        <xs:attribute name="default" type="xs:boolean" use="required" />
      </xs:extension>
    </xs:simpleContent>
  </xs:complexType>

  <xs:complexType name="PackageStructureType">
    <xs:sequence>
      <xs:element name="Metadata" type="tns:MetadataType" minOccurs="2" maxOccurs="unbounded" />
      <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="MetadataType">
    <xs:simpleContent>
      <xs:extension base="xs:string">
        <xs:attribute name="MetadataID" type="xs:anyURI" use="required" />
      </xs:extension>
    </xs:simpleContent>
  </xs:complexType>

  <xs:complexType name="RelationshipsType">
    <xs:sequence>
      <xs:element name="ExperienceID" type="tns:GUIDType" minOccurs="0" />
      <xs:element name="LanguageNeutralIdentifier" type="tns:GUIDType" minOccurs="0" />
      <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded"
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="MetadataBuilderInformationType">
    <xs:sequence>
      <xs:element name="Application" type="tns:ApplicationType" />
      <xs:element name="Version" type="tns:VersionType" />
      <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
  </xs:complexType>

  <xs:simpleType name="ApplicationType">
    <xs:restriction base="xs:string">
      <xs:minLength value="1" />
      <xs:maxLength value="256" />
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="VersionType">
    <xs:restriction base="xs:string">
      <xs:minLength value="1" />
      <xs:maxLength value="256" />
    </xs:restriction>
  </xs:simpleType>
</xs:schema>
```

The following is the PackageInfo v2 XML schema metadata (packageinfov2.xsd):

``` syntax
<?xml version="1.0" encoding="UTF-8"?>

<xs:schema targetNamespace="http://schemas.microsoft.com/windows/2010/08/DeviceMetadata/PackageInfov2"
           xmlns:tns="http://schemas.microsoft.com/windows/2010/08/DeviceMetadata/PackageInfov2"
           xmlns:xs="http://www.w3.org/2001/XMLSchema"
           elementFormDefault="qualified"
           blockDefault="#all">

<xs:element name="MultipleLocale" type ="xs:boolean" />

</xs:schema>
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20PackageInfo%20XML%20schema%20definition%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




