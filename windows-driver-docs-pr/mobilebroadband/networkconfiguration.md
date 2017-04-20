---
title: NetworkConfiguration
description: NetworkConfiguration
ms.assetid: 4a52b185-1bfb-4626-99fb-6be364e88e85
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NetworkConfiguration


The NetworkConfiguration element specifies the purchase and Internet mobile broadband profiles to be used. The files that are referenced in this element should be included in the **ServiceInformation** directory. These files help in getting users connected to the operator network. It also specifies whether standard users should be allowed to perform PIN unlock operations on their Mobile Broadband SIMs.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<NetworkConfiguration>
  child elements
</NetworkConfiguration>
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
<td><p>[MobileBroadbandProfiles](mobilebroadbandprofiles.md)</p></td>
<td><p>Specifies the purchase and Internet mobile broadband profiles to be used.</p></td>
</tr>
<tr class="even">
<td><p>[AllowStandardUserPinUnlock](allowstandarduserpinunlock.md)</p></td>
<td><p>Specifies whether standard users should be allowed to perform PIN unlock operations on their Mobile Broadband SIMs.</p></td>
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
<td><p>[MobileBroadbandInfo](mobilebroadbandinfo.md)</p></td>
<td><p>The [MobileBroadbandInfo](mobilebroadbandinfo.md) element is the parent element of the [MobileBroadbandInfo XML schema](mobilebroadbandinfo-xml-schema.md).</p></td>
</tr>
</tbody>
</table>

 

## <span id="XSD"></span><span id="xsd"></span>XSD


``` syntax
<xs:element name="NetworkConfiguration" type="tns:NetworkConfigType" minOccurs="0" />

<xs:complexType name="NetworkConfigType">
  <xs:sequence>
    <xs:element name="MobileBroadbandProfiles" type="tns:MobileBroadbandProfilesType" minOccurs="0" />
    <xs:element name="AllowStandardUserPinUnlock" type="xs:boolean" minOccurs="0" />
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
  </xs:sequence>
</xs:complexType>
```

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


-   In order to set a plan purchase APN or an Internet connection APN, the mobile network operator (MNO) should specify the XML profiles that correspond to these states as part of this element.

-   The child elements in this element are optional. If these are not specified, the APN values from the APN database included with Windows are used to help the user get connected.

-   Typically, only users in the Administrators security group are allowed to perform PIN unlock operations on their Mobile Broadband SIMs. However, setting the [AllowStandardUserPinUnlock](allowstandarduserpinunlock.md) element to true allows the mobile operator to specify whether standard users are allowed to perform this function.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20NetworkConfiguration%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




