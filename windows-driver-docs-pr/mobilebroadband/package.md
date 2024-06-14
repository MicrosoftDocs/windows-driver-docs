---
title: Package (SoftwareInfo)
description: Package (SoftwareInfo)
ms.date: 04/20/2017
---

# Package (SoftwareInfo)

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

The Package element specifies the app that will be downloaded when the operator’s mobile broadband hardware is detected on the PC.

## Usage


``` syntax
<Package>
  child elements
</Package>
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
<td><p><a href="identity.md" data-raw-source="[Identity](identity.md)">Identity</a></p></td>
<td><p>The publisher identify of the app.</p></td>
</tr>
<tr class="even">
<td><p><a href="applications.md" data-raw-source="[Applications](applications.md)">Applications</a></p></td>
<td><p>The app that will be download when the Mobile Broadband hardware device is detected.</p></td>
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
<td><p><a href="softwareinfo.md" data-raw-source="[SoftwareInfo](softwareinfo.md)">SoftwareInfo</a></p></td>
<td><p>The parent element of the <a href="softwareinfo-xml-schema.md" data-raw-source="[SoftwareInfo XML schema](softwareinfo-xml-schema.md)">SoftwareInfo XML schema</a>.</p></td>
</tr>
</tbody>
</table>

 

## XSD


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

## Remarks


The Package element is optional.

 

 





