---
title: OID_WWAN_RADIO_STATE
author: windows-driver-content
description: OID\_WWAN\_RADIO\_STATE sets or returns information about a MB device's radio power state.
ms.assetid: e6d09ae8-65c8-4544-9581-8937f61f0747
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_WWAN_RADIO_STATE Network Drivers Starting with Windows Vista
---

# OID\_WWAN\_RADIO\_STATE


OID\_WWAN\_RADIO\_STATE sets or returns information about a MB device's radio power state.

Miniport drivers must process set and query requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending an [**NDIS\_STATUS\_WWAN\_RADIO\_STATE**](ndis-status-wwan-radio-state.md) status notification containing an [**NDIS\_WWAN\_RADIO\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567915) structure that indicates the MB device's current radio power state regardless of completing set or query requests.

Callers requesting to set the MB device's radio power state provide an [**NDIS\_WWAN\_SET\_RADIO\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567925) structure to the miniport driver with the appropriate information.

Remarks
-------

For more information about using this OID, see [WWAN Radio Power State Operations](https://msdn.microsoft.com/library/windows/hardware/ff559107).

Miniport drivers should not access the provider network, or the Subscriber Identity Module (SIM card), when processing query or set operations.

Miniport drivers must retain software radio power states across system restart or device removal and reinsertion. Miniport drivers should store the device's software radio information and use it for setting the device software radio power state immediately on each restart or reinsertion of device. The effective radio power state of the device is decided based on combination of software and hardware radio power state as per the table in [**WWAN\_RADIO\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff571225).

If the value is *WwanRadioOn*, miniport drivers must turn on the radio power and set the **RadioState.SwRadioState** member of the WWAN\_RADIO\_STATE structure to *WwanRadioOn*. If the **RadioState.HwRadioState** member was *WwanRadioOff*, miniport drivers should cache this power state information and ensure to physically turn on the radio power state when **RadioState.HwRadioState** changes to *WwanRadioOn*.

If the value is *WwanRadioOff*, miniport drivers must turn off the radio power state and set the **RadioState.SwRadioState** member to *WwanRadioOff*.

Refer to the following table for the expected radio state programming by miniport drivers.

**Valid Combinations for PIN Mode and PIN State**

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>HwRadioState value</th>
<th>SwRadioState value</th>
<th>Overall radio power state</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>WwanRadioOff</p></td>
<td><p>WwanRadioOff</p></td>
<td><p>WwanRadioOff</p></td>
</tr>
<tr class="even">
<td><p>WwanRadioOff</p></td>
<td><p>WwanRadioOn</p></td>
<td><p>WwanRadioOff</p></td>
</tr>
<tr class="odd">
<td><p>WwanRadioOn</p></td>
<td><p>WwanRadioOff</p></td>
<td><p>WwanRadioOff</p></td>
</tr>
<tr class="even">
<td><p>WwanRadioOn</p></td>
<td><p>WwanRadioOn</p></td>
<td><p>WwanRadioOn</p></td>
</tr>
</tbody>
</table>

 

For devices that do not provide a hardware radio power switch, the **RadioState.HwRadioState** member of the NDIS\_WWAN\_RADIO\_STATE structure must always be set to *WwanRadioOn*.

Starting in Windows 10, version 1703, OID\_WWAN\_RADIO\_STATE has additional specifications for how a multi-executor supported modem should handle radio state configuration from the OS.

With a multi-executor supported modem, there are power benefits to configuring radio power state per executor. When an executor’s radio is turned off, the OS expects the modem to de-register from the network and does not attempt any scanning or location updates from it. The modem should support a radio state for each executor that it advertises to the OS so it can determine the hardware power state in which it should be.

As an example, if the modem has two executors and one of the executors' radio is off while the other is on, then the modem may keep the RF front end powered on to maintain registration on the executor whose radio is on but does not need to do scanning/pinging/location updates or other cellular services for the executor that is turned off. If both radios are turned off, the modem can turn off its RF front end and bring the overall hardware to a lower power state. The implementation specifics are left to each IHV.

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


[**NDIS\_WWAN\_RADIO\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567915)

[**NDIS\_WWAN\_SET\_RADIO\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567925)

[**NDIS\_STATUS\_WWAN\_RADIO\_STATE**](ndis-status-wwan-radio-state.md)

[WWAN Radio Power State Operations](https://msdn.microsoft.com/library/windows/hardware/ff559107)

[**WWAN\_RADIO\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff571225)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_RADIO_STATE%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


