---
title: PackageInfo
description: PackageInfo
ms.assetid: b74bfc2a-6779-4f53-9e46-71ca8ae26fda
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# PackageInfo


The PackageInfo element is the parent element of the [PackageInfo XML schema](packageinfo-xml-schema.md). The child elements of the PackageInfo element specify the attributes of the service metadata package.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<PackageInfo>
  child elements
</PackageInfo>
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
<td><p>[MetadataBuilderInformation](metadatabuilderinformation.md)</p></td>
<td><p>The [MetadataBuilderInformation](metadatabuilderinformation.md) element specifies information about the application that created the service metadata package.</p></td>
</tr>
<tr class="even">
<td><p>[MetadataKey](metadatakey.md)</p></td>
<td><p>The [MetadataKey](metadatakey.md) element specifies the attributes of the service metadata package. These include the following:</p>
<ul>
<li><p>The identifier for each hardware function supported by the device.</p></li>
<li><p>The language-specific locale for the text strings within the package.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>[PackageStructure](packagestructure.md)</p></td>
<td><p>The [PackageStructure](packagestructure.md) element specifies the XML schemas which are referenced by the service metadata package.</p></td>
</tr>
<tr class="even">
<td><p>[Relationships](relationships.md)</p></td>
<td><p>The [Relationships](relationships.md) element, through its child elements, specifies data that is used to track a service metadata package within the device metadata cache.</p></td>
</tr>
</tbody>
</table>

 

## <span id="Parent_elements"></span><span id="parent_elements"></span><span id="PARENT_ELEMENTS"></span>Parent elements


There are no parent elements.

## <span id="XSD"></span><span id="xsd"></span>XSD


``` syntax
<xs:element name="PackageInfo" type="tns:PackageInfoType" />

<xs:complexType name="PackageInfoType">
  <xs:sequence>
    <xs:element name="MetadataKey" type="tns:MetadataKeyType" />
    <xs:element name="PackageStructure" type="tns:PackageStructureType" />
    <xs:element name="Relationships" type="tns:RelationshipsType" minOccurs="0" />
    <xs:element name="MetadataBuilderInformation" type="tns:MetadataBuilderInformationType" minOccurs="0" />
    <xs:any namespace="##other" processContents="lax" minOccurs="0"
      maxOccurs="unbounded" />
  </xs:sequence>
</xs:complexType>
```

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


The PackageInfo element must contain one instance of the [MetadataKey](metadatakey.md), [PackageStructure](packagestructure.md), and [Relationships](relationships.md) elements.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20PackageInfo%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




