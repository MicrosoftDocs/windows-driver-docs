---
title: AllowTethering
description: AllowTethering
ms.assetid: f9b92c46-5e0e-447a-b571-bf549e9a749d
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# AllowTethering

[!include[MBAE deprecation warning](mbae-deprecation-warning.md)]

The AllowTethering element specifies whether the user is always allowed, never allowed, or allowed after an entitlement check to use Internet sharing.

**Note**  
If this element is configured to allow after an entitlement check, you must specify a [DeviceNotificationHandler](devicenotificationhandler.md) in your app that will handle the entitlement check.

 

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<AllowTethering>
  text
</AllowTethering>
```

## <span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes


There are no attributes.

## <span id="Text_value"></span><span id="text_value"></span><span id="TEXT_VALUE"></span>Text value


A string indicating whether Internet sharing is always allowed, never allowed, or allowed after an entitlement check.

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
<td><p><a href="networkconfiguration.md" data-raw-source="[NetworkConfiguration](networkconfiguration.md)">NetworkConfiguration</a></p></td>
<td><p>Specifies the purchase and Internet mobile broadband profiles to be used or whether standard user can perform PIN unlock operations.</p></td>
</tr>
</tbody>
</table>

 

## <span id="XSD"></span><span id="xsd"></span>XSD


``` syntax
<xs:element name="name="AllowTethering" type="tns:TetheringAllowedType" minOccurs="0" />

<xs:simpleType name="TetheringAllowedType">  
  <xs:restriction base="xs:string">
    <xs:enumeration value="Never"/>
    <xs:enumeration value="Always"/>
    <xs:enumeration value="EntitlementCheckRequired"/>
  </xs:restriction>
</xs:simpleType>
```

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


This element is only applicable to Windows 8.1 and Windows 10.

The AllowTethering element is optional.

 

 





