---
title: Standardized INF Keywords for SR-IOV
description: Standardized INF Keywords for SR-IOV
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Standardized INF Keywords for SR-IOV


This topic describes the standardized INF keywords for the single root I/O virtualization (SR-IOV) interface. These keywords apply to the INF file for the miniport driver of the PCI Express (PCIe) Physical Function (PF) of an SR-IOV network adapter.

The SR-IOV INF keywords are described in the following sections:

[Standardized INF Keywords for the Enabling or Disabling SR-IOV Support](#standardized-inf-keywords-for-enabling-or-disabling-sr-iov-support)

[Standardized INF Keywords for Configuration of the Default NIC Switch](#standardized-inf-keywords-for-configuration-of-the-default-nic-switch)

## Standardized INF Keywords for Enabling or Disabling SR-IOV Support


Standardized INF keywords are defined to enable or disable support for the SR-IOV features of a network adapter.

**\*SRIOV**  
A value that describes whether the device has enabled or disabled the SR-IOV feature.

After the driver is installed, administrators can update the **\*SRIOV** keyword value in the **Advanced** property page for the network adapter. For more information about advanced properties, see [Specifying Configuration Parameters for the Advanced Properties Page](specifying-configuration-parameters-for-the-advanced-properties-page.md).

**Note**   The miniport driver is automatically restarted after a change is made in the **Advanced** property page for the adapter.

 

**\*SriovPreferred**  
A value that defines whether SR-IOV capabilities should be enabled instead of virtual machine queue (VMQ) or receive side scaling (RSS) capabilities.

This is a hidden keyword value that must not be specified in the INF file and is not displayed in **Advanced** property page for the network adapter.

For more information about how to interpret SR-IOV, VMQ, and RSS keywords, see [Handling SR-IOV, VMQ, and RSS Standardized INF Keywords](handling-sr-iov--vmq--and-rss-standardized-inf-keywords.md).

The SR-IOV standardized INF keywords are enumeration keywords and are described in the following table. The columns in this table describe the following attributes for an enumeration keyword:

SubkeyName  
The name of the keyword that you must specify in the INF file. This name also appears in the registry under the **NDI\\params\\** key for the network adapter.

ParamDesc  
The display text that is associated with the **SubkeyName** keyword.

**Note**  The independent hardware vendor (IHV) can define any descriptive text for the SubkeyName.

 
Value  
The enumeration integer value that is associated with each **SubkeyName** keyword in the list.

EnumDesc  
The display text that is associated with each value that appears in the menu.

|SubkeyName|ParamDesc|Value|EnumDesc|
|--- |--- |--- |--- |
|**\*SRIOV**|SR-IOV|0|Disabled|
|||1 (Default)|Enabled|
|**\*SriovPreferred**|The ParamDesc and EnumDesc entries for this subkey cannot be used in either INF files or a user interface.|0 (Default)|Report RSS or VMQ capabilities based on the **\*VmqOrRssPreferrence** keyword. Do not report SR-IOV capabilities. For more information about the **\*VmqOrRssPreferrence** keyword, see [Standardized INF Keywords for VMQ](standardized-inf-keywords-for-vmq.md).|
|||1|Report SR-IOV capabilities.|

 

For more information about standardized INF keywords, see [Standardized INF Keywords for Network Devices](standardized-inf-keywords-for-network-devices.md).

## Standardized INF Keywords for Configuration of the Default NIC Switch


Starting with Windows Server 2012, the SR-IOV interface supports only one NIC switch on the network adapter. This switch is known as the *default NIC switch*, and is referenced by the NDIS\_DEFAULT\_SWITCH\_ID identifier.

The INF file for the PF miniport driver must specify the configuration of the default NIC switch on the SR-IOV network adapter. This allows the network installer to copy the default switch configuration information from the INF to the miniport registry configuration under the subkey for the default switch (**NDI\\params\\NicSwitches\\0**).

These keywords are not displayed in the **Advanced** property page for the network adapter and cannot be configured by the user. These keywords are specified by using the **AddReg** directive in the **DDInstall** section of the INF file. Each keyword is specified by a separate **AddReg** directive.

The following table describes the INF keywords for the default NIC switch configuration of the SR-IOV network adapter. The columns in this table describe the following attributes for these keywords:

SubkeyName  
The name of the keyword that you must specify in the INF file. This name also appears in the registry under the **NDI\\params\\NicSwitches\\0** key for the network adapter.

Data value  
The value that is associated with the **SubkeyName** keyword.

Data type  
The type of the data value.

|SubkeyName|Data value|Data type|Notes|
|--- |--- |--- |--- |
|**\*Flags**|0|REG_DWORD|The keyword must be assigned this value.|
|**\*SwitchType**|1|REG_DWORD|The keyword must be assigned this value.|
|**\*SwitchId**|0|REG_DWORD|The keyword must be assigned this value.|
|**\*SwitchName**|“Default Switch”|REG_SZ|The keyword must be assigned this value.|
|**\*NumVFs**|(0-_n_),|REG_DWORD|_n_ is the maximum number of PCIe Virtual Functions (VFs) that are supported by the SR-IOV network adapter. **Note** This registry key defines the maximum number of VFs that the network adapter supports. When the miniport driver calls [**NdisMSetMiniportAttributes**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes), it can advertise less than this value depending on the available hardware resources on the network adapter. For more information, see [Determining NIC Switch Capabilities](determining-nic-switch-capabilities.md).| 

The following is an example of **AddReg** directives for the default NIC switch configuration of an SR-IOV network adapter:

``` syntax
HKR, NicSwitches\0, *SwitchId,   0x00010001, 0
HKR, NicSwitches\0, *SwitchName, 0x00000000, “Default Switch”
```

For more information about the syntax of the **AddReg** directive, see [**INF AddReg Directive**](../install/inf-addreg-directive.md).

For more information about the default NIC switch, see [NIC Switches](nic-switches.md).

