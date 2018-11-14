---
title: ServiceSpecificExtension
description: ServiceSpecificExtension
ms.assetid: 49c8e902-d943-4884-96e4-c5472a82b568
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ServiceSpecificExtension

[!include[MBAE deprecation warning](mbae-deprecation-warning.md)]

The ServiceSpecificExtension element specifies the relative location of the MobileBroadbandInfo.xml file.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<ServiceSpecificExtension 
  name = “xs:anyURI”>
  text
</ServiceSpecificExtension>
```

## <span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes


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

 

## <span id="Text_value"></span><span id="text_value"></span><span id="TEXT_VALUE"></span>Text value


The name of the XML file that contains the MobileBroadbandInfo schema.

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
<xs:element name="ServiceSpecificExtension" type="tns:ServiceSpecificExtensionType" minOccurs="0" />

<xs:complexType name="ServiceSpecificExtensionType">
  <xs:simpleContent>
    <xs:extension base="xs:string">
      <xs:attribute name="namespace" type="xs:anyURI" use="required" />
    </xs:extension>
  </xs:simpleContent>
</xs:complexType>
```

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


The ServiceSpecificExtension element is required.

 

 





