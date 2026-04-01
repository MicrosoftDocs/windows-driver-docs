---
title: Updates for IddCx Versions 1.11 and Later
description: Learn about version 1.11 updates to the Indirect Display Driver Class eXtension (IddCx) for console and remote indirect display drivers.
ms.date: 04/01/2026
keywords:
- IddCx version 1.11
- Console and remote indirect display driver, IddCx versions 1.11 and later
- Console and remote IDD, IddCx versions 1.11 and later
- Console indirect display driver
- Console IDD
- Remote indirect display driver
- Remote IDD
- D3D12 support, IddCx
- Atomic read/write I2C DDI support, IddCx
- DisplayID only descriptors support, IddCx
- Static desktop reencode count support, IddCx
ms.topic: release-notes

#customer intent: As a driver developer, I want to know what changed in IddCx 1.11 so that I can update my indirect display driver to use the new features.

---

# Updates for IddCx versions 1.11 and later

> [!IMPORTANT]
> Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

This article describes the changes being made in IddCx 1.11. A single indirect display driver (IDD) binary built against IddCx 1.11 can run on Windows 10 1803 and above using runtime checks to verify if DDI changes in IddCx 1.11 are available on that system. For more information, see [Building a WDF driver for multiple versions of Windows](../wdf/building-a-wdf-driver-for-multiple-versions-of-windows.md).

The IddCx 1.11 changes fall into the following categories:

* Update the [IddCxGetVersion](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxgetversion) version (console and remote). For a complete list of IddCx-related version information, see [IddCx versions](iddcx-versions.md).
* Add ability to query OS feature support.
* Add support for using the D3D12 API.
* Add a new atomic read/write I2C DDI.
* Add support for DisplayID only descriptors.
* Add support for updating the static desktop reencode count.

## Update IddCxGetVersion version

The value returned by **IddCxGetVersion** has been updated to return 0x1B00.

## Query OS feature support

Drivers now have the ability to determine if a particular feature of IddCx 1.11 is available in the underlying OS by calling [IddCxCheckOsFeatureSupport](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxcheckosfeaturesupport). Multiple OS versions can report support for IddCx 1.11 through **IddCxGetVersion**, but possibly only some of the features will be available.

## D3D12 support

IddCx 1.11 drivers that support D3D12 can associate an [ID3D12Device](/windows/win32/api/d3d12/nn-d3d12-id3d12device) object with a swapchain and receive [ID3D12Resource](/windows/win32/api/d3d12/nn-d3d12-id3d12resource) objects using calls to [IddCxSwapChainReleaseAndAcquireBuffer2](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxswapchainreleaseandacquirebuffer2). An overview of the related changes is given in the following sections.

### Associating a D3D12 device with a swapchain

If a driver wishes to receive D3D12 frames then an **ID3D12Device** object needs to be provided in a call to [IddCxSwapChainSetDevice2](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxswapchainsetdevice2).

### Receiving D3D12 frames

After a driver has called **IddCxSwapChainSetDevice2** and provided an **ID3D12Device** object, the [IDARG_OUT_RELEASEANDACQUIREBUFFER2](/windows-hardware/drivers/ddi/iddcx/ns-iddcx-idarg_out_releaseandacquirebuffer2) passed to calls to [IddCxSwapChainReleaseAndAcquireBuffer2](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxswapchainreleaseandacquirebuffer2) will have the **IDDCX_METADATA2_VALID_FLAGS_D3D12SURFACE** flag set and then the driver should use **IDARG_OUT_RELEASEANDACQUIREBUFFER2.MetaData.pD3d12Surface** to access the pixel data.

### Synchronizing access to D3D12 surfaces

A significant change when a driver uses D3D12 is the synchronization model that controls access to the swap chain surfaces and avoid issues such as lock ups and accessing out of date pixel data has changed. Due to the more fine grained control D3D12 uses, drivers need to explicitly tell the OS which command queue is going to use the surface as input data.

More details on the driver responsibilities with regards to synchronization are given in the [IDDCX_METADATA2](/windows-hardware/drivers/ddi/iddcx/ns-iddcx-iddcx_metadata2) additions remarks.

## Atomic I2C support

A 1.11 driver that supports I2C by providing the [EVT_IDD_CX_MONITOR_I2C_RECEIVE](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_monitor_i2c_receive) and [EVT_IDD_CX_MONITOR_I2C_TRANSMIT](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_monitor_i2c_transmit) DDIs must also provide [EVT_IDD_CX_MONITOR_I2C_TRANSMIT_AND_RECEIVE](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_monitor_i2c_transmit_and_receive). This new DDI performs an I2C operation in a single call to help drivers that perform their own I2C operations from not interleaving with OS calls.

> [!NOTE]
> Drivers that provide the new DDI should not assume that the existing DDIs will no longer be used.

## DisplayID only descriptor support

A new descriptor type, IDDCX_MONITOR_DESCRIPTION_TYPE_DISPLAYID, has been added to the [IDDCX_MONITOR_DESCRIPTION_TYPE](/windows-hardware/drivers/ddi/iddcx/ne-iddcx-iddcx_monitor_description_type) enumeration used in the arguments passed to [IddCxMonitorCreate](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxmonitorcreate) and [IddCxMonitorCreate2](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxmonitorcreate2). This should be used when the provided descriptor contains just a DisplayID descriptor and no EDID blocks at all.

## Updating static desktop reencode count

Currently the static desktop reencode count is specified when creating an adapter. A new DDI now allows this value to be updated on a swap chain after the adapter is created.

## Supporting a 1.11 driver running down level

If a 1.11 driver is to run on older Windows releases, there are steps you need to take to ensure compatibility.

* The driver must set the size of the [IDD_CX_CLIENT_CONFIG](/windows-hardware/drivers/ddi/iddcx/ns-iddcx-idd_cx_client_config) structure using the **IDD_CX_CLIENT_CONFIG_INIT** macro.
* The driver must not set any of the new flags added to [IDDCX_ADAPTER_FLAGS](/windows-hardware/drivers/ddi/iddcx/ne-iddcx-iddcx_adapter_flags).
* The driver must not try and call any new functions provided by the OS as they aren't available. **IDD_IS_FUNCTION_AVAILABLE** can be used to check.
* None of the new functions can be exported. Drivers can use the **IDD_IS_FIELD_AVAILABLE** macro to check if the EvtIddXxx callback should be written to the **IDD_CX_CLIENT_CONFIG** structure.
* Even if the OS returns 0x1B00 from a call to **IddCxGetVersion**, the driver must query for specific feature support by calling **IddCxCheckOsFeatureSupport**.

The following example shows how **IDD_IS_FIELD_AVAILABLE** can be used:

```cpp
if (IDD_IS_FIELD_AVAILABLE(IDD_CX_CLIENT_CONFIG, EvtIddCxMonitorI2CTransmitAndReceive))
{
    IddCxClientConfig.EvtIddCxMonitorI2CTransmitAndReceive = MonitorI2CTransmitAndReceive;
}
```

For more information, see [Building IddCx 1.4 drivers](building-iddcx1.4-drivers.md).

## Which functions are used

| IddCx 1.11 feature | New functions OS calls for 1.11 adapters | Previous equivalent |
| ------------------ | -------------------------------------------- | ------------------- |
| Atomic I2C | [EVT_IDD_CX_MONITOR_I2C_TRANSMIT_AND_RECEIVE](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_monitor_i2c_transmit_and_receive) | [EVT_IDD_CX_MONITOR_I2C_TRANSMIT](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_monitor_i2c_transmit) and [EVT_IDD_CX_MONITOR_I2C_RECEIVE](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_monitor_i2c_receive) |

| IddCx 1.11 feature | New functions a driver must call | Previous equivalent |
| ------------------ | -------------------------------- | ------------------- |
| D3D12 | [IddCxSwapChainSetDevice2](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxswapchainsetdevice2) | [IddCxSwapChainSetDevice](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxswapchainsetdevice) |
| Update reencode count | [IddCxSwapChainUpdateStaticDesktopReencodeFrameCount](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxswapchainupdatestaticdesktopreencodeframecount) | N/A |

## Previous releases

For information about changes in earlier IddCx versions, see the following articles:

* [Updates for IddCx versions 1.10 and later](iddcx1.10-updates.md)
* [Updates for IddCx versions 1.9 and later](iddcx1.9-updates.md)
* [Updates for IddCx versions 1.8 and later](iddcx1.8-updates.md)
* [Updates for IddCx versions 1.7 and later](iddcx1.7-updates.md)
* [Updates for IddCx versions 1.6 and later](iddcx1.6-updates.md)
* [Updates for IddCx versions 1.4 and later](iddcx1.4-updates-for-console-and-remote-idds.md)

