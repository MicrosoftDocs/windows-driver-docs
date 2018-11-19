---
title: Configuring an INF File for a Modifying Filter Driver
description: Configuring an INF File for a Modifying Filter Driver
ms.assetid: d9eac8f6-a560-41e5-ae71-3bd9d6714c3a
keywords:
- INF files WDK network , filter drivers
- modifying filter drivers WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Configuring an INF File for a Modifying Filter Driver





The following NDIS filter driver installation issues are associated with modifying filter drivers. To create your own modifying filter driver INF file, you can also adapt the [sample NDIS 6.0 filter driver](http://go.microsoft.com/fwlink/p/?LinkId=618052).

-   Set the **Class** INF file entry to **NetService** in the INF file. The following example shows a sample **Class** entry for the INF file.
    ```INF
    Class = NetService
    ```

-   The *DDInstall* section in a filter driver INF file must have a **Characteristics** entry. The following example shows how you should define the **Characteristics** entry in your filter INF file.

    ```INF
    Characteristics=0x40000
    ```

    The 0x40000 value indicates that NCF\_LW\_FILTER (0x40000) is set. Filter drivers must not set the NCF\_FILTER (0x400) flag. The values of the NCF\_ *Xxx* flags are defined in *Netcfgx.h*. For more information about NCF\_ *Xxx* flags, see [DDInstall Section in a Network INF File](ddinstall-section-in-a-network-inf-file.md).

-   Set the **NetCfgInstanceId** INF file entry in the INF file, as the following example shows.

    ```INF
    NetCfgInstanceId="{5cbf81bd-5055-47cd-9055-a76b2b4e3697}"
    ```

    You can use the *Uuidgen.exe* tool to create the GUID for the **NetCfgInstanceId** entry.

-   The *DDInstall* section of the INF file for a filter driver must include an **Addreg** directive for an **Ndi** key. The INF file must specify the **Service** entry under the **Ndi** key. The **ServiceBinary** entry in the *service-install* section of the INF file specifies the path to the binary for the filter driver. For more information, see [Adding Service Related Values to the Ndi Key](adding-service-related-values-to-the-ndi-key.md) and [DDInstall.Services Section in a Network INF File](ddinstall-services-section-in-a-network-inf-file.md).

-   The *DDInstall* section in a filter driver INF file must have **FilterType** and **FilterRunType** entries. To specify a modifying filter, define the **FilterType** entry in your INF file, as the following example shows.

    ```INF
    HKR, Ndi,FilterType,0x00010001 ,0x00000002
    ```

    The **FilterType** value 0x00000002 indicates that the filter is a modifying filter.

-   Define the **FilterRunType** entry in your INF file, as the following example shows.

    ```INF
    HKR, Ndi,FilterRunType,0x00010001 ,0x00000001
    ```

    The 0x00000001 value in the preceding example indicates that the filter module is mandatory. To install an optional filter module, set the **FilterRunType** entry to 0x00000002. For more information, see [Mandatory Filter Drivers](mandatory-filter-drivers.md).

-   The following example shows how a modifying filter driver INF file specifies the name of the service.

    ```INF
    HKR, Ndi,Service,,"NdisLwf"
    ```

    In this example, NdisLwf is the name of the driver's service as it is reported to NDIS. Note that the name of a filter driver's service can be different from the name of the binary for the driver—but typically they are the same.

-   The following example shows how the filter INF file references the name of the filter driver's service when it adds that service.
    ```INF
    [Install.Services]
    AddService=NdisLwf,,NdisLwf_Service_Inst;, common.EventLog 

    [NdisLwf_Service_Inst]
    DisplayName     = %NdisLwf_Desc%
    ServiceType     = 1 ;SERVICE_KERNEL_DRIVER
    StartType       = 1 ;SERVICE_SYSTEM_START
    ErrorControl    = 1 ;SERVICE_ERROR_NORMAL
    ServiceBinary   = %12%\ndislwf.sys
    LoadOrderGroup  = NDIS
    Description     = %NdisLwf_Desc%
    AddReg          = Common.Params.reg
    ```

-   A filter INF file must specify at least the primary service name of the filter for the **CoServices** attribute, as the following example shows.

    ```INF
    HKR, Ndi,CoServices,0x00010000,"NdisLwf"
    ```

    For more information about the **CoServices** attribute, see [Adding Service Related Values to the Ndi Key](adding-service-related-values-to-the-ndi-key.md).

-   The **FilterClass** value in the INF file for a filter driver determines its order in a stack of filters. Filter drivers must define the **FilterClass** key. The class of the driver can be one of the values in the following table.

    <table>
    <colgroup>
    <col width="50%" />
    <col width="50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th align="left">Value</th>
    <th align="left">Description</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td align="left"><p>scheduler</p></td>
    <td align="left"><p>Packet scheduling filter service. This class of filter driver is the highest-level driver that can exist above encryption class filters in a driver stack. A packet scheduler detects the 802.1p priority classification that is given to packets by quality of service (QoS) signaling components and the scheduler sends those packets levels to underlying drivers according to their priority.</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>encryption</p></td>
    <td align="left"><p>Encryption class filter drivers exist between scheduler and compression class filters.</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>compression</p></td>
    <td align="left"><p>Compression class filter drivers exist between encryption and vpn class filters.</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>vpn</p></td>
    <td align="left"><p>VPN class filter drivers exist between compression and load balance filter drivers.</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>loadbalance</p></td>
    <td align="left"><p>Load balancing filter service. This class of filter driver exists between packet scheduling and failover drivers. A load balancing filter service balances its workload of packet transfers by distributing the workload over its set of underlying miniport adapters.</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>failover</p></td>
    <td align="left"><p>Failover filter service. This class of filter driver exists between load balance and diagnostics drivers.</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>diagnostic</p></td>
    <td align="left"><p>Diagnostic filter drivers exist below failover drivers in the stack.</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>custom</p></td>
    <td align="left"><p>Filter drivers in custom class exist below diagnostic drivers.</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>provider_address</p></td>
    <td align="left"><p>Provider address filter drivers exist below the in-box Hyper-V Network Virtualization ms_wnv filter and operate on provider address (PA) packets.</p></td>
    </tr>
    </tbody>
    </table>




**Note**  More than one filter driver of a specific class can exist in a layered stack of modifying filter drivers. For example, two modifying filter drivers of **FilterClass** "scheduler" can exist in a stack simultaneously. The filter driver that has an earlier installation time stamp is installed below (that is, closer to the miniport adapter) the filter driver with the later time stamp. However, the order of multiple filter drivers with the same class is exactly the same over different miniport adapters on the same computer.



The following example shows a sample **FilterClass** .

```INF
HKR, Ndi,FilterClass,, compression
```


- Only Hyper-V switch extension filter drivers are valid in the Hyper-V Extensible Switch. Hyper-V extensible switch filter drivers must define the FilterClass key with one of the values in the following table.

  <table>
  <colgroup>
  <col width="50%" />
  <col width="50%" />
  </colgroup>
  <thead>
  <tr class="header">
  <th align="left">Value</th>
  <th align="left">Description</th>
  </tr>
  </thead>
  <tbody>
  <tr class="odd">
  <td align="left"><p>ms_switch_capture</p></td>
  <td align="left"><p>Starting with NDIS 6.30, capture drivers monitor packet traffic in the Hyper-V extensible switch driver stack. This class of filter driver exists below custom drivers in the stack.</p>
  <p>For more information about this class of driver, see <a href="capturing-extensions.md" data-raw-source="[Capturing Extensions](capturing-extensions.md)">Capturing Extensions</a>.</p></td>
  </tr>
  <tr class="even">
  <td align="left"><p>ms_switch_filter</p></td>
  <td align="left"><p>Starting with NDIS 6.30, filtering drivers filter packet traffic and enforce port or switch policy for packet delivery through the extensible switch driver stack. This class of filter driver exists below <strong>ms_switch_capture</strong> drivers in the stack.</p>
  <p>For more information about this class of driver, see <a href="filtering-extensions.md" data-raw-source="[Filtering Extensions](filtering-extensions.md)">Filtering Extensions</a>.</p></td>
  </tr>
  <tr class="odd">
  <td align="left"><p>ms_switch_forward</p></td>
  <td align="left"><p>Starting with NDIS 6.30, forwarding drivers filter perform the same functions as a filtering driver. Forwarding drivers also forward packets to and from extensible switch ports. This class of filter driver exists below <strong>ms_switch_filter</strong> drivers in the stack.</p>
  <p>For more information about this class of driver, see <a href="forwarding-extensions.md" data-raw-source="[Forwarding Extensions](forwarding-extensions.md)">Forwarding Extensions</a>.</p></td>
  </tr>
  </tbody>
  </table>



- You must define the following entries in the modifying filter driver INF file to control the driver bindings.

  ```INF
  HKR, Ndi\Interfaces,UpperRange,,"noupper"
  HKR, Ndi\Interfaces,LowerRange,,"nolower"
  HKR, Ndi\Interfaces, FilterMediaTypes,,"ethernet"
  ```

  For more information about controlling the driver bindings, see [Specifying Filter Driver Binding Relationships](specifying-filter-driver-binding-relationships.md).

- A modifying filter INF file should specify common parameter definitions for the driver and parameters that are associated with a specific adapter. The following example shows some common parameter definitions.
  ```INF
  [Common.Params.reg]

  HKR, FilterDriverParams\DriverParam,  ParamDesc, , "Driverparam for lwf"
  HKR, FilterDriverParams\DriverParam,  default, , "5"
  HKR, FilterDriverParams\DriverParam,  type,  , "int"

  HKR, FilterAdapterParams\AdapterParam,  ParamDesc, , "Adapterparam for lwf"
  HKR, FilterAdapterParams\AdapterParam,  default, , "10"
  HKR, FilterAdapterParams\AdapterParam,  type,  , "int"
  ```









