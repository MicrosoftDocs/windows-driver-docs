---
title: Metadata
description: Metadata
ms.date: 04/20/2017
---

# Metadata

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

The Metadata element specifies the namespaces of the XML schemas that are referenced in the service metadata package.

## Usage

``` syntax
<Metadata
  MetadataID = "xs:anyURI">
  text
</Metadata>
```

## Attributes

|Attribute|Type|Required|Description|
|----|----|----|----|
|MetadataID|xs:anyURI|Yes|Specifies the namespace of an XML schema that is referenced within the service metadata package.|

## Text value

The Uniform Resource Identifier (URI) of the namespace of a service metadata XML schema. The XML schema must be one of the schemas referenced within the services metadata package.

## Child elements

There are no child elements.

## Parent elements

|Element|Description|
|----|----|
|[PackageStructure](packagestructure.md)|The [PackageStructure](packagestructure.md) element specifies the XML schemas which are referenced by the service metadata package.|

## XSD

``` syntax
<xs:element name="PackageStructure" type="tns:PackageStructureType" />

<xs:complexType name="PackageStructureType">
   <xs:sequence>
     <xs:element name="Metadata" type="tns:MetadataType" minOccurs="3" maxOccurs="unbounded" />
   </xs:sequence>
</xs:complexType>

<xs:complexType name="MetadataType">
  <xs:simpleContent>
    <xs:extension base="xs:string">
      <xs:attribute name="MetadataID" type="xs:anyURI" use="required" />
    </xs:extension>
  </xs:simpleContent>
</xs:complexType>
```

## Remarks

In the [PackageInfo](packageinfo.md) element, a minimum of two instances of the Metadata element must be specified. Each instance must specify the namespace of one of the following required XML schemas that are used to create a service metadata package:

- [PackageInfo XML schema](packageinfo-xml-schema.md)

- [ServiceInfo XML schema](serviceinfo-xml-schema.md)

- [WindowsInfo XML schema](windowsinfo-xml-schema.md)

- [SoftwareInfo XML schema](softwareinfo-xml-schema.md)

The easiest approach is to copy the following example above into your Packageinfo.xml file. If any of the folders specified above are not included in the service metadata package, make sure to remove the Metadata element from the [PackageStructure](packagestructure.md) element.

``` syntax
<PackageStructure>
  <Metadata MetadataID="http://schemas.microsoft.com/windows/DeviceMetadata/PackageInfo/2007/11">PackageInfo.xml</Metadata>
  <Metadata MetadataID="http://schemas.microsoft.com/windows/2010/05/DeviceMetadata/ServiceInfo">ServiceInformation</Metadata>
  <Metadata MetadataID="http://schemas.microsoft.com/windows/DeviceMetadata/WindowsInfo/2007/11/">WindowsInformation</Metadata>
  <Metadata MetadataID="http://schemas.microsoft.com/windows/2010/08/DeviceMetadata/SoftwareInfo">SoftwareInformation</Metadata>
</PackageStructure>
```

The SoftwareInformation folder and service metadata packages are not supported on devices running Windows 7.

Each folder name can be changed to an arbitrary name as long as the name is set in this metadata element. The following example shows how to use “WindowsInfo” as a folder name:

``` syntax
<Metadata MetadataID="http://schemas.microsoft.com/windows/DeviceMetadata/WindowsInfo/2007/11/">WindowsInfo</Metadata>
```
