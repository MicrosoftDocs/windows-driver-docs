---
title: DesktopAutoplayHandler
description: DesktopAutoplayHandler
ms.assetid: e1a07580-36dd-4618-b522-3f7605c9b87b
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DesktopAutoplayHandler

[!include[MBAE deprecation warning](mbae-deprecation-warning.md)]

The DesktopAutoplayHandler element specifies a desktop app that should appear as the recommended AutoPlay action when the device is connected and no default action is set. The AutoPlay event is raised whenever a user plugs in a device.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<DesktopAutoplayHandler>
  text
</DesktopAutoplayHandler>
```

## <span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes


There are no attributes.

## <span id="Text_value"></span><span id="text_value"></span><span id="TEXT_VALUE"></span>Text value


String indicating the desktop app that handles the AutoPlay event.

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
<td><p><a href="windowsinfo.md" data-raw-source="[WindowsInfo](windowsinfo.md)">WindowsInfo</a></p></td>
<td><p>The parent element of the <a href="windowsinfo-xml-schema.md" data-raw-source="[WindowsInfo XML schema](windowsinfo-xml-schema.md)">WindowsInfo XML schema</a>.</p></td>
</tr>
</tbody>
</table>

 

## <span id="XSD"></span><span id="xsd"></span>XSD


``` syntax
<xs:element name="DesktopAutoplayHandler" type="xs:string" />
```

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


You specify the desktop AutoPlay Handler string in the DesktopAutoplayHandler element when you set the desktop app. You can retrieve the string from the handler subkey name that is registered under the following registry key:

``` syntax
HKLM\Software\Microsoft\Windows\CurrentVersion\Explorer\AutoplayHandlers\Handlers
```

The DesktopAutoplayHandler element is optional.

 

 





