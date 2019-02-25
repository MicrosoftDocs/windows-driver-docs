---
title: Porting NDIS miniport drivers to NetAdapterCx
description: Porting NDIS miniport drivers to NetAdapterCx
ms.assetid: F5C798C6-B746-43CB-BF63-DBA7DD0975ED
keywords:
- Porting miniport drivers to the Network Adapter Class Extension, porting to the Network Adapter WDF Class Extension, porting NDIS 6.x to NetAdapterCx
ms.date: 06/05/2017
ms.localizationpriority: medium
---

# Porting NDIS miniport drivers to NetAdapterCx

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

This page describes how to convert an NDIS 6.x miniport driver into a NetAdapterCx client driver.

For general information about WDF, please review the [WDF Driver Development Guide](../wdf/index.md).

## Compilation settings

Open your existing NDIS miniport driver project in Visual Studio and use the following steps to convert it to a KMDF project.

1. First, navigate to **Configuration Properties->Driver Settings->Driver Model** and verify that **Type of driver** is set to KMDF, and that **KMDF Version Major** and **KMDF Version Minor** are both empty.
2. In project properties, open **Driver Settings->Network Adapter Driver** and set **Link to the Network Adapter Class Extension** to **Yes**.
   * If your converted driver will still call NDIS APIs, continue to link against `ndis.lib`.
3. Remove NDIS preprocessor macros, like `NDIS650_MINIPORT=1`.
4. Add the following headers to every source file (or to your common/precompiled header):
  
   ```C++
   #include <ntddk.h>
   #include <wdf.h>
   #include <netadaptercx.h>
   ```
  
5. Add [standard WDF decorations](../wdf/specifying-wdf-directives-in-inf-files.md) to your INF:
  
   ```INF
   [Yourdriver.Wdf]
   KmdfService = Yourdriverservice, Yourdriver.wdfsect

   [Yourdriver.wdfsect]
   KmdfLibraryVersion = <insert here>
   ```
6. Add new required networking keywords to the NT section of your INF:

   - **\*IfConnectorPresent**
   - **\*ConnectionType**
   - **\*DirectionType**
   - **\*AccessType**
   - **\*HardwareLoopback**

     For more information about these keywords and an example, see [INF files for NetAdapterCx client drivers](inf-files-for-netadaptercx-client-drivers.md).

## Driver initialization

Remove the call to [**NdisMRegisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563654) from [*DriverEntry*](https://msdn.microsoft.com/library/windows/hardware/ff540807), and add the following:

```C++
WDF_DRIVER_CONFIG_INIT(&config, EvtDriverDeviceAdd);
status = WdfDriverCreate(. . . );
if (!NT_SUCCESS(status)) {
  return status;
}
```

If it is set, remove the **WdfDriverInitNoDispatchOverride** flag from the call to [**WdfDriverCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547175).

*DriverUnload* is an optional routine for a WDF networking client driver, so you can remove it if you like. Do not call [**NdisMDeregisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563578) from *DriverUnload*.

## Device initialization

Next, you'll distribute code from *MiniportInitializeEx* into the appropriate WDF event callback handlers, several of which are optional. For details on the callback sequence, see [Power-Up Sequence for an Network Adapter WDF Client Driver](power-up-sequence-for-a-netadaptercx-client-driver.md).

You'll call the methods equivalent to [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) when you're starting your net adapter, but before you call [**NetAdapterStart**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-netadapterstart). However, instead of calling one routine with a generic [**NDIS_MINIPORT_ADAPTER_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565920) structure, the client driver calls different functions to set different types of capabilities.

For info on the callbacks you'll need to provide and when to start a net adapter, see [Device and adapter initialization](device-and-adapter-initialization.md).

## Creating queues to manage control requests

Next, still in [*EVT_WDF_DRIVER_DEVICE_ADD*](https://msdn.microsoft.com/library/windows/hardware/ff541693), set up the object identifier (OID) path. The OID path is modeled like a WDF queue, but you'll be getting OIDs instead of WDFREQUESTs.

There are two high level approaches you might take when porting this. The first option is to register a [*EVT_NET_REQUEST_DEFAULT*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netrequestqueue/nc-netrequestqueue-evt_net_request_default) handler that receives OID requests in a very similar way to how a miniport driver receives requests from NDIS. This is the easiest port, since you'll likely just need to adjust a function signature from your old MINIPORT_OID_REQUEST handler.

The other option is to break apart your OID handler's switch statement and provide a separate handler for each individual OID. You might choose this option if your device requires OID-specific functionality.

If you used the [**Direct OID Request Interface in NDIS 6.1**](../network/direct-oid-request-interface-in-ndis-6-1.md), replace it with a parallel WDF queue. Similarly, the regular (serial) request interface in NDIS should become a sequential WDF queue.

For info on registering handlers for OIDs, see [Handling control requests](handling-control-requests.md).

## Reading configuration from the registry

Next, replace calls to [**NdisOpenConfigurationEx**](https://msdn.microsoft.com/library/windows/hardware/ff563717) and related functions with the `NetConfiguration*` methods. The `NetConfiguration*` methods are similar to the `Ndis*Configuration*` functions, and you won't need to restructure your code.

For more info, see [Accessing configuration information](accessing-configuration-information.md).

## Receiving I/O control codes (IOTCLs) from user mode

Read this section if your NDIS driver calls [**NdisRegisterDeviceEx**](https://msdn.microsoft.com/library/windows/hardware/ff564518), a routine used to create a control device object (CDO) to receive IOCTLs from user mode.

Here are two ways to do this in your WDF networking client driver.

The most straightforward port is to create a control device object by calling [**WdfControlDeviceInitAllocate**](https://msdn.microsoft.com/library/windows/hardware/ff545841) from the client's [*EVT_WDF_DRIVER_DEVICE_ADD*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback. For more info, see [Using Control Device Objects](../wdf/using-control-device-objects.md).

However, the recommended solution is to create a device interface, as described in [Using Device Interfaces](using-device-interfaces.md).

## Finishing device initialization

At this point in [*EVT_WDF_DRIVER_DEVICE_ADD*](https://msdn.microsoft.com/library/windows/hardware/ff541693), you can do anything else you'd like to initialize your device, like allocating interrupts.

## Handling power state change notifications

A WDF client driver does not receive [**OID_PNP_SET_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff569780) for power state changes.

Instead, a WDF client registers optional callback functions to receive power state change notifications. For an overview, see [Supporting PnP and Power Management in Function Drivers](../wdf/supporting-pnp-and-power-management-in-function-drivers.md).

Typically, the code in your [**OID_PNP_SET_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff569780) handler moves to [*EVT_WDF_DEVICE_D0_EXIT*](https://msdn.microsoft.com/library/windows/hardware/ff540855) and [*EVT_WDF_DEVICE_D0_ENTRY*](https://msdn.microsoft.com/library/windows/hardware/ff540848).

Because the WDF power state machine is slightly different, you might need to make minor modifications to the code.

Specifically, in its [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) callback function, an NDIS miniport driver performs one-time initialization tasks as well as work to bring the device to the D0 state. Then, it repeats the work to go to D0 in its [*OID_PNP_SET_POWER*](https://msdn.microsoft.com/library/windows/hardware/ff569780) handler.

In contrast, a WDF client performs one-time initialization tasks in event callbacks before [**EVT_WDF_DEVICE_D0_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/ff540848), during which the device is in a low-power state. Then it does the work to go to D0 in [**EVT_WDF_DEVICE_D0_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/ff540848).

To summarize, in WDF, you put your "go to D0" code in one place, instead of two.

For details on the callback sequence, see [Power-Up sequence for a NetAdapterCx client driver](power-up-sequence-for-a-netadaptercx-client-driver.md).

## Querying and setting power management capabilities

Similarly, a WDF client driver does not receive [**OID_PM_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff569768) to query or set power management hardware capabilities of the network adapter.

Instead, the driver queries the necessary wake-on-LAN (WoL) configuration from the NETPOWERSETTINGS object. For more info, see [Configuring power management](configuring-power-management.md).

The actual flags you get back have the same semantics as they do for an NDIS 6 miniport, so you don't need to make deep changes to the logic. The main difference is that you can now query these flags during the power-down sequence. See [Power-down sequence for a NetAdapterCx client driver](power-down-sequence-for-a-netadaptercx-client-driver.md).

Once you've moved this code around, you can delete your OID handlers for [*OID_PNP_SET_POWER*](https://msdn.microsoft.com/library/windows/hardware/ff569780) and [*OID_PM_PARAMETERS*](https://msdn.microsoft.com/library/windows/hardware/ff569768).

Because the NetAdapter framework keeps your device at D0 while the host uses the network interface, the client typically does not implement power logic; the default NetAdapter power behavior is sufficient.

## Data path

The data path programming model has changed significantly. Here are some key differences:

* In the NetAdapter model, network traffic is no longer per adapter, as in NDIS, but rather per WDF queue. See [Creating I/O Queues](../wdf/creating-i-o-queues.md).
* Instead of NET_BUFFER_LIST and NET_BUFFER pools, NetAdapterCx introduces a ring buffer that is comprised of net packets, which map to NDIS as follows:
  * A [**NET_PACKET**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacket/ns-netpacket-_net_packet) is similar to a NET_BUFFER_LIST + NET_BUFFER.
  * A [**NET_PACKET_FRAGMENT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacket/ns-netpacket-_net_packet_fragment) is similar to a memory descriptor list (MDL). Each [**NET_PACKET**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacket/ns-netpacket-_net_packet) has one or more of these.
  * For details on the replacement structures and how to use them, see [Packet descriptors and extensions](packet-descriptors-and-extensions.md).
* In NDIS 6.x, the miniport needs to handle start and pause semantics. In the NetAdapterCx model, this is no longer the case.
* The [*EVT_RXQUEUE_ADVANCE*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netrxqueue/nc-netrxqueue-evt_rxqueue_advance) callback is similar to [**MINIPORT_RETURN_NET_BUFFER_LISTS**](https://msdn.microsoft.com/library/windows/hardware/ff559437) in NDIS 6.x.
* The [*EVT_TXQUEUE_ADVANCE*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/nettxqueue/nc-nettxqueue-evt_txqueue_advance) callback is similar to [**MINIPORT_SEND_NET_BUFFER_LISTS**](https://msdn.microsoft.com/library/windows/hardware/ff559440) in NDIS 6.x.

## Device removal

Device removal for a WDF NIC driver is the same as in any other WDF device driver, with no networking specific processing required. The network data path shuts down first, followed by the WDF device. For info about WDF shutdown, see [A User Unplugs a Device](../wdf/a-user-unplugs-a-device.md).

Your *MiniportHaltEx* handler will likely be distributed between [*EVT_WDF_DEVICE_D0_EXIT*](https://msdn.microsoft.com/library/windows/hardware/ff540855) and [*EVT_WDF_DEVICE_RELEASE_HARDWARE*](https://msdn.microsoft.com/library/windows/hardware/ff540890).

The WDF client does not need to delete the NetAdapter or any of the OID and datapath queues that it created. WDF deletes these objects automatically.

You can delete *MiniportShutdownEx*, *MiniportResetEx* and *MiniportCheckForHangEx*. These callbacks are no longer supported.

## NDIS-WDF function equivalents

Most `NdisXxx` functions can be replaced with a WDF equivalent. In general, you should find that you need very little functionality that is imported from `NDIS.SYS`.

For a list of function equivalents, see [NDIS-WDF function equivalents](ndis-wdf-function-equivalents.md).

For functions with no WDF equivalent, the client can call [**NetAdapterWdmGetNdisHandle**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-netadapterwdmgetndishandle) to retrieve an NDIS_HANDLE for use with NDIS functions. For example:

```C++
NdisGetRssProcessorInformation(NetAdapterWdmGetNdisHandle(NetAdapter), . . .);
```

## Debugging

See [Debugging a NetAdapterCx client driver](debugging-a-netadaptercx-client-driver.md).

The [!ndiskd.netadapter](../debugger/-ndiskd-netadapter.md) debugger extension shows similar results to what **!ndiskd.miniport** shows for an NDIS 6 driver.

## Conclusion

Using the steps in this topic, you should have a working driver that starts and stops your device.
