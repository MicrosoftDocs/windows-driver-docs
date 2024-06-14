---
title: WindowsInfo
description: WindowsInfo
ms.date: 04/20/2017
---

# WindowsInfo

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

The WindowsInfo element is the parent element of the [WindowsInfo XML schema](windowsinfo-xml-schema.md).

## Usage


``` syntax
<WindowsInfo>
  child elements
</WindowsInfo>
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
<td><p><a href="showdeviceindisconnectedstate.md" data-raw-source="[ShowDeviceInDisconnectedState](showdeviceindisconnectedstate.md)">ShowDeviceInDisconnectedState</a></p></td>
<td><p>This value should be set to <strong>false</strong> because it does not apply to service metadata packages in Windows 8, Windows 8.1, and Windows 10.</p></td>
</tr>
<tr class="even">
<td><p><a href="launchdevicestageondeviceconnect.md" data-raw-source="[LaunchDeviceStageOnDeviceConnect](launchdevicestageondeviceconnect.md)">LaunchDeviceStageOnDeviceConnect</a></p></td>
<td><p>This value should be set to <strong>false</strong> because it does not apply to service metadata packages in Windows 8, Windows 8.1, and Windows 10.</p></td>
</tr>
<tr class="odd">
<td><p><a href="launchdevicestagefromexplorer.md" data-raw-source="[LaunchDeviceStageFromExplorer](launchdevicestagefromexplorer.md)">LaunchDeviceStageFromExplorer</a></p></td>
<td><p>This value should be set to <strong>false</strong> because it does not apply to service metadata packages in Windows 8, Windows 8.1, and Windows 10.</p></td>
</tr>
</tbody>
</table>

 

## Parent elements


There are no parent elements.

## XSD


``` syntax
<xs:element name="WindowsInfo" type="tns:WindowsInfoType" />

<xs:complexType name="WindowsInfoType">
  <xs:sequence>
    <xs:element name="ShowDeviceInDisconnectedState" type="xs:boolean" default="false" />
    <xs:element name="LaunchDeviceStageOnDeviceConnect" type="xs:boolean" default="false" minOccurs="0" />
    <xs:element name="LaunchDeviceStageFromExplorer" type="xs:boolean" default="false" minOccurs="0" />
    <xs:element ref="v2:LaunchApplicationOnDeviceConnect" minOccurs="0" />
    <xs:element ref="v2:WindowsHardwareLogoCertified" minOccurs="0" />
  </xs:sequence>
</xs:complexType>
```

## Remarks


The WindowsInfo element is required.

 

 





