---
title: Disabling Hyper-V Extensible Switch Extensions
description: Disabling Hyper-V Extensible Switch Extensions
ms.date: 04/20/2017
---

# Disabling Hyper-V Extensible Switch Extensions


The [Disable-VMSwitchExtension](/powershell/module/hyper-v/disable-vmswitchextension) PowerShell cmdlet disables an extension on a specific instance of an extensible switch.

The [Disable-VMSwitchExtension](/powershell/module/hyper-v/disable-vmswitchextension) cmdlet uses the following syntax:

``` syntax
Disable-VMSwitchExtension [-VMSwitchExtensionName] <string[]> [-ComputerName <string[]>] [<CommonParameters>]

Disable-VMSwitchExtension [-VMSwitchExtensionName] <string[]> [-VMSwitchName] <string[]> [-ComputerName
    <string[]>] [<CommonParameters>]

Disable-VMSwitchExtension [-VMSwitchExtensionName] <string[]> [-VMSwitch] <VMSwitch[]> [-ComputerName <string[]>]
    [<CommonParameters>]

Disable-VMSwitchExtension [-VMSwitchExtension] <VMSwitchExtension[]> [-ComputerName <string[]>]
    [<CommonParameters>]
```

The following shows an example of how to use the [Disable-VMSwitchExtension](/powershell/module/hyper-v/disable-vmswitchextension) cmdlet.

``` syntax
PS C:\Windows\system32> Disable-VMSwitchExtension "Switch Extensibility Test Extension 1" PrivateNetwork

PS C:\Windows\system32> Get-VMSwitchExtension PrivateNetwork "Switch Extensibility Test Extension 1" | fl -property @("Name","ExtensionType", "SwitchName","Enabled")

Name          : Switch Extensibility Test Extension 1
ExtensionType : Filter
SwitchName    : PrivateNetwork
Enabled       : False
```

## Related topics


[Disable-VMSwitchExtension](/powershell/module/hyper-v/disable-vmswitchextension)

[Get-VMSwitchExtension](/powershell/module/hyper-v/get-vmsystemswitchextension)

[**Msvm\_EthernetSwitchExtension**](/windows/desktop/HyperV_v2/msvm-ethernetswitchextension)

 

