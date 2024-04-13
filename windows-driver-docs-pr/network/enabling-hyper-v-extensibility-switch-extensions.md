---
title: Enabling Hyper-V Extensible Switch Extensions
description: Enabling Hyper-V Extensible Switch Extensions
ms.date: 04/20/2017
---

# Enabling Hyper-V Extensible Switch Extensions


When Hyper-V extensible switch extensions are installed, they are bound to each instance of an extensible switch. However, the extensions are disabled by default and must be explicitly enabled on each extensible switch instance.

The [Enable-VMSwitchExtension](/powershell/module/hyper-v/enable-vmswitchextension) PowerShell cmdlet enables an extension on a specific instance of an extensible switch. This cmdlet uses the following syntax:

``` syntax
Enable-VMSwitchExtension [-Name] <string[]> [-ComputerName <string[]>] [<CommonParameters>]

Enable-VMSwitchExtension [-Name] <string[]> [-VMSwitchName] <string[]> [-ComputerName <string[]>]
    [<CommonParameters>]

Enable-VMSwitchExtension [-Name] <string[]> [-VMSwitch] <VMSwitch[]> [-ComputerName <string[]>]
    [<CommonParameters>]

Enable-VMSwitchExtension [-VMSwitchExtension] <VMSwitchExtension[]> [-ComputerName <string[]>] [<CommonParameters>]
```

The following shows an example of how to use the Enable-VMSwitchExtension cmdlet.

``` syntax
PS C:\Windows\system32> Enable-VMSwitchExtension "Switch Extensibility Test Extension 1" PrivateNetwork

PS C:\Windows\system32> Get-VMSwitchExtension PrivateNetwork "Switch Extensibility Test Extension 1" | fl -property @("Name","ExtensionType", "SwitchName","Enabled")

Name          : Switch Extensibility Test Extension 1
ExtensionType : Filter
SwitchName    : PrivateNetwork
Enabled       : True
```

**Note**  The Windows Filtering Platform (WFP) in-box filtering extension (Wfplwfs.sys ) is enabled by default on each extensible switch instance.

 

## Related topics


[Enable-VMSwitchExtension](/powershell/module/hyper-v/enable-vmswitchextension)

[Get-VMSwitchExtension](/powershell/module/hyper-v/get-vmsystemswitchextension)

[**Msvm\_EthernetSwitchExtension**](/windows/desktop/HyperV_v2/msvm-ethernetswitchextension)

 

