---
title: ConnectionInfoList
description: ConnectionInfoList
ms.date: 04/20/2017
---

# ConnectionInfoList


The ConnectionInfoList element specifies a list of connections for the specified operator.

## Usage


``` syntax
<ConnectionInfoList>
  child elements
</ConnectionInfoList>
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
<td><p><a href="connectioninfo.md" data-raw-source="[ConnectionInfo](connectioninfo.md)">ConnectionInfo</a></p></td>
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
<xs:element ref="ConnectionInfoList"/>

<xs:element name="ConnectionInfoList">
  <xs:complexType>
    <xs:sequence>
      <xs:element ref="ConnectionInfo" maxOccurs="unbounded"/>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```

## Remarks


The ConnectionInfoList element is required.

 

 





