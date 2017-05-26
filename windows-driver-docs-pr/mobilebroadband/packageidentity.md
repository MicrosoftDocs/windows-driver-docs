---
title: PackageIdentity
description: PackageIdentity
ms.assetid: b5533962-ea42-416e-bbd8-ce9dce1a9a40
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# PackageIdentity


The PackageIdentity element specifies a Windows Store device app that should appear as the recommended AutoPlay action when a user plugs in a device.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<PackageIdentity Name=”tns:PackageNameType” Publisher=”tns:PublisherType” />
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
<td><p>[AutoplayHandler](autoplayhandler.md)</p></td>
<td><p>Specifies a Windows Store device app that should appear as the recommended AutoPlay action when a user plugs in a device.</p></td>
</tr>
</tbody>
</table>

 

## <span id="XSD"></span><span id="xsd"></span>XSD


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

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


Copy the Name and Publisher attributes from the application manifest's &lt;Identity&gt; element after the app has been associated with the Windows Store, because the process of associating your app will update the app manifest.

Here is an example of how the &lt;Identity&gt; element may look inside an app manifest.

``` syntax
<Identity Name="64022FABRIKAM.FabrikamDeviceApp" Publisher="CN=05558413-FFF6-4AA5-8176-AD43036533FA" Version="1.0.0.0" />
```

The PackageIdentity element is optional.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20PackageIdentity%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




