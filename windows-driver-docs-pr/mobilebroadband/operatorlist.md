---
title: OperatorList
description: OperatorList
ms.date: 04/20/2017
---

# OperatorList


The OperatorList element specifies a list of operators included in the COSA database.

## Usage


``` syntax
<OperatorList>
  child elements
</OperatorList>
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
<td><p><a href="operator.md" data-raw-source="[Operator](operator.md)">Operator</a></p></td>
<td><p>Specifies the details of the operator.</p></td>
</tr>
</tbody>
</table>

 

## Parent elements


There are no parent elements.

## XSD


``` syntax
<xs:element name="OperatorList">
  <xs:complexType>
    <xs:sequence>
      <xs:element ref="Operator" maxOccurs="unbounded"/>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```

## Remarks


The OperatorList element is required.

 

 





