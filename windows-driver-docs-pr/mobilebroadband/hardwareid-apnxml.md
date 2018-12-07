---
title: HardwareId (APN element)
description: HardwareId (APN element)
ms.assetid: 9c09915c-d0f6-4ddf-b2e1-79f00599c3a0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# HardwareId (APN element)


The HardwareId element specifies the HWID for the specified operator.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<HardwareId>
...insert text here
</HardwareId>
```

## <span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes


There are no attributes.

## <span id="Text_value"></span><span id="text_value"></span><span id="TEXT_VALUE"></span>Text value


A string that represents an encoded hardware ID. Generating the proper hardware ID values involves a complex algorithm. We recommend that you use mbidgenerator.exe to generate your hardware IDs.

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
<td><p><a href="hardwareidlist-apnxml.md" data-raw-source="[HardwareIdList](hardwareidlist-apnxml.md)">HardwareIdList</a></p></td>
<td><p>Specifies the list of hardware IDs for an operator.</p></td>
</tr>
</tbody>
</table>

 

## <span id="XSD"></span><span id="xsd"></span>XSD


``` syntax
<xs:element ref="HardwareId" maxOccurs="unbounded"/>

<xs:element name="HardwareId">
  <xs:complexType>
    <xs:attribute name="id" type="xs:string" use="required"/>
  </xs:complexType>
</xs:element>
```

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


The HardwareId element must represent one of the following:

-   GSM networks: IMSI range

-   GSM networks: ICCID range

-   CDMA networks: Provider name value

-   CDMA networks: Provider ID value (also known as SID)

The HardwareId element is required.

 

 





