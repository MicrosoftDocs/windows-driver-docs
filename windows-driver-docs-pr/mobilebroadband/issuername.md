---
title: IssuerName
description: IssuerName
ms.assetid: 189c9b8f-11de-4ef2-9474-b0068b8178bc
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IssuerName

[!include[MBAE deprecation warning](mbae-deprecation-warning.md)]

The IssuerName element specifies the Issuer Name of a trusted certificate.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<IssuerName>
  text
</IssuerName>
```

## <span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes


There are no attributes.

## <span id="Text_value"></span><span id="text_value"></span><span id="TEXT_VALUE"></span>Text value


A string with the Issuer Name of the certificate.

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
<td><p><a href="trustedcertificate.md" data-raw-source="[TrustedCertificate](trustedcertificate.md)">TrustedCertificate</a></p></td>
<td><p>Specifies a trusted certificate.</p></td>
</tr>
</tbody>
</table>

 

## <span id="XSD"></span><span id="xsd"></span>XSD


``` syntax
<xs:element name="IssuerName" type="xs:string" />
```

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


The IssuerName element is optional.

 

 





