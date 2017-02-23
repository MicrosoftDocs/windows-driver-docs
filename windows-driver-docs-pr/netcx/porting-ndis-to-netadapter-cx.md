# Porting NDIS Miniport Drivers to NetAdapter Class Extension

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

You are reading a practical guide on how to convert a pre-existing NDIS 6.x miniport driver into a WDF-based networking client miniport driver (called the client driver in this section).

Before beginning this conversion, it will be helpful to understand some of the <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/wdf/index">basic architecture & conventions</a> of WDF.

## Compilation Settings

Ensure your project links against the latest version of KMDF.  Also link against NetAdapterCxStub.lib (located in “Windows Kits\10\Lib\<latest_windows_version>\km\<architecture>\netadaptercx\1.0”).

It is no longer strictly necessary to link against ndis.lib, although you may still want to use some NDIS APIs, so you may still link against it.

It is no longer necessary to set NDIS preprocessor macros, like NDIS650_MINIPORT=1.

Add these headers to every source file (or to your common/precompiled header):

```ManagedCPlusPlus
#include <ntddk.h>
#include <wdf.h>
#include <netadaptercx.h>
```

Add the <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/wdf/specifying-wdf-directives-in-inf-files">standard WDF decorations</a> to your INF, if not already there.  Example:

```Inf
[Yourdriver.Wdf]
KmdfService = Yourdriverservice, Yourdriver.wdfsect

[Yourdriver.wdfsect]
KmdfLibraryVersion = <insert here>
```

## Driver Initialization

Remove the call to [**NdisMRegisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563654) from DriverEntry.

Put the standard WDF driver initialization in [DriverEntry](https://msdn.microsoft.com/library/windows/hardware/ff540807).  Do not specify the **WdfDriverInitNoDispatchOverride** flag in the call to [**WdfDriverCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547175). Remove this flag if you were using WDF in miniport mode in your NDIS 6.x driver.  For example:

```ManagedCPlusPlus
WDF_DRIVER_CONFIG_INIT(&config, EvtDriverDeviceAdd);
status = WdfDriverCreate(. . . );
if (!NT_SUCCESS(status)) {
    return status;
}
```

 Consider removing the *DriverUnload* routine from your client driver, as it is an optional routine for a WDF networking client driver.  If you keep it, remove the call to [**NdisMDeregisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563578) from *DriverUnload*.

## Device Initialization

Next, we need to break *MiniportInitializeEx* into several pieces, each of which is a standard WDF event.  <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/wdf/power-up-sequence-for-a-function-or-filter-driver">The full sequence of events</a> includes many events, most of which are optional.  You should move code into the most logical place, based on the WDF semantics of each state.

In general, callbacks you'll need to provide are:

- [*EVT_WDF_DRIVER_DEVICE_ADD*](https://msdn.microsoft.com/library/windows/hardware/ff541693)
- [*EVT_WDF_DEVICE_PREPARE_HARDWARE*](https://msdn.microsoft.com/library/windows/hardware/ff540880)
- [*EVT_WDF_DEVICE_D0_ENTRY*](https://msdn.microsoft.com/library/windows/hardware/ff540848)

While you may need to handle several events to properly manage your device, the system requires only that the client driver do a few things in [*EVT_WDF_DRIVER_DEVICE_ADD*](https://msdn.microsoft.com/library/windows/hardware/ff541693).

## Creating the NETADAPTER Object

In [*EVT_WDF_DRIVER_DEVICE_ADD*](https://msdn.microsoft.com/library/windows/hardware/ff541693), your driver should do the following:

1. Call [**NetAdapterDeviceInitConfig**](netadapterdeviceinitconfig.md).
2. Load pointers to your driver's callbacks and call [**WdfDeviceInitSetPnpPowerEventCallbacks**](https://msdn.microsoft.com/library/windows/hardware/ff546135).  For example:

    ```ManagedCPlusPlus
    status = NetAdapterDeviceInitConfig(DeviceInit);
    if (!NT_SUCCESS(status)) {
        return status;
    }

    WDF_PNPPOWER_EVENT_CALLBACKS_INIT(&pnpPowerCallbacks);
    pnpPowerCallbacks.EvtDevicePrepareHardware      = ...;
    pnpPowerCallbacks.EvtDeviceD0Entry              = ...;
    pnpPowerCallbacks.EvtDeviceD0Exit               = ...;
    pnpPowerCallbacks.EvtDeviceReleaseHardware      = ...;

    WdfDeviceInitSetPnpPowerEventCallbacks(DeviceInit, &pnpPowerCallbacks);
    ```

3. Call [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926).

4. Next you'll create the NETADAPTER object.  This object represents your NIC, which is the endpoint for all networking I/O.  To create it, initialize a config block and then call NetAdapterCreate.  For example:

    ```ManagedCPlusPlus
    WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE(&attribs, MYDRIVER_ADAPTER_CONTEXT);

    NET_ADAPTER_CONFIG_INIT (
        &config,
        EvtAdapterSetCapabilities,
        EvtAdapterCreateTxQueue,
        EvtAdapterCreateRxQueue);

    status = NetAdapterCreate(device, &attribs, &config, &adapter);
    ```

Typically, you'll have one NETADAPTER per WDFDEVICE, with the WDFDEVICE being the parent object of the NETADAPTER.

As with any WDF object, you can (and probably likely will want to) set your own context block onto the object (in the example above, that's the MYDRIVER_ADAPTER_CONTEXT).   Since WDF allows you to set a context on any WDF object, you can actually set contexts on the WDFDEVICE and/or the NETADAPTER.

We recommend that you put device-related data in your WDFDEVICE's context, and networking-related data into your NETADAPTER context.  However, this is not a requirement, and you can organize your contexts however you like.  If you are porting an existing NDIS 6.x driver, you'll likely have a single MiniportAdapterContext that combines networking- and device-related data into a single data structure.  To simplify the porting process, you can just convert that entire structure to the WDFDEVICE context, and make the NETADAPTER's context be a small structure that just points to the WDFDEVICE's context.

You'll provide 3 callbacks to NET_ADAPTER_CONFIG_INIT.  [EVT_NET_ADAPTER_CREATE_TXQUEUE](evt-net-adapter-create-txqueue.md) and [EVT_NET_ADAPTER_CREATE_RXQUEUE](evt-net-adapter-create-rxqueue.md) are specific to the new data path programming model.

The [EVT_NET_ADAPTER_SET_CAPABILITIES](evt-net-adapter-set-capabilities.md) is where you call the APIs equivalent to [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672), but instead of having one API taking a generic [**NDIS_MINIPORT_ADAPTER_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565920) structure there are different APIs to set different types of capabilities.  For example, your [EVT_NET_ADAPTER_SET_CAPABILITIES](evt-net-adapter-set-capabilities.md) might call:

* [**NetAdapterSetCurrentLinkState**](netadaptersetcurrentlinkstate.md)
* [**NetAdapterSetDataPathCapabilities**](netadaptersetdatapathcapabilities.md)
* [**NetAdapterSetLinkLayerCapabilities**](netadaptersetlinklayercapabilities.md)
* [**NetAdapterSetPowerCapabilities**](netadaptersetpowercapabilities.md)

If you want to set an attribute that does not have a equivalent NetAdapter API you can call [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) from this callback.

## Initializing the OID path

Next, while we're still in [*EVT_WDF_DRIVER_DEVICE_ADD*](https://msdn.microsoft.com/library/windows/hardware/ff541693), we're going to set up the OID path.  The OID path is modelled like a WDF queue.  Except instead of WDFREQUESTs, you'll be getting OIDs.

You have two choices in how to port this.  You can get a low level hook that will just give you the OID requests in a very similar way to how NDIS gives requests to a miniport driver.  This is the easiest port, since you'll mostly just need to adjust a function signature from your old MiniportOidRequest handler.

The other choice is to break apart your OID handler's switch statement, so each OID is its own function.  This makes for cleaner code, but requires more work.

You can use both approaches in the same driver – some OIDs can have a custom function per OID, while the rest get dumped into a catch-all function with a big switch statement.  So you can incrementally move out individual OIDs if they become too unwieldy to lump into a single function.

Here's how to register default handlers for all query OIDs and all set OIDs:

```ManagedCPlusPlus
NET_REQUEST_QUEUE_CONFIG config;
NET_REQUEST_QUEUE_CONFIG_INIT_DEFAULT_SEQUENTIAL(&config, NetAdapter);
config.EvtRequestDefaultQueryData = MyQueryHandler;
config.EvtRequestDefaultSetData = MySetHandler;
```

You can then optionally add a special-purpose handler for any particular OID.  For example:

```ManagedCPlusPlus
NET_REQUEST_QUEUE_CONFIG_ADD_QUERY_DATA_HANDLER(
    &config, OID_GEN_VENDOR_DESCRIPTION,
    EvtQueryGenVendorDescription, sizeof(NIC_VENDOR_DESC));
```

Once you've set up the OID queue the way you like, you create it with NetRequestQueueCreate.  Example:

```ManagedCPlusPlus
status = NetRequestQueueCreate(&config, WDF_NO_OBJECT_ATTRIBUTES, NULL);

if(!NT_SUCCESS(status))
{
    return status;
}
```

## Querying Network Advanced Keywords

Next we'll replace NdisOpenConfiguration[Ex] and related APIs with the NETCONFIGURATION APIs.  The APIs are similar, and you won't need to restructure your code.  For example:

```ManagedCPlusPlus
NETCONFIGURATION config = NULL;

status = NetAdapterOpenConfiguration(NetAdapter, WDF_NO_OBJECT_ATTRIBUTES, &config);
if (!NT_SUCCESS(status)) {
    return status;
}

status = NetConfigurationQueryUlong(config, 0, &SomeValue, &myvalue);

NetConfigurationClose(configuration);
```

There are configuration functions for querying ULONGs, Strings, Multi-Strings (similar to REG_MULTI_SZ), binary blobs, and MAC addresses.

## Creating Device Interfaces

Read this section if your NDIS driver calls [**NdisRegisterDeviceEx**](https://msdn.microsoft.com/library/windows/hardware/ff564518).  An NDIS driver typically does this to create a control device object (CDO) so that it can receive IOCTLs from user mode.

Here are two ways to do the same in your WDF networking client driver.

The first option is to create a control device object by calling [**WdfControlDeviceInitAllocate**](https://msdn.microsoft.com/library/windows/hardware/ff545841).  Alternatively, the driver can create a device interface by calling [**WdfDeviceCreateDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff545935) with a reference string, as shown here:

```ManagedCPlusPlus
DECLARE_CONST_UNICODE_STRING(c_RefString, L"MyRefString");
status = WdfDeviceCreateDeviceInterface(
            device, 
            &GUID_MY_DEVICE_INTERFACE, 
            &c_RefString);
if (!NT_SUCCESS(status)) {
    return status;
}
```

Any component that sends requests to a handle opened on this device interface results in I/O requests being delivered to your device driver.  You can use [WDF queue objects](../wdf/framework-queue-objects.md) to handle the incoming I/O requests.

## Finishing Up [*EVT_WDF_DRIVER_DEVICE_ADD*](https://msdn.microsoft.com/library/windows/hardware/ff541693)

At this point, you can do anything else you'd like to initialize your device, like allocate interrupts.

## Power Management

Power state changes are no longer delivered by OID_PNP_SET_POWER.  You'll never receive that OID; instead the power state changes operate in <a href="https://msdn.microsoft.com/windows/hardware/drivers/wdf/supporting-pnp-and-power-management-in-function-drivers">the same way that any other WDF driver would see them</a>.  So the code you have in your OID_PNP_SET_POWER handler will likely be moved to your [EVT_WDF_DEVICE_D0_EXIT](https://msdn.microsoft.com/library/windows/hardware/ff540855) and [EVT_WDF_DEVICE_D0_ENTRY](https://msdn.microsoft.com/library/windows/hardware/ff540848) handlers.

You may find that you need to tweak the code a bit, since the state machines are slightly different.
In particular, NDIS assumes a device initializes in D0.
However, WDF assumes that a device initializes into D3, and provides an explicit [**EVT_WDF_DEVICE_D0_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/ff540848) callback function as part of device initialization. 

Likewise, a WDF network adapter driver will not receive OID_PM_PARAMETERS.  Instead, the driver can query the necessary WoL configuration from the NETPOWERSETTINGS object.  Access to this object is available only when you need to arm/disarm your hardware for wake, which in WDF is the [EVT_WDF_DEVICE_ARM_WAKE_FROM_S0](https://msdn.microsoft.com/library/windows/hardware/ff540843) and related callback functions.  For example:

```ManagedCPlusPlus
NTSTATUS
EvtDeviceArmWakeFromS0(WDFDEVICE Device)
{
    NETPOWERSETTINGS powerSettings = NetAdapterGetPowerSettings(Adapter->NetAdapter);

    ULONG EnabledWakePatterns = NetPowerSettingsGetEnabledWakePatterns(powerSettings);
    ULONG EnabledProtocolOffloads = NetPowerSettingsGetEnabledProtocolOffloads(powerSettings);
    ULONG WakeUpFlags = NetPowerSettingsGetEnabledWakeUpFlags(powerSettings);

    // ...
}
```

The actual flags you get back have the same semantics as they do for an NDIS 6 miniport, so you don't need to make deep changes to the logic.  The main difference is that you can now query these flags at a more convenient time during the power-down sequence.

Once you've moved this code around, you can delete your OID handlers for OID_PNP_SET_POWER and OID_PM_PARAMETERS.

Your driver is the <a href="https://msdn.microsoft.com/windows/hardware/drivers/wdf/power-policy-ownership">power policy owner</a> for the NIC's device stack.  This allows you to freely use most of WDF's power management features.  For example, you can use **IdleCanWakeFromS0** to add your own idle logic. For info, see [Supporting System Wake-Up](../wdf/supporting-system-wake-up.md).

Note that when you associate a NetAdapter with your device, the NetAdapter framework keeps your device at D0 when the OS is using your network interface.  Therefore, in most cases, it's not necessary for you to implement your own power logic, as the default behavior that comes with NetAdapter is sufficient.

## Data Path

The data path programming model has changed significantly and requires a more in-depth explanation. This section explains the bare minimum to enable you to install and remove your device.

First, new data structures have being created to work with the new model, here is a list of some of them:

|New data path structures|Description|
|-|-|
|[**NET_PACKET**](net-packet.md)|Similar to a NET_BUFFER|
|[**NET_PACKET_FRAGMENT**](net-packet-fragment.md)|Similar to a memory descriptor list (MDL). Each NET_PACKET has one or more of these.|
|[**NET_RING_BUFFER**](net-ring-buffer.md)|Ring buffer shared between the OS and a client, holds NET_PACKETs|

In the NetAdapterCx model, network traffic is no longer per adapter, as in NDIS, but rather per queue.  Specifically, WDF objects represent network packet queues. When your client driver calls [**NET_ADAPTER_CONFIG_INIT**](net-adapter-config-init.md), it provides two queue creation callbacks [EVT_NET_ADAPTER_CREATE_TXQUEUE](evt-net-adapter-create-txqueue.md) and [EVT_NET_ADAPTER_CREATE_RXQUEUE](evt-net-adapter-create-rxqueue.md). NetAdapterCx calls these callbacks when it's time for the client to create a transmit or receive queue.

In NDIS 6.x, miniports have start and pause semantics; in WDF, queues are only created and deleted.

The client creates a transmit queue as follows:

```ManagedCPlusPlus
NTSTATUS
EvtAdapterCreateTxQueue(NETADAPTER Adapter, PNETTXQUEUE_INIT NetTxQueueInit)
{
    NETTXQUEUE txQueue;

    NET_TXQUEUE_CONFIG txQueueConfig;
    NET_TXQUEUE_CONFIG_INIT(&txQueueConfig, 
                            EvtTxQueueAdvance,
                            EvtTxQueueSetNotificationEnabled,
                            EvtTxQueueCancel);
    NTSTATUS status = NetTxQueueCreate(
        NetTxQueueInit,
        WDF_NO_OBJECT_ATTRIBUTES,
        &txQueueConfig,
        &txQueue);

    return status;
}
```
To create an receive queue from [EVT_NET_ADAPTER_CREATE_RXQUEUE](evt-net-adapter-create-rxqueue.md), use the same pattern.

As shown in the above example, when creating transmit/receive queues you need to provide a set of callbacks:

### [*EVT_TXQUEUE_ADVANCE*](evt-txqueue-advance.md)

This callback is similar to [**MINIPORT_SEND_NET_BUFFER_LISTS**](https://msdn.microsoft.com/library/windows/hardware/ff559440) in NDIS 6.x.
NetAdapterCx calls this callback when new packets need to be sent.
However, in the NetAdapterCx model, the client must complete packets from within the *Advance* event callback, typically by calling by calling [**NetRingBufferReturnCompletedPackets method**](netringbufferreturncompletedpackets.md).  In a production driver, the client would retrieve packets from the queue (by calling ring buffer macros), send the data, and then complete the packets. The following example simply completes incoming transmit packets:

```ManagedCPlusPlus
VOID
EvtTxQueueAdvance(NETTXQUEUE TxQueue)
{
    NET_RING_BUFFER *ringBuffer = NetTxQueueGetRingBuffer(TxQueue);
    NET_PACKET *netPacket;

    while ((netPacket = NetRingBufferGetNextPacket(ringBuffer)) != nullptr)
    {
        netPacket->Data.Completed = TRUE;

        NetRingBufferAdvanceNextPacket(ringBuffer);
    }

    NetRingBufferReturnCompletedPackets(ringBuffer);
}
```

### EVT_TXQUEUE_SET_NOTIFICATION_ENABLED

If there is no activity in [*EVT_TXQUEUE_ADVANCE*](evt-txqueue-advance.md), NetAdapterCx might stop calling your advance callback. When this happens it will call [**EVT_TXQUEUE_SET_NOTIFICATION_ENABLED**](evt-txqueue-set-notification-enabled.md) with TRUE to notify the client that it shoudl call [**NetTxQueueNotifyMoreCompletedPacketsAvailable**](nettxqueuenotifymorecompletedpacketsavailable.md) when it is ready to make forward progress. In the code above, it's not necessary to handle this case because we always complete the incoming packets.
You might eventually use this callback to enable or disable your interrupt handler.

### EVT_TXQUEUE_CANCEL

The [**EVT_TXQUEUE_CANCEL**](evt-txqueue-cancel.md) callback function is a hint that the client driver should complete the buffers as soon as possible, regardless of whether pending Tx packets have been successfully transmitted.
You can safely ignore this handler for now.

### EVT_RXQUEUE_ADVANCE

In the new programming model there are no NET_BUFFER_LIST or NET_BUFFER pools. To get a descriptor to use to receive packets, you need to retrieve one in your [**EVT_RXQUEUE_ADVANCE**](evt-rxqueue-advance.md) callback function. You'll use this callback to indicate that a receive operation is complete. For example, use the following to retrieve all available receive buffers:

```ManagedCPlusPlus
VOID
EvtRxQueueAdvance(NETRXQUEUE RxQueue)
{
    NET_RING_BUFFER *ringBuffer = NetRxQueueGetRingBuffer(RxQueue);
    NET_PACKET *netPacket;

    while ((pNetPacket = NetRingBufferGetNextPacket(pRingBuffer)) != NULL)
    {
        NetRingBufferAdvanceNextPacket(ringBuffer);
    }
}
```

### EVT_RXQUEUE_SET_NOTIFICATION_ENABLED

The purpose of this callback is the same of [*EVT_TXQUEUE_SET_NOTIFICATION_ENABLED*](evt-txqueue-set-notification-enabled.md).

### EVT_RXQUEUE_CANCEL

This is similar to [*EVT_TXQUEUE_CANCEL*](evt-txqueue-cancel.md), a hint from the OS that the client driver should return all the buffers as soon as possible. 
In this example we're didn't give the buffers to any hardware, so it's safe to immediately return all the buffers to the OS in the cancellation handler.
The fastest way to do that is to adjust the [*NET_RING_BUFFER*](net-ring-buffer.md) pointers like this:

```ManagedCPlusPlus
VOID
EvtRxQueueCancel(NETRXQUEUE RxQueue)
{
    NET_RING_BUFFER *ringBuffer = NetRxQueueGetRingBuffer(RxQueue);

    ringBuffer->BeginIndex = ringBuffer->NextIndex = ringBuffer->EndIndex;
}
```

### Conclusion

As mentioned, this is the minimum to get your device starting and stopping. To receive and transmit data, you need to understand how the ring buffer works, which is out of scope for this porting guide.

## Stopping the Device

Device removal for a WDF NIC driver is the same as in any other WDF device driver, with no networking specific processing required.  The network datapath shuts down first, followed by the WDF device.  For more info, see [A User Unplugs a Device](../wdf/a-user-unplugs-a-device.md).

Your MiniportHaltEx handler can be distributed among the various WDF events for teardown: most typically [EVT_WDF_DEVICE_D0_EXIT](https://msdn.microsoft.com/library/windows/hardware/ff540855) and [*EVT_WDF_DEVICE_RELEASE_HARDWARE*](https://msdn.microsoft.com/library/windows/hardware/ff540890).

There's no need to manually delete the NetAdapter or any of the OID and datapath queues you created earlier, as these are cleaned up automatically by WDF.

Generally, a NIC driver does not need to handle MiniportShutdownEx, and in most cases you won't need any WDF equivalent.  You can just delete MiniportShutdownEx if it exists.

MiniportResetEx and MiniportCheckForHangEx are no longer supported, and you should just delete that code.
If these callbacks were doing something critical, like link detection, you can replicate their functionality with a periodic timer.
However, we generally discourage drivers from polling periodically, as this prevents the CPU from entering its most efficient power-saving states.

## General Purpose Functions

Most NdisXxx functions can be replaced with a WDF equivalent.  This table lists a few examples:

Generally, you should find that you need very few APIs that are imported from NDIS.SYS.

|NDIS API Family|WDF Equivalent|
|-|-|
|NdisAllocateIoWorkItem|[**WdfWorkItemCreate**](https://msdn.microsoft.com/library/windows/hardware/ff551201)|
|NdisAllocateTimerObject|[**WdfTimerCreate**](https://msdn.microsoft.com/library/windows/hardware/ff550050)|
|NdisAcquireSpinLock|[**WdfSpinLockAcquire**](https://msdn.microsoft.com/library/windows/hardware/ff550040)|
|NdisInterlockedIncrement|InterlockedIncrement (compiler intrinsic)|
|NdisInitialzeEvent|[**KeInitializeEvent**](https://msdn.microsoft.com/library/windows/hardware/ff552137)|
|NdisMInitializeScatterGatherDma|[**WdfDmaEnablerCreate**](https://msdn.microsoft.com/library/windows/hardware/ff546983)|
|NdisInitializeString|[**WdfStringCreate**](https://msdn.microsoft.com/library/windows/hardware/ff550046)|
|NdisSystemActiveProcessorCount|[**KeGetCurrentProcessorNumberEx**](https://msdn.microsoft.com/library/windows/hardware/ff552076) (kernel)|
|NdisWriteRegisterUchar|[**WDF_WRITE_REGISTER_UCHAR**](https://msdn.microsoft.com/library/windows/hardware/dn265684)|

In some cases, you may be forced to call an NDIS API, because there is no equivalent in WDF, or because it would be difficult to refactor the code at this moment.  In that case, you can use NetAdapterWdmGetNdisHandle to get back an NDIS_HANDLE that works in many NDIS APIs as if it were a handle for an NDIS 6 miniport adapter.  Example:

```Management
NdisGetRssProcessorInformation(NetAdapterWdmGetNdisHandle(NetAdapter), . . .);
```

Debugging
---------

Since your driver is now a full-featured WDF driver, you can use all the usual !wdfkd commands, as you can for any other driver.  In addition, the latest version of !ndiskd.netadapter can see the networking aspect of your driver, and show similar results to what [**!ndiskd.miniport**](https://msdn.microsoft.com/library/windows/hardware/ff564142) showed for your NDIS 6 driver.
!ndiskd.netadapter accepts a WDF-style NETADAPTER handle.
