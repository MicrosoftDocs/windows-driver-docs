---
title: Standardized INF Keywords for NDIS QoS
description: Standardized INF Keywords for NDIS QoS
ms.assetid: 7967D633-850F-4707-9577-9262AEB1A597
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Standardized INF Keywords for NDIS QoS


A standardized INF keyword is defined to enable or disable support for NDIS Quality of Service (QoS) on a miniport driver.

The INF file for the miniport driver of an adapter that supports NDIS QoS must specify the **\*QOS** standardized INF keyword. After the driver is installed, administrators can update the **\*QOS** keyword value in the **Advanced** property page for the adapter. For more information about advanced properties, see [Specifying Configuration Parameters for the Advanced Properties Page](specifying-configuration-parameters-for-the-advanced-properties-page.md).

**Note**   The miniport driver is automatically restarted after a change is made in the **Advanced** property page for the adapter.

 

The **\*QOS** INF keyword is an enumeration keyword. The following table describes the possible INF entries for the **\*QOS** INF keyword. The columns in this table describe the following attributes for an enumeration keyword:

<a href="" id="subkeyname"></a>SubkeyName  
The name of the keyword that you must specify in the INF file. This name also appears in the registry under the **NDI\\params\\** key for the network adapter.

<a href="" id="paramdesc"></a>ParamDesc  
The display text that is associated with SubkeyName.

**Note**  The independent hardware vendor (IHV) can define any descriptive text for SubkeyName.

 

<a href="" id="value"></a>Value  
The enumeration integer value that is associated with each SubkeyName in the list.

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
<td align="left"><p><strong>*QOS</strong></p></td>
<td align="left"><p>NDIS QoS</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>QoS Disabled</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>1 (Default)</p></td>
<td align="left"><p>QoS Enabled</p></td>
</tr>
</tbody>
</table>

 

When NDIS calls the miniport driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function, the driver must do the following:

-   The miniport driver must register the NDIS QoS hardware capabilities that the network adapter supports.

-   The miniport driver must also read the **\*QOS** keyword value in the registry to register the current status of the adapter's NDIS QoS hardware capabilities.

The miniport driver must follow these guidelines when it registers the current status of the NDIS QoS hardware capabilities:

-   If the **\*QOS** keyword has a value of one, the miniport driver must register all NDIS QoS hardware capabilities as currently enabled. The driver must enable its NDIS QoS hardware capabilities regardless of the following:

    -   Whether the Microsoft Data Center Bridging (DCB) server feature is installed or enabled on Windows Server 2012 and later versions of Windows Server. For more information about this server feature and related components, see [NDIS QoS Architecture for Data Center Bridging](ndis-qos-architecture-for-data-center-bridging.md).

    -   Whether the local Data Center Bridging Exchange (DCBX) Willing state is enabled on the network adapter. When this state is enabled, the network adapter and miniport driver can resolve its operational NDIS QoS parameters from remote NDIS QoS parameters that were received from the remote peer. For more information, see [Managing the Local DCBX Willing State](managing-the-local-dcbx-willing-state.md).

    For more information on how to register QoS hardware and current capabilities, see [Registering NDIS QoS Capabilities](registering-ndis-qos-capabilities.md).

    **Note**  The miniport driver must always issue [**NDIS\_STATUS\_QOS\_OPERATIONAL\_PARAMETERS\_CHANGE**](https://msdn.microsoft.com/library/windows/hardware/hh439810) and [**NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE**](https://msdn.microsoft.com/library/windows/hardware/hh439812) status indications if its NDIS QoS hardware capabilities are currently enabled. Starting with Windows Server 2012, these status indications report on the current operational and remote QoS parameter settings, respectively. These indications allow system administrators to view NDIS QoS and DCB settings regardless of whether the Microsoft DCB server feature is installed. For more information, see [Indicating NDIS QoS Parameter Status](indicating-ndis-qos-parameter-status.md).

     

-   If the **\*QOS** keyword has a value of zero, the miniport driver must report all NDIS QoS hardware capabilities as currently disabled. In this case, the operating system will not configure the driver with NDIS QoS capabilities.

    **Note**  The driver must disable DCB and DCBX on the network adapter if the **\*QOS** keyword has a value of zero.

     

-   If the **\*QOS** keyword is not present in the registry, the miniport driver must not report any NDIS QoS hardware capabilities. In this case, the operating system will not configure the driver with NDIS QoS capabilities.

    **Note**  The driver must disable DCB and DCBX on the network adapter if the **\*QOS** keyword is not present in the registry.

     

In addition to the **\*QOS** keyword, the miniport driver must read the **\*PriorityVLANTag** keyword. This keyword specifies whether the network adapter is enabled to insert the 802.1Q tags for packet priority and virtual LANs (VLANs).

The following table summarizes the relationship between the **\*QOS** and **\*PriorityVLANTag** keyword values.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left"><em>QOS keyword setting</th>
<th align="left"></em>PriorityVLANTag keyword setting</th>
<th align="left">*PriorityVLANTag setting description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">0 or not present</td>
<td align="left"><p>0</p></td>
<td align="left"><p>Packet priority &amp; VLAN disabled</p></td>
</tr>
<tr class="even">
<td align="left">0 or not present</td>
<td align="left"><p>1</p></td>
<td align="left"><p>Packet priority enabled</p></td>
</tr>
<tr class="odd">
<td align="left">0 or not present</td>
<td align="left"><p>2</p></td>
<td align="left"><p>VLAN Enabled</p></td>
</tr>
<tr class="even">
<td align="left">0 or not present</td>
<td align="left"><p>3 (Default)</p></td>
<td align="left"><p>Packet priority and VLAN enabled</p></td>
</tr>
<tr class="odd">
<td align="left">1</td>
<td align="left"><p>0</p></td>
<td align="left"><p>Packet priority enabled</p></td>
</tr>
<tr class="even">
<td align="left">1</td>
<td align="left"><p>1</p></td>
<td align="left"><p>Packet priority enabled</p></td>
</tr>
<tr class="odd">
<td align="left">1</td>
<td align="left"><p>2</p></td>
<td align="left"><p>Packet priority and VLAN enabled</p></td>
</tr>
<tr class="even">
<td align="left">1</td>
<td align="left"><p>3 (Default)</p></td>
<td align="left"><p>Packet priority and VLAN enabled</p></td>
</tr>
</tbody>
</table>

 

For more information about the **\*PriorityVLANTag** keyword, see [Enumeration Keywords](enumeration-keywords.md).

For more information about standardized INF keywords, see [Standardized INF Keywords for Network Devices](standardized-inf-keywords-for-network-devices.md).

For more information on how to register NDIS QoS capabilities, see [Registering NDIS QoS Capabilities](registering-ndis-qos-capabilities.md).

 

 





