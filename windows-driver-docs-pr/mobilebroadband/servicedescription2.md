---
title: ServiceDescription2
description: ServiceDescription2
ms.date: 04/20/2017
---

# ServiceDescription2

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

The ServiceDescription2 element is not currently used.

## Usage


``` syntax
<ServiceDescription2>
  text
</ServiceDescription2>
```

## Attributes


There are no attributes.

## Text value


A string that is less than 1024 characters in length.

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
<xs:element name="ServiceDescription2" type="tns:ServiceDescriptionType" minOccurs="0"/>

<xs:simpleType name="ServiceDescriptionType">
  <xs:restriction base="xs:string">
    <xs:minLength value="1"/>
    <xs:maxLength value="1024"/>
  </xs:restriction>
</xs:simpleType>
```

## Remarks


The ServiceDescription2 is not currently used.

 

 





