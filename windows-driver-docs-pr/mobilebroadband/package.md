---
title: Package (SoftwareInfo)
description: Package (SoftwareInfo)
ms.assetid: f15f0ffe-593d-4007-8002-4d593d18dd9a
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Package (SoftwareInfo)

[!include[MBAE deprecation warning](mbae-deprecation-warning.md)]

The Package element specifies the app that will be downloaded when the operator’s mobile broadband hardware is detected on the PC.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<Package>
  child elements
</Package>
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
<td><p><a href="identity.md" data-raw-source="[Identity](identity.md)">Identity</a></p></td>
<td><p>The publisher identify of the app.</p></td>
</tr>
<tr class="even">
<td><p><a href="applications.md" data-raw-source="[Applications](applications.md)">Applications</a></p></td>
<td><p>The app that will be download when the Mobile Broadband hardware device is detected.</p></td>
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
<td><p><a href="softwareinfo.md" data-raw-source="[SoftwareInfo](softwareinfo.md)">SoftwareInfo</a></p></td>
<td><p>The parent element of the <a href="softwareinfo-xml-schema.md" data-raw-source="[SoftwareInfo XML schema](softwareinfo-xml-schema.md)">SoftwareInfo XML schema</a>.</p></td>
</tr>
</tbody>
</table>

 

## <span id="XSD"></span><span id="xsd"></span>XSD


``` syntax
<xs:element name="Package" type="tns:PackageType" maxOccurs="unbounded" />

<xs:complexType name="PackageType">
    <xs:sequence>
        <xs:element name="Identity" type="tns:IdentityType" />
        <xs:element name="Applications" type="tns:ApplicationsType" />
      <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
</xs:complexType>
```

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


The Package element is optional.

 

 





