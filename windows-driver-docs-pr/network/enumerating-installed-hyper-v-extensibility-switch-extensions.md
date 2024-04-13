---
title: Enumerating Hyper-V Extensible Switch Extensions
description: Enumerating Hyper-V Extensible Switch Extensions
ms.date: 04/20/2017
---

# Enumerating Hyper-V Extensible Switch Extensions


The [Get-VMSwitchExtension](/powershell/module/hyper-v/get-vmsystemswitchextension) PowerShell cmdlet enumerates the Hyper-V extensible switch extensions that are currently bound to an instance of an extensible switch. This cmdlet also reports whether the extension is enabled in the extensible switch instance.

The [Get-VMSwitchExtension](/powershell/module/hyper-v/get-vmsystemswitchextension) cmdlet uses the following syntax:

``` syntax
Get-VMSwitchExtension [[-VMSwitchName] <string[]>] [[-Name] <string[]>] [-ComputerName <string[]>]
    [<CommonParameters>]

Get-VMSwitchExtension [[-VMSwitch] <VMSwitch[]>] [-ComputerName <string[]>] [<CommonParameters>]
```

The following example shows the output from the [Get-VMSwitchExtension](/powershell/module/hyper-v/get-vmsystemswitchextension) cmdlet.

``` syntax
PS C:\Windows\system32> Get-VMSwitchExtension PrivateNetwork | fl -property @("Name","ExtensionType", "SwitchName","Enabled")

Name          : NDIS Capture LightWeight Filter
ExtensionType : Capture
SwitchName    : PrivateNetwork
Enabled       : False

Name          : Switch Extensibility Test Extension 2
ExtensionType : Filter
SwitchName    : PrivateNetwork
Enabled       : False

Name          : Switch Extensibility Test Extension 1
ExtensionType : Filter
SwitchName    : PrivateNetwork
Enabled       : False

Name          : WFP extensible switch Layers LightWeight Filter
ExtensionType : Filter
SwitchName    : PrivateNetwork
Enabled       : True
```

**Note**  In order to minimize the amount of information, the example pipes the returned extension objects through the filter command "fl". This causes a subset of information to be displayed that matches the attributes of the **-property** switch.

 

## Related topics


[Get-VMSwitchExtension](/powershell/module/hyper-v/get-vmsystemswitchextension)

[**Msvm\_EthernetSwitchExtension**](/windows/desktop/HyperV_v2/msvm-ethernetswitchextension)

 

