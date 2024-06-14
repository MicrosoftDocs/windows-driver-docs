---
title: SubjectName
description: SubjectName
ms.date: 04/20/2017
---

# SubjectName

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

The SubjectName element specifies the Subject Name of a trusted certificate.

## Usage


``` syntax
<SubjectName>
  text
</SubjectName>
```

## Attributes


There are no attributes.

## Text value


A string with the Subject Name of the certificate.

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
<td><p><a href="trustedcertificate.md" data-raw-source="[TrustedCertificate](trustedcertificate.md)">TrustedCertificate</a></p></td>
<td><p>Specifies a trusted certificate.</p></td>
</tr>
</tbody>
</table>

 

## XSD


``` syntax
<xs:element name="SubjectName" type="xs:string" />
```

## Remarks


The SubjectName element is optional.

 

 





