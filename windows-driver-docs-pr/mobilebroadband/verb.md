---
title: Verb
description: Verb
ms.assetid: 38edbb37-5fd4-4301-adc0-4a66a7e8a564
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Verb

[!include[MBAE deprecation warning](mbae-deprecation-warning.md)]

The Verb element specifies the Verb that the application registers.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<Verb />
```

## <span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes


There are no attributes.

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
<xs:element name="Verb" type="tns:VerbType" />

<xs:simpleType name="VerbType">
  <xs:restriction base="tns:AllowedAsciiCharSetType">
    <xs:pattern value="[^ ]+"/>
    <xs:maxLength value="64"/>
  </xs:restriction>
</xs:simpleType>
```

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


The Verb element is optional.

 

 





