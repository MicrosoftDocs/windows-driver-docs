---
title: Verb
description: Verb
ms.date: 04/20/2017
---

# Verb

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

The Verb element specifies the Verb that the application registers.

## Usage


``` syntax
<Verb />
```

## Attributes


There are no attributes.

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
<xs:element name="Verb" type="tns:VerbType" />

<xs:simpleType name="VerbType">
  <xs:restriction base="tns:AllowedAsciiCharSetType">
    <xs:pattern value="[^ ]+"/>
    <xs:maxLength value="64"/>
  </xs:restriction>
</xs:simpleType>
```

## Remarks


The Verb element is optional.

 

 





