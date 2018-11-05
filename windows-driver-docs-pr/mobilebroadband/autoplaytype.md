---
title: AutoplayType
description: AutoplayType
ms.assetid: 06097d2a-7883-416e-a81d-3a8abccc620b
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# AutoplayType

[!include[MBAE deprecation warning](mbae-deprecation-warning.md)]

The AutoplayType element specifies whether the AutoPlay event is a device event or a content event. AutoPlay determines the type of device and raises either a Device event for non-volume devices, or a Content event for volume devices.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<AutoplayType>
  type
</AutoplayType>
```

## <span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes


There are no attributes.

## <span id="Text_value"></span><span id="text_value"></span><span id="TEXT_VALUE"></span>Text value


A string that has either the value "Device" or the value "Content".

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
<td><p><a href="autoplayhandler.md" data-raw-source="[AutoplayHandler](autoplayhandler.md)">AutoplayHandler</a></p></td>
<td><p>Specifies a UWP device app that should appear as the recommended AutoPlay action when a user plugs in a device.</p></td>
</tr>
</tbody>
</table>

 

## <span id="XSD"></span><span id="xsd"></span>XSD


``` syntax
<xs:element name="AutoplayType" type="tns:AutoplayTypeType" />

<xs:simpleType name="AutoplayTypeType">
  <xs:restriction base="xs:string">
     <xs:enumeration value="Device" />
     <xs:enumeration value="Content" />
  </xs:restriction>
</xs:simpleType>
```

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


The AutoplayType element is optional.

 

 





