---
title: MobileBroadbandProfiles
description: MobileBroadbandProfiles
ms.date: 04/20/2017
---

# MobileBroadbandProfiles

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

The MobileBroadbandProfiles element specifies the purchase and Internet mobile broadband profile files to use.

## Usage


``` syntax
<MobileBroadbandProfiles>
  child elements
</MobileBroadbandProfiles>
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
<td><p><a href="purchase.md" data-raw-source="[Purchase](purchase.md)">Purchase</a></p></td>
<td><p>Specifies the purchase mobile broadband profile file to use.</p></td>
</tr>
<tr class="even">
<td><p><a href="internet.md" data-raw-source="[Internet](internet.md)">Internet</a></p></td>
<td><p>Specifies the Internet mobile broadband profile file to use.</p></td>
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
<td><p><a href="networkconfiguration.md" data-raw-source="[NetworkConfiguration](networkconfiguration.md)">NetworkConfiguration</a></p></td>
<td><p>Specifies the purchase and Internet mobile broadband profiles to be used or whether standard user can perform PIN unlock operations.</p></td>
</tr>
</tbody>
</table>

 

## XSD


``` syntax
<xs:element name="MobileBroadbandProfiles" type="tns:MobileBroadbandProfilesType" minOccurs="0" />

<xs:complexType name="MobileBroadbandProfilesType">
  <xs:sequence>
    <xs:element name="Purchase" type="tns:FileType" minOccurs="0" />
    <xs:element name="Internet" type="tns:FileType" minOccurs="0" />
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
  </xs:sequence>
</xs:complexType>
```

## Remarks


The MobileBroadbandProfiles element is optional.

 

 





