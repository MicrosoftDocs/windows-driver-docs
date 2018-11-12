---
title: TrustedCertificate (APN element)
description: TrustedCertificate (APN element)
ms.assetid: 8b1b09ab-7ab8-4d6d-9ea6-395a109def91
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# TrustedCertificate (APN element)


The TrustedCertificate element specifies a trusted certificate for the specified operator.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<TrustedCertificate SubjectName=”xs:string” IssuerName=”xs:string”>
</TrustedCertificate>
```

## <span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes


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

 

## <span id="Child_elements"></span><span id="child_elements"></span><span id="CHILD_ELEMENTS"></span>Child elements


There are no child elements.

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
<td><p><a href="trustedcertificatelist.md" data-raw-source="[TrustedCertificateList](trustedcertificatelist.md)">TrustedCertificateList</a></p></td>
<td><p>Specifies a list of trusted certificates for the operator.</p></td>
</tr>
</tbody>
</table>

 

## <span id="XSD"></span><span id="xsd"></span>XSD


``` syntax
<xs:element ref="TrustedCertificate" maxOccurs="unbounded"/>

<xs:element name="TrustedCertificate">
  <xs:complexType>
    <xs:attribute name="SubjectName" type="xs:string" use="required"/>
    <xs:attribute name="IssuerName" type="xs:string" use="required"/>
  </xs:complexType>
</xs:element>
```

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


The TrustedCertificate element is optional.

 

 





