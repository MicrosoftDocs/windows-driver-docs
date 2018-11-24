---
title: TrustedCertificateList
description: TrustedCertificateList
ms.assetid: 116ee448-b0a8-4441-845c-945fc5ae0ddd
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# TrustedCertificateList


The TrustedCertificateList element specifies a list of trusted certificates for the operator.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<TrustedCertificateList>
   child elements
</TrustedCertificateList>
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
<td><p><a href="trustedcertificate-apnxml.md" data-raw-source="[TrustedCertificate](trustedcertificate-apnxml.md)">TrustedCertificate</a></p></td>
<td><p>A certificate trusted by the operator.</p></td>
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
<td><p><a href="operatorlist.md" data-raw-source="[OperatorList](operatorlist.md)">OperatorList</a></p></td>
<td><p>The parent element of the <a href="apn-xml-schema.md" data-raw-source="[APN XML schema](apn-xml-schema.md)">APN XML schema</a>.</p></td>
</tr>
</tbody>
</table>

 

## <span id="XSD"></span><span id="xsd"></span>XSD


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

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


The TrustedCertificateList element is optional.

 

 





