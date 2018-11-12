---
title: SoftwareInfo
description: SoftwareInfo
ms.assetid: 736040e9-76cd-4f59-b16a-1e8fc3b687fa
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SoftwareInfo

[!include[MBAE deprecation warning](mbae-deprecation-warning.md)]

The SoftwareInfo element is the parent element of the [SoftwareInfo XML schema](softwareinfo-xml-schema.md).

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<SoftwareInfo>
  child elements
</SoftwareInfo>
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
<td><p><a href="devicecompanionapplications.md" data-raw-source="[DeviceCompanionApplications](devicecompanionapplications.md)">DeviceCompanionApplications</a></p></td>
<td><p>Specifies the app that will be downloaded when the operator’s Mobile Broadband hardware is detected on the PC.</p></td>
</tr>
<tr class="even">
<td><p><a href="privilegedapplications.md" data-raw-source="[PrivilegedApplications](privilegedapplications.md)">PrivilegedApplications</a></p></td>
<td><p>Specifies the app that will be allowed to access privileged Mobile Broadband interfaces.</p></td>
</tr>
</tbody>
</table>

 

## <span id="Parent_elements"></span><span id="parent_elements"></span><span id="PARENT_ELEMENTS"></span>Parent elements


There are no parent elements.

## <span id="XSD"></span><span id="xsd"></span>XSD


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

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


The SoftwareInfo element is required.

 

 





