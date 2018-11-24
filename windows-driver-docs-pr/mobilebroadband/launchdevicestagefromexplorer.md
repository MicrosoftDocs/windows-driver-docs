---
title: LaunchDeviceStageFromExplorer
description: LaunchDeviceStageFromExplorer
ms.assetid: 8c1d16e5-e183-4658-8379-09bfed9fe975
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# LaunchDeviceStageFromExplorer

[!include[MBAE deprecation warning](mbae-deprecation-warning.md)]

The LaunchDeviceStageFromExplorer element should be set to **false** because it does not apply to service metadata packages in Windows 8, Windows 8.1, and Windows 10.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<LaunchDeviceStageFromExplorer>
  text
</LaunchDeviceStageFromExplorer>
```

## <span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes


There are no attributes.

## <span id="Text_value"></span><span id="text_value"></span><span id="TEXT_VALUE"></span>Text value


Should be set to **false** because it does not apply to service metadata packages in Windows 8, Windows 8.1, and Windows 10.

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
<xs:element name="LaunchDeviceStageFromExplorer" type="xs:boolean" default="false" />
```

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


The LaunchDeviceStageFromExplorer element is optional.

 

 





