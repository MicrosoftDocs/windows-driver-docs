---
title: SoftwareInfo
description: SoftwareInfo
ms.date: 04/20/2017
---

# SoftwareInfo

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

The SoftwareInfo element is the parent element of the [SoftwareInfo XML schema](softwareinfo-xml-schema.md).

## Usage


``` syntax
<SoftwareInfo>
  child elements
</SoftwareInfo>
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
<td><p><a href="devicecompanionapplications.md" data-raw-source="[DeviceCompanionApplications](devicecompanionapplications.md)">DeviceCompanionApplications</a></p></td>
<td><p>Specifies the app that will be downloaded when the operator’s Mobile Broadband hardware is detected on the PC.</p></td>
</tr>
<tr class="even">
<td><p><a href="privilegedapplications.md" data-raw-source="[PrivilegedApplications](privilegedapplications.md)">PrivilegedApplications</a></p></td>
<td><p>Specifies the app that will be allowed to access privileged Mobile Broadband interfaces.</p></td>
</tr>
</tbody>
</table>

 

## Parent elements


There are no parent elements.

## XSD


``` syntax
<xs:element name="SoftwareInfo" type="tns:SoftwareInfoType" />

<xs:complexType name="SoftwareInfoType">
  <xs:choice>
    <xs:sequence>
      <xs:element name="DeviceCompanionApplications" type="tns:DeviceCompanionApplicationsType" />
      <xs:element name="PrivilegedApplications" type="tns:PrivilegedApplicationsType" minOccurs="0" />
      <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
    <xs:element name="PrivilegedApplications" type="tns:PrivilegedApplicationsType" />
  </xs:choice>
</xs:complexType>
```

## Remarks


The SoftwareInfo element is required.

 

 





