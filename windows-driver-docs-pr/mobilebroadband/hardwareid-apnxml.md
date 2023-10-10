---
title: HardwareId (APN element)
description: HardwareId (APN element)
ms.date: 04/20/2017
---

# HardwareId (APN element)


The HardwareId element specifies the HWID for the specified operator.

## Usage


``` syntax
<HardwareId>
...insert text here
</HardwareId>
```

## Attributes


There are no attributes.

## Text value


A string that represents an encoded hardware ID. Generating the proper hardware ID values involves a complex algorithm. We recommend that you use mbidgenerator.exe to generate your hardware IDs.

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
<td><p><a href="hardwareidlist-apnxml.md" data-raw-source="[HardwareIdList](hardwareidlist-apnxml.md)">HardwareIdList</a></p></td>
<td><p>Specifies the list of hardware IDs for an operator.</p></td>
</tr>
</tbody>
</table>

 

## XSD


``` syntax
<xs:element ref="HardwareId" maxOccurs="unbounded"/>

<xs:element name="HardwareId">
  <xs:complexType>
    <xs:attribute name="id" type="xs:string" use="required"/>
  </xs:complexType>
</xs:element>
```

## Remarks


The HardwareId element must represent one of the following:

-   GSM networks: IMSI range

-   GSM networks: ICCID range

-   CDMA networks: Provider name value

-   CDMA networks: Provider ID value (also known as SID)

The HardwareId element is required.

 

 





