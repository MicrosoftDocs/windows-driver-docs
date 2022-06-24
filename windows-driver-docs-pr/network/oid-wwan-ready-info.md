---
title: OID_WWAN_READY_INFO
description: OID_WWAN_READY_INFO returns the device ready-state, which includes its Subscriber Identity Module (SIM card).
ms.date: 06/24/2022
keywords: 
 -OID_WWAN_READY_INFO Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID_WWAN_READY_INFO

OID_WWAN_READY_INFO returns the device ready-state, which includes its Subscriber Identity Module (SIM card). This typically occurs at the beginning of any session.

Set requests are not supported.

The host can query the ready-state from either the active SIM slot or inactive SIM slot in the device if the device supports dual SIM slots. This OID's payload contains an [**NDIS_WWAN_QUERY_READY_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-ndis_wwan_query_ready_info) structure, which in turn contains a [**WWAN_QUERY_READY_INFO**](/windows-hardware/drivers/ddi/wwan/ns-wwan-wwan_query_ready_info) structure that specifies the UICC slot ID.

Miniport drivers must process query requests asynchronously, initially returning NDIS_STATUS_INDICATION_REQUIRED to the original request, and later sending an [**NDIS_STATUS_WWAN_READY_INFO**](ndis-status-wwan-ready-info.md) status notification containing an [**NDIS_WWAN_READY_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_ready_info) structure that indicates the MB device's ready-state when completing query requests.

## Remarks

For more information about using this OID, see [MB device Readiness](./mb-device-readiness.md).

Miniport drivers can access device memory or the SIM card when processing query operations, but should not access the provider network.

Miniport drivers should wait until the PIN is cleared (if required) and then read the subscriber's identity and telephone number(s) (TNs), and then set the ReadyInfo.ReadyState member of the NDIS_WWAN_READY_INFO structure to WwanReadyStateInitialized.

Miniport drivers must never fail OID_WWAN_READY_INFO and must always return the correct device ready-state.

Miniport drivers must always notify the MB Service whenever the device ready-state changes.

Miniport drivers should follow these steps to provide a good user experience:

- If PIN1 is locked, miniport drivers must first send a ready-state event notification with **ReadyInfo.ReadyState** set to *WwanReadyStateDeviceLocked*. The MB Service then sends the miniport driver an OID set request of OID_WWAN_PIN. After the device unlocks then the miniport driver must send another ready-state event notification with **ReadyInfo.ReadyState** set to *WwanReadyStateInitialized*. Until PIN1 is successfully unlocked, miniport drivers must not change the device ready-state to *WwanReadyStateInitialized*.

- Miniport drivers must first send an event notification with **ReadyInfo.ReadyState** set to *WwanReadyStateSimNotInserted* when the MB Service loads the miniport driver if no SIM card is present, as may be the case with devices that allow SIM cards to be inserted or removed. If the device has the capability to detect a hot insertion of a SIM card, the miniport driver must send another event notification with **ReadyInfo.ReadyState** set to *WwanReadyStateInitialized* when the user inserts a SIM.

- Devices that have the capability to detect service activation state must set **ReadyInfo.ReadyState** to *WwanReadyStateNotActivated*. Furthermore, if the miniport driver supports service activation, the miniport driver will receive an OID set request of OID_WWAN_SERVICE_ACTIVATION. On successful completion of service activation, miniport drivers must send another event notification with **ReadyInfo.ReadyState** set to *WwanReadyStateInitialized*.

- Miniport drivers that require a specific firmware revision must ensure that the correct firmware revision is available. If the firmware revision is not available, the miniport driver should complete the event notification transaction by setting **ReadyInfo.ReadyState** to *WwanReadyStateFailure*.

## Requirements

**Version**: Available in Windows 7 and later versions of Windows.

**Header**: Ntddndis.h (include Ndis.h)

## See also

[**NDIS_WWAN_READY_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_ready_info)

[**NDIS_STATUS_WWAN_READY_INFO**](ndis-status-wwan-ready-info.md)

[**NDIS_WWAN_QUERY_READY_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-ndis_wwan_query_ready_info)

[**WWAN_QUERY_READY_INFO**](/windows-hardware/drivers/ddi/wwan/ns-wwan-wwan_query_ready_info)

[MB device Readiness](./mb-device-readiness.md)
