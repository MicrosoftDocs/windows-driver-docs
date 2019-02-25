---
title: HardwareIdList (PackageInfo)
description: HardwareIdList (PackageInfo)
ms.assetid: 32bd11f8-767f-4082-b753-efa9debf23cc
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# HardwareIdList (PackageInfo)

[!include[MBAE deprecation warning](mbae-deprecation-warning.md)]

The HardwareIDList element specifies one or more hardware identification strings for the service metadata package. Each string is specified by a [HardwareID](hardwareid.md) element.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<HardwareIDList>
  child elements
</HardwareIDList>
```

## <span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes


There are no attributes.

## <span id="Text_value"></span><span id="text_value"></span><span id="TEXT_VALUE"></span>Text value


Must contain one or more [HardwareID](hardwareid.md) elements.

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
<td><p><a href="hardwareid.md" data-raw-source="[HardwareID](hardwareid.md)">HardwareID</a></p></td>
<td><p>The <a href="hardwareid.md" data-raw-source="[HardwareID](hardwareid.md)">HardwareID</a> elements represent the mobile network operator.</p></td>
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
<td><p><a href="metadatakey.md" data-raw-source="[MetadataKey](metadatakey.md)">MetadataKey</a></p></td>
<td><p>The <a href="metadatakey.md" data-raw-source="[MetadataKey](metadatakey.md)">MetadataKey</a> element specifies the attributes of the device metadata package. These include the following:</p>
<ul>
<li><p>The identifier for each hardware function supported by the device.</p></li>
<li><p>The language-specific locale for the text strings within the package.</p></li>
</ul></td>
</tr>
</tbody>
</table>

 

## <span id="XSD"></span><span id="xsd"></span>XSD


``` syntax
<xs:element name="HardwareIDList" type="tns:HardwareIDListType" />

<xs:complexType name="HardwareIDListType">
  <xs:sequence>
    <xs:element name="HardwareID" type="tns:HardwareIDType" maxOccurs="unbounded" />
  </xs:sequence>
</xs:complexType>
```

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


The HardwareIDList element is required.

 

 





