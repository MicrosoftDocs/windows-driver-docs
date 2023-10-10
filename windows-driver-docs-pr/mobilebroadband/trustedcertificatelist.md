---
title: TrustedCertificateList
description: TrustedCertificateList
ms.date: 04/20/2017
---

# TrustedCertificateList


The TrustedCertificateList element specifies a list of trusted certificates for the operator.

## Usage


``` syntax
<TrustedCertificateList>
   child elements
</TrustedCertificateList>
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
<td><p><a href="trustedcertificate-apnxml.md" data-raw-source="[TrustedCertificate](trustedcertificate-apnxml.md)">TrustedCertificate</a></p></td>
<td><p>A certificate trusted by the operator.</p></td>
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
<td><p><a href="operatorlist.md" data-raw-source="[OperatorList](operatorlist.md)">OperatorList</a></p></td>
<td><p>The parent element of the <a href="apn-schema-definition.md" data-raw-source="[APN XML schema](apn-schema-definition.md)">APN XML schema</a>.</p></td>
</tr>
</tbody>
</table>

 

## XSD


``` syntax
<xs:element ref="TrustedCertificateList" minOccurs="0"/>

<xs:element name="TrustedCertificateList">
  <xs:complexType>
    <xs:sequence>
      <xs:element ref="TrustedCertificate" maxOccurs="unbounded"/>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```

## Remarks


The TrustedCertificateList element is optional.

 

 





