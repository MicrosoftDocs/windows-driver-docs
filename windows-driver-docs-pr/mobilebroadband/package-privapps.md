---
title: Package (SoftwareInfo - priviliged applications)
description: Package (SoftwareInfo - priviliged applications)
ms.assetid: c9b22498-a7b6-4e17-9688-536883aa5844
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Package (SoftwareInfo - priviliged applications)

[!include[MBAE deprecation warning](mbae-deprecation-warning.md)]

The Package element specifies an app that should have access to the privileged Mobile Broadband interfaces.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<Package>
  child element
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
<td><p><a href="identity-privapps.md" data-raw-source="[Identity](identity-privapps.md)">Identity</a></p></td>
<td><p>The publisher identify of the app.</p></td>
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
<td><p><a href="privilegedapplications.md" data-raw-source="[PrivilegedApplications](privilegedapplications.md)">PrivilegedApplications</a></p></td>
<td><p>The apps that should have access to the privileged Mobile Broadband interfaces.</p></td>
</tr>
</tbody>
</table>

 

## <span id="XSD"></span><span id="xsd"></span>XSD


``` syntax
<xs:element name="Package" type="tns:PackageForPrivilegedApplications" maxOccurs="unbounded" />

<xs:complexType name="PackageForPrivilegedApplications">
  <xs:sequence>
    <xs:element name="Identity" type="tns:IdentityForPrivilegedApplicationsType" />
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
  </xs:sequence>
</xs:complexType>
```

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


The Package element is optional.

 

 





