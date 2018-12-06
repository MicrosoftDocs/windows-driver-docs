---
title: HardwareIDList (APN element)
description: HardwareIDList (APN element)
ms.assetid: 9a3ca581-0afb-42fa-b13e-d233d9555b7e
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# HardwareIdList (APN element)


The HardwareIdList element specifies a list of hardware IDs for the operator.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<HardwareIdList>
  child elements
</Operator>
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
<td><p><a href="hardwareid-apnxml.md" data-raw-source="[HardwareId](hardwareid-apnxml.md)">HardwareId</a></p></td>
<td><p>An operator hardware ID.</p></td>
</tr>
</tbody>
</table>

 

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
<td><p><a href="operator.md" data-raw-source="[Operator](operator.md)">Operator</a></p></td>
<td><p>Specifies the details for an operator in the APN database.</p></td>
</tr>
</tbody>
</table>

 

## <span id="XSD"></span><span id="xsd"></span>XSD


``` syntax
<xs:element name="HardwareIdList">
  <xs:complexType>
    <xs:sequence>
      <xs:element ref="HardwareId" maxOccurs="unbounded"/>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


The HardwareIdList element is required.

 

 





