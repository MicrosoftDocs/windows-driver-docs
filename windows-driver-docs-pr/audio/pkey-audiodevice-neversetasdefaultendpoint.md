---
title: PKEY\_AudioDevice\_NeverSetAsDefaultEndpoint
description: PKEY\_AudioDevice\_NeverSetAsDefaultEndpoint
ms.assetid: cb619972-d9d9-4f33-bb4a-720bfc29e3e8
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# PKEY\_AudioDevice\_NeverSetAsDefaultEndpoint


You might decide to set up certain devices so that they can never be selected as default devices. These include, for example, modem lines and medical audio devices.Windows 7 and later versions of Windows provide the **PKEY\_AudioDevice\_NeverSetAsDefaultEndpoint** registry key to allow you to prevent the selection of the endpoint of a device as the default endpoint.

The following INF file excerpt shows how to use **PKEY\_AudioDevice\_NeverSetAsDefaultEndpoint** to set up an endpoint so that it can never be selected as default.

```inf
[Version]
Signature="$Windows NT$"
Class=MEDIA
ClassGuid= {4d36e96c-e325-11ce-bfc1-08002be10318}
...

[USBAudio]
...

[USBAudio.Interfaces]
AddInterface=%KSCATEGORY_AUDIO%,”GLOBAL”,USBAudio.Interface
...

[USBAudio.Interface]
AddReg=Xyz.AddReg
...

;; AddReg section to setup endpoint so that
;; it cannot be selected as the default endpoint.
[Xyz.AddReg]
HKR,"EP\\n",%PKEY_AudioEndpoint_Association%,,%KSNODETYPE_GUID%
HKR,"EP\\n",%PKEY_AudioDevice_NeverSetAsDefaultEndpoint%,0x00010001,NeverSetAsDefaultEndpointMaskValue
...

[Strings]
KSCATEGORY_AUDIO=” {6994AD04-93EF-11D0-A3CC-00A0C9223196}”
PKEY_AudioEndpoint_Association="{1DA5D803-D492-4EDD-8C23-E0C0FFEE7F0E},2"
PKEY_AudioDevice_NeverSetAsDefaultEndpoint = "{F3E80BEF-1723-4FF2-BCC4-7F83DC5E46D4},3"
...
```

In the preceding example, NeverSetAsDefaultEndpointMaskValue represents a DWORD mask value that is a combination of device role flags and data flow flags.

The following INF file snippet shows how an undefined output device (KSNODETYPE\_OUTPUT\_UNDEFINED) is set up so that its endpoint is never selected as default, regardless of the device role and the data flow direction.

```inf
[Version]
Signature="$Windows NT$"
Class=MEDIA
ClassGuid= {4d36e96c-e325-11ce-bfc1-08002be10318}
...

[USBAudio]
...

[USBAudio.Interfaces]
AddInterface=%KSCATEGORY_AUDIO%,”GLOBAL”,USBAudio.Interface
...

[USBAudio.Interface]
AddReg=MDVAD.EPProperties.AddReg
...

;; AddReg section to setup endpoint so that
;; it cannot be selected as the default endpoint.
[MDVAD.EPProperties.AddReg]
HKR,"EP\\0",%PKEY_AudioEndpoint_Association%,,%KSNODETYPE_OUTPUT_UNDEFINED%
HKR,"EP\\0",%PKEY_AudioDevice_NeverSetAsDefaultEndpoint%,0x00010001,0x00000305
...

[Strings]
KSCATEGORY_AUDIO=” {6994AD04-93EF-11D0-A3CC-00A0C9223196}”
KSNODETYPE_OUTPUT_UNDEFINED="{DFF21CE0-F70F-11D0-B917-00A0C9223196}"
PKEY_AudioEndpoint_Association="{1DA5D803-D492-4EDD-8C23-E0C0FFEE7F0E},2"
PKEY_AudioDevice_NeverSetAsDefaultEndpoint = "{F3E80BEF-1723-4FF2-BCC4-7F83DC5E46D4},3"
```

In the preceding example, 0x00000305 is the bitwise OR combination of all the flags and masks available for **PKEY\_AudioDevice\_NeverSetAsDefaultEndpoint**. The following table shows the flags and masks and their values.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Flag or endpoint mask</th>
<th align="left">Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>FLOW_MASK_CAPTURE</p></td>
<td align="left"><p>0x00000200</p></td>
</tr>
<tr class="even">
<td align="left"><p>FLOW_MASK_RENDER</p></td>
<td align="left"><p>0x00000100</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ROLE_MASK_COMMUNICATION</p></td>
<td align="left"><p>0x00000004</p></td>
</tr>
<tr class="even">
<td align="left"><p>ROLE_MASK_CONSOLE</p></td>
<td align="left"><p>0x00000001</p></td>
</tr>
</tbody>
</table>

 

 

 





