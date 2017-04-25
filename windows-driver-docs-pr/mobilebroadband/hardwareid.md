---
title: HardwareId (PackageInfo)
description: HardwareId (PackageInfo)
ms.assetid: edd05106-1bbc-45da-80cc-792d7fcce192
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# HardwareId (PackageInfo)


For service metadata packages, the HardwareID values represent the mobile network operator in the form of the following:

-   GSM networks: IMSI value

-   GSM networks: ICCID value

-   CDMA networks: Provider name value

-   CDMA networks: Provider ID value (also known as a SID)

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<HardwareID>
  text
</HardwareID>
```

## <span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes


There are no attributes.

## <span id="Text_value"></span><span id="text_value"></span><span id="TEXT_VALUE"></span>Text value


Generating the proper hardware ID values as part of metadata creation involves a complex algorithm. You should generate hardware ID values by using MBIDGenerator.exe included in the Windows Driver Kit (WDK).

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
<td><p>[HardwareIDList](hardwareidlist.md)</p></td>
<td><p>The [HardwareIDList](hardwareidlist.md) element specifies one or more hardware identification strings for the service metadata package.</p></td>
</tr>
</tbody>
</table>

 

## <span id="XSD"></span><span id="xsd"></span>XSD


``` syntax
<xs:element name="HardwareID" type="tns:HardwareIDType" maxOccurs="unbounded" />

<xs:simpleType name="HardwareIDType">
  <xs:restriction base="xs:string">
    <xs:minLength value="1" />
    <xs:maxLength value="207" />
    <xs:pattern value="^([a-zA-Z0-9!#$%&amp;()*+\-./:;&lt;=&gt;?@[\\\]^_`{|}~])*$" /> 
  </xs:restriction>
</xs:simpleType>
```

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


-   Hardware IDs that are included in PackageInfo.xml must have the “DOID:” prefix added to them. For example: DOID:MBAE:0:*hashednumber1*

-   More than one HardwareID element can be used to specify a service.

-   For GSM IMSI or ICCID ranges, the start range value must end in 00 and the end range value must end in 99. For privacy reasons, matching occurs in blocks of 100 for IMSI and ICCID values.

The HardwareID element is required.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20HardwareID%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




