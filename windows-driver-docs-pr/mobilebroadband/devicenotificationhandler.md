---
title: DeviceNotificationHandler
description: DeviceNotificationHandler
ms.assetid: 04c4edb5-6dd1-4810-b23a-4f7ddc8af338
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DeviceNotificationHandler

[!include[MBAE deprecation warning](mbae-deprecation-warning.md)]

The DeviceNotificationHandler element specifies a device notification handler. A device notification handler allows you to run code in response to events, such as mobile network operator administrative SMS or USSD notifications, even if the Microsoft Store app is not running. For more information about implementing a notification handler, see the [Mobile Operator Notifications](http://go.microsoft.com/fwlink/?linkid=242062) white paper.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<DeviceNotificationHandler EventID=”xs:string” EventAsset=”xs:string”/>
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
<td><p>EventID</p></td>
<td><p>xs:string</p></td>
<td><p>Yes</p></td>
<td><p>The event ID for the device notification handler.</p></td>
</tr>
<tr class="even">
<td><p>EventAsset</p></td>
<td><p>xs:string</p></td>
<td><p>Yes</p></td>
<td><p>The event asset for the device notification handler.</p></td>
</tr>
</tbody>
</table>

 

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
<td><p><a href="devicenotificationhandlers.md" data-raw-source="[DeviceNotificationHandlers](devicenotificationhandlers.md)">DeviceNotificationHandlers</a></p></td>
<td><p>Specifies the device notification handlers.</p></td>
</tr>
</tbody>
</table>

 

## <span id="XSD"></span><span id="xsd"></span>XSD


``` syntax
<xs:element name="DeviceNotificationHandler" type="tns:DeviceNotificationHandlerType" maxOccurs="unbounded" />

<xs:complexType name="DeviceNotificationHandlerType">
  <xs:attribute name="EventID" type="xs:string" use="required"/>
  <xs:attribute name="EventAsset" type="xs:string" use="required"/>
</xs:complexType>
```

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


-   When you specify the DeviceNotificationHandler in the [Application](application-softwareinfo-schema.md) element, the system calls the event handler and invokes the event when the device changes to the state.

-   The **EventID** attribute is the SMSEventHandler for the SMS device case.

-   The **EventAsset** attribute is the same value that you specify in the app manifest as an extension of Windows.BackgroundTasks.

The DeviceNotificationHandler element is optional.

 

 





