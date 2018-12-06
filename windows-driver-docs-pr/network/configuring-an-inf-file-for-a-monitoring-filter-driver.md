---
title: Configuring an INF File for a Monitoring Filter Driver
description: Configuring an INF File for a Monitoring Filter Driver
ms.assetid: b45c6f40-7254-4cc1-a007-d40eaa74a290
keywords:
- INF files WDK network , filter drivers
- monitoring filter drivers WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Configuring an INF File for a Monitoring Filter Driver





The following NDIS filter driver installation issues are associated with monitoring filter drivers:

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
    NetCfgInstanceId="{5cbf81bf-5055-47cd-9055-a76b2b4e3697}"
    ```

    You can use the *Uuidgen.exe* tool to create the GUID for the **NetCfgInstanceId** entry.

-   The *DDInstall* section of the INF file for a filter driver must include an **Addreg** directive for an **Ndi** key. The INF file must specify the **Service** entry under the **Ndi** key. The **ServiceBinary** entry in the *service-install* section of the INF file specifies the path to the binary for the filter driver. For more information, see [Adding Service-Related Values to the Ndi Key](adding-service-related-values-to-the-ndi-key.md) and [DDInstall.Services Section in a Network INF File](ddinstall-services-section-in-a-network-inf-file.md).

-   The *DDInstall* section in a filter driver INF file must have **FilterType** and **FilterRunType** entries. To specify a monitoring filter, define the **FilterType** entry in your INF file, as the following example shows.

    ```INF
    HKR, Ndi,FilterType,0x00010001 ,0x00000001
    ```

    The **FilterType** value 0x00000001 indicates that the filter is a monitoring filter.

-   Define the **FilterRunType** entry in your INF file, as the following example shows.

    ```INF
    HKR, Ndi,FilterRunType,0x00010001 ,0x00000002
    ```

    The 0x00000002 value in the preceding example indicates that the filter module is optional. To install a mandatory filter module, set the **FilterRunType** entry to 0x00000001. For more information, see [Mandatory Filter Drivers](mandatory-filter-drivers.md).

    **Note**  We highly recommend that a monitoring lightweight filter (LWF) driver should not be mandatory, unless it is to be used in a controlled environment where there will be no optional modifying LWF drivers. This is because a mandatory monitoring LWF driver can cause optional modifying LWF drivers to fail [*FilterAttach*](https://msdn.microsoft.com/library/windows/hardware/ff549905). A monitoring LWF driver is bound over every modifying filter and binding by design to facilitate monitoring of networking traffic at all levels. Consider the following scenario:
    -   An instance of a mandatory monitoring LWF driver is installed over an optional modifying LWF driver.
    -   The lower modifying optional LWF driver fails to attach to a lower component. This will cause the mandatory monitoring LWF driver’s [*FilterAttach*](https://msdn.microsoft.com/library/windows/hardware/ff549905) handler not to be called.
    -   Because now an instance of a mandatory LWF driver is not loaded, NDIS will not bind any protocols (such as TCP/IP) to the interface or NIC, thus rendering the interface to be unusable.

     

-   The following example shows how a filter driver INF file specifies the name of the service.

    ```INF
    HKR, Ndi,Service,,"NdisMon"
    ```

    In this example, "NdisMon" is the name of the driver's service as it is reported to NDIS. Note that the name of a filter driver's service can be different from the name of the binary for the driver, but typically they are the same.

-   The following example shows how the filter INF file references the name of the filter driver's service when it adds that service.
    ```INF
    [Install.Services]
    AddService=NdisMon,,NdisMon_Service_Inst

    [NdisMon_Service_Inst]
    DisplayName     = %NdisMon_Desc%
    ServiceType     = 1 ;SERVICE_KERNEL_DRIVER
    StartType       = 1 ;SERVICE_SYSTEM_START
    ErrorControl    = 1 ;SERVICE_ERROR_NORMAL
    ServiceBinary   = %12%\ndisMon.sys
    LoadOrderGroup  = NDIS
    Description     = %NdisMon_Desc%
    AddReg          = Common.Params.Reg
    ```

-   A filter INF file must specify at least the primary service name of the filter for the **CoServices** attribute, as the following example shows.

    ```INF
    HKR, Ndi,CoServices,0x00010000,"NdisMon"
    ```

    For more information about the **CoServices** attribute, see [Adding Service-Related Values to the Ndi Key](adding-service-related-values-to-the-ndi-key.md).

-   The **FilterClass** value in the INF file for a filter driver determines its order in a stack of modifying filters. However, monitoring filter drivers do not define the **FilterClass** key. Instead the monitoring filter module that is installed first is closest to the miniport adapter.

-   You must define the following entries in the monitoring filter driver INF file to control the driver bindings:

    ```INF
    HKR, Ndi\Interfaces,UpperRange,,"noupper"
    HKR, Ndi\Interfaces,LowerRange,,"nolower"
    HKR, Ndi\Interfaces, FilterMediaTypes,,"ethernet"
    ```

    For more information about controlling the driver bindings, see [Specifying Filter Driver Binding Relationships](specifying-filter-driver-binding-relationships.md).

-   A monitoring filter INF file should specify common parameter definitions for the filter driver, parameters that are associated with a specific adapter, and parameters that are associated with a particular instance (filter module). The following example shows some common parameter definitions.
    ```INF
    [Common.Params.reg]

    HKR, FilterDriverParams\DriverParam, ParamDesc, ,"Driverparam for filter"
    HKR, FilterDriverParams\DriverParam, default, ,"5"
    HKR, FilterDriverParams\DriverParam, type,  ,"int"

    HKR, FilterAdapterParams\AdapterParam, ParamDesc, ,"Adapterparam for filter"
    HKR, FilterAdapterParams\AdapterParam, default, ,"10"
    HKR, FilterAdapterParams\AdapterParam, type,  ,"int"

    HKR, FilterInstanceParams\InstanceParam, ParamDesc, ,"Instance param for filter"
    HKR, FilterInstanceParams\InstanceParam, default, ,"15"
    HKR, FilterInstanceParams\InstanceParam, type,  ,"int"
    ```

 

 





