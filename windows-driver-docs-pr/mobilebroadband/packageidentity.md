---
title: PackageIdentity
description: PackageIdentity
ms.date: 04/20/2017
---

# PackageIdentity

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

The PackageIdentity element specifies a UWP device app that should appear as the recommended AutoPlay action when a user plugs in a device.

## Usage


``` syntax
<PackageIdentity Name=”tns:PackageNameType” Publisher=”tns:PublisherType” />
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
<td><p>tns:PackageNameType</p></td>
<td><p>Yes</p></td>
<td><p>Copy this element from the Name attribute of the app manifest's Identity element, described in Remarks.</p></td>
</tr>
<tr class="even">
<td><p>Publisher</p></td>
<td><p>tns:PublisherType</p></td>
<td><p>Yes</p></td>
<td><p>Copy this element from the Publisher attribute of the app manifest's Identity element, described in Remarks.</p></td>
</tr>
</tbody>
</table>

 

## Child elements


There are no child elements.

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
<td><p><a href="autoplayhandler.md" data-raw-source="[AutoplayHandler](autoplayhandler.md)">AutoplayHandler</a></p></td>
<td><p>Specifies a UWP device app that should appear as the recommended AutoPlay action when a user plugs in a device.</p></td>
</tr>
</tbody>
</table>

 

## XSD


``` syntax
<xs:element name="PackageIdentity" type="tns:PackageIdentityType" />

  <xs:complexType name="PackageIdentityType">
    <xs:attribute name="Name" type="tns:PackageNameType" use="required" />
    <xs:attribute name="Publisher" type="tns:PublisherType" use="required" />
  </xs:complexType>

  <xs:simpleType name="PackageNameType">
    <xs:restriction base="tns:AsciiIdentifierType">
      <xs:minLength value="3"/>
      <xs:maxLength value="50"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="PublisherType">
    <xs:restriction base="tns:DistinguishedNameType">
      <xs:maxLength value="8192"/>
    </xs:restriction>
  </xs:simpleType>
```

## Remarks


Copy the Name and Publisher attributes from the application manifest's &lt;Identity&gt; element after the app has been associated with the Microsoft Store, because the process of associating your app will update the app manifest.

Here is an example of how the &lt;Identity&gt; element may look inside an app manifest.

``` syntax
<Identity Name="64022FABRIKAM.FabrikamDeviceApp" Publisher="CN=05558413-FFF6-4AA5-8176-AD43036533FA" Version="1.0.0.0" />
```

The PackageIdentity element is optional.

 

 





