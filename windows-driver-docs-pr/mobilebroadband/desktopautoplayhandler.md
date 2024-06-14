---
title: DesktopAutoplayHandler
description: DesktopAutoplayHandler
ms.date: 04/20/2017
---

# DesktopAutoplayHandler

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

The DesktopAutoplayHandler element specifies a desktop app that should appear as the recommended AutoPlay action when the device is connected and no default action is set. The AutoPlay event is raised whenever a user plugs in a device.

## Usage


``` syntax
<DesktopAutoplayHandler>
  text
</DesktopAutoplayHandler>
```

## Attributes


There are no attributes.

## Text value


String indicating the desktop app that handles the AutoPlay event.

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
<td><p><a href="windowsinfo.md" data-raw-source="[WindowsInfo](windowsinfo.md)">WindowsInfo</a></p></td>
<td><p>The parent element of the <a href="windowsinfo-xml-schema.md" data-raw-source="[WindowsInfo XML schema](windowsinfo-xml-schema.md)">WindowsInfo XML schema</a>.</p></td>
</tr>
</tbody>
</table>

 

## XSD


``` syntax
<xs:element name="DesktopAutoplayHandler" type="xs:string" />
```

## Remarks


You specify the desktop AutoPlay Handler string in the DesktopAutoplayHandler element when you set the desktop app. You can retrieve the string from the handler subkey name that is registered under the following registry key:

``` syntax
HKLM\Software\Microsoft\Windows\CurrentVersion\Explorer\AutoplayHandlers\Handlers
```

The DesktopAutoplayHandler element is optional.

 

 





