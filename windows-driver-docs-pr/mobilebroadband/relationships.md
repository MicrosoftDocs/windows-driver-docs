---
title: Relationships
description: Relationships
ms.assetid: 78443a49-96c6-45d9-a4f3-8213005f82d5
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Relationships


The Relationships element specifies data that is used to track a device metadata package within the device metadata cache.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<Relationships>
  text
  child elements
</Relationships>
```

## <span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes


There are no attributes.

## <span id="Text_value"></span><span id="text_value"></span><span id="TEXT_VALUE"></span>Text value


If the Relationships element is specified, it must specify the [ExperienceID](experienceid.md) element or the [LanguageNeutralIdentifier](languageneutralidentifier.md) element, or both.

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
<td><p>[ExperienceID](experienceid.md)</p></td>
<td><p>The [ExperienceID](experienceid.md) element specifies a GUID that is managed by the Windows Dev Center Dashboard. This GUID is used to group one or more metadata packages for the same device identifiers independent of the packages’ locale.</p></td>
</tr>
<tr class="even">
<td><p>[LanguageNeutralIdentifier](languageneutralidentifier.md)</p></td>
<td><p>The [LanguageNeutralIdentifier](languageneutralidentifier.md) element specifies a GUID that identifies the device metadata package independent of its locale.</p></td>
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
<td><p>[PackageInfo](packageinfo.md)</p></td>
<td><p>The [PackageInfo](packageinfo.md) element specifies the attributes of the service metadata package.</p></td>
</tr>
</tbody>
</table>

 

## <span id="XSD"></span><span id="xsd"></span>XSD


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

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


The child elements of the Relationships element ([ExperienceID](experienceid.md) and [LanguageNeutralIdentifier](languageneutralidentifier.md)) provide separate search keys that the operating system uses to query device metadata packages that are installed within the device metadata cache.

 

 





