---
title: TrustedCertificate (APN element)
description: TrustedCertificate (APN element)
ms.date: 04/20/2017
---

# TrustedCertificate (APN element)


The TrustedCertificate element specifies a trusted certificate for the specified operator.

## Usage


``` syntax
<TrustedCertificate SubjectName=”xs:string” IssuerName=”xs:string”>
</TrustedCertificate>
```

## Attributes


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
<td><p>SubjectName</p></td>
<td><p>xs:string</p></td>
<td><p>Yes</p></td>
<td><p>The subject name of the certificate.</p></td>
</tr>
<tr class="even">
<td><p>IssuerName</p></td>
<td><p>xs:string</p></td>
<td><p>Yes</p></td>
<td><p>The issuer name of the certificate.</p></td>
</tr>
</tbody>
</table>

 

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
<td><p><a href="trustedcertificatelist.md" data-raw-source="[TrustedCertificateList](trustedcertificatelist.md)">TrustedCertificateList</a></p></td>
<td><p>Specifies a list of trusted certificates for the operator.</p></td>
</tr>
</tbody>
</table>

 

## XSD


``` syntax
<xs:element ref="TrustedCertificate" maxOccurs="unbounded"/>

<xs:element name="TrustedCertificate">
  <xs:complexType>
    <xs:attribute name="SubjectName" type="xs:string" use="required"/>
    <xs:attribute name="IssuerName" type="xs:string" use="required"/>
  </xs:complexType>
</xs:element>
```

## Remarks


The TrustedCertificate element is optional.

 

 





