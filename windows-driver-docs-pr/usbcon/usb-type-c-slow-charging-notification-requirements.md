---
title: USB Type-C slow charging notification requirements in Windows
description: This article describes how to use Windows notifications when a user plugs in a USB Type-C power source that results in a suboptimal power delivery contract.
ms.date: 03/15/2023
ms.custom: template-concept
---

# USB Type-C slow charging notification requirements in Windows

With the adoption of USB Type-C, a user could employ a suboptimal power source to charge their system. This article describes how to use Windows notifications when a user plugs in a USB Type-C power source that results in a suboptimal power delivery contract.

## USB Type-C charging

To provide users with consistent experience, Microsoft has defined the system certification requirement [USBTypeCCharging](/windows-hardware/test/hlk/testref/7f445d97-75e5-4a47-bbe2-dd191228ef44). The requirement states that if a system with a battery contains USB Type-C ports that can be used to charge the system, those ports must meet the following requirements, in addition to the USB Type-C and power deliver (PD) specs:

- The system must be able to charge from a dead battery using a USB Type-C charger that provides sufficient power for the system.
- All USB Type-C ports on the system must support charging the system.
- All USB Type-C ports on the system must support sourcing at 15 watts.
- Systems must allow charging from any PD-compliant charger that provides sufficient power for the system.
- Systems and software must treat all PD-compliant power sources (for example, charger, hub, dock) the same, regardless of manufacturer.
- All USB Type-C charging notifications must rely on built-in Windows notifications and not be provided by third-party software.

Windows can notify the user when they plug in a charger or a charging dock that has negotiated a lesser power contract than what machine requires for optimal charging. This feature is present in all machines with USB Type-C connectors managed by the following types of UcmCx drivers:

1. On [UCSI](/windows-hardware/drivers/usbcon/ucsi) capable machines, inbox the UCM-UCSI ACPI client driver manages USB Type-C connectors. This solution is recommended because it uses Windows provided drivers and doesn't depend on an OEM or IHV developing their own driver.
1. [UcmCx client drivers](/windows-hardware/drivers/usbcon/developing-windows-drivers-for-usb-type-c-connectors) for machines that have implemented PD state machines in hardware or firmware and aren't UCSI compliant.

## UCSI capable machines

UCSI capable machines typically have an embedded controller containing platform policy manager (PPM) firmware to manage PD state machines. This management is transparent to the OS policy manager (OPM), an entity in the OS that the inbox UCSI driver implements. The PPM uses the interaction mechanism laid out by the [UCSI specification](https://www.intel.com/content/www/us/en/products/docs/io/universal-serial-bus/usb-type-c-ucsi-spec.html) to interact with the OPM.

The following are mechanisms by which a PPM can notify OPM about slow charging. Slow charging is reported to Windows only if the power role of the connector is power consumer.

1. A notification from the PPM to the OPM with the connector change indicator (CCI) set to the connector number from which the slow charging notification is intended to come. In response to this notification, the OPM sends a GET_CONNECTOR_STATUS UCSI command to the PPM. The PMM should respond to this command with GET_CONNECTOR_STATUS data with the following bits set.
    1. Connector status change (16-0) battery charging status change bit set to 1.
    1. Battery charging capability status (65-64) set to *not* charging (value 0), slow charging rate (value 2) or very slow charging rate (value 3).

1. If a slow charger is connected while the machine is shut down or in Sx (x > 0), the PPM must set the battery charging capability status to reflect one of the three values mentioned in 1b above when the OPM sends GET_CONNECTOR_STATUS to PPM after boot or Sx resume. On Sx resume, the OPM generally sends the GET_CONNECTOR_STATUS command to the PPM after a PPM_RESET.

    Conversely, if a nominal charger is connected when the machine is in Sx (x>0), OPM expects GET_CONNECTION_STATUS data to have the battery charging capability status field (65-64) set to nominal charging rate (value 1) when OPM sends GET_CONNECTOR_STATUS.

### Special consideration for BatteryChargingCapabilityStatus::NotCharging (value 0)

GET_CONNECTOR_STATUS::Batter Charging Capability Status' "Not Charging" value is 0, which is also the default. Therefore, unless the connector status change (16-0) battery charging status change bit is set to 1, OPM can't determine if this is a default value or this was explicitly set to 0 by PPM to indicate not charging. If this bit is set to 0, the OS may ignore the battery charging status when the status is Not Charging.

Hence, our strong recommendation to PPM would be to always set the connector status change (16-0) battery charging status change bit to 1 when reporting not/slow/very slow charging. This recommendation is to make PPM implementation simple for managing charging statuses.

### Special case for slow and very slow charging

This section doesn't contain any specific recommendations for OEMs, IHVs or UCSI firmware owners. Rather describes a specific logic that inbox UCSI driver adopts around charging notifications that might be useful knowledge while designing UCSI firmware.

On the first notification following a partner attach, after it gets the response data of GET_CONNECTOR_STATUS, UCSI driver will report slow charging to the OS even if connector status change (16-0) battery charging status change bit isn't set to 1, if the following conditions are true:

1. Connector status change (16-0): ConnectChange indicates this is the partner's first attach notification.
1. Battery charging capability status (62-65) is set to value 2 or 3.

The rationale behind this behavior is UCSI driver doesn't know if Not Charging was intentional since its value is 0, which is also the default value. However, values 2 and 3 can be handled without relying on the battery charging status change. For more information, see the next section.

### UCSI Compliance Test

Since optimal power contract is specific to the machine, Windows doesn't provide tests for *Slow* or *Not Charging* toast notifications on Windows as the test would now know what power levels to validate the notification against. However, we recommend OEMs validate if their battery charging notifications from PPM to OPM are working as expected using the following UCSI Compliance test that uses USB Type-C MUTT as the port partner:

- [UcsiTest::TestBatteryChargingNotification](/windows-hardware/test/hlk/testref/dc0dbe87-3202-4aa4-aa66-3256ca0c4f61)

## UCMCx Client drivers

UcmCx client drivers manage USB Type-C connectors without being compliant to UCSI specifications. Among reporting other information about USB Type-C connectors to the OS, the class extension keeps the OS informed about the changes in charging levels of the USB Type-C connector. Here are UmCx DDIs through with a client driver may inform the OS of [UCM_CHARGING_STATE](/windows-hardware/drivers/ddi/ucmtypes/ne-ucmtypes-_ucm_charging_state) of the connectors.

1. [UcmConnectorTypeCAttach](/windows-hardware/drivers/ddi/ucmmanager/nf-ucmmanager-ucmconnectortypecattach): when reporting a new port partner attached to UCM, a client may report the charging level using the input parameter [UCM_CONNECTOR_TYPEC_ATTACH_PARAMS::ChargingState](/windows-hardware/drivers/ddi/ucmmanager/ns-ucmmanager-_ucm_connector_typec_attach_params)

1. [UcmConnectorPdConnectionStateChanged](/windows-hardware/drivers/ddi/ucmmanager/nf-ucmmanager-ucmconnectorpdconnectionstatechanged): While reporting the RDO to UCM for the negotiated power contract. The client may report the charging level using [UCM_CONNECTOR_PD_CONN_STATE_CHANGED_PARAMS::ChargingState](/windows-hardware/drivers/ddi/ucmmanager/ns-ucmmanager-_ucm_connector_pd_conn_state_changed_params)

1. [UcmConnectorChargingStateChanged](/windows-hardware/drivers/ddi/ucmmanager/nf-ucmmanager-ucmconnectorchargingstatechanged): On any occasion where the client driver would like to update the charging state to the OS. Param2 of this DDI contains the charging state of the connector.

Consider the following values of the enum [UCM_CHARGING_STATE](/windows-hardware/drivers/ddi/ucmtypes/ne-ucmtypes-_ucm_charging_state) to show the toast notification to the user:

- UcmChargingStateNotCharging
- UcmChargingStateSlowCharging
- UcmChargingStateTrickleCharging

## Related topics

- [Windows support for USB Type-C connectors](oem-tasks-for-bringing-up-a-usb-typec.md)
- [Hardware design: USB Type-C systems](hardware-design-of-a-usb-type-c-system.md)
- [OEM tasks for USB Type-C systems](oem-tasks-for-usb-type-c-systems-running-windows.md)
- [USBTypeCCharging](/windows-hardware/test/hlk/testref/7f445d97-75e5-4a47-bbe2-dd191228ef44)
- [UCSI specification](https://www.intel.com/content/www/us/en/products/docs/io/universal-serial-bus/usb-type-c-ucsi-spec.html)
