---
title: WindowsInfo
description: WindowsInfo
ms.assetid: 62b3a7d3-503e-4815-aadb-8c67318c54e0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WindowsInfo

[!include[MBAE deprecation warning](mbae-deprecation-warning.md)]

The WindowsInfo element is the parent element of the [WindowsInfo XML schema](windowsinfo-xml-schema.md).

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<WindowsInfo>
  child elements
</WindowsInfo>
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

 

## <span id="Parent_elements"></span><span id="parent_elements"></span><span id="PARENT_ELEMENTS"></span>Parent elements


There are no parent elements.

## <span id="XSD"></span><span id="xsd"></span>XSD


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

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


The WindowsInfo element is required.

 

 





