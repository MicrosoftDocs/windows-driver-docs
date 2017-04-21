---
title: Identity (SoftwareInfo)
description: Identity (SoftwareInfo)
ms.assetid: fcec93ad-54d4-466e-8fac-888377115689
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Identity (SoftwareInfo)


The Identity element specifies the publisher identity and application manifest name of the app.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<Identity Name=”tns:AsciiIdentifierType” Publisher=”tns:DistinguishedNameType” />
```

## <span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes


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
<td><p>tns:AsciiIdentifierType</p></td>
<td><p>Yes</p></td>
<td><p>The name of the app as specified in the app manifest file.</p></td>
</tr>
<tr class="even">
<td><p>Publisher</p></td>
<td><p>tns:DistinguishedNameType</p></td>
<td><p>Yes</p></td>
<td><p>The publisher identity of the app.</p></td>
</tr>
</tbody>
</table>

 

## <span id="Child_elements"></span><span id="child_elements"></span><span id="CHILD_ELEMENTS"></span>Child elements


There are no child elements.

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
<td><p>[DeviceCompanionApplications](devicecompanionapplications.md)</p></td>
<td><p>Specifies the app that will be downloaded when the operator’s Mobile Broadband hardware is detected on the PC.</p></td>
</tr>
</tbody>
</table>

 

## <span id="XSD"></span><span id="xsd"></span>XSD


``` syntax
<xs:element name="Identity" type="tns:IdentityType" />

<xs:complexType name="IdentityType">
  <xs:attribute name="Name" type="tns:PackageNameType" use="required"/>
  <xs:attribute name="Publisher" type="tns:PublisherType" use="required"/>
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

<xs:simpleType name="AsciiIdentifierType">
  <xs:restriction base="tns:AllowedAsciiCharSetType">
    <xs:pattern value="[^_ ]+"/>
  </xs:restriction>
</xs:simpleType>

<xs:simpleType name="DistinguishedNameType">
  <xs:restriction base="tns:NonEmptyStringType">
    <xs:pattern value="(CN|L|O|OU|E|C|S|STREET|T|G|I|SN|DC|SERIALNUMBER|(OID\.(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*))+))=(([^,+=&quot;&lt;&gt;#;])+|&quot;.*&quot;)(, ((CN|L|O|OU|E|C|S|STREET|T|G|I|SN|DC|SERIALNUMBER|(OID\.(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*))+))=(([^,+=&quot;&lt;&gt;#;])+|&quot;.*&quot;)))*"/>
  </xs:restriction>
</xs:simpleType>

<xs:simpleType name="NonEmptyStringType">
  <xs:restriction base="xs:string">
    <xs:minLength value="1"/>
    <xs:maxLength value="32767"/>
    <xs:pattern value="[^\s]|([^\s].*[^\s])"/>
  </xs:restriction>
</xs:simpleType>

<xs:simpleType name="AllowedAsciiCharSetType">
  <xs:restriction base="tns:NonEmptyStringType">
    <xs:pattern value="[-_. A-Za-z0-9]+"/>
  </xs:restriction>
</xs:simpleType>
```

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


The Identity element is optional.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Identity%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




