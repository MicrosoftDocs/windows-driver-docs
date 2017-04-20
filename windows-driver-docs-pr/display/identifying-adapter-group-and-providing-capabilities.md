---
title: Identifying Adapter Group and Providing Capabilities
description: Identifying Adapter Group and Providing Capabilities
ms.assetid: 44a2ac71-8852-472f-82a2-7bd4d7dffa1a
keywords:
- multiple-head hardware WDK DirectX 9.0 , configuring
- multiple-head hardware WDK DirectX 9.0 , adapters
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Identifying Adapter Group and Providing Capabilities


## <span id="ddk_identifying_adapter_group_and_providing_capabilities_gg"></span><span id="DDK_IDENTIFYING_ADAPTER_GROUP_AND_PROVIDING_CAPABILITIES_GG"></span>


The DirectX 9.0 runtime sends a **GetDriverInfo2** request using the D3DGDI2\_TYPE\_GETADAPTERGROUP value to a DirectX 9.0 version driver to request the identifier for the group of adapters that make up the driver's multiple-head video card. The driver returns the identifier in the **ulUniqueAdapterGroupId** member of a [**DD\_GETADAPTERGROUPDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551529) structure. The driver must provide a unique identifier for the master and all subordinate adapters within a group. The runtime uses this identifier in subsequent operations to determine whether the given adapter is part of a group. This identifier must be unique across drivers, including drivers from other hardware vendors. Therefore, it is recommended to report this identifier as a unique nonzero kernel-mode address that cannot be common with other multiple-head video cards.

A DirectX 9.0 version driver indicates how its multiple-head hardware is configured by setting the following members of the D3DCAPS9 structure:

-   **NumberOfAdaptersInGroup**

    Specifies the number of adapters in the adapter group (only if master). This is 1 for single-head cards (conventional adapters). The value is greater than 1 for the master adapter of a multiple-head card. The value is 0 for a subordinate adapter of a multiple-head card. Each card can have at most one master, but can have many subordinates.

-   **MasterAdapterOrdinal**

    Specifies the number for the master adapter in the group. This number is relevant if the system contains more than one multiple-head card. For example, if the system contains a single-head card, a double-head card, and a triple-head card, the system references the heads as: 0 for the single, 1 and 2 for the double, and 3, 4, and 5 for the triple. In this case, the master adapter is: 0 for the single, 1 for the double, and 3 for the triple.

-   **AdapterOrdinalInGroup**

    Specifies a number that indicates the order in which heads in a group are referenced by the driver. This value is always 0 for the master adapter and numbered consecutively for each subordinate adapter (that is, 1, 2, and so on).

The driver returns a D3DCAPS9 structure in response to a **GetDriverInfo2** query similarly to how it returns a D3DCAPS8 structure as described in [Reporting DirectX 8.0 Style Direct3D Capabilities](reporting-directx-8-0-style-direct3d-capabilities.md). Support of this query is described in [Supporting GetDriverInfo2](supporting-getdriverinfo2.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Identifying%20Adapter%20Group%20and%20Providing%20Capabilities%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




