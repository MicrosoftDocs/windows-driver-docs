---
title: MetadataBuilderInformation
description: MetadataBuilderInformation
ms.date: 04/20/2017
---

# MetadataBuilderInformation

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

The MetadataBuilderInformation element specifies information about the application that created the device metadata package.

## Usage


``` syntax
<MetadataBuilderInformation>
  text
  child elements
</MetadataBuilderInformation>
```

## Attributes


There are no attributes.

## Text value


A string that contains between 1 and 256 printable characters inclusive.

## Child elements


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="application-service-schema.md" data-raw-source="[Application](application-service-schema.md)">Application</a></p></td>
<td><p>The <a href="application-service-schema.md" data-raw-source="[Application](application-service-schema.md)">Application</a> element specifies the name of the application software that created the service metadata package.</p></td>
</tr>
<tr class="even">
<td><p><a href="version.md" data-raw-source="[Version](version.md)">Version</a></p></td>
<td><p>The <a href="version.md" data-raw-source="[Version](version.md)">Version</a> element specifies the version of the application software that created the service metadata package.</p></td>
</tr>
</tbody>
</table>

 

## Parent elements


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="packageinfo.md" data-raw-source="[PackageInfo](packageinfo.md)">PackageInfo</a></p></td>
<td><p>The <a href="packageinfo.md" data-raw-source="[PackageInfo](packageinfo.md)">PackageInfo</a> element is the parent element of the <a href="packageinfo-xml-schema.md" data-raw-source="[PackageInfo XML schema](packageinfo-xml-schema.md)">PackageInfo XML schema</a>. The child elements of the PackageInfo element specify the attributes of the device metadata package.</p></td>
</tr>
</tbody>
</table>

 

## XSD


``` syntax
<xs:element name="MetadataBuilderInformation" type="tns:MetadataBuilderInformationType" minOccurs="0" /> 

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
```

## Remarks


The MetadataBuilderInformation element is not used by any component of the operating system. It is reserved for use by the OEM, IHV, and ISV.

 

 





