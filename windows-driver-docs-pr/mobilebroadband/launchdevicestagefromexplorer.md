---
title: LaunchDeviceStageFromExplorer
description: LaunchDeviceStageFromExplorer
ms.date: 04/20/2017
---

# LaunchDeviceStageFromExplorer

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

The LaunchDeviceStageFromExplorer element should be set to **false** because it does not apply to service metadata packages in Windows 8, Windows 8.1, and Windows 10.

## Usage


``` syntax
<LaunchDeviceStageFromExplorer>
  text
</LaunchDeviceStageFromExplorer>
```

## Attributes


There are no attributes.

## Text value


Should be set to **false** because it does not apply to service metadata packages in Windows 8, Windows 8.1, and Windows 10.

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
<xs:element name="LaunchDeviceStageFromExplorer" type="xs:boolean" default="false" />
```

## Remarks


The LaunchDeviceStageFromExplorer element is optional.

 

 





