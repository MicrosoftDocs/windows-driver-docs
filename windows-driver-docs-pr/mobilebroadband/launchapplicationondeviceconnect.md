---
title: LaunchApplicationOnDeviceConnect
description: LaunchApplicationOnDeviceConnect
ms.assetid: d8a5f20a-bd88-4279-9e15-4f20287edfd4
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# LaunchApplicationOnDeviceConnect

[!include[MBAE deprecation warning](mbae-deprecation-warning.md)]

The LaunchApplicationOnDeviceConnect element specifies an app that should appear as the recommended AutoPlay action when a user plugs in the device.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<LaunchApplicationOnDeviceConnect>
  child elements
</LaunchApplicationOnDeviceConnect>
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
<td><p><a href="autoplayhandler.md" data-raw-source="[AutoplayHandler](autoplayhandler.md)">AutoplayHandler</a></p></td>
<td><p>Specifies a UWP device app that should appear as the recommended AutoPlay action when a user plugs in a device.</p></td>
</tr>
<tr class="even">
<td><p><a href="desktopautoplayhandler.md" data-raw-source="[DesktopAutoplayHandler](desktopautoplayhandler.md)">DesktopAutoplayHandler</a></p></td>
<td><p>Specifies a desktop app that should appear as the recommended AutoPlay action when a user plugs in a device.</p></td>
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
<td><p><a href="windowsinfo.md" data-raw-source="[WindowsInfo](windowsinfo.md)">WindowsInfo</a></p></td>
<td><p>The parent element of the <a href="windowsinfo-xml-schema.md" data-raw-source="[WindowsInfo XML schema](windowsinfo-xml-schema.md)">WindowsInfo XML schema</a>.</p></td>
</tr>
</tbody>
</table>

 

## <span id="XSD"></span><span id="xsd"></span>XSD


``` syntax
<xs:element name="LaunchApplicationOnDeviceConnect" type ="tns:LaunchApplicationOnDeviceConnectType" />

<xs:complexType name="LaunchApplicationOnDeviceConnectType">
    <xs:choice>
      <xs:element name="AutoplayHandler" type="tns:AutoplayHandlerType" />
      <xs:element name="DesktopAutoplayHandler" type="xs:string" />
      <xs:any namespace="##other" processContents="lax" />
    </xs:choice>
  </xs:complexType>
```

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


You must specify either a UWP device app or a desktop app. Use [AutoplayHandler](autoplayhandler.md) if you will specify a UWP device app, and use [DesktopAutoplayHandler](desktopautoplayhandler.md) if you specify a desktop application.

The LaunchApplicationOnDeviceConnect element is optional.

 

 





