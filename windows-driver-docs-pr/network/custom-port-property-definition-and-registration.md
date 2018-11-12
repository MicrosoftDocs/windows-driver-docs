---
title: Custom Port Property Definition and Registration
description: Custom Port Property Definition and Registration
ms.assetid: 55FCA402-191B-4DC9-A126-77AA15183E90
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Custom Port Property Definition and Registration


Custom property definitions for a Hyper-V extensible switch port policy are registered with the WMI management layer by using managed object format (MOF) class definitions. In addition to the structure members that define the attributes of the custom port property, the MOF class must also contain the following:

-   A UUID that uniquely identifies the custom port property.

-   A GUID that uniquely identifies the extensible switch extension. This GUID is declared as the **ExtensionId** qualifier of the MOF class and must match the value of the **NetCfgInstanceId** entry that is declared in the extension's INF file.

-   A descriptive class name string. The name of the vendor must be included in the string.

The following shows an example of a MOF class for a custom property of an extensible switch port policy.

```C++
#pragma namespace("\\\\.\\root\\virtualization\\v2")

[ Dynamic, 
 UUID("EB29F0F2-F5DC-45C6-81BB-3CD9F219BBBB"),
 ExtensionId("5CBF81BE-5055-47CD-9055-A76B2B4E369E"), 
 Provider("VmmsWmiInstanceAndMethodProvider"), 
 Locale(0x409),
 InterfaceVersion("1"),
 InterfaceRevison("0"),
DisplayName("Fabrikam, Inc. Port Settings Friendly Name") : Amended,
Description("Fabrikam, Inc. Port Settings detailed description.") : Amended]
class Fabrikam_PortCustomSettingData : Msvm_EthernetSwitchPortFeatureSettingData {
   
    [ Read,
      Write,
      WmiDataId(1),
      InterfaceVersion("1"),
      InterfaceRevision("0"),
      Description (
         "int32 setting.") : Amended]
    uint32 SettingIntA = 0;

    [ Read,
      Write,
      WmiDataId(2),
      InterfaceVersion("1"),
      InterfaceRevision("0"),
      Description (
         "int64 setting.") : Amended]
    uint64 SettingIntB = 0;
};
```

The MOF classes for custom properties of a port policy are registered in the common information model (CIM) repository by using the MOF compiler (Mofcomp.exe). Once registered, the MOF class can be configured through PowerShell cmdlets and WMI-based application programs.

The following example shows the commands that must be entered to register a file (Fabrikam\_PortCustomSettingData.mof) that contains the MOF class for a custom port property.

```PowerShell
net stop vmms
mofcomp -N:root\virtualization\v2 Fabrikam_PortCustomSettingData.mof
net start vmms
```

For more information about how to use the MOF compiler, see [Compiling a Driver's MOF File](https://msdn.microsoft.com/library/windows/hardware/ff542012).

The following example shows how you can configure the sample feature. In this example, the Fabrikam\_PortCustomSettingData MOF class is used to configure a port from a Hyper-V partition named "TestVm".

```PowerShell
# Retrieve the template object for the custom configuration. We know the ID already so
# we can retrieve it directly, otherwise Get-VmSystemSwitchExtensionPortFeature can list all available
# properties. 
PS C:\> $feature = Get-VMSystemSwitchExtensionPortFeature -FeatureId EB29F0F2-F5DC-45C6-81BB-3CD9F219BBBB

# Output the values
PS C:\> $feature

Id            : eb29f0f2-f5dc-45c6-81bb-3cd9f219bbbb
ExtensionId   : 5cbf81bd-5055-47cd-9055-a76b2b4e369d
ExtensionName : Fabrican Extension
Name          : Fabrikam, Inc. Port Settings Friendly Name
ComputerName  : TEST_SERVER
SettingData   : \\TEST_SERVER\root\virtualization\v2:VendorName_SwitchPortCustomSettingData.InstanceID="Microsoft:Defini
                tion\\EB29F0F2-F5DC-45C6-81BB-3CD9F219BBBB\\Default"

# Cast the SettingsData to a WMI object to see the actual configurable values. 
PS C:\> $wmiObj = [wmi]$feature.SettingData
PS C:\> $wmiObj

__GENUS          : 2
__CLASS          : Fabrikam_PortCustomSettingData
__SUPERCLASS     : Msvm_EthernetSwitchFeatureSettingData
__DYNASTY        : CIM_ManagedElement
__RELPATH        : Fabrikam_PortCustomSettingData.InstanceID="Microsoft:Definition\\EB29F0F2-F5DC-45C6-81BB-3CD
                   9F219BBBB\\Default"
__PROPERTY_COUNT : 6
__DERIVATION     : {Msvm_EthernetSwitchFeatureSettingData, CIM_SettingData, CIM_ManagedElement}
__SERVER         : TEST_SERVER
__NAMESPACE      : root\virtualization\v2
__PATH           : \\TEST_SERVER\root\virtualization\v2:Fabrikam_PortCustomSettingData.InstanceID="Microsoft:Def
                   inition\\EB29F0F2-F5DC-45C6-81BB-3CD9F219BBBB\\Default"
Caption          : Fabrikam, Inc. Port Settings Friendly Name
Description      : Fabrikam, Inc. Port Settings detailed description.
ElementName      : Fabrikam, Inc. Port Settings Friendly Name
InstanceID       : Microsoft:Definition\EB29F0F2-F5DC-45C6-81BB-3CD9F219BBBB\Default
SettingIntA      : 0
SettingIntB      : 0

# Update the property settings and add to the NIC attached to TestVm
PS C:\> $wmiObj.SettingIntA = 100
PS C:\> $wmiObj.SettingIntB = 9999
PS C:\> Add-VMSwitchExtensionPortFeature -VMSwitchExtensionFeature $feature -VmName TestVm
 
# Validate that the properties are now set on the VM’s NIC
PS C:\> $feature = Get-VmSwitchExtensionPortFeature -FeatureId EB29F0F2-F5DC-45C6-81BB-3CD9F219BBBB -VmName TestVm

PS C:\> [wmi]$feature.SettingData


__GENUS          : 2
__CLASS          : Fabrikam_PortCustomSettingData
__SUPERCLASS     : Msvm_EthernetSwitchFeatureSettingData
__DYNASTY        : CIM_ManagedElement
__RELPATH        : Fabrikam_PortCustomSettingData.InstanceID="Microsoft:6208FB20-2490-4DC1-B121-877B68B4CE11\\4
                   DDC57F5-6DAE-4A36-9D62-7A838D5601F2\\C\\EB29F0F2-F5DC-45C6-81BB-3CD9F219BBBB\\CB323B56-FA54-4506-B58
                   B-78C70C0B3229"
__PROPERTY_COUNT : 6
__DERIVATION     : {Msvm_EthernetSwitchFeatureSettingData, CIM_SettingData, CIM_ManagedElement}
__SERVER         : TEST_SERVER
__NAMESPACE      : root\virtualization\v2
__PATH           : \\TEST_SERVER\root\virtualization\v2:Fabrikam_PortCustomSettingData.InstanceID="Microsoft:620
                   8FB20-2490-4DC1-B121-877B68B4CE11\\4DDC57F5-6DAE-4A36-9D62-7A838D5601F2\\C\\EB29F0F2-F5DC-45C6-81BB-
                   3CD9F219BBBB\\CB323B56-FA54-4506-B58B-78C70C0B3229"
Caption          : Fabrikam, Inc. Port Settings Friendly Name
Description      : Fabrikam, Inc. Port Settings detailed description.
ElementName      : Fabrikam, Inc. Port Settings Friendly Name
InstanceID       : Microsoft:6208FB20-2490-4DC1-B121-877B68B4CE11\4DDC57F5-6DAE-4A36-9D62-7A838D5601F2\C\EB29F0F2-F5DC-
                   45C6-81BB-3CD9F219BBBB\CB323B56-FA54-4506-B58B-78C70C0B3229
SettingIntA      : 100
SettingIntB      : 9999
```

For more information on how extensible switch extensions manage port policies, see [Managing Port Policies](managing-port-policies.md).

 

 





