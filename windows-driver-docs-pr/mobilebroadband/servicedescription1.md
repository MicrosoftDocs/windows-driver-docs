---
title: ServiceDescription1
description: ServiceDescription1
ms.date: 04/20/2017
---

# ServiceDescription1

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

The ServiceDescription1 element specifies descriptive information about the service. This is applied to the description field of the wireless wide area network (WWAN) connection profile. It is not displayed in the user interface to the end user and should be left blank.

## Usage


``` syntax
<ServiceDescription1>
  text
</ServiceDescription1>
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
<xs:element name="ServiceDescription1" type="tns:ServiceDescriptionType" minOccurs="0"/>

<xs:simpleType name="ServiceDescriptionType">
  <xs:restriction base="xs:string">
    <xs:minLength value="1"/>
    <xs:maxLength value="1024"/>
  </xs:restriction>
</xs:simpleType>
```

## Remarks


The ServiceDescription1 element does not appear to the end user in any user interface.

The ServiceDescription1 element is optional and should be left blank.

 

 





