---
title: DeviceCompanionApplications
description: DeviceCompanionApplications
ms.assetid: 3e0b21a8-aa1f-4f7a-84fc-447bba172794
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DeviceCompanionApplications

[!include[MBAE deprecation warning](mbae-deprecation-warning.md)]

The DeviceCompanionApplications element specifies the app that will be downloaded when the operator’s mobile broadband hardware is detected on the PC.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<DeviceCompanionApplications>
  child elements
</DeviceCompanionApplications>
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
<td><p>[Package](package.md)</p></td>
<td><p>Specifies the package that will be used for the Microsoft Store device app.</p></td>
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
<td><p>[SoftwareInfo](softwareinfo.md)</p></td>
<td><p>The parent element of the [SoftwareInfo XML schema](softwareinfo-xml-schema.md).</p></td>
</tr>
</tbody>
</table>

 

## <span id="XSD"></span><span id="xsd"></span>XSD


``` syntax
<xs:element name="DeviceCompanionApplications" type="tns:DeviceCompanionApplicationsType" />

<xs:complexType name="DeviceCompanionApplicationsType">
  <xs:sequence>
    <xs:element name="Package" type="tns:PackageType" maxOccurs="unbounded" />
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
  </xs:sequence>
</xs:complexType>
```

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


-   When you specify the DeviceCompanionApplications element, the specified app will be downloaded when Windows detects the operator’s mobile broadband hardware.

-   The structure for the package [Identity](identity.md) and [Application](application-softwareinfo-schema.md) element are identical with the application manifest structure.

-   For Windows 8, Windows 8.1, and Windows 10, you can specify only one package and one application ID. The second package or application ID will be ignored if you specify it.

The DeviceCompanionApplications element is optional.

 

 





