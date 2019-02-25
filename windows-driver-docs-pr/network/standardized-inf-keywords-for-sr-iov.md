---
title: Standardized INF Keywords for SR-IOV
description: Standardized INF Keywords for SR-IOV
ms.assetid: 5CA33B4F-E43A-4EB6-BCAB-365CA1FD3EF2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Standardized INF Keywords for SR-IOV


This topic describes the standardized INF keywords for the single root I/O virtualization (SR-IOV) interface. These keywords apply to the INF file for the miniport driver of the PCI Express (PCIe) Physical Function (PF) of an SR-IOV network adapter.

The SR-IOV INF keywords are described in the following sections:

[Standardized INF Keywords for the Enabling or Disabling SR-IOV Support](#sr-iov)

[Standardized INF Keywords for Configuration of the Default NIC Switch](#nic-switch)

## Standardized INF Keywords for Enabling or Disabling SR-IOV Support


Standardized INF keywords are defined to enable or disable support for the SR-IOV features of a network adapter.

<a href="" id="-sriov"></a>**\*SRIOV**  
A value that describes whether the device has enabled or disabled the SR-IOV feature.

After the driver is installed, administrators can update the **\*SRIOV** keyword value in the **Advanced** property page for the network adapter. For more information about advanced properties, see [Specifying Configuration Parameters for the Advanced Properties Page](specifying-configuration-parameters-for-the-advanced-properties-page.md).

**Note**   The miniport driver is automatically restarted after a change is made in the **Advanced** property page for the adapter.

 

<a href="" id="-sriovpreferred"></a>**\*SriovPreferred**  
A value that defines whether SR-IOV capabilities should be enabled instead of virtual machine queue (VMQ) or receive side scaling (RSS) capabilities.

This is a hidden keyword value that must not be specified in the INF file and is not displayed in **Advanced** property page for the network adapter.

For more information about how to interpret SR-IOV, VMQ, and RSS keywords, see [Handling SR-IOV, VMQ, and RSS Standardized INF Keywords](handling-sr-iov--vmq--and-rss-standardized-inf-keywords.md).

The SR-IOV standardized INF keywords are enumeration keywords and are described in the following table. The columns in this table describe the following attributes for an enumeration keyword:

<a href="" id="subkeyname"></a>SubkeyName  
The name of the keyword that you must specify in the INF file. This name also appears in the registry under the **NDI\\params\\** key for the network adapter.

<a href="" id="paramdesc"></a>ParamDesc  
The display text that is associated with the**SubkeyName** keyword.

**Note**  The independent hardware vendor (IHV) can define any descriptive text for the SubkeyName.

 

<a href="" id="value"></a>Value  
The enumeration integer value that is associated with each **SubkeyName** keyword in the list.

<a href="" id="enumdesc"></a>EnumDesc  
The display text that is associated with each value that appears in the menu.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">SubkeyName</th>
<th align="left">ParamDesc</th>
<th align="left">Value</th>
<th align="left">EnumDesc</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong><em>SRIOV</strong></p></td>
<td align="left"><p>SR-IOV</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Disabled</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>1 (Default)</p></td>
<td align="left"><p>Enabled</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong></em>SriovPreferred</strong></p></td>
<td align="left"><p>The ParamDesc and EnumDesc entries for this subkey cannot be used in either INF files or a user interface.</p></td>
<td align="left"><p>0 (Default)</p></td>
<td align="left"><p>Report RSS or VMQ capabilities based on the <strong><em>VmqOrRssPreferrence</strong> keyword. Do not report SR-IOV capabilities,</p>
<p>For more information about the <strong></em>VmqOrRssPreferrence</strong> keyword, see <a href="standardized-inf-keywords-for-vmq.md" data-raw-source="[Standardized INF Keywords for VMQ](standardized-inf-keywords-for-vmq.md)">Standardized INF Keywords for VMQ</a>.</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>1</p></td>
<td align="left"><p>Report SR-IOV capabilities.</p></td>
</tr>
</tbody>
</table>

 

For more information about standardized INF keywords, see [Standardized INF Keywords for Network Devices](standardized-inf-keywords-for-network-devices.md).

## Standardized INF Keywords for Configuration of the Default NIC Switch


Starting with Windows Server 2012, the SR-IOV interface supports only one NIC switch on the network adapter. This switch is known as the *default NIC switch*, and is referenced by the NDIS\_DEFAULT\_SWITCH\_ID identifier.

The INF file for the PF miniport driver must specify the configuration of the default NIC switch on the SR-IOV network adapter. This allows the network installer to copy the default switch configuration information from the INF to the miniport registry configuration under the subkey for the default switch (**NDI\\params\\NicSwitches\\0**).

These keywords are not displayed in the **Advanced** property page for the network adapter and cannot be configured by the user. These keywords are specified by using the **AddReg** directive in the **DDInstall** section of the INF file. Each keyword is specified by a separate **AddReg** directive.

The following table describes the INF keywords for the default NIC switch configuration of the SR-IOV network adapter. The columns in this table describe the following attributes for these keywords:

<a href="" id="subkeyname"></a>SubkeyName  
The name of the keyword that you must specify in the INF file. This name also appears in the registry under the **NDI\\params\\NicSwitches\\0** key for the network adapter.

<a href="" id="data-value"></a>Data value  
The value that is associated with the **SubkeyName** keyword.

<a href="" id="data-type"></a>Data type  
The type of the data value.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">SubkeyName</th>
<th align="left">Data value</th>
<th align="left">Data type</th>
<th align="left">Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong><em>Flags</strong></p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>REG_DWORD</p></td>
<td align="left"><p>The keyword must be assigned this value.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong></em>SwitchType</strong></p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>REG_DWORD</p></td>
<td align="left"><p>The keyword must be assigned this value.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong><em>SwitchId</strong></p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>REG_DWORD</p></td>
<td align="left"><p>The keyword must be assigned this value.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong></em>SwitchName</strong></p></td>
<td align="left"><p>“Default Switch”</p></td>
<td align="left"><p>REG_SZ</p></td>
<td align="left"><p>The keyword must be assigned this value.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>*NumVFs</strong></p></td>
<td align="left"><p>(0-<em>n</em>),</p></td>
<td align="left"><p>REG_DWORD</p></td>
<td align="left"><p><em>n</em> is the maximum number of PCIe Virtual Functions (VFs) that are supported by the SR-IOV network adapter.</p>
<div class="alert">
<strong>Note</strong>  This registry key defines the maximum number of VFs that the network adapter supports. When the miniport driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff563672" data-raw-source="[&lt;strong&gt;NdisMSetMiniportAttributes&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563672)"><strong>NdisMSetMiniportAttributes</strong></a>, it can advertise less than this value depending on the available hardware resources on the network adapter. For more information, see <a href="determining-nic-switch-capabilities.md" data-raw-source="[Determining NIC Switch Capabilities](determining-nic-switch-capabilities.md)">Determining NIC Switch Capabilities</a>.
</div>
<div>
 
</div></td>
</tr>
</tbody>
</table>

 

The following is an example of **AddReg** directives for the default NIC switch configuration of an SR-IOV network adapter:

``` syntax
HKR, NicSwitches\0, *SwitchId,   0x00010001, 0
HKR, NicSwitches\0, *SwitchName, 0x00000000, “Default Switch”
```

For more information about the syntax of the **AddReg** directive, see [**INF AddReg Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320).

For more information about the default NIC switch, see [NIC Switches](nic-switches.md).

 

 





