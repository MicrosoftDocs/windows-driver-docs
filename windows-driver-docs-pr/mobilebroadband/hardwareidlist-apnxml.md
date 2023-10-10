---
title: HardwareIDList (APN element)
description: HardwareIDList (APN element)
ms.date: 04/20/2017
---

# HardwareIdList (APN element)


The HardwareIdList element specifies a list of hardware IDs for the operator.

## Usage


``` syntax
<HardwareIdList>
  child elements
</Operator>
```

## Attributes


There are no attributes.

## Child elements


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
<td><p><a href="hardwareid-apnxml.md" data-raw-source="[HardwareId](hardwareid-apnxml.md)">HardwareId</a></p></td>
<td><p>An operator hardware ID.</p></td>
</tr>
</tbody>
</table>

 

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
<td><p><a href="operator.md" data-raw-source="[Operator](operator.md)">Operator</a></p></td>
<td><p>Specifies the details for an operator in the COSA database.</p></td>
</tr>
</tbody>
</table>

 

## XSD


``` syntax
<xs:element name="HardwareIdList">
  <xs:complexType>
    <xs:sequence>
      <xs:element ref="HardwareId" maxOccurs="unbounded"/>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```

## Remarks


The HardwareIdList element is required.

 

 





