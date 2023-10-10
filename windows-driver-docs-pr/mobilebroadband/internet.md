---
title: Internet
description: Internet
ms.date: 04/20/2017
---

# Internet

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

The Internet element specifies the purchase mobile broadband profile file to use.

## Usage


``` syntax
<Internet>
  child element
</Internet>
```

## Attributes


There are no attributes.

## Text value


The name of a file in the ServiceInformation directory.

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
<td><p><a href="mobilebroadbandprofiles.md" data-raw-source="[MobileBroadbandProfiles](mobilebroadbandprofiles.md)">MobileBroadbandProfiles</a></p></td>
<td><p>Specifies the purchase and Internet mobile broadband profile files to use</p></td>
</tr>
</tbody>
</table>

 

## XSD


``` syntax
<xs:element name="Internet" type="tns:FileType" minOccurs="0"/>

<xs:simpleType name="FileType">
  <xs:restriction base="xs:string">
    <xs:whiteSpace value="preserve"/>
    <xs:pattern value="[\p{L}\p{N}\.\-_ ]+"/>
    <xs:minLength value="1"/>
    <xs:maxLength value="260"/>
  </xs:restriction>
</xs:simpleType>
```

## Remarks


The Internet element is optional.

 

 





