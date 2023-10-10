---
title: Operator
description: Operator
ms.date: 04/20/2017
---

# Operator


The Operator element specifies the details of an operator that is included in the COSA database.

## Usage


``` syntax
<Operator name=”xs:string” AccountExperienceURL=”xs:anyURI” OperatorGUID=”GUID”>
  child elements
</Operator>
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
<td><p>Name</p></td>
<td><p>xs:string</p></td>
<td><p>Yes</p></td>
<td><p>The name and country/region of the operator.</p>
<p>Example: Contoso (Argentina)</p></td>
</tr>
<tr class="even">
<td><p>AccountExperienceURL</p></td>
<td><p>xs:anyURI</p></td>
<td><p>No</p></td>
<td><p>The URL of the operator’s website used to configure Mobile Broadband.</p></td>
</tr>
<tr class="odd">
<td><p>OperatorGUID</p></td>
<td><p>GUID</p></td>
<td><p>No</p></td>
<td><p>A GUID used to identify the operator.</p></td>
</tr>
</tbody>
</table>

 

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
<td><p><a href="hardwareidlist-apnxml.md" data-raw-source="[HardwareIdList](hardwareidlist-apnxml.md)">HardwareIdList</a></p></td>
<td><p>A list of hardware IDs that are assigned to the operator.</p></td>
</tr>
<tr class="even">
<td><p><a href="connectioninfolist.md" data-raw-source="[ConnectionInfoList](connectioninfolist.md)">ConnectionInfoList</a></p></td>
<td><p>A list of access strings.</p></td>
</tr>
<tr class="odd">
<td><p><a href="trustedcertificatelist.md" data-raw-source="[TrustedCertificateList](trustedcertificatelist.md)">TrustedCertificateList</a></p></td>
<td><p>A list of trusted certificates used to verify that account provisioning is provided by a purchase website owned by the operator.</p></td>
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
<xs:element name="Operator">
  <xs:complexType>
    <xs:sequence>
      <xs:element ref="HardwareIdList"/>
      <xs:element ref="ConnectionInfoList"/>
      <xs:element ref="TrustedCertificateList" minOccurs="0"/>
    </xs:sequence>
    <xs:attribute name="name" type="xs:string" use="required"/>
    <xs:attribute name="AccountExperienceURL" type="xs:anyURI" use="optional"/>
    <xs:attribute name="OperatorGUID" type="GUID" use="optional"/>
  </xs:complexType>
</xs:element>
```

## Remarks


The Operator element is required.

 

 





