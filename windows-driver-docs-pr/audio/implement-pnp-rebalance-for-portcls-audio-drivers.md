---
title: Implement PnP Rebalance for PortCls Audio Drivers
description: PnP rebalancing is used in certain PCI scenarios where memory resources need to be reallocated.
ms.date: 04/09/2019
ms.localizationpriority: medium
---

# Implement PnP Rebalance for PortCls Audio Drivers


PnP rebalancing is used in certain PCI scenarios where memory resources need to be reallocated.

Rebalance can be triggered in two main scenarios:

1. PCI hotplug: A user plugs in a device and the PCI bus does not have enough resources to load the driver for the new device. Some examples of devices that fall into this category include Thunderbolt, USB-C and NVME Storage. In this scenario memory resources need to be rearranged and consolidated (rebalanced) to support the additional devices being added.
2. PCI resizeable BARs: After a driver for a device is successfully loaded in memory, it requests additional resources. Some examples of devices include high-end graphics cards and storage devices. For more information about video driver support see, [Resizable BAR support](../display/resizable-bar-support.md).
This topic describes what needs to be done to implement PnP rebalance for PortCls audio drivers.

PnP rebalancing is available in Windows 10, version 1511 and later versions of Windows.

## <span id="Rebalance_Requirements"></span><span id="rebalance_requirements"></span><span id="REBALANCE_REQUIREMENTS"></span>Rebalance Requirements


Portcls audio drivers have the ability to support rebalance if the following conditions are met:

-   The Miniport must register the [IAdapterPnpManagement](/windows-hardware/drivers/ddi/portcls/nn-portcls-iadapterpnpmanagement) interface with Portcls.
-   The Miniport must return PcRebalanceRemoveSubdevices from [**IAdapterPnpManagement::GetSupportedRebalanceType**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iadapterpnpmanagement-getsupportedrebalancetype).
-   Topology and WaveRT are the two Port types supported.

In order to support rebalance when there are active audio streams, portcls audio drivers need to meet one of these two additional requirements.

-   The driver supports the [**IMiniportWaveRTInputStream::GetReadPacket**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavertinputstream-getreadpacket) and [IMiniportWaveRTOutputStream](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportwavertoutputstream) packet interfaces for the audio stream. This is the recommended option.

OR

-   If the driver doesn’t support get/write IMiniportWaveRT for the streams, the driver must not support [**KSPROPERTY\_RTAUDIO\_POSITIONREGISTER**](./ksproperty-rtaudio-positionregister.md) and [**KSPROPERTY\_RTAUDIO\_CLOCKREGISTER**](./ksproperty-rtaudio-clockregister.md). The audio engine will use the [**IMiniportWaveRTStream::GetPosition**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavertstream-getposition) in this scenario.

## <span id="Audio_Stream_Behavior_When_Rebalancing_Occurs"></span><span id="audio_stream_behavior_when_rebalancing_occurs"></span><span id="AUDIO_STREAM_BEHAVIOR_WHEN_REBALANCING_OCCURS"></span>Audio Stream Behavior When Rebalancing Occurs


If the rebalance is triggered, when there are active audio streams, and the driver provides supports rebalance for active audio streams, then all active audio streams will be stopped and they will not be restarted automatically.

## <span id="IPortClsPnp_COM_Interface"></span><span id="iportclspnp_com_interface"></span><span id="IPORTCLSPNP_COM_INTERFACE"></span>IPortClsPnp COM Interface


`IPortClsPnp` is the PnP management interface that the port class driver (PortCls) exposes to the adapter.

`IPortClsPnp` inherits from **IUnknown** and also supports the following methods:

-   [**IPortClsPnp::RegisterAdapterPnpManagement**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iportclspnp-registeradapterpnpmanagement)
-   [**IPortClsPnp::UnregisterAdapterPnpManagement**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iportclspnp-unregisteradapterpnpmanagement)

Audio miniport drivers can register a PNP notification interface using Portcls exports or via the [**IPortClsPnp**](/windows-hardware/drivers/ddi/portcls/nn-portcls-iportclspnp) COM interface IPortClsPnp exposed on the WaveRT port object. Use [**IPortClsPnp::RegisterAdapterPnpManagement**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iportclspnp-registeradapterpnpmanagement) and [**IPortClsPnp::UnregisterAdapterPnpManagement**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iportclspnp-unregisteradapterpnpmanagement) to register and unregister.

## <span id="Required_PortCls_Export_DDIs"></span><span id="required_portcls_export_ddis"></span><span id="REQUIRED_PORTCLS_EXPORT_DDIS"></span>Required PortCls Export DDIs


[IAdapterPnpManagement](/windows-hardware/drivers/ddi/portcls/nn-portcls-iadapterpnpmanagement) is an interface that adapters should implement and register if they want to receive PnP management messages. Register this interface with PortCls using [**PcRegisterAdapterPnpManagement**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcregisteradapterpnpmanagement). Unregister this interface with PortCls using [**PcUnregisterAdapterPnpManagement**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcunregisteradapterpnpmanagement).

## <span id="Required_Driver_DDIs"></span><span id="required_driver_ddis"></span><span id="REQUIRED_DRIVER_DDIS"></span>Required Driver DDIs


The following [IAdapterPnpManagement](/windows-hardware/drivers/ddi/portcls/nn-portcls-iadapterpnpmanagement) DDIs must be implemented to support rebalance.

-   [**IAdapterPnpManagement::GetSupportedRebalanceType**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iadapterpnpmanagement-getsupportedrebalancetype) is called by Portcls while processing the QueryStop. The miniport returns the supported rebalance type as defined in the [**PC\_REBALANCE\_TYPE**](/windows-hardware/drivers/ddi/portcls/ne-portcls-pc_rebalance_type) enum.

    **Note**  Portcls acquires the device global lock before making this call, thus the miniport must execute this call as fast as possible.

     

-   [**IAdapterPnpManagement::PnpQueryStop**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iadapterpnpmanagement-pnpquerystop) is invoked by portcls just before succeeding the QueryStop IRP. This is just a notification and the call doesn’t return a value.

    **Note**  Portcls acquires the device global lock before making this call, thus the miniport must execute this call as fast as possible. While a Stop is pending, Portcls will block (hold) any new create requests.

     

-   [**IAdapterPnpManagement::PnpCancelStop**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iadapterpnpmanagement-pnpcancelstop) is invoked by portcls while processing the CanceStop IRP. This is just a notification. It is possible for the miniport to receive PnpCancelStop even without previously receiving a PnpQueryStop notification. The miniport should be written to accommodate this behavior. For example, this is the case when the QueryStop logic fails the IRP before Portcls has an opportunity to forward this notification to the miniport. In this scenario PnP manager still invokes a PnP Cancel Stop.

    **Note**  Portcls acquires the device global lock before making this call, thus the miniport must execute this call as fast as possible. While a Stop is pending, Portcls will block (hold) any new create requests. PortCls restarts any pended create requests when a pending Stop is cancelled.

     

-   [**IAdapterPnpManagement::PnpStop**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iadapterpnpmanagement-pnpstop) is invoked by Portcls after stopping all Ioctl operations and moving active streams from \[run|pause|acquire\] state to the \[stop\] state. This call is not made while holding the device global lock. Thus the miniport has an opportunity to wait for its async operations (work-items, dpc, async threads) and unregister its audio subdevices. Before returning from this call the miniport must ensure that all the h/w resources have been released.

    **Note**  The miniport must not wait for the current miniport/stream objects to be deleted since it is unclear when existing audio clients will release the current handles. The PnpStop thread cannot block forever without crashing the system, i.e., this is a PnP/Power thread.

     

## <span id="_IMiniportPnpNotify"></span><span id="_iminiportpnpnotify"></span><span id="_IMINIPORTPNPNOTIFY"></span> IMiniportPnpNotify


[IMiniportPnpNotify](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportpnpnotify) is an optional interface to allow miniport objects (audio subdevices) to receive PnP state change notifications.

Miniports have an opportunity to receive a PnP Stop notification for each audio subdevice they have registered. To receive this notification, the subdevice must support [IMiniportPnpNotify](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportpnpnotify). Only the [**IMiniportPnpNotify::PnpStop**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportpnpnotify-pnpstop) notification is defined on this interface.

IMiniportPnpNotify interface available is on both WaveRT and Topology.

**Note**  Because Portcls acquires the device global lock before making this call, the miniport must execute this call as fast as possible. The miniport must not wait on other activity while processing this call to prevent deadlock when other threads/work-items are waiting for the device global lock. If needed, the miniport can wait in the [**IAdapterPnpManagement::PnpStop**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iadapterpnpmanagement-pnpstop) call.
