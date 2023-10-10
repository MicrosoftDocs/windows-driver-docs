---
title: ServiceSpecificExtension
description: ServiceSpecificExtension
ms.date: 04/20/2017
---

# ServiceSpecificExtension

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

The ServiceSpecificExtension element specifies the relative location of the MobileBroadbandInfo.xml file.

## Usage


``` syntax
<ServiceSpecificExtension 
  name = “xs:anyURI”>
  text
</ServiceSpecificExtension>
```

## Attributes


<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>namespace</p></td>
<td><p>xs:anyURI</p></td>
<td><p>Yes</p></td>
<td><p>The URI of the namespace that is used for the MobileBroadbandInfo.xml file.</p></td>
</tr>
</tbody>
</table>

 

## Text value


The name of the XML file that contains the MobileBroadbandInfo schema.

## Child elements


There are no child elements.

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
<td><p><a href="serviceinfo.md" data-raw-source="[ServiceInfo](serviceinfo.md)">ServiceInfo</a></p></td>
<td><p>The <a href="serviceinfo.md" data-raw-source="[ServiceInfo](serviceinfo.md)">ServiceInfo</a> element is the parent element of the <a href="serviceinfo-xml-schema.md" data-raw-source="[ServiceInfo XML schema](serviceinfo-xml-schema.md)">ServiceInfo XML schema</a>.</p></td>
</tr>
</tbody>
</table>

 

## XSD


``` syntax
<xs:element name="ServiceSpecificExtension" type="tns:ServiceSpecificExtensionType" minOccurs="0" />

<xs:complexType name="ServiceSpecificExtensionType">
  <xs:simpleContent>
    <xs:extension base="xs:string">
      <xs:attribute name="namespace" type="xs:anyURI" use="required" />
    </xs:extension>
  </xs:simpleContent>
</xs:complexType>
```

## Remarks


The ServiceSpecificExtension element is required.

 

 





