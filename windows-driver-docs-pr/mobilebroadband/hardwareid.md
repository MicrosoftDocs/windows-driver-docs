---
title: HardwareId (PackageInfo)
description: HardwareId (PackageInfo)
ms.date: 04/20/2017
---

# HardwareId (PackageInfo)

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

For service metadata packages, the HardwareID values represent the mobile network operator in the form of the following:

-   GSM networks: IMSI value

-   GSM networks: ICCID value

-   CDMA networks: Provider name value

-   CDMA networks: Provider ID value (also known as a SID)

## Usage


``` syntax
<HardwareID>
  text
</HardwareID>
```

## Attributes


There are no attributes.

## Text value


Generating the proper hardware ID values as part of metadata creation involves a complex algorithm. You should generate hardware ID values by using MBIDGenerator.exe included in the Windows Driver Kit (WDK).

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
<td><p><a href="hardwareidlist.md" data-raw-source="[HardwareIDList](hardwareidlist.md)">HardwareIDList</a></p></td>
<td><p>The <a href="hardwareidlist.md" data-raw-source="[HardwareIDList](hardwareidlist.md)">HardwareIDList</a> element specifies one or more hardware identification strings for the service metadata package.</p></td>
</tr>
</tbody>
</table>

 

## XSD


``` syntax
<xs:element name="HardwareID" type="tns:HardwareIDType" maxOccurs="unbounded" />

<xs:simpleType name="HardwareIDType">
  <xs:restriction base="xs:string">
    <xs:minLength value="1" />
    <xs:maxLength value="207" />
    <xs:pattern value="^([a-zA-Z0-9!#$%&()*+\-./:;&lt;=&gt;?@[\\\]^_`{|}~])*$" /> 
  </xs:restriction>
</xs:simpleType>
```

## Remarks


-   Hardware IDs that are included in PackageInfo.xml must have the “DOID:” prefix added to them. For example: DOID:MBAE:0:*hashednumber1*

-   More than one HardwareID element can be used to specify a service.

-   For GSM IMSI or ICCID ranges, the start range value must end in 00 and the end range value must end in 99. For privacy reasons, matching occurs in blocks of 100 for IMSI and ICCID values.

The HardwareID element is required.

 

 





