---
title: Custom Switch Feature Status
description: Custom Switch Feature Status
ms.assetid: 2362EE05-9CC9-451D-80D1-C18CC9274BAB
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Custom Switch Feature Status


The Hyper-V platform and Hyper-V extensible switch interface provide the infrastructure to obtain custom status information for an extensible switch. This information is known as *switch feature status* information.

Custom switch feature status definitions are registered with the WMI management layer by using managed object format (MOF) class definitions. In addition to the structure members that define the attributes of the custom switch feature status definition, the MOF class must also contain the following:

-   A UUID that uniquely identifies the custom switch feature status definition.

-   A GUID that uniquely identifies the extensible switch extension. This GUID is declared as the **ExtensionId** qualifier of the MOF class and must match the value of the **NetCfgInstanceId** entry that is declared in the extension's INF file.

-   A descriptive class name string. The name of the vendor must be included in the string.

The following shows an example of a MOF class for a custom feature status definition of an extensible switch.

```C++
#pragma namespace("\\\\.\\root\\virtualization\\v2")

[ Dynamic,
  UUID("B3E57D77-8E95-4977-97DE-524F8DAF03E4"),
  ExtensionId("5CBF81BE-5055-47CD-9055-A76B2B4E369E"), 
  Provider("VmmsWmiInstanceAndMethodProvider"), 
  InterfaceVersion("1"),
  InterfaceRevison("0"),
  Locale(0x409),
  Description(
   "Fabricam, Inc. Switch custom feature status description.") : Amended,
  DisplayName("Fabricam, Inc. Switch custom feature status friendly name.") : Amended]
class Fabrikam_CustomSwitchData  : Msvm_EthernetSwitchFeatureSettingData{
    [ Read,
       Write,
       WmiDataId(1),
       InterfaceVersion("1"),
       InterfaceRevision("0"),
       Description(
         "The current status of custom feature on this switch.") : Amended]
     uint32 CurrentStatus = 0 ;
};
```

The MOF classes for custom feature status definition of an extensible switch are registered in the common information model (CIM) repository by using the MOF compiler (Mofcomp.exe). After it is registered, the MOF class can be configured through PowerShell cmdlets and WMI-based application programs.

The following example shows the commands that must be entered to register a file (Fabrikam\_CustomSwitchData.mof) that contains the MOF class for a custom switch feature status definition.

```PowerShell
net stop vmms
mofcomp -N:root\virtualization\v2 Fabrikam_CustomSwitchData.mof
net start vmms
```

For more information about how to use the MOF compiler, see [Compiling a Driver's MOF File](https://msdn.microsoft.com/library/windows/hardware/ff542012).

The following example shows how you can use the custom switch feature status definition to obtain switch data. In this example, the Fabrikam\_CustomSwitchData MOF class is used to obtain switch status from a switch named “TestSwitch”. The Fabrikam, Inc. extension is enabled on the vSwitch “TestSwitch”, and is returning 123 for the status.

```PowerShell
PS C:\> $switchData = Get-VMSwitchExtensionSwitchData -SwitchName TestSwitch -FeatureId B3E57D77-8E95-4977-97DE-524F8DAF03E4
# Output the current value
PS C:\> $switchData$customSwitchData.Data.CurrentStatus
123
```

For more information on how extensible switch extensions manage switch feature status information, see [Managing Custom Switch Feature Status Information](managing-custom-switch-feature-status-information.md).

 

 





