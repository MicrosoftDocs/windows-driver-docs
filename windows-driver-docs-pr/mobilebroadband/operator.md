---
title: Operator
description: Operator
ms.assetid: 770ad50d-d42d-49ad-a302-e839a0ca1fb4
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# Operator


The Operator element specifies the details of an operator that is included in the APN database.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<Operator name=”xs:string” AccountExperienceURL=”xs:anyURI” OperatorGUID=”GUID”>
  child elements
</Operator>
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
<td><p>[HardwareIdList](hardwareidlist-apnxml.md)</p></td>
<td><p>A list of hardware IDs that are assigned to the operator.</p></td>
</tr>
<tr class="even">
<td><p>[ConnectionInfoList](connectioninfolist.md)</p></td>
<td><p>A list of access strings.</p></td>
</tr>
<tr class="odd">
<td><p>[TrustedCertificateList](trustedcertificatelist.md)</p></td>
<td><p>A list of trusted certificates used to verify that account provisioning is provided by a purchase website owned by the operator.</p></td>
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

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


The Operator element is required.

 

 





