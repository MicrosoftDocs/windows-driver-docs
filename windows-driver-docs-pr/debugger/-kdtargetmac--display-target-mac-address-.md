---
title: .kdtargetmac (Display Target MAC Address)
description: Display Target MAC Address.
ms.assetid: 95042682-BD92-44B0-AAA8-AB8661393230
keywords: [".kdtargetmac (Display Target MAC Address) Windows Debugging"]
ms.author: domars
ms.date: 05/21/2018
topic_type:
- apiref
api_name:
- .kdtargetmac (Display Target MAC Address)
api_type:
- NA
ms.localizationpriority: medium
---

# .kdtargetmac (Display Target MAC Address)


Display Target MAC Address

```dbgcmd
.kdtargetmac 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>kernel mode only</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live debugging only</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

Use the .kdtargetmac command to display the MAC (media access control) address of the target system.

```dbgcmd
0: kd> .kdtargetmac 

The target machine MAC address in open-device format is: XXXXXXXXXXXX
```

The .kdtargetmac is command is available if KDNET is enabled on the target system. Use the BCDEdit command with the /dbgsettings option to display the configuration on the target system. A debugtype of *NET* indicates that KDNET is configured.

```dbgcmd
C:\WINDOWS\system32>bcdedit /dbgsettings
key                     1.2.3.4
debugtype               NET
hostip                  192.168.1.10
port                    50000
dhcp                    Yes
The operation completed successfully.
```

For more information, see [Setting Up KDNET Network Kernel Debugging Manually](setting-up-a-network-debugging-connection.md).

Remarks
-------

Knowing the MAC address of the target system can be useful for network tracing and other utilities.

 

 





