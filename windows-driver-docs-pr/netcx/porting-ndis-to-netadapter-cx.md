# Porting NDIS Miniport Drivers to NetAdapter Class Extension

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

You are reading a practical guide on how to convert a pre-existing NDIS 6.x miniport driver to use WDF with networking.  Before beginning this conversion, it will be helpful to understand some of the <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/wdf/index">basic architecture & conventions</a> of WDF.

## Compilation Settings

Ensure your project links against the latest version of KMDF.  Also link against NetAdapterCxStub.lib (located in “Windows Kits\10\Lib\<latest_windows_version>\km\<architecture>\netadaptercx\1.0”).

It is no longer strictly necessary to link against ndis.lib, although you may still want to use some NDIS APIs, so you may still link against it.

It is no longer necessary to set NDIS preprocessor macros, like NDIS650_MINIPORT=1

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

Remove the call to NdisMRegisterMiniportDriver from DriverEntry.

Put <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/ff540807(v=vs.85).aspx">the standard WDF driver initialization</a> in DriverEntry.  Do not specify the WdfDriverInitNoDispatchOverride flag – remove it if you were already using WDF in miniport mode in your NDIS 6.x driver.  Example:

```ManagedCPlusPlus
WDF_DRIVER_CONFIG_INIT(&config, EvtDriverDeviceAdd);
status = WdfDriverCreate(. . . );
if (!NT_SUCCESS(status)) {
    return status;
}
```

Remove NdisMDeregisterMiniportDriver from DriverUnload.  DriverUnload is not required by networking, but you can certainly add it if you want it.  Otherwise, you can delete any Unload handler you had.

## Device Initialization

Next, we need to break MiniportInitializeEx into several pieces, each of which is a standard WDF event.  <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/wdf/power-up-sequence-for-a-function-or-filter-driver">The full sequence of events</a> includes many events, most of which are optional.  You should move code into the most logical place, based on the WDF semantics of each state.

In general, the most interesting events are:

- <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/ff541693(v=vs.85).aspx">EvtDriverDeviceAdd</a>
- <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/ff540880(v=vs.85).aspx">EvtDevicePrepareHardware</a>
- <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/ff540848(v=vs.85).aspx">EvtDeviceD0Entry</a>

While you may need to handle several events to properly manage your device, the OS’s networking stack only requires specific action in EvtDriverDeviceAdd.

## Creating the NETADAPTER Object

In EvtDriverDeviceAdd, call NetAdapterDeviceInitConfig to let NetAdapterCx take over some necessary configuration, for a list of what this call do, see this <TODO: add link to API page> link.  Then set up a call to WdfDeviceInitSetPnpPowerEventCallbacks as normal. Example:

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

Next you can call <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/ff545926(v=vs.85).aspx">WdfDeviceCreate</a>, as in any other WDF device driver.

Next you’ll create the NETADAPTER object.  This object represents your NIC, it’s the endpoint for all networking I/O.  To create it, initialize a config block, then call NetAdapterCreate.  Example:

```ManagedCPlusPlus
WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE(&attribs, MYDRIVER_ADAPTER_CONTEXT);

NET_ADAPTER_CONFIG_INIT (
    &config,
    EvtAdapterSetCapabilities,
    EvtAdapterCreateTxQueue,
    EvtAdapterCreateRxQueue);

status = NetAdapterCreate(device, &attribs, &config, &adapter);
```

Typically, you’ll have a 1-1 relationship between instances of a WDFDEVICE and of a NETADAPTER, with the WDFDEVICE being the parent object of the NETADAPTER.

As with any WDF object, you can (and probably likely will want to) set your own context block onto the object (in the example above, that’s the MYDRIVER_ADAPTER_CONTEXT).   Since WDF allows you to set a context on any WDF object, you can actually set contexts on the WDFDEVICE and/or the NETADAPTER.  We recommend that you put device-related data in your WDFDEVICE’s context, and networking-related data into your NETADAPTER context.  However, this is not a requirement, and you can organize your contexts however you like.  If you are porting an existing NDIS 6.x driver, you’ll likely have a single MiniportAdapterContext that combines networking- and device-related data into a single data structure.  To simplify the porting process, you can just convert that entire structure to the WDFDEVICE context, and make the NETADAPTER’s context be a small structure that just points to the WDFDEVICE’s context.

You’ll provide 3 callbacks to NET_ADAPTER_CONFIG_INIT.  EvtAdapterCreateTxQueue and EvtAdapterCreateRxQueue are specific to the new data path programming model.

The EvtAdapterSetCapabilities is where you call the APIs equivalent to NdisMSetMiniportAttributes, but instead of having one API taking a generic NDIS_MINIPORT_ADAPTER_ATTRIBUTES  structure there are different APIs to set different types of capabilities. <TODO: link to EvtAdapterSetCapabilities>. If you want to set an attribute that does not have a equivalent NetAdapter* API you can call NdisMSetMiniportAttributes from this callback.

## Initializing the OID path

Next, while we’re still in EvtDriverDeviceAdd, we’re going to set up the OID path.  The OID path is modelled like a WDF queue.  Except instead of WDFREQUESTs, you’ll be getting OIDs.

You have two choices in how to port this.  You can get a low level hook that will just give you the OID requests in a very similar way to how NDIS gives requests to a miniport driver.  This is the easiest port, since you’ll mostly just need to adjust a function signature from your old MiniportOidRequest handler.

The other choice is to break apart your OID handler’s switch statement, so each OID is its own function.  This makes for cleaner code.  However, it will be more churn.

You can use both approaches in the same driver – some OIDs can have a custom function per OID, while the rest get dumped into a catch-all function with a giant switch statement.  So you can incrementally move out individual OIDs if they become too unwieldy to lump into a single function.

To get a single handler for all OIDs:

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

Once you’ve set up the OID queue the way you like, you create it with NetRequestQueueCreate.  Example:

```ManagedCPlusPlus
status = NetRequestQueueCreate(&config, WDF_NO_OBJECT_ATTRIBUTES, NULL);

if(!NT_SUCCESS(status))
{
    return status;
}
```

## Querying Network Advanced Keywords

Next we’ll replace NdisOpenConfiguration[Ex] and related APIs.  Instead, use the NETCONFIGURATION APIs.  The APIs are similar, and you won’t need to restructure your code.  Example:

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

In NDIS, to get IOCTLs from user mode you would create a Control Device Object with a call to NdisRegisterDeviceEx. In WDF you can still create a Control Device (see <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/ff545841(v=vs.85).aspx">WdfControlDeviceInitAllocate</a>), but you can also create a device interface with a call to WdfDeviceCreateDeviceInterface, but with a caveat, you need to call this API with a ref string:

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

Any handle opened on this device interface will direct IO to your device driver, meaning you can use WDF objects to handle it, like WDFQUEUE <link to WDFQUEUE>.

## Finishing Up EvtDriverDeviceAdd

At this point, you can do anything else you’d like to initialize your device.  E.g., you can create an endpoint for ioctls to usermode, etc.

## Power Management

Power state changes are no longer delivered by OID_PNP_SET_POWER.  You’ll never receive that OID; instead the power state changes operate in <a href="https://msdn.microsoft.com/windows/hardware/drivers/wdf/supporting-pnp-and-power-management-in-function-drivers">the same way that any other WDF driver would see them</a>.  So the code you have in your OID_PNP_SET_POWER handler will likely be moved to your EvtDeviceD0Exit and EvtDeviceD0Entry handlers.

Likewise, a WDF network adapter driver will not receive OID_PM_PARAMETERS.  Instead, the driver can query the necessary WoL configuration from the NETPOWERSETTINGS object.  Access to this object is available only when you need to arm/disarm your hardware for wake, which in WDF is the EvtDeviceArm/DisarmWakeFromS0/SX event.  Example:

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

The actual flags you get back have the same semantics as they do for an NDIS 6 miniport, so you don’t need to make deep changes to the logic.  The main difference is that you can now query these flags at a more convenient time during the power-down sequence.

Once you’ve moved this code around, you can delete your OID handlers for OID_PNP_SET_POWER and OID_PM_PARAMETERS.

Your driver is the <a href="https://msdn.microsoft.com/windows/hardware/drivers/wdf/power-policy-ownership">power policy owner</a> for the NIC’s device stack.  This allows you to freely use most of WDF’s power management features.  For example, you can use IdleCanWakeFromS0 to add your own idle logic.  However, when you associate a NetAdapter with your device, the NetAdapter framework will provide some hints to keep your device at D0 when the OS is using your network interface.  Therefore, in most cases, it’s not necessary for you to implement your own power logic, as the default behavior that comes with NetAdapter is sufficient.

## Data Path

The data path programming model had a lot of changes and will require more in depth explanation. This section will explain the bare minimum to get your device succeeding loading and tear down.

First, new data structures have being created to work with the new model, here is a list of some of them:

|New data path structures|Description|
|-|-|
|NET_PACKET|Similar to a NET_BUFFER|
|NET_PACKET_FRAGMENT|Similar to a MDL, each NET_PACKET has one or more of these|
|NET_RING_BUFFER|Ring buffer shared between the OS and a client, holds NET_PACKETs|

Network traffic is not per adapter, but rather per queue, as such new WDF objects represent such queues. Back when you called NET_ADAPTER_CONFIG_INIT you provided two queue creation callbacks (EvtAdapterCreateTxQueue and EvtAdapterCreateRxQueue). NetAdapterCx will call into those whenever it needs you driver to create a Tx or Rx queue. Queues don't have start/pause semantics like miniports had in NDIS 6.x, rather they are only created and destroyed. You can create a Tx queue as follow:

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
To create a Rx queue from EvtAdapterCreateRxQueue you can follow a similar pattern.

As shown in the above example, when creating Tx/Rx queues you need to provide a set of callbacks:

### EvtTxQueueAdvance

This callback can be seen as similar to SendNetBufferListsHandler in NDIS 6.x, the OS will call this every time new packets need to be sent, the big difference is that completions are required to be indicated from this event callback. The mechanics of how to retrieve packets to send from the queue and indicate completions requires understanding how the NET_RING_BUFFER works. The following example just completes any incoming Tx packets:

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

### EvtTxQueueSetNotificationEnabled

If there is no activity in EvtTxQueueAdvance the OS might stop calling your advance callback. When this happens it will call this event callback with TRUE to tell you should notify the OS whenever you're ready to make forward progress. In the code above it won't be necessary to handle this because we always complete the incoming packets.

### EvtTxQueueCancel

This event callback is called when the OS wants to destroy the queue. This is not a state changing event callback, it simply hints your queue that it will be destroyed soon, your advance callback might still be called after you receive this.

### EvtRxQueueAdvance

In the new programming model there are no NET_BUFFER_LIST or NET_BUFFER pools. To get a descriptor to use to receive packets you need to retreive one in your advance callback. Similar to the Tx case, to indicate that a receive is complete you are required to use this event callback, and both things work through the NET_RING_BUFFER. The following piece of code will just grab all the available Rx buffers and do nothing with them.

```ManagedCPlusPlus
VOID
EvtRxQueueAdvance(NETRXQUEUE RxQueue)
{
    NET_RING_BUFFER *ringBuffer = NetRxQueueGetRingBuffer(RxQueue);
    NET_PACKET *netPacket;

    while ((pNetPacket = NetRingBufferGetNextPacket(pRingBuffer)) != nullptr)
    {
        NetRingBufferAdvanceNextPacket(ringBuffer);
    }
}
```

### EvtRxQueueSetNotificationEnabled

The purpose of this callback is the same of EvtTxQueueSetNotificationEnabled.

### EvtRxQueueCancel

This is similar EvtTxQueueCancel, a hint from the OS indicating the queue will be destroyed shortly. In this example we're not doing any receives, so we're just going to return all the buffers to the OS by adjusting the NET_RING_BUFFER pointers:

```ManagedCPlusPlus
VOID
EvtRxQueueCancel(NETRXQUEUE RxQueue)
{
    NET_RING_BUFFER *ringBuffer = NetRxQueueGetRingBuffer(RxQueue);

    ringBuffer->BeginIndex = ringBuffer->NextIndex = ringBuffer->EndIndex;
}
```

### Conclusion

As mentioned, this is the minimum to get your device starting and stopping. To do something useful you need to understand how the ring buffer works.

## Stopping the Device

Tear-down in a WDF NIC driver is the same as <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/wdf/a-user-unplugs-a-device">in any other WDF device driver</a>.  There’s no special handling required for networking, per se.  The network datapath will be paused, then WDF will proceed to tear down the device.

Your MiniportHaltEx handler can be distributed among the various WDF events for teardown: most typically EvtDeviceD0Exit and EvtDeviceReleaseHardware.

There’s no need to manually delete the NetAdapter or any of the OID and datapath queues you created earlier, as these are cleaned up automatically by WDF.

Generally, a NIC driver does not need to handle MiniportShutdownEx, and in most cases you won’t need any WDF equivalent.  You can just delete MiniportShutdownEx if it exists.

MiniportResetEx and MiniportCheckForHangEx are no longer supported, and you should just delete that code.

## General Purpose Functions

Most NdisXxx functions can be replaced with a WDF equivalent.  This table lists a few examples:

Generally, you should find that you need very few APIs that are imported from NDIS.SYS.

|NDIS API Family|WDF Equivalent|
|-|-|
|NdisAllocateIoWorkItem|WdfWorkItemCreate|
|NdisAllocateTimerObject|WdfTimerCreate|
|NdisAcquireSpinLock|WdfSpinLockAcquire|
|NdisInterlockedIncrement|InterlockedIncrement (compiler intrinsic)|
|NdisInitialzeEvent|KeInitialzeEvent|
|NdisMInitializeScatterGatherDma|WdfDmaEnablerCreate|
|NdisInitializeString|WdfStringCreate|
|NdisSystemActiveProcessorCount|KeGetCurrentProcessorNumberEx (kernel)|
|NdisWriteRegisterUchar|WDF_WRITE_REGISTER_UCHAR|

In some cases, you may be forced to call an NDIS API, because there is no equivalent in WDF, or because it would be difficult to refactor the code at this moment.  In that case, you can use NetAdapterWdmGetNdisHandle to get back an NDIS_HANDLE that works in many NDIS APIs as if it were a handle for an NDIS 6 miniport adapter.  Example:

```Management
NdisGetRssProcessorInformation(NetAdapterWdmGetNdisHandle(NetAdapter), . . .);
```

Debugging
---------

Since your driver is now a full-featured WDF driver, you can use all the usual !wdfkd commands, as you can for any other driver.  In addition, the latest version of !ndiskd.netadapter can see the networking aspect of your driver, and show all the usual things that !ndiskd.miniport showed for your NDIS 6 driver.

