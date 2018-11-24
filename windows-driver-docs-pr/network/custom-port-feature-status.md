---
title: Custom Port Feature Status
description: Custom Port Feature Status
ms.assetid: 87E88302-6FEA-4D71-A80D-E7AD6D42C0BE
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Custom Port Feature Status


The Hyper-V platform and Hyper-V extensible switch interface provide the infrastructure to obtain custom status information for an extensible switch port. This information is known as *port feature status* information.

Custom feature status definitions for a Hyper-V extensible switch port property are registered with the WMI management layer by using managed object format (MOF) class definitions. In addition to the structure members that define the attributes of the custom port feature status definition, the MOF class must also contain the following:

-   A UUID that uniquely identifies the custom port feature status definition.

-   A GUID that uniquely identifies the extensible switch extension. This GUID is declared as the **ExtensionId** qualifier of the MOF class and must match the value of the **NetCfgInstanceId** entry that is declared in the extension's INF file.

-   A descriptive class name string. The name of the vendor must be included in the string.

The following shows an example of a MOF class for a custom feature status definition of an extensible switch port.

```C++
#pragma namespace("\\\\.\\root\\virtualization\\v2")

[ Dynamic,
  UUID("DAA0B7CC-74DB-41ef-8354-7002F9FA463E"),
  ExtensionId("5CBF81BE-5055-47CD-9055-A76B2B4E369E"), 
  Provider("VmmsWmiInstanceAndMethodProvider"), 
  InterfaceVersion("1"),
  InterfaceRevison("0"),
  Locale(0x409),
  Description("Fabricam, Inc. port custom feature status description.") : Amended,
  DisplayName("Fabricam, Inc.port custom feature status friendly name.") : Amended]
class Fabrikam_CustomPortData  : Msvm_EthernetPortData {
    [ Read,
       Write,
       WmiDataId(1),
      InterfaceVersion("1"),
      InterfaceRevision("0"),
       Description(
         "The current status of custom feature on this port.") : Amended]
     uint32 CurrentStatus = 0 ;
};
```

The MOF classes for custom feature status definition of a port are registered in the common information model (CIM) repository by using the MOF compiler (Mofcomp.exe). After it is registered, the MOF class can be configured through PowerShell cmdlets and WMI-based application programs.

The following example shows the commands that must be entered to register a file (Fabrikam\_CustomPortData.mof) that contains the MOF class for a custom port feature status definition.

```PowerShell
net stop vmms
mofcomp -N:root\virtualization\v2 Fabrikam_CustomPortData.mof
net start vmms
```

For more information about how to use the MOF compiler, see [Compiling a Driver's MOF File](https://msdn.microsoft.com/library/windows/hardware/ff542012).

The following example shows how you can use the custom port feature status definition to obtain port data. In this example, the Fabrikam\_CustomPortData MOF class is used to obtain port status from a Hyper-V partition named "TestVm". The Fabrikam, Inc. extension is enabled on the vSwitch “TestSwitch”, and is returning 123 for the status.

```PowerShell
PS C:\> $portData = Get-VMSwitchExtensionPortData -VmName TestVm -FeatureId DAA0B7CC-74DB-41ef-8354-7002F9FA463E
# Output the current value
PS C:\> $portData.Data.CurrentStatus
123
```

For more information on how extensible switch extensions manage port feature status information, see [Managing Custom Port Feature Status Information](managing-custom-port-feature-status-information.md).

 

 





