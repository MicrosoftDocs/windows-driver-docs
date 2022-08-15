---
title: INF Requirements for NDKPI
description: The INF file for a miniport driver that supports Network Direct kernel (NDK) must meet the following requirements.
ms.date: 04/20/2017
---

# INF Requirements for NDKPI


The INF file for a miniport driver that supports Network Direct kernel (NDK) must meet the following requirements.

-   The miniport driver's INF file must specify an NDIS upper range value of "ndis5" in order for Windows components to discover and use the NDK-capable miniport adapters that are serviced by the driver. This value is specified as follows:

    ```INF
    HKR, Ndi\Interfaces, UpperRange, 0, "ndis5"
    ```

-   The INF file must specify the **\*NetworkDirect** keyword value as follows. Once the driver is installed, administrators can update the **\*NetworkDirect** keyword value in the **Advanced** property page for the adapter. 

    **Note**   The miniport driver is automatically restarted after a change is made in the **Advanced** property page for the adapter.

    ```INF
    HKR, Ndi\Params\*NetworkDirect,        ParamDesc,  0, "NetworkDirect Functionality"
    HKR, Ndi\Params\*NetworkDirect,        Type,       0, "enum"
    HKR, Ndi\Params\*NetworkDirect,        Default,    0, "1"
    HKR, Ndi\Params\*NetworkDirect\enum,   "0",        0, "Disabled"
    HKR, Ndi\Params\*NetworkDirect\enum,   "1",        0, "Enabled"
    ```

-   The INF file must specify the **\*NetworkDirectTechnology** keyword value as follows. Once the driver is installed, administrators can update the **\*NetworkDirectTechnology** keyword value in the **Advanced** property page for the adapter. The enumerations are mutually exclusive, meaning  the selection of a NetworkDirectTechnology value excludes all others.  This allows for the Platform to define strict device behavior.  
-   A device must express only the supported transports.  The transport values are identifiers which map to WDK **NDK_RDMA_TECHNOLOGY**.  A redefinition of the identifiers is prohibited.
-   The behavior of devices with multiple concurrent transports is undefined.  The device **must** specify a transport type.

    **Note**   The miniport driver is automatically restarted after a change is made in the **Advanced** property page for the adapter.

    ```INF
    HKR, Ndi\Params\*NetworkDirectTechnology,        ParamDesc,  0,  "NetworkDirect Technology"
    HKR, Ndi\Params\*NetworkDirectTechnology,        Default,    0,  "1"
    HKR, Ndi\Params\*NetworkDirectTechnology,        Type,       0,  "enum"
    HKR, Ndi\Params\*NetworkDirectTechnology\enum,   1,          0,  "iWARP"
    HKR, Ndi\Params\*NetworkDirectTechnology\enum,   2,          0,  "InfiniBand"
    HKR, Ndi\Params\*NetworkDirectTechnology\enum,   3,          0,  "RoCE"
    HKR, Ndi\Params\*NetworkDirectTechnology\enum,   4,          0,  "RoCEv2"
    HKR, Ndi\Params\*NetworkDirectTechnology,        Optional,   0,  "0"
    ```

    For more information about advanced properties, see [Specifying Configuration Parameters for the Advanced Properties Page](specifying-configuration-parameters-for-the-advanced-properties-page.md).

    For more information about using standardized INF keywords, see [Standardized INF Keywords for Network Devices](standardized-inf-keywords-for-network-devices.md).

## Related topics


[Network Direct Kernel Provider Interface (NDKPI)](./overview-of-network-direct-kernel-provider-interface--ndkpi-.md)

