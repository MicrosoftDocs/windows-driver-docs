---
title: Enumerating Hyper-V Extensible Switch Instances
description: Enumerating Hyper-V Extensible Switch Instances
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enumerating Hyper-V Extensible Switch Instances


The [Get-VMSwitch](/powershell/module/hyper-v/get-vmswitch) PowerShell cmdlet enumerates the Hyper-V virtual networks that have been created. One or more Hyper-V child partitions can be assigned to each virtual network. The Hyper-V virtualization stack creates an instance of a Hyper-V extensible switch for a virtual network when the first Hyper-V child partition that is assigned to the network is started.

The [Get-VMSwitch](/powershell/module/hyper-v/get-vmswitch) cmdlet uses the following syntax:

``` syntax
Get-VMSwitch [[-Name] <string>] [-SwitchType <VMSwitchType[]>] [[-ResourcePoolName] <string[]>] [-ComputerName
    <string[]>] [<CommonParameters>]

Get-VMSwitch [[-Id] <Guid[]>] [-SwitchType <VMSwitchType[]>] [[-ResourcePoolName] <string[]>] [-ComputerName
    <string[]>] [<CommonParameters>]
```

The following example shows the output from the [Get-VMSwitch](/powershell/module/hyper-v/get-vmswitch) cmdlet.

``` syntax
PS C:\Windows\system32> Get-VMSwitch

Name                           Learnable Status
                               Addresses
----                           --------- ------
Virtual Network - 1            2048      {OK}
Virtual Network - 2            2048      {OK}
```

## Related topics


[Get-VMSwitch](/powershell/module/hyper-v/get-vmswitch)

[**Msvm\_VirtualEthernetSwitch**](/windows/desktop/HyperV_v2/msvm-virtualethernetswitch)

 

