---
title: Device initialization
description: Device initialization
ms.assetid: EBBEF0FB-6CDB-4899-AAE9-71812EE20AFB
keywords:
- NetAdapterCx device initialization, NetCx device initialization
ms.author: windowsdriverdev
ms.date: 06/05/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# Device initialization

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

A NetAdapterCx driver registers its [*EVT_WDF_DRIVER_DEVICE_ADD*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function when it calls [**WdfDriverCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547175) from its [*DriverEntry*](https://msdn.microsoft.com/library/windows/hardware/ff540807) routine.

## EVT_WDF_DRIVER_DEVICE_ADD

In [*EVT_WDF_DRIVER_DEVICE_ADD*](https://msdn.microsoft.com/library/windows/hardware/ff541693), a NetAdapterCx client driver should do the following in order:

1. Call [**NetAdapterDeviceInitConfig**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-netadapterdeviceinitconfig).

    ```C++
    status = NetAdapterDeviceInitConfig(DeviceInit);
    if (!NT_SUCCESS(status)) 
    {
        return status;
    }
    ```

2. Call [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926).

3. Create the NETADAPTER object.  This object represents your NIC, which is the endpoint for all networking I/O.  To create the NETADAPTER object, the client typically calls [**NetDefaultAdapterInitAllocate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-netdefaultadapterinitallocate) if this is the primary NETADAPTER, followed by **NetAdapterInitXxx** functions to initailize the adapter's capabilities. Finally, the client calls [**NetAdapterCreate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-netadaptercreate). 

    ```C++
    WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE(&attribs, MYDRIVER_ADAPTER_CONTEXT);

    PNETADAPTER_INIT adapterInit = NetDefaultAdapterInitAllocate(device);

    // Datapath callbacks for creating packet queues
    PNET_ADAPTER_DATAPATH_CALLBACKS datapathCallbacks;
    NET_ADAPTER_DATAPATH_CALLBACKS_INIT(datapathCallbacks,
                                        MyEvtAdapterCreateTxQueue,
                                        MyEvtAdapterCreateRxQueue);
    NetAdapterInitSetDatapathCallbacks(adapterInit,
                                       datapathCallbacks);

    // Power settings attributes
    NetAdapterInitSetNetPowerSettingsAttributes(adapterInit,
                                                WDF_NO_OBJECT_ATTRIBUTES);

    // Net request attributes
    NetAdapterInitSetNetRequestAttributes(adapterInit,
                                          WDF_NO_OBJECT_ATTRIBUTES);

    // Create the adapter
    status = NetAdapterCreate(adapterInit, &attribs, &adapter);
    if(!NT_SUCCESS(status))
    {
        NetAdapterInitFree(adapterInit);
        goto Exit;
    }
    ```

You can have multiple NETADAPTER objects per WDFDEVICE, with the WDFDEVICE being the parent object of each NETADAPTER. The primary NETADAPTER is called the *default adapter*. Most NIC drivers only have one adapter, but some server NIC drivers or [mobile broadband class extension (MBBCx)](mobile-broadband-mbb-wdf-class-extension-mbbcx.md) drivers might have more than one. Each subsequent NETADAPTER is initialized with [**NetAdapterInitAllocate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-netadapterinitallocate) instead of **NetDefaultAdapterInitAllocate**. You can find the object hierarchy in [Summary of objects](summary-of-objects.md).

Optionally, you can add context space to the NETADAPTER object. Since you can set a context on any WDF object, you could add separate context space for the WDFDEVICE and the NETADAPTER objects. In the example in step 4, the client adds `MYDRIVER_ADAPTER_CONTEXT` to the NETADAPTER object. For more info, see [Framework Object Context Space](../wdf/framework-object-context-space.md).

We recommend that you put device-related data in the context for your WDFDEVICE, and networking-related data into your NETADAPTER context.  If you are porting an existing NDIS 6.x driver, you'll likely have a single MiniportAdapterContext that combines networking-related and device-related data into a single data structure.  To simplify the porting process, just convert that entire structure to the WDFDEVICE context, and make the NETADAPTER's context a small structure that points to the WDFDEVICE's context.

You'll provide 2 callbacks to the [**NET_ADAPTER_DATAPATH_CALLBACKS_INIT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-net_adapter_datapath_callbacks_init) method:

* [*EVT_NET_ADAPTER_CREATE_TXQUEUE*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nc-netadapter-evt_net_adapter_create_txqueue)
* [*EVT_NET_ADAPTER_CREATE_RXQUEUE*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nc-netadapter-evt_net_adapter_create_rxqueue)

For details on what to provide in your implementations of these callbacks, see the individual reference pages.
