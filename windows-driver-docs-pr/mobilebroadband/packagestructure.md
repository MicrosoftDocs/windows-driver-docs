---
title: PackageStructure
description: PackageStructure
ms.date: 04/20/2017
---

# PackageStructure

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

The PackageStructure element specifies the XML schemas that are referenced by the service metadata package. Each XML schema is specified through the [Metadata](metadata-service-schema.md) element.

## Usage


``` syntax
<PackageStructure>
  text
  child elements
</PackageStructure>
```

## Attributes


There are no attributes.

## Text value


Four or more [Metadata](metadata-service-schema.md) elements are required.

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
<td><p><a href="metadata-service-schema.md" data-raw-source="[Metadata](metadata-service-schema.md)">Metadata</a></p></td>
<td><p>The <a href="metadata-service-schema.md" data-raw-source="[Metadata](metadata-service-schema.md)">Metadata</a> element specifies the XML schemas that are referenced through the device metadata package.</p></td>
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
<xs:element name="PackageStructure" type="tns:PackageStructureType" />

<xs:complexType name="PackageStructureType">
  <xs:sequence>
    <xs:element name="Metadata" type="tns:MetadataType" minOccurs="2" maxOccurs="unbounded" />
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
  </xs:sequence>
</xs:complexType>
```

## Remarks


A minimum of four instances of the [Metadata](metadata-service-schema.md) element must be specified within the PackageStructure element. Each instance must specify one of the required XML schemas that are used to create a service metadata package:

-   [PackageInfo XML schema](packageinfo-xml-schema.md)

-   [ServiceInfo XML schema](serviceinfo-xml-schema.md)

-   [SoftwareInfo XML schema](softwareinfo-xml-schema.md)

-   [MobileBroadbandInfo XML schema](mobilebroadbandinfo-xml-schema.md)

The PackageStructure element is required.

 

 





