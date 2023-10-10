---
title: Relationships
description: Relationships
ms.date: 04/20/2017
---

# Relationships

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

The Relationships element specifies data that is used to track a device metadata package within the device metadata cache.

## Usage


``` syntax
<Relationships>
  text
  child elements
</Relationships>
```

## Attributes


There are no attributes.

## Text value


If the Relationships element is specified, it must specify the [ExperienceID](experienceid.md) element or the [LanguageNeutralIdentifier](languageneutralidentifier.md) element, or both.

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
<td><p><a href="experienceid.md" data-raw-source="[ExperienceID](experienceid.md)">ExperienceID</a></p></td>
<td><p>The <a href="experienceid.md" data-raw-source="[ExperienceID](experienceid.md)">ExperienceID</a> element specifies a GUID that is managed by the Windows Dev Center Dashboard. This GUID is used to group one or more metadata packages for the same device identifiers independent of the packages’ locale.</p></td>
</tr>
<tr class="even">
<td><p><a href="languageneutralidentifier.md" data-raw-source="[LanguageNeutralIdentifier](languageneutralidentifier.md)">LanguageNeutralIdentifier</a></p></td>
<td><p>The <a href="languageneutralidentifier.md" data-raw-source="[LanguageNeutralIdentifier](languageneutralidentifier.md)">LanguageNeutralIdentifier</a> element specifies a GUID that identifies the device metadata package independent of its locale.</p></td>
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
<td><p><a href="packageinfo.md" data-raw-source="[PackageInfo](packageinfo.md)">PackageInfo</a></p></td>
<td><p>The <a href="packageinfo.md" data-raw-source="[PackageInfo](packageinfo.md)">PackageInfo</a> element specifies the attributes of the service metadata package.</p></td>
</tr>
</tbody>
</table>

 

## XSD


``` syntax
<xs:element name="Relationships" type="tns:RelationshipsType" minOccurs="0" />

<xs:complexType name="RelationshipsType">
  <xs:sequence>
    <xs:element name="ExperienceID" type="tns:GUIDType" minOccurs="0" />
    <xs:element name="LanguageNeutralIdentifier" type="tns:GUIDType" minOccurs="0" />
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded"
  </xs:sequence>
</xs:complexType>
```

## Remarks


The child elements of the Relationships element ([ExperienceID](experienceid.md) and [LanguageNeutralIdentifier](languageneutralidentifier.md)) provide separate search keys that the operating system uses to query device metadata packages that are installed within the device metadata cache.

 

 





