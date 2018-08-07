---
title: Device and adapter initialization
description: Device and adapter initialization
ms.assetid: EBBEF0FB-6CDB-4899-AAE9-71812EE20AFB
keywords:
- NetAdapterCx device initialization, NetCx device initialization, NetAdapterCx adapter initialization, NetCx adapter initialization
ms.author: windowsdriverdev
ms.date: 08/02/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# Device and adapter initialization

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

This topic describes the steps for a NetAdapterCx client driver to initialize and start WDFDEVICE and NETADAPTER objects. For more info about these objects and their relationship, see [Summary of NetAdapterCx objects](summary-of-netadaptercx-objects.md).

## EVT_WDF_DRIVER_DEVICE_ADD

A NetAdapterCx client driver registers its [*EVT_WDF_DRIVER_DEVICE_ADD*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback function when it calls [**WdfDriverCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547175) from its [*DriverEntry*](https://msdn.microsoft.com/library/windows/hardware/ff540807) routine.

In [*EVT_WDF_DRIVER_DEVICE_ADD*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add), a NetAdapterCx client driver should do the following in order:

1. Call [**NetAdapterDeviceInitConfig**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-netadapterdeviceinitconfig).

    ```C++
    status = NetAdapterDeviceInitConfig(DeviceInit);
    if (!NT_SUCCESS(status)) 
    {
        return status;
    }
    ```

2. Call [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926).

3. Create the default NETADAPTER object. To do so, the client calls [**NetDefaultAdapterInitAllocate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-netdefaultadapterinitallocate), followed by optional **NetAdapterInitSetXxx** methods to initailize the adapter's attributes. Finally, the client calls [**NetAdapterCreate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-netadaptercreate). 

    ```C++
    WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE(&attribs, MYDRIVER_ADAPTER_CONTEXT);

    PNETADAPTER_INIT adapterInit = NetDefaultAdapterInitAllocate(device);
    if(adapterInit == NULL)
    {
        return status;
    }

    //
    // Optional: Set additional attributes
    //

    // Datapath callbacks for creating packet queues
    PNET_ADAPTER_DATAPATH_CALLBACKS datapathCallbacks;
    NET_ADAPTER_DATAPATH_CALLBACKS_INIT(datapathCallbacks,
                                        MyEvtAdapterCreateTxQueue,
                                        MyEvtAdapterCreateRxQueue);
    NetAdapterInitSetDatapathCallbacks(adapterInit,
                                       datapathCallbacks);

    // Power settings attributes
    NetAdapterInitSetNetPowerSettingsAttributes(adapterInit,
                                                attribs);

    // Net request attributes
    NetAdapterInitSetNetRequestAttributes(adapterInit,
                                          attribs);

    // 
    // Required: create the adapter
    //
    status = NetAdapterCreate(adapterInit, &attribs, &adapter);
    if(!NT_SUCCESS(status))
    {
        NetAdapterInitFree(adapterInit);
        adapterInit = NULL;
        return status;
    }
    ```

Optionally, you can add context space to the NETADAPTER object. Since you can set a context on any WDF object, you could add separate context space for the WDFDEVICE and the NETADAPTER objects. In the example in step 4, the client adds `MYDRIVER_ADAPTER_CONTEXT` to the NETADAPTER object. For more info, see [Framework Object Context Space](../wdf/framework-object-context-space.md).

We recommend that you put device-related data in the context for your WDFDEVICE, and networking-related data into your NETADAPTER context. If you are porting an existing NDIS 6.x driver, you'll likely have a single MiniportAdapterContext that combines networking-related and device-related data into a single data structure. To simplify the porting process, just convert that entire structure to the WDFDEVICE context, and make the NETADAPTER's context a small structure that points to the WDFDEVICE's context.

You'll provide 2 callbacks to the [**NET_ADAPTER_DATAPATH_CALLBACKS_INIT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-net_adapter_datapath_callbacks_init) method:

* [*EVT_NET_ADAPTER_CREATE_TXQUEUE*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nc-netadapter-evt_net_adapter_create_txqueue)
* [*EVT_NET_ADAPTER_CREATE_RXQUEUE*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nc-netadapter-evt_net_adapter_create_rxqueue)

For details on what to provide in your implementations of these callbacks, see the individual reference pages.

## EVT_WDF_DEVICE_PREPARE_HARDWARE

To register an [*EVT_WDF_DEVICE_PREPARE_HARDWARE*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware) callback function, a NetAdapterCx client driver must call [**WdfDeviceInitSetPnpPowerEventCallbacks**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdeviceinitsetpnppowereventcallbacks). 

In [*EVT_WDF_DEVICE_PREPARE_HARDWARE*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware), the client driver must call [**NetAdapterStart**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-netadapterstart). Before doing so, the driver can optionally set capabilities like in the following example.

```C++
//
// Optional: set adapter capabilities
//
NETADAPTER* netAdapter = MyGetDeviceContext(device)->NetAdapter;

MyAdapterSetLinkLayerCapabilities(&netAdapter);

MyAdapterSetReceiveScalingCapabilities(&netAdapter);

MyAdapterSetPowerCapabilities(&netAdapter);

MyAdapterSetDatapathCapabilities(&netAdapter);

MyAdapterSetOffloadCapabilities(&netAdapter);

//
// Required: start the adapter
//
status = NetAdapterStart(&netAdapter);
if(!NT_SUCCESS(status))
{
    return status;
}
```