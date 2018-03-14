---
title: TrustedCertificateList
description: TrustedCertificateList
ms.assetid: 116ee448-b0a8-4441-845c-945fc5ae0ddd
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td><p>[TrustedCertificate](trustedcertificate-apnxml.md)</p></td>
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
<td><p>[OperatorList](operatorlist.md)</p></td>
<td><p>The parent element of the [APN XML schema](apn-xml-schema.md).</p></td>
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

 

 





