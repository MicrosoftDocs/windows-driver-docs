---
title: Reordering Hyper-V Extensible Switch Extensions
description: Reordering Hyper-V Extensible Switch Extensions
ms.assetid: DAB7FAE0-1632-4FD1-8697-48553A51BD20
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reordering Hyper-V Extensible Switch Extensions


Multiple Hyper-V extensible switch capturing or filtering extensions can be enabled in each instance of an extensible switch.

**Note**  Only one forwarding extension can be enabled in each instance of an extensible switch.

 

By default, multiple capturing or filtering extensions are ordered based on their type and when they were installed. For example, multiple capturing extensions are layered in the extensible switch driver stack with the most recently installed extension closest to the protocol edge of the switch.

When multiple capturing or filtering extensions are installed, you can use PowerShell cmdlets to reorder the drivers in the extensible switch driver stack. The following example shows the commands that you enter from a PowerShell window to do this.

``` syntax
# Show the current order. The ExtensionOrder field contains paths to WMI extension instances.
# The [wmi] operator can be used to convert the paths to full WMI objects. 
PS C:\Windows\system32> $privateNetwork = Get-VMSwitch PrivateNetwork
PS C:\Windows\system32> $extensionOrder = $privateNetwork.ExtensionOrder
PS C:\Windows\system32> $extensionOrder | ForEach-Object { Write-Host "Name:" ([wmi]$_).ElementName }
Name: NDIS Capture LightWeight Filter
Name: Switch Extensibility Test Extension 2
Name: Switch Extensibility Test Extension 1
Name: WFP extensible switch Layers LightWeight Filter

# Place “Test Extension 1” above “Test Extension 2” in the ordered list of extensions.
PS C:\Windows\system32> $tmp = $extensionOrder[1]
PS C:\Windows\system32> $extensionOrder[1] = $extensionOrder[2]
PS C:\Windows\system32> $extensionOrder[2] = $tmp

# Commit the updated order.
PS C:\Windows\system32> $privateNetwork.ExtensionOrder = $extensionOrder

# Retrieve the switch information again to validate the order.
PS C:\Windows\system32> $privateNetwork = Get-VMSwitch PrivateNetwork
PS C:\Windows\system32> $privateNetwork.ExtensionOrder | ForEach-Object { Write-Host "Name:" ([wmi]$_).ElementName }
Name: NDIS Capture LightWeight Filter
Name: Switch Extensibility Test Extension 1
```

## Related topics


[Get-VMSwitch](http://technet.microsoft.com/library/hh848499.aspx)

[**Msvm\_EthernetSwitchExtension**](https://msdn.microsoft.com/library/hh850139)

[**Msvm\_VirtualEthernetSwitchSettingData**](https://msdn.microsoft.com/library/hh850246)

 

 






