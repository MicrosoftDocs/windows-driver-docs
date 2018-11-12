---
title: Internet
description: Internet
ms.assetid: 13723c21-0054-4b91-9059-c7c985e83773
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Internet

[!include[MBAE deprecation warning](mbae-deprecation-warning.md)]

The Internet element specifies the purchase mobile broadband profile file to use.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<Internet>
  child element
</Internet>
```

## <span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes


There are no attributes.

## <span id="Text_value"></span><span id="text_value"></span><span id="TEXT_VALUE"></span>Text value


The name of a file in the ServiceInformation directory.

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
<td><p><a href="mobilebroadbandprofiles.md" data-raw-source="[MobileBroadbandProfiles](mobilebroadbandprofiles.md)">MobileBroadbandProfiles</a></p></td>
<td><p>Specifies the purchase and Internet mobile broadband profile files to use</p></td>
</tr>
</tbody>
</table>

 

## <span id="XSD"></span><span id="xsd"></span>XSD


``` syntax
<xs:element name="Internet" type="tns:FileType" minOccurs="0"/>

<xs:simpleType name="FileType">
  <xs:restriction base="xs:string">
    <xs:whiteSpace value="preserve"/>
    <xs:pattern value="[\p{L}\p{N}\.\-_ ]+"/>
    <xs:minLength value="1"/>
    <xs:maxLength value="260"/>
  </xs:restriction>
</xs:simpleType>
```

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


The Internet element is optional.

 

 





