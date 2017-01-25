---
title: Relationships
description: Relationships
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 78443a49-96c6-45d9-a4f3-8213005f82d5
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Relationships%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




