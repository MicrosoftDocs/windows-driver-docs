---
title: MobileBroadbandInfo
description: MobileBroadbandInfo
ms.date: 04/20/2017
---

# MobileBroadbandInfo

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

The MobileBroadbandInfo element is the parent element of the [MobileBroadbandInfo XML schema](mobilebroadbandinfo-xml-schema.md).

## Usage


``` syntax
<MobileBroadbandInfo>
  child elements
</MobileBroadbandInfo>
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
<td><p><a href="networkconfiguration.md" data-raw-source="[NetworkConfiguration](networkconfiguration.md)">NetworkConfiguration</a></p></td>
<td><p>The <a href="networkconfiguration.md" data-raw-source="[NetworkConfiguration](networkconfiguration.md)">NetworkConfiguration</a> element specifies the purchase and Internet mobile broadband profiles to be used.</p></td>
</tr>
<tr class="even">
<td><p><a href="provisioningengine.md" data-raw-source="[ProvisioningEngine](provisioningengine.md)">ProvisioningEngine</a></p></td>
<td><p>The <a href="provisioningengine.md" data-raw-source="[ProvisioningEngine](provisioningengine.md)">ProvisioningEngine</a> element specifies trusted certificate values for Subject Name and Issuer Name.</p></td>
</tr>
</tbody>
</table>

 

## Parent elements


There are no parent elements.

## XSD


``` syntax
<xs:element name="MobileBroadbandInfo" type="tns:MobileBroadbandInfoType" />

<xs:complexType name="MobileBroadbandInfoType">
  <xs:sequence>
    <xs:element name="NetworkConfiguration" type="tns:NetworkConfigType" minOccurs="0" />
    <xs:element name="ProvisioningEngine" type="tns:ProvisioningEngineType" minOccurs="0" />
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
  </xs:sequence>
</xs:complexType>
```

## Remarks


The MobileBroadbandInfo element is required.

 

 





