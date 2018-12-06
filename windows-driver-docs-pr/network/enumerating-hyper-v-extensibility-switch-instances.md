---
title: Enumerating Hyper-V Extensible Switch Instances
description: Enumerating Hyper-V Extensible Switch Instances
ms.assetid: 1C4FE71E-689C-4BE8-BDA8-FFC318E37A26
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enumerating Hyper-V Extensible Switch Instances


The [Get-VMSwitch](http://technet.microsoft.com/library/hh848499.aspx) PowerShell cmdlet enumerates the Hyper-V virtual networks that have been created. One or more Hyper-V child partitions can be assigned to each virtual network. The Hyper-V virtualization stack creates an instance of a Hyper-V extensible switch for a virtual network when the first Hyper-V child partition that is assigned to the network is started.

The [Get-VMSwitch](http://technet.microsoft.com/library/hh848499.aspx) cmdlet uses the following syntax:

``` syntax
Get-VMSwitch [[-Name] <string>] [-SwitchType <VMSwitchType[]>] [[-ResourcePoolName] <string[]>] [-ComputerName
    <string[]>] [<CommonParameters>]

Get-VMSwitch [[-Id] <Guid[]>] [-SwitchType <VMSwitchType[]>] [[-ResourcePoolName] <string[]>] [-ComputerName
    <string[]>] [<CommonParameters>]
```

The following example shows the output from the [Get-VMSwitch](http://technet.microsoft.com/library/hh848499.aspx) cmdlet.

``` syntax
PS C:\Windows\system32> Get-VMSwitch

Name                           Learnable Status
                               Addresses
----                           --------- ------
Virtual Network - 1            2048      {OK}
Virtual Network - 2            2048      {OK}
```

## Related topics


[Get-VMSwitch](http://technet.microsoft.com/library/hh848499.aspx)

[**Msvm\_VirtualEthernetSwitch**](https://msdn.microsoft.com/library/hh850242)

 

 






