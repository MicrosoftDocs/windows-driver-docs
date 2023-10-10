---
title: Package (SoftwareInfo - priviliged applications)
description: Package (SoftwareInfo - priviliged applications)
ms.date: 04/20/2017
---

# Package (SoftwareInfo - priviliged applications)

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

The Package element specifies an app that should have access to the privileged Mobile Broadband interfaces.

## Usage


``` syntax
<Package>
  child element
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
<td><p><a href="identity-privapps.md" data-raw-source="[Identity](identity-privapps.md)">Identity</a></p></td>
<td><p>The publisher identify of the app.</p></td>
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
<td><p><a href="privilegedapplications.md" data-raw-source="[PrivilegedApplications](privilegedapplications.md)">PrivilegedApplications</a></p></td>
<td><p>The apps that should have access to the privileged Mobile Broadband interfaces.</p></td>
</tr>
</tbody>
</table>

 

## XSD


``` syntax
<xs:element name="Package" type="tns:PackageForPrivilegedApplications" maxOccurs="unbounded" />

<xs:complexType name="PackageForPrivilegedApplications">
  <xs:sequence>
    <xs:element name="Identity" type="tns:IdentityForPrivilegedApplicationsType" />
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
  </xs:sequence>
</xs:complexType>
```

## Remarks


The Package element is optional.

 

 





