---
title: EnableAutoPlayForRegisteredApps
description: EnableAutoPlayForRegisteredApps
ms.date: 04/20/2017
---

# EnableAutoPlayForRegisteredApps

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

The EnableAutoPlayForRegisteredApps element specifies whether AutoPlay is enabled for registered apps.

## Usage


``` syntax
<EnableAutoPlayForRegisteredApps>
  text
</EnableAutoPlayForRegisteredApps>
```

## Attributes


There are no attributes.

## Text value


A Boolean value of either “true” or “false”.

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
<xs:element name="EnableAutoPlayForRegisteredApps" type ="xs:boolean" default="false"/>
```

## Remarks


This element is only applicable on Windows 8.1 and Windows 10.

The EnableAutoPlayForRegisteredApps element is optional.

 

 





