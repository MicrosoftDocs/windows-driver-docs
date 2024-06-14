---
title: PackageInfo
description: PackageInfo
ms.date: 04/20/2017
---

# PackageInfo

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

The PackageInfo element is the parent element of the [PackageInfo XML schema](packageinfo-xml-schema.md). The child elements of the PackageInfo element specify the attributes of the service metadata package.

## Usage


``` syntax
<PackageInfo>
  child elements
</PackageInfo>
```

## Attributes


There are no attributes.

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
<td><p><a href="metadatabuilderinformation.md" data-raw-source="[MetadataBuilderInformation](metadatabuilderinformation.md)">MetadataBuilderInformation</a></p></td>
<td><p>The <a href="metadatabuilderinformation.md" data-raw-source="[MetadataBuilderInformation](metadatabuilderinformation.md)">MetadataBuilderInformation</a> element specifies information about the application that created the service metadata package.</p></td>
</tr>
<tr class="even">
<td><p><a href="metadatakey.md" data-raw-source="[MetadataKey](metadatakey.md)">MetadataKey</a></p></td>
<td><p>The <a href="metadatakey.md" data-raw-source="[MetadataKey](metadatakey.md)">MetadataKey</a> element specifies the attributes of the service metadata package. These include the following:</p>
<ul>
<li><p>The identifier for each hardware function supported by the device.</p></li>
<li><p>The language-specific locale for the text strings within the package.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p><a href="packagestructure.md" data-raw-source="[PackageStructure](packagestructure.md)">PackageStructure</a></p></td>
<td><p>The <a href="packagestructure.md" data-raw-source="[PackageStructure](packagestructure.md)">PackageStructure</a> element specifies the XML schemas which are referenced by the service metadata package.</p></td>
</tr>
<tr class="even">
<td><p><a href="relationships.md" data-raw-source="[Relationships](relationships.md)">Relationships</a></p></td>
<td><p>The <a href="relationships.md" data-raw-source="[Relationships](relationships.md)">Relationships</a> element, through its child elements, specifies data that is used to track a service metadata package within the device metadata cache.</p></td>
</tr>
</tbody>
</table>

 

## Parent elements


There are no parent elements.

## XSD


``` syntax
<xs:element name="PackageInfo" type="tns:PackageInfoType" />

<xs:complexType name="PackageInfoType">
  <xs:sequence>
    <xs:element name="MetadataKey" type="tns:MetadataKeyType" />
    <xs:element name="PackageStructure" type="tns:PackageStructureType" />
    <xs:element name="Relationships" type="tns:RelationshipsType" minOccurs="0" />
    <xs:element name="MetadataBuilderInformation" type="tns:MetadataBuilderInformationType" minOccurs="0" />
    <xs:any namespace="##other" processContents="lax" minOccurs="0"
      maxOccurs="unbounded" />
  </xs:sequence>
</xs:complexType>
```

## Remarks


The PackageInfo element must contain one instance of the [MetadataKey](metadatakey.md), [PackageStructure](packagestructure.md), and [Relationships](relationships.md) elements.

 

 





