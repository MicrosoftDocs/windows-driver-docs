---
title: ServiceDescription2
description: ServiceDescription2
ms.assetid: 92de51be-dfd7-443b-987c-b4b364e1aaa6
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ServiceDescription2

[!include[MBAE deprecation warning](mbae-deprecation-warning.md)]

The ServiceDescription2 element is not currently used.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<ServiceDescription2>
  text
</ServiceDescription2>
```

## <span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes


There are no attributes.

## <span id="Text_value"></span><span id="text_value"></span><span id="TEXT_VALUE"></span>Text value


A string that is less than 1024 characters in length.

## <span id="Child_elements"></span><span id="child_elements"></span><span id="CHILD_ELEMENTS"></span>Child elements


There are no child elements.

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
<td><p><a href="serviceinfo.md" data-raw-source="[ServiceInfo](serviceinfo.md)">ServiceInfo</a></p></td>
<td><p>The <a href="serviceinfo.md" data-raw-source="[ServiceInfo](serviceinfo.md)">ServiceInfo</a> element is the parent element of the <a href="serviceinfo-xml-schema.md" data-raw-source="[ServiceInfo XML schema](serviceinfo-xml-schema.md)">ServiceInfo XML schema</a>.</p></td>
</tr>
</tbody>
</table>

 

## <span id="XSD"></span><span id="xsd"></span>XSD


``` syntax
<xs:element name="ServiceDescription2" type="tns:ServiceDescriptionType" minOccurs="0"/>

<xs:simpleType name="ServiceDescriptionType">
  <xs:restriction base="xs:string">
    <xs:minLength value="1"/>
    <xs:maxLength value="1024"/>
  </xs:restriction>
</xs:simpleType>
```

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


The ServiceDescription2 is not currently used.

 

 





