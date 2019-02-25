---
title: Custom Switch Property Definition and Registration
description: Custom Switch Property Definition and Registration
ms.assetid: DB80E86D-8553-47B5-8AE1-6D430FDDE206
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Custom Switch Property Definition and Registration


Custom property definitions for a Hyper-V extensible switch policy are registered with the WMI management layer by using managed object format (MOF) class definitions. In addition to the structure members that define the attributes of the custom switch property, the MOF class must also contain the following:

-   A UUID that uniquely identifies the custom switch property.

-   A GUID that uniquely identifies the extensible switch extension. This GUID is declared as the **ExtensionId** qualifier of the MOF class and must match the value of the **NetCfgInstanceId** entry that is declared in the extension's INF file.

-   A descriptive class name string. The name of the vendor must be included in the string.

The following shows an example of a MOF class for a custom property of an extensible switch policy.

```C++
#pragma namespace("\\\\.\\root\\virtualization\\v2")

[ Dynamic, 
 UUID("FF36C3A6-D2F1-46ed-A376-32B43D6B8390"),
 ExtensionId("5CBF81BE-5055-47CD-9055-A76B2B4E369E"), 
 Provider("VmmsWmiInstanceAndMethodProvider"), 
  Locale(0x409),
 InterfaceVersion("1"),
 InterfaceRevison("0"),
DisplayName("Fabrikam, Inc.  Switch Settings Friendly Name") : Amended,
Description("Fabrikam, Inc.  Switch Settings detailed description.") : Amended]
class Fabrikam_SwitchCustomSettingData : Msvm_EthernetSwitchFeatureSettingData {
   
    [ Read,
      Write,
      WmiDataId(1),
      InterfaceVersion("1"),
      InterfaceRevision("0"),
      Description (
         "int32 setting.") : Amended]
    uint32 SwitchSettingIntA = 0;

    [ Read,
      Write,
      WmiDataId(2),
      InterfaceVersion("1"),
      InterfaceRevision("0"),
      Description (
         "int64 setting.") : Amended]
    uint64 SwitchSettingIntB = 0;
};
```

The MOF classes for custom properties of a switch policy are registered in the common information model (CIM) repository by using the MOF compiler (Mofcomp.exe). Once registered, the MOF class can be configured through PowerShell cmdlets and WMI-based application programs.

The following example shows the commands that must be entered to register a file (Fabrikam\_SwitchCustomSettingData.mof) that contains the MOF class for a custom port property.

```PowerShell
net stop vmms
mofcomp -N:root\virtualization\v2 Fabrikam_SwitchCustomSettingData.mof
net start vmms
```

For more information about how to use the MOF compiler, see [Compiling a Driver's MOF File](https://msdn.microsoft.com/library/windows/hardware/ff542012).

The following example shows how you can configure the sample feature. In this example, the Fabrikam\_SwitchCustomSettingData MOF class is used to configure a switch named “TestSwitch”.

```PowerShell
# Retrieve the template object for the custom configuration. We know the ID already so
# we can retrieve it directly, otherwise Get-VMSystemSwitchExtensionSwitchFeature can list all available
# properties. 
PS C:\> $feature = Get-VMSystemSwitchExtensionSwitchFeature -FeatureId FF36C3A6-D2F1-46ed-A376-32B43D6B8390

# Output the values
PS C:\temp> $feature


Id            : ff36c3a6-d2f1-46ed-a376-32b43d6b8390
ExtensionId   : 5CBF81BE-5055-47CD-9055-A76B2B4E369E
ExtensionName : Fabrican Extension
Name          : Fabrikam, Inc. Switch Settings Friendly Name
ComputerName  : TEST_SERVER
SettingData   : \\TEST_SERVER\root\virtualization\v2:VendorName_SwitchCustomSettingData.InstanceID="Microsoft:Definition\\
                FF36C3A6-D2F1-46ED-A376-32B43D6B8390\\Default"

# Cast the SettingsData to a WMI object to see the actual configurable values. 
PS C:\> $wmiObj = [wmi]$feature.SettingData
PS C:\> $wmiObj


__GENUS           : 2
__CLASS           : Fabrikam_SwitchCustomSettingData 
__SUPERCLASS      : Msvm_EthernetSwitchFeatureSettingData
__DYNASTY         : CIM_ManagedElement
__RELPATH         : Fabrikam_SwitchCustomSettingData .InstanceID="Microsoft:Definition\\FF36C3A6-D2F1-46ED-A376-32B43D
                    6B8390\\Default"
__PROPERTY_COUNT  : 6
__DERIVATION      : {Msvm_EthernetSwitchFeatureSettingData, Msvm_FeatureSettingData, CIM_SettingData,
                    CIM_ManagedElement}
__SERVER          : TEST_SERVER
__NAMESPACE       : root\virtualization\v2
__PATH            : \\TEST_SERVER\root\virtualization\v2:Fabrikam_SwitchCustomSettingData .InstanceID="Microsoft:Definiti
                    on\\FF36C3A6-D2F1-46ED-A376-32B43D6B8390\\Default"
Caption           : Fabrikam, Inc. Switch Settings Friendly Name
Description       : Fabrikam, Inc. Switch Settings detailed description.
ElementName       : Fabrikam, Inc. Switch Settings Friendly Name
InstanceID        : Microsoft:Definition\FF36C3A6-D2F1-46ED-A376-32B43D6B8390\Default
SwitchSettingIntA : 0
SwitchSettingIntB : 0
PSComputerName    : TEST_SERVER

# Update the property settings and add to the NIC attached to TestVm
PS C:\> $wmiObj.SwitchSettingIntA = 100
PS C:\> $wmiObj.SwitchSettingIntB = 9999
PS C:\> Add-VMSwitchExtensionSwitchFeature -VMSwitchExtensionFeature $feature -SwitchName TestSwitch
 
# Validate that the properties are now set on the VM’s NIC
PS C:\> $feature = Get-VmSwitchExtensionSwitchFeature -FeatureId FF36C3A6-D2F1-46ed-A376-32B43D6B8390 -SwitchName TestSwitch

PS C:\> [wmi]$feature.SettingData


__GENUS           : 2
__CLASS           : Fabrikam_SwitchCustomSettingData 
__SUPERCLASS      : Msvm_EthernetSwitchFeatureSettingData
__DYNASTY         : CIM_ManagedElement
__RELPATH         : Fabrikam_SwitchCustomSettingData .InstanceID="Microsoft:88835394-FDE1-437C-B249-D840575154E2\\FF36
                    C3A6-D2F1-46ED-A376-32B43D6B8390\\F9EA07E7-7B73-431A-8705-26EC2B592306"
__PROPERTY_COUNT  : 6
__DERIVATION      : {Msvm_EthernetSwitchFeatureSettingData, Msvm_FeatureSettingData, CIM_SettingData,
                    CIM_ManagedElement}
__SERVER          : TEST_SERVER
__NAMESPACE       : root\virtualization\v2
__PATH            : \\TEST_SERVER\root\virtualization\v2:Fabrikam_SwitchCustomSettingData .InstanceID="Microsoft:88835394
                    -FDE1-437C-B249-D840575154E2\\FF36C3A6-D2F1-46ED-A376-32B43D6B8390\\F9EA07E7-7B73-431A-8705-26EC2B5
                    92306"
Caption           : Fabrikam, Inc. Switch Settings Friendly Name
Description       : Fabrikam, Inc. Switch Settings detailed description.
ElementName       : Fabrikam, Inc. Switch Settings Friendly Name
InstanceID        : Microsoft:88835394-FDE1-437C-B249-D840575154E2\FF36C3A6-D2F1-46ED-A376-32B43D6B8390\F9EA07E7-7B73-4
                    31A-8705-26EC2B592306
SwitchSettingIntA : 100
SwitchSettingIntB : 9999
PSComputerName    : TEST_SERVER
```

For more information on how extensible switch extensions manage switch policies, see [Managing Switch Policies](managing-switch-policies.md).

 

 





