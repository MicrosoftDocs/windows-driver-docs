---
title: TrustedCertificate (MobileBroadbandInfo)
description: TrustedCertificate (MobileBroadbandInfo)
ms.date: 04/20/2017
---

# TrustedCertificate (MobileBroadbandInfo)

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

The TrustedCertificate element specifies the Subject Name and Issuer name of a trusted certificate.

## Usage


``` syntax
<TrustedCertificate>
  child elements
</TrustedCertificate>
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
<td><p><a href="subjectname.md" data-raw-source="[SubjectName](subjectname.md)">SubjectName</a></p></td>
<td><p>The Subject Name of the trusted certificate.</p></td>
</tr>
<tr class="even">
<td><p><a href="issuername.md" data-raw-source="[IssuerName](issuername.md)">IssuerName</a></p></td>
<td><p>The Issuer Name of the trusted certificate.</p></td>
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
<td><p><a href="trustedcertificates.md" data-raw-source="[TrustedCertificates](trustedcertificates.md)">TrustedCertificates</a></p></td>
<td><p>Specifies the trusted certificates.</p></td>
</tr>
</tbody>
</table>

 

## XSD


``` syntax
<xs:element name="TrustedCertificate" type="tns:TrustedCertificateType" minOccurs="0" maxOccurs="256" />

<xs:complexType name="TrustedCertificateType">
  <xs:sequence>
    <xs:element name="SubjectName" type="xs:string" />
    <xs:element name="IssuerName" type="xs:string" />
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
  </xs:sequence>
</xs:complexType>
```

## Remarks


The TrustedCertificate element is optional.

 

 





