---
title: NetworkConfiguration
description: NetworkConfiguration
ms.assetid: 4a52b185-1bfb-4626-99fb-6be364e88e85
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NetworkConfiguration

[!include[MBAE deprecation warning](mbae-deprecation-warning.md)]

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
<td><p><a href="mobilebroadbandprofiles.md" data-raw-source="[MobileBroadbandProfiles](mobilebroadbandprofiles.md)">MobileBroadbandProfiles</a></p></td>
<td><p>Specifies the purchase and Internet mobile broadband profiles to be used.</p></td>
</tr>
<tr class="even">
<td><p><a href="allowstandarduserpinunlock.md" data-raw-source="[AllowStandardUserPinUnlock](allowstandarduserpinunlock.md)">AllowStandardUserPinUnlock</a></p></td>
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
<td><p><a href="mobilebroadbandinfo.md" data-raw-source="[MobileBroadbandInfo](mobilebroadbandinfo.md)">MobileBroadbandInfo</a></p></td>
<td><p>The <a href="mobilebroadbandinfo.md" data-raw-source="[MobileBroadbandInfo](mobilebroadbandinfo.md)">MobileBroadbandInfo</a> element is the parent element of the <a href="mobilebroadbandinfo-xml-schema.md" data-raw-source="[MobileBroadbandInfo XML schema](mobilebroadbandinfo-xml-schema.md)">MobileBroadbandInfo XML schema</a>.</p></td>
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

 

 





