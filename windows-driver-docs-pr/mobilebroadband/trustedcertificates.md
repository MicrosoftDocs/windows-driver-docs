---
title: TrustedCertificates
description: TrustedCertificates
ms.assetid: f035a453-d767-4cb5-b556-dfcf7b0b1962
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# TrustedCertificates

[!include[MBAE deprecation warning](mbae-deprecation-warning.md)]

The TrustedCertificates element specifies a list of trusted certificates.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<TrustedCertificates>
  child elements
</TrustedCertificates>
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
<td><p><a href="trustedcertificate.md" data-raw-source="[TrustedCertificate](trustedcertificate.md)">TrustedCertificate</a></p></td>
<td><p>Specifies the trusted certificate.</p></td>
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
<td><p><a href="provisioningengine.md" data-raw-source="[ProvisioningEngine](provisioningengine.md)">ProvisioningEngine</a></p></td>
<td><p>Specifies the trusted certificates.</p></td>
</tr>
</tbody>
</table>

 

## <span id="XSD"></span><span id="xsd"></span>XSD


``` syntax
<xs:element name="TrustedCertificates" type="tns:TrustedCertificateListType" minOccurs="0" />

<xs:complexType name="TrustedCertificateListType">
  <xs:sequence>
    <xs:element name="TrustedCertificate" type="tns:TrustedCertificateType" minOccurs="0" maxOccurs="256" />
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
  </xs:sequence>
</xs:complexType>
```

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


The TrustedCertificates element is optional.

 

 





