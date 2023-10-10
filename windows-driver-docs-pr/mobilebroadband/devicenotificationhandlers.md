---
title: DeviceNotificationHandlers
description: DeviceNotificationHandlers
ms.date: 04/20/2017
---

# DeviceNotificationHandlers

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

The DeviceNotificationHandlers element specifies the device notification handlers.

## Usage


``` syntax
<DeviceNotificationHandlers>
  Child element
</DeviceNotificationHandlers>
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
<td><p><a href="devicenotificationhandler.md" data-raw-source="[DeviceNotificationHandler](devicenotificationhandler.md)">DeviceNotificationHandler</a></p></td>
<td><p>Specifies a device notification handler.</p></td>
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
<td><p><a href="application-softwareinfo-schema.md" data-raw-source="[Application](application-softwareinfo-schema.md)">Application</a></p></td>
<td><p>Specifies the app that will be downloaded when the operator’s Mobile Broadband hardware is detected on the PC.</p></td>
</tr>
</tbody>
</table>

 

## XSD


``` syntax
<xs:element name="DeviceNotificationHandlers" type="tns:DeviceNotificationHandlersType" minOccurs="0" />

<xs:complexType name="DeviceNotificationHandlersType">
  <xs:sequence>
    <xs:element name="DeviceNotificationHandler" type="tns:DeviceNotificationHandlerType" maxOccurs="unbounded" />
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
  </xs:sequence>
</xs:complexType>
```

## Remarks


The DeviceNotificationHandlers element is optional.

 

 





