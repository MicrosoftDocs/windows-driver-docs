---
title: MobileBroadbandInfo
description: MobileBroadbandInfo
ms.assetid: 02279e23-becd-49ef-8981-6afb8e5aab91
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MobileBroadbandInfo

[!include[MBAE deprecation warning](mbae-deprecation-warning.md)]

The MobileBroadbandInfo element is the parent element of the [MobileBroadbandInfo XML schema](mobilebroadbandinfo-xml-schema.md).

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<MobileBroadbandInfo>
  child elements
</MobileBroadbandInfo>
```

## <span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes


There are no attributes.

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
<td><p><a href="networkconfiguration.md" data-raw-source="[NetworkConfiguration](networkconfiguration.md)">NetworkConfiguration</a></p></td>
<td><p>The <a href="networkconfiguration.md" data-raw-source="[NetworkConfiguration](networkconfiguration.md)">NetworkConfiguration</a> element specifies the purchase and Internet mobile broadband profiles to be used.</p></td>
</tr>
<tr class="even">
<td><p><a href="provisioningengine.md" data-raw-source="[ProvisioningEngine](provisioningengine.md)">ProvisioningEngine</a></p></td>
<td><p>The <a href="provisioningengine.md" data-raw-source="[ProvisioningEngine](provisioningengine.md)">ProvisioningEngine</a> element specifies trusted certificate values for Subject Name and Issuer Name.</p></td>
</tr>
</tbody>
</table>

 

## <span id="Parent_elements"></span><span id="parent_elements"></span><span id="PARENT_ELEMENTS"></span>Parent elements


There are no parent elements.

## <span id="XSD"></span><span id="xsd"></span>XSD


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

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


The MobileBroadbandInfo element is required.

 

 





