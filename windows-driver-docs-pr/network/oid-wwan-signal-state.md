---
title: OID\_WWAN\_SIGNAL\_STATE
author: windows-driver-content
description: OID\_WWAN\_SIGNAL\_STATE returns or sets the current signal state.
ms.assetid: 6f5d8fd6-b4cf-4058-a27e-d4f7cea19f47
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_WWAN_SIGNAL_STATE Network Drivers Starting with Windows Vista
---

# OID\_WWAN\_SIGNAL\_STATE


OID\_WWAN\_SIGNAL\_STATE returns or sets the current signal state.

Miniport drivers must process set and query requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending an [**NDIS\_STATUS\_WWAN\_SIGNAL\_STATE**](ndis-status-wwan-signal-state.md) status notification containing an [**NDIS\_WWAN\_SIGNAL\_STATE**](ndis-wwan-signal-state.md) structure to provide information about the current signal state indication shown to the end-user regardless of completing set or query requests.

Callers requesting to set the current signal state indication to the end user provide an [**NDIS\_WWAN\_SET\_SIGNAL\_INDICATION**](ndis-wwan-set-signal-indication.md) structure to the miniport driver with the appropriate information.

Remarks
-------

For more information about using this OID, see [WWAN Signal Strength Operations](https://msdn.microsoft.com/library/windows/hardware/ff559125).

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

Requirements
------------

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


[**NDIS\_WWAN\_SET\_SIGNAL\_INDICATION**](ndis-wwan-set-signal-indication.md)

[WWAN Signal Strength Operations](https://msdn.microsoft.com/library/windows/hardware/ff559125)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_SIGNAL_STATE%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


