---
title: OID_WWAN_SIGNAL_STATE
description: OID_WWAN_SIGNAL_STATE returns or sets the current signal state.
ms.date: 04/05/2019
keywords: 
 -OID_WWAN_SIGNAL_STATE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
ms.custom: 19H1
---

# OID\_WWAN\_SIGNAL\_STATE


OID\_WWAN\_SIGNAL\_STATE returns or sets the current signal state.

Miniport drivers must process set and query requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending an [**NDIS\_STATUS\_WWAN\_SIGNAL\_STATE**](ndis-status-wwan-signal-state.md) status notification containing an [**NDIS\_WWAN\_SIGNAL\_STATE**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_signal_state) structure to provide information about the current signal state indication shown to the end-user regardless of completing set or query requests.

Callers requesting to set the current signal state indication to the end user provide an [**NDIS\_WWAN\_SET\_SIGNAL\_INDICATION**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_set_signal_indication) structure to the miniport driver with the appropriate information.

## Remarks

For more information about using this OID, see [WWAN Signal Strength Operations](./mb-signal-strength-operations.md).

Miniport drivers should not access the provider network, or the Subscriber Identity Module (SIM card), when processing query or set operations.

Generally, signal state should be indicated rather than polled. However, this OID is made available in case the current signal state needs to be determined by the MB Service.

For response to query requests, miniport drivers should send an NDIS\_STATUS\_WWAN\_SIGNAL\_STATE notification.

On a set request from the MB Service, miniport drivers should:

-   Return the current values for **Rssi** and **ErrorRate** in the NDIS\_WWAN\_SIGNAL\_STATE structure in addition to reporting the absolute values for **RssiInterval** and **RssiThreshold** that has been set in the miniport driver.

-   Internally cache the **RssiInterval** and/or **RssiThreshold** values even if the device is not currently registered with any operator and that any restriction imposed by device in setting parameters can only be possible post-registration state. The miniport driver should try to apply these settings in the next immediate available situation.

-   Complete the request successfully, if the hardware and/or software radio switch state is currently OFF. Miniport driver cache the request data and start reporting the signal strength after the switch is turned ON.

-   Can fail this request with the appropriate **uStatus** error code set.

Miniport drivers can do the following when processing query requests from the MB Service:

-   Return the current values for **Rssi** and **ErrorRate** in the NDIS\_WWAN\_SIGNAL\_STATE structure in addition to reporting the absolute values for **RssiInterval** and **RssiThreshold** that has been set in the miniport driver.

-   Fail this request with the appropriate **uStatus** error code set.

Return Values:

NDIS\_STATUS\_NOT\_SUPPORTED

Miniport drivers can return this for specific devices that are aware of device capabilities not supporting the signal strength can fail the request with this error code.

**Recommended Implementation**

1.  Devices must support signal strength indications.

2.  Drivers must report signal strength indications of at least 50% of the **RssiInterval** setting over a time period of five minutes.

3.  Devices must avoid reporting the signal strength in the following states:
    1.  Device not registered or deregistered and is applicable only for GSM devices.
    2.  Effective state of radio is OFF.
    3.  In the above states, a query to the signal strength must be returned with the following data by the miniport driver:

        Rssi = WWAN\_RSSI\_UNKNOWN

        ErrorRate = WWAN\_ERROR\_RATE\_UNKNOWN;

        RssiInterval = &lt; WWAN\_RSSI\_DISABLE, WWAN\_RSSI\_DEFAULT or last set value&gt;

        RssiThreshold = &lt; WWAN\_RSSI\_DISABLE, WWAN\_RSSI\_DEFAULT or the last set value&gt;

### Windows 10, version 1903

Starting in Windows 10, version 1903, OID_WWAN_SIGNAL_STATE has been upgraded to revision 3. This revision enables the host to query new reference signal received power (RSRP) and Signal-to-Noise (SNR) values from the miniport driver. A miniport driver must use revision 3 of this OID and its data structures if the driver supports 5G.

For more info about 5G data class support, see [MB 5G data class support](./mb-5g-operations-overview.md).

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available in Windows 7 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_WWAN\_SET\_SIGNAL\_INDICATION**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_set_signal_indication)

[WWAN Signal Strength Operations](./mb-signal-strength-operations.md)

