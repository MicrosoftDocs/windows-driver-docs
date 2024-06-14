---
title: HardwareIdList (PackageInfo)
description: HardwareIdList (PackageInfo)
ms.date: 04/20/2017
---

# HardwareIdList (PackageInfo)

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

The HardwareIDList element specifies one or more hardware identification strings for the service metadata package. Each string is specified by a [HardwareID](hardwareid.md) element.

## Usage


``` syntax
<HardwareIDList>
  child elements
</HardwareIDList>
```

## Attributes


There are no attributes.

## Text value


Must contain one or more [HardwareID](hardwareid.md) elements.

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
<td><p><a href="hardwareid.md" data-raw-source="[HardwareID](hardwareid.md)">HardwareID</a></p></td>
<td><p>The <a href="hardwareid.md" data-raw-source="[HardwareID](hardwareid.md)">HardwareID</a> elements represent the mobile network operator.</p></td>
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
<td><p><a href="metadatakey.md" data-raw-source="[MetadataKey](metadatakey.md)">MetadataKey</a></p></td>
<td><p>The <a href="metadatakey.md" data-raw-source="[MetadataKey](metadatakey.md)">MetadataKey</a> element specifies the attributes of the device metadata package. These include the following:</p>
<ul>
<li><p>The identifier for each hardware function supported by the device.</p></li>
<li><p>The language-specific locale for the text strings within the package.</p></li>
</ul></td>
</tr>
</tbody>
</table>

 

## XSD


``` syntax
<xs:element name="HardwareIDList" type="tns:HardwareIDListType" />

<xs:complexType name="HardwareIDListType">
  <xs:sequence>
    <xs:element name="HardwareID" type="tns:HardwareIDType" maxOccurs="unbounded" />
  </xs:sequence>
</xs:complexType>
```

## Remarks


The HardwareIDList element is required.

 

 





