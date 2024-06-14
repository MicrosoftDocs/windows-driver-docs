---
title: AutoplayType
description: AutoplayType
ms.date: 04/20/2017
---

# AutoplayType

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

The AutoplayType element specifies whether the AutoPlay event is a device event or a content event. AutoPlay determines the type of device and raises either a Device event for non-volume devices, or a Content event for volume devices.

## Usage


``` syntax
<AutoplayType>
  type
</AutoplayType>
```

## Attributes


There are no attributes.

## Text value


A string that has either the value "Device" or the value "Content".

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
<xs:element name="AutoplayType" type="tns:AutoplayTypeType" />

<xs:simpleType name="AutoplayTypeType">
  <xs:restriction base="xs:string">
     <xs:enumeration value="Device" />
     <xs:enumeration value="Content" />
  </xs:restriction>
</xs:simpleType>
```

## Remarks


The AutoplayType element is optional.

 

 





