---
title: Applications
description: Applications
ms.date: 04/20/2017
---

# Applications

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

The Applications element specifies the apps that are associated with the Mobile Broadband hardware device.

## Usage


``` syntax
<Applications>
  Child element
</Applications>
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
<td><p><a href="application-softwareinfo-schema.md" data-raw-source="[Application](application-softwareinfo-schema.md)">Application</a></p></td>
<td><p>Specifies the app that will be downloaded when the operator’s Mobile Broadband hardware is detected on the PC.</p></td>
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
<td><p><a href="package.md" data-raw-source="[Package](package.md)">Package</a></p></td>
<td><p>Specifies the app that will be downloaded when the operator’s Mobile Broadband hardware is detected on the PC.</p></td>
</tr>
</tbody>
</table>

 

## XSD


``` syntax
<xs:element name="Applications" type="tns:ApplicationsType" />

  <xs:complexType name="ApplicationsType">
    <xs:sequence>
      <xs:element name="Application" type="tns:ApplicationType" />
      <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
  </xs:complexType>
```

## Remarks


The Applications element is optional.

 

 





