---
title: DDInstall Section in a Network INF File
description: DDInstall Section in a Network INF File
ms.assetid: f6621796-0d1f-4d96-9850-720718e7ac44
keywords:
- INF files WDK network , DDInstall section
- network INF files WDK , DDInstall section
- DDInstall section WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DDInstall Section in a Network INF File





A *DDInstall* section in a network INF file is based on the generic [**INF DDInstall section**](https://msdn.microsoft.com/library/windows/hardware/ff547344).

A *DDInstall* section in a network INF file has the following network-specific entries:

-   [Characteristics](#characteristics)
-   [BusType](#bustype)
-   [Port1DeviceNumber and Port1FunctionNumber](#port1devicenumber-and-port1functionnumber)

### Characteristics

Each *DDInstall* section in a network INF file must have a **Characteristics** entry. The **Characteristics** entry specifies certain characteristics of the network component being installed and may limit the user's actions regarding that component. For example, the **Characteristics** entry can specify whether the component supports a user interface, whether it can be removed, or whether it is hidden from the user.

The **Characteristics** entry can have one or more of the following values (multiple values are summed together):

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Hex value</th>
<th align="left">Name</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x1</p></td>
<td align="left"><p>NCF_VIRTUAL</p></td>
<td align="left"><p>Component is a virtual adapter. The device is not on a physical bus, such as the PCI bus or USB, but is on the root bus. This flag is only applicable to drivers which use the Net device setup class.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x2</p></td>
<td align="left"><p>NCF_SOFTWARE_ENUMERATED</p></td>
<td align="left"><p>Component is a software-enumerated adapter. This flag is only applicable to drivers which use the Net device setup class.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x4</p></td>
<td align="left"><p>NCF_PHYSICAL</p></td>
<td align="left"><p>Component is a physical adapter that the driver communicates with directly (for example, through the PCI bus) or indirectly (for example, through USB).</p>
<p>Select this option if the driver supports a physical network interface.¹ This flag is only applicable to drivers which use the Net device setup class.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x8</p></td>
<td align="left"><p>NCF_HIDDEN</p></td>
<td align="left"><p>Component should not be shown in any user interface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x10</p></td>
<td align="left"><p>NCF_NO_SERVICE</p></td>
<td align="left"><p>Component does not have an associated service (device driver).</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x20</p></td>
<td align="left"><p>NCF_NOT_USER_</p>
<p>REMOVABLE</p></td>
<td align="left"><p>Component cannot be removed by the user (for example, through Control Panel or Device Manager).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x80</p></td>
<td align="left"><p>NCF_HAS_UI</p></td>
<td align="left"><p>Component supports a user interface (for example, the Advanced Page or a custom properties sheet).</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x400</p></td>
<td align="left"><p>NCF_FILTER</p></td>
<td align="left"><p>Component is a Filter Intermediate driver.  Filter Intermediate drivers are not supported in Windows 10 or later.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x4000</p></td>
<td align="left"><p>NCF_NDIS_PROTOCOL</p></td>
<td align="left"><p>Component requires the unload event that is provided by the binding engine to the <strong>NetTrans</strong> device setup class (typically used by filter Intermediate drivers which use the <strong>NetService</strong> device setup class).</p></td>
</tr>
</tr>
<tr class="even">
<td align="left"><p>0x40000</p></td>
<td align="left"><p>NCF_LW_FILTER</p></td>
<td align="left"><p>Component is a lightweight filter driver.  This flag is only applicable to drivers which use the NetService device setup class.</p></td>
</tr>
</tbody>
</table>

 

¹When using Windows Server 2012 R2, at least one network interface on the system must be marked with NCF\_PHYSICAL in order to be eligible for DHCPv6 client.

The following combinations of **Characteristics** values are not allowed:

-   NCF\_VIRTUAL, NCF\_SOFTWARE\_ENUMERATED, and NCF\_PHYSICAL are mutually exclusive. 

-   NCF\_NO\_SERVICE cannot be used with NCF\_VIRTUAL, NCF\_SOFTWARE\_ENUMERATED, or NCF\_PHYSICAL. A virtual, software-enumerated, or physical adapter must always have an associated service (device driver).

The following is an example of a **Characteristics** entry for a physical adapter that supports a user interface:

```INF
Characteristics = 0x84; NCF_PHYSICAL, NCF_HAS_UI
```

### BusType

A *DDInstall* section for a physical network adapter must contain a **BusType** entry that specifies the type of bus (such as PCI or ISA) on which the adapter can function. The possible values for the **BusType** entry are specified by the INTERFACE\_TYPE enumeration in the NDIS header file (ndis.h) as follows:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">BusType Entry</th>
<th align="left">Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>ISA</p></td>
<td align="left"><p>1</p></td>
</tr>
<tr class="even">
<td align="left"><p>EISA</p></td>
<td align="left"><p>2</p></td>
</tr>
<tr class="odd">
<td align="left"><p>MicroChannel</p></td>
<td align="left"><p>3</p></td>
</tr>
<tr class="even">
<td align="left"><p>TurboChannel</p></td>
<td align="left"><p>4</p></td>
</tr>
<tr class="odd">
<td align="left"><p>PCIBus</p></td>
<td align="left"><p>5</p></td>
</tr>
<tr class="even">
<td align="left"><p>VMEbus</p></td>
<td align="left"><p>6</p></td>
</tr>
<tr class="odd">
<td align="left"><p>NuBus</p></td>
<td align="left"><p>7</p></td>
</tr>
<tr class="even">
<td align="left"><p>PCMCIABus</p></td>
<td align="left"><p>8</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Cbus</p></td>
<td align="left"><p>9</p></td>
</tr>
<tr class="even">
<td align="left"><p>MPIBus</p></td>
<td align="left"><p>10</p></td>
</tr>
<tr class="odd">
<td align="left"><p>MPSABus</p></td>
<td align="left"><p>11</p></td>
</tr>
<tr class="even">
<td align="left"><p>PNPISABus</p></td>
<td align="left"><p>14</p></td>
</tr>
<tr class="odd">
<td align="left"><p>PNPBus</p></td>
<td align="left"><p>15</p></td>
</tr>
</tbody>
</table>

 

**Note**  If an adapter can function on more than one type of bus, the INF file that installs that adapter should contain a *DDInstall* section for each bus type.

 

For example, if an adapter can function on both the ISA bus and the PnPISA bus, the INF file for that adapter should contain a *DDInstall* section for ISA and a *DDInstall* section for PnPISA. The **BusType** entry in each such *DDInstall* section should specify the appropriate bus type for that section as follows:

```INF
[a1.isa]
BusType=1
 
[a1.pnpisa]
BusType=14
```

### Port1DeviceNumber and Port1FunctionNumber

The *DDInstall* section of an INF file that installs a multiport network adapter must include either a **Port1DeviceNumber** entry or a **Port1FunctionNumber** entry. Specifying such an entry causes the adapter's port information to be displayed in the **Connection Properties** dialog box (which is accessed through the **Network** and **Dial-Up Connections** folder) when you select the adapter name or icon.

-   If an adapter's port numbers map sequentially to PCI device numbers, use the **Port1DeviceNumber** entry. Set **Port1DeviceNumber** to the first PCI device number in the sequence. For example, if PCI device number 4 maps to port 1, PCI device number 5 maps to port 2, PCI device number 6 maps to port 3, and so forth, use the following entry:
    ```INF
    Port1DeviceNumber = 4
    ```

-   If an adapter's port numbers map sequentially to PCI function numbers, use the **Port1FunctionNumber** entry. Set **Port1FunctionNumber** to the first PCI function number in the sequence. For example, if PCI function number 2 maps to port 1, PCI function number 3 maps to port 2, PCI function number 4 maps to port 3, and so forth, use the following entry:
    ```INF
    Port1FunctionNumber = 2
    ```

**Note**  It is assumed that the mapping of PCI device numbers or PCI functions to port numbers is static. It is also assumed that the adapter's ports are numbered sequentially.

 

The **Port1DeviceNumber** and **Port1FunctionNumber** entries are mutually exclusive. If both entries are present in a given *DDInstall* Section, only the **Port1DeviceNumber** entry is used.

 

 





