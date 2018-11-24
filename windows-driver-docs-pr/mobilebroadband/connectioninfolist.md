---
title: ConnectionInfoList
description: ConnectionInfoList
ms.assetid: e62f0106-0f2b-4990-aaf3-9cb398abfb2d
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ConnectionInfoList


The ConnectionInfoList element specifies a list of connections for the specified operator.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<ConnectionInfoList>
  child elements
</ConnectionInfoList>
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
<td><p><a href="connectioninfo.md" data-raw-source="[ConnectionInfo](connectioninfo.md)">ConnectionInfo</a></p></td>
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
<xs:element ref="ConnectionInfoList"/>

<xs:element name="ConnectionInfoList">
  <xs:complexType>
    <xs:sequence>
      <xs:element ref="ConnectionInfo" maxOccurs="unbounded"/>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


The ConnectionInfoList element is required.

 

 





