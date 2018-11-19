---
title: NDIS_STATUS_WWAN_REGISTER_STATE
description: Miniport drivers use the NDIS_STATUS_WWAN_REGISTER_STATE notification to communicate changes to the MB device's registration state to the MB Service.
ms.assetid: 3da8489a-6ca3-4897-9794-86665ce10e81
ms.date: 08/08/2017
keywords: 
 -NDIS_STATUS_WWAN_REGISTER_STATE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WWAN\_REGISTER\_STATE


Miniport drivers use the NDIS\_STATUS\_WWAN\_REGISTER\_STATE notification to communicate changes to the MB device's registration state to the MB Service.

Miniport drivers can also send unsolicited events with this notification.

This notification uses the [**NDIS\_WWAN\_REGISTRATION\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567917) structure.

Remarks
-------

As the registration state of the device changes, the miniport driver must send appropriate indications so that the MB Service can reflect the correct state to the user.

Registration state changes due to a number of reasons. It may directly result from *set* requests from the MB Service for OID\_WWAN\_REGISTER\_STATE such as a transient state transition from **WwanRegisterStateSearching** to **WwanRegisterStateHome**. It may also result from automatic operations by the miniport driver in the case of automatic provider selection. Finally, it may be caused by change of network availability, for example, losing network coverage may result in transition from **WwanRegisterStateHome** to **WwanRegisterStateDeregistered**.

Except for the changes caused by MB Service OID\_WWAN\_REGISTER\_STATE requests, the miniport driver shall notify the MB Service whenever the registration state changes regardless of the underlying cause.

CDMA devices do not support the MB Service initiated registration and deregistration. However, a device initiated register state change notifications based on the availability or non-availability of the carrier network must be sent to the MB Service. CDMA devices must do automatic registration.

For devices that do automatic registration on power-up, irrespective of the current registration mode--auto or manual, the miniport driver must send the register state notification on successful registration.

For manual registration, the MB Service shall only initiate registration after the miniport driver indicates that **ReadyState** is **WwanReadyStateInitialized**.

Miniport driver must use the following guidelines while responding to *set* requests:

-   Drivers must not respond with transient state for a *set* requests. Transient state for registration is **WwanRegisterStateSearching**.

-   When **RegisterAction** is set to **WwanRegisterActionManual**, if the provider is not visible when the miniport driver receives the request, the miniport driver shall return error code WWAN\_STATUS\_PROVIDER\_NOT\_VISIBLE. The device must not switch to automatic registration because of a failure in setting the manual mode. If the device was earlier set to manually register to another network, this request should change the device to register to the network specified in the request. The value of **RegisterState** in response to the request should be set to **WwanRegisterStateDeregistered**.

-   When **RegisterAction** is set to **WwanRegisterActionManual**, if the miniport driver has already registered with the same network that is been requested, it shall respond with WWAN\_STATUS\_SUCCESS.

-   The driver should attempt to register to the requested data-class in the set OID\_WWAN\_REGISTER request. If the miniport driver cannot register to the requested data-class, it should register to the best possible data-class. This is also applicable when the device is already registered to a provider (automatic and manual registration mode) with some other data-class. Any change in the data-class should also result in NDIS\_STATUS\_WWAN\_PACKET\_SERVICE notification.

-   When **RegisterAction** is set to **WwanRegisterActionManual**, and the Radio is OFF, the miniport driver must program the device to manual registration mode and complete the request with the transaction notification. The **RegisterState** should be set to **WwanRegisterStateDeregistered**. The device must attempt a manual registration when the Radio changes to ON state and the event notification must be sent.

-   When **RegisterAction** is set to **WwanRegisterActionAutomatic**, and the Radio is OFF, the miniport driver must program the device to automatic registration mode and must complete the request with the transaction notification. The **RegisterState** should be set to **WwanRegisterStateDeregistered**. The device must do an automatic registration when the Radio goes to ON state and the event notification must be sent.

-   In case of emergency state registration ( **WwanRegisterStateDenied**), the **uStatus** should be set to WWAN\_STATUS\_SUCCESS and NDIS\_STATUS\_WWAN\_READY\_INFO notification must be sent with **EmergencyMode** set to **WwanEmergencyModeOn**.

-   For using the state **WwanRegisterStateDeregistered** the miniport driver must use the following guidelines:

    -   **WwanRegisterStateDeregistered** is used by the miniport drivers for notifying the MB Service that the Radio is OFF but the request for **RegisterAction** is completed.

    -   **WwanRegisterStateDeregistered** is used by the miniport drivers for notifying the MB Service of a network initiated deregistration.

    -   **WwanRegisterStateDeregistered** is used by the miniport drivers for notifying the MB Service of the lost connectivity to the network due to no network coverage.

-   GSM and CDMA devices must send the register state notification to notify the availability or non-availability of the carrier for a PS connection. When the MB device detects the availability of the carrier network, it must send an event notification with one of the appropriate register states-- **WwanRegisterStateHome**, **WwanRegisterStateRoaming**, or **WwanRegisterStatePartner**. On losing the carrier network signal, an event notification with **WwanRegisterStateDeregistered** must be indicated to the MB Service.

The miniport driver returns the query result according to the following rules:

-   When the device is trying to lock on to a provider during registration, the miniport driver shall set **RegisterState** as **WwanRegisterStateSearching**. Both the **ProviderName** and **RoamingText** members should be set to **NULL**. In case of Manual register mode, **ProviderId** must be filled in with the ProviderId from the last manual registration set request. **ProviderId** can be set to **NULL** in case of automatic register mode.

-   This is a transient state as the miniport driver will eventually move to a stable state at the end of registration, for example, **WwanRegisterStateHome**, **WwanRegisterStatePartner**, or **WwanRegisterStateRoaming** for a successful registration; or **WwanRegisterStateDenied** for an emergency state registration.

-   If the device is not registered with any provider, the miniport driver shall return **WwanRegisterStateDeregistered**. Both the **ProviderName** and **RoamingText** members should be set to **NULL**. In case of Manual register mode, **ProviderId** must be filled in with the ProviderId from the last manual registration set request. **ProviderId** can be set to **NULL** in case of automatic register mode.

-   If the device is registered with the home provider, the miniport driver shall set **RegisterState** as **WwanRegisterStateHome**. The **ProviderId** member shall be set to the home provider ID. The **ProviderName** must be set to the name of home provider network. The **RoamingText** member should be set to **NULL**.

-   If the device is registered with a roaming provider, the miniport driver shall set **RegisterState** as **WwanRegisterStatePartner** if the provider is a preferred roaming partner or just **WwanRegisterStateRoaming** for a roaming partner, respectively. If the miniport driver does not distinguish the two, it shall set the value to **WwanRegisterStateRoaming**. The **ProviderId** member shall be set to the provider ID of the current provider the device is registered with and the **ProviderName** must be filled in with the current registered provider name. The **RoamingText** member should be set to some provider specific string value if exists or to **NULL** otherwise.

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
<td>Ndis.h</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_WWAN\_REGISTRATION\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567917)

[OID\_WWAN\_REGISTER\_STATE](oid-wwan-register-state.md)

 

 




