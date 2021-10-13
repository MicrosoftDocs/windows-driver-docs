---
title: OID_WWAN_REGISTER_STATE
description: OID_WWAN_REGISTER_STATE selects a network provider to register with.
ms.date: 08/08/2017
keywords: 
 -OID_WWAN_REGISTER_STATE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
ms.custom: 19H1
---

# OID\_WWAN\_REGISTER\_STATE


OID\_WWAN\_REGISTER\_STATE selects a network provider to register with.

Miniport drivers must process set and query requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending an [**NDIS\_STATUS\_WWAN\_REGISTER\_STATE**](ndis-status-wwan-register-state.md) status notification containing an [**NDIS\_WWAN\_REGISTRATION\_STATE**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_registration_state) structure to provide information about the registered network provider regardless of completing set or query requests.

Callers requesting to set the network provider to register with provide an [**NDIS\_WWAN\_SET\_REGISTER\_STATE**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_set_register_state) structure to the miniport driver with the appropriate information.

## Remarks

For more information about using this OID, see [WWAN Registration Operations](./mb-registration-operations.md).

Miniport drivers can access the provider network when processing query or set operations, but should not access the Subscriber Identity Module (SIM card).

The MB driver model supports two registration methods--automatic and manual. For CDMA-based networks, the MB driver model supports only automatic registration.

Devices supporting manual registration must set the **WwanControlCaps** member in [**WWAN\_DEVICE\_CAPS**](/windows-hardware/drivers/ddi/wwan/ns-wwan-_wwan_device_caps) structure to WWAN\_CTRL\_CAPS\_REG\_MANUAL. Be aware that GSM-based devices must support manual registration.

If the registration state is automatic, miniport drivers must instruct their device to select a network provider based on the selection algorithm specific to the cellular technology and proceed with registration.

The semantics of RegisterAction values are defined as follows:

-   The *WwanRegisterActionAutomatic* flag is used by the MB Service to instruct the miniport driver to set the device to automatic register mode and let the device select the best provider network. The miniport driver must ignore **ProviderId** parameter. This setting is persistent across radio states (ON/OFF), and device power cycles, until it is explicitly change by the MB Service.

-   The *WwanRegisterActionManual* flag is used by the MB Service to instruct the miniport driver to register with the provider network identified by the **ProviderId** parameter. The **ProviderId** value shall come from the **ProviderId** member of WWAN\_PROVIDER data structure of one of the visible providers. This setting is persistent across radio states (ON/OFF), and device power cycles, until it is explicitly changed by the MB Service.

-   Changing between the different RegisterAction values are allowed even if the device is currently registered to a provider. If the device need to deregister before switching between the Automatic and Manual registration modes, the miniport driver must ensure that the device is set to deregistration before setting to the new registration mode.

-   The *Manual* and *Automatic* registration mode only affects the network selection mode. The MB device should try to register to selected network whenever the radio is turned on.

### Windows 10, version 1903

A new revision 3 for this OID is supported starting in Windows 10, version 1903. This extension enables the host to query the preferred radio access technologies (RATs) from the miniport driver. 

To control the preferred RAT, the host sets a bitmask representing WWAN_DATA_CLASS values in the **WwanDataClass** member of the [**WWAN_SET_REGISTER_STATE**](/windows-hardware/drivers/ddi/wwan/ns-wwan-_wwan_set_register_state) structure. This member represents the data access technologies that are preferred for a connection. If this field is set to **WWAN_DATA_CLASS_NONE**, then the modem should take no action for this parameter.

The host can also query the currently preferred data classes from the miniport driver. The miniport driver uses the **PreferredDataClasses** field of the [**WWAN_REGISTRATION_STATE**](/windows-hardware/drivers/ddi/wwan/ns-wwan-_wwan_registration_state) structure to report the preferred data access technologies that are currently set in the modem.

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


[**NDIS\_WWAN\_SET\_REGISTER\_STATE**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_set_register_state)

[**NDIS\_STATUS\_WWAN\_REGISTER\_STATE**](ndis-status-wwan-register-state.md)

[WWAN Registration Operations](./mb-registration-operations.md)

