---
title: DeviceNotificationHandler
description: DeviceNotificationHandler
ms.assetid: 04c4edb5-6dd1-4810-b23a-4f7ddc8af338
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DeviceNotificationHandler


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
<td><p>[DeviceNotificationHandlers](devicenotificationhandlers.md)</p></td>
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20DeviceNotificationHandler%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




