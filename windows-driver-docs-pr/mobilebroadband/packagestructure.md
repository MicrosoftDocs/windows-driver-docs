---
title: PackageStructure
description: PackageStructure
ms.assetid: 44be9d7d-79b0-49b6-b427-e729efadb88c
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PackageStructure

[!include[MBAE deprecation warning](mbae-deprecation-warning.md)]

The PackageStructure element specifies the XML schemas that are referenced by the service metadata package. Each XML schema is specified through the [Metadata](metadata-service-schema.md) element.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<PackageStructure>
  text
  child elements
</PackageStructure>
```

## <span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes


There are no attributes.

## <span id="Text_value"></span><span id="text_value"></span><span id="TEXT_VALUE"></span>Text value


Four or more [Metadata](metadata-service-schema.md) elements are required.

## <span id="Child_elements"></span><span id="child_elements"></span><span id="CHILD_ELEMENTS"></span>Child elements


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

 

## <span id="Parent_elements"></span><span id="parent_elements"></span><span id="PARENT_ELEMENTS"></span>Parent elements


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

 

## <span id="XSD"></span><span id="xsd"></span>XSD


``` syntax
<xs:element name="PackageStructure" type="tns:PackageStructureType" />

<xs:complexType name="PackageStructureType">
  <xs:sequence>
    <xs:element name="Metadata" type="tns:MetadataType" minOccurs="2" maxOccurs="unbounded" />
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
  </xs:sequence>
</xs:complexType>
```

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


A minimum of four instances of the [Metadata](metadata-service-schema.md) element must be specified within the PackageStructure element. Each instance must specify one of the required XML schemas that are used to create a service metadata package:

-   [PackageInfo XML schema](packageinfo-xml-schema.md)

-   [ServiceInfo XML schema](serviceinfo-xml-schema.md)

-   [SoftwareInfo XML schema](softwareinfo-xml-schema.md)

-   [MobileBroadbandInfo XML schema](mobilebroadbandinfo-xml-schema.md)

The PackageStructure element is required.

 

 





