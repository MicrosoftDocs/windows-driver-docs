---
title: Indicating Connection Status
description: Indicating Connection Status
ms.assetid: 8a511c14-6b09-47fe-90de-6a90dab93171
keywords:
- WMI WDK networking , media connection status
- miniport drivers WDK networking , media connection status
- NDIS miniport drivers WDK , media connection status
- connection status WDK networking
- media connections WDK networking
- NDIS_STATUS_MEDIA_CONNECT
- NDIS_STATUS_MEDIA_DISCONNECT
- status information WDK NDIS miniport
- status indications WDK networking , media connections
- sleeping state WDK networking
- Waking state WDK networking
- Resetting state WDK networking
- Halting state WDK networking
- Initializing state WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Indicating Connection Status





A miniport driver calls [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600) or [**NdisMCoIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563562) to indicate a change in the media connection status. The miniport driver passes one of the following status indications to **NdisM(Co)IndicateStatus**:

<a href="" id="ndis-status-media-connect"></a>NDIS\_STATUS\_MEDIA\_CONNECT  
Indicates a media connection status change from disconnected to connected. A media connect status change occurs when a disconnected adapter makes a network connection. For example, the adapter connects when it comes within range (for a wireless adapter) or the user connects the network cable.

<a href="" id="ndis-status-media-disconnect"></a>NDIS\_STATUS\_MEDIA\_DISCONNECT  
Indicates a media connection status change from connected to disconnected. A media disconnect status change occurs when a connected adapter loses a network connection. For example, the adapter loses the connection because it is out of range (for a wireless adapter) or the user unplugs the network cable.

Unless specified otherwise, miniport drivers should indicate media connection status changes within two seconds after detecting the status change.

A miniport driver can check the media connection status while performing certain operations (see the following list). If the status is the same after the operation is complete as it was before the operation started,the miniport driver does not have to report any status changes that might have occurred during the operation.

The following list describes additional requirements for indicating media connection status changes for miniport drivers:

<a href="" id="resetting"></a>Resetting  
NDIS calls [*MiniportResetEx*](https://msdn.microsoft.com/library/windows/hardware/ff559432) to reset a miniport driver. The miniport driver can complete the reset either synchronously or asynchronously.

If the media connection status is different after resetting, the driver should indicate the status within two seconds after completing the reset.

A miniport driver should not complete the reset operation until it has determined the media connection status.

<a href="" id="halting"></a>Halting  
A miniport driver must not indicate any media connection status changes when NDIS calls [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388).

<a href="" id="initializing"></a>Initializing  
NDIS calls a miniport driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function to initialize an adapter. During the adapter initialization, the miniport driver must follow these guidelines:

-   If the miniport driver does not indicate the media connection status after returning from *MiniportInitializeEx*, NDIS uses the value of the **MediaConnectState** member of the [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923) structure to determine the media connection status. The miniport driver provides NDIS with this structure when the driver calls [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) from its *MiniportInitializeEx* function.

    **Note**  If the **MediaConnectState** member is set to MediaConnectStateUnknown, NDIS will proceed as if the adapter is disconnected.

     

-   If an adapter is connected after NDIS calls *MiniportInitializeEx*, the miniport driver can indicate NDIS\_STATUS\_MEDIA\_CONNECT within 5 seconds after it returns from *MiniportInitializeEx*.

-   If an adapter is disconnected after NDIS calls *MiniportInitializeEx*, the miniport driver should indicate NDIS\_STATUS\_MEDIA\_DISCONNECT within 2 seconds after it returns from *MiniportInitializeEx*.

-   While initializing, the miniport driver should process [OID\_GEN\_MEDIA\_CONNECT\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff569604) or [OID\_GEN\_CO\_MEDIA\_CONNECT\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff569455) requests asynchronously. The miniport driver should not complete such requests until after it has determined the connection status.

-   Determination of the media connection status should not delay initialization. If necessary, the miniport driver should initiate the process to determine the connection status within *MiniportInitializeEx*, and complete the process at a later time. For example, the miniport driver could set a timer to poll the adapter for the connection status.

-   A deserialized miniport driver can indicate a media disconnect during initialization, but a serialized miniport driver should not.

<a href="" id="sleeping"></a>Sleeping  
A miniport driver enters a network sleep state when it receives an [OID\_PNP\_SET\_POWER](https://msdn.microsoft.com/library/windows/hardware/ff569780) request to set a device power state of D1, D2, or D3.

A miniport driver must not indicate any media connection status changes when it enters a sleep state or while it is in a sleeping state.

<a href="" id="waking"></a>Waking  
A miniport driver wakes from a sleep state when it receives an OID\_PNP\_SET\_POWER request to set the device power state to D0.

If the adapter's media connection status after waking is the same as the status was prior to sleeping, the miniport driver should not indicate a media connection status change. If the connection status changed, the miniport driver should indicate the new connection status within two seconds after waking.

While waking, the miniport driver should process OID\_GEN\_MEDIA\_CONNECT\_STATUS or OID\_GEN\_CO\_MEDIA\_CONNECT\_STATUS requests asynchronously. The miniport driver should not complete such requests until after it has determined the connection status.

 

 





