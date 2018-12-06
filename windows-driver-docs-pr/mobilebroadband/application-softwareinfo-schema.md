---
title: Application (SoftwareInfo)
description: Application (SoftwareInfo)
ms.assetid: 1f16a690-4453-4563-a4b1-44bbd5d02f47
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Application (SoftwareInfo)

[!include[MBAE deprecation warning](mbae-deprecation-warning.md)]

The Application element specifies the associated device notification handler.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<Application Id=”tns:ApplicationIdType”>
  Child element
</Application>
```

## <span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes


<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Id</p></td>
<td><p>tns:ApplicationIdType</p></td>
<td><p>Yes</p></td>
<td><p>The ID of the application.</p></td>
</tr>
</tbody>
</table>

 

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
<td><p><a href="devicenotificationhandlers.md" data-raw-source="[DeviceNotificationHandlers](devicenotificationhandlers.md)">DeviceNotificationHandlers</a></p></td>
<td><p>Specifies a list of device notification handlers.</p></td>
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
<td><p><a href="applications.md" data-raw-source="[Applications](applications.md)">Applications</a></p></td>
<td><p>Specifies the app that will be downloaded when the operator’s Mobile Broadband hardware is detected on the PC.</p></td>
</tr>
</tbody>
</table>

 

## <span id="XSD"></span><span id="xsd"></span>XSD


``` syntax
<xs:element name="Application" type="tns:ApplicationType"/>

<xs:complexType name="ApplicationType">
  <xs:sequence>
    <xs:element name="DeviceNotificationHandlers" type="tns:DeviceNotificationHandlersType" minOccurs="0" />
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
  </xs:sequence>
  <xs:attribute name="Id" type="tns:ApplicationIdType" use="required"/>
</xs:complexType>
```

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


The Application element is optional.

 

 





