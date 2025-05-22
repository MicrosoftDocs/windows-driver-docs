---
title: USB Type-C Slow Charging Notification Requirements in Windows
description: This article describes how to use Windows notifications when a user plugs in a USB Type-C power source that results in a suboptimal power delivery contract.
ms.date: 01/17/2024
ms.custom: template-concept
---

# USB Type-C slow charging notification requirements in Windows

With the adoption of USB Type-C, a user could employ a suboptimal power source to charge their system. This article describes how hardware and firmware vendors can use Windows notifications when a user plugs in a USB Type-C power source resulting in a suboptimal power delivery contract.

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

## Windows USB-C troubleshooting notifications

| Category | Scenario | Notification title or message | Trigger conditions for systems with UCSI | Trigger Conditions for Systems with Custom UCM Client Driver |
|--|--|--|--|--|
| Power | A user connects a slow USB-C charger. | Slow charger<br><br>To speed up charging, use a higher-watt charger. | In response to UCSI command GET_CONNECTOR_STATUS, UCSI PPM returns with both of the following fields.<br><br>-  ConnectorStatusChange.BatteryChargingStatusChange = 1<br>-  BatteryChargingCapabilityStatus = 2 (Slow Charging) or 3 (Trickle Charging) | The UcmCx client driver calls UcmConnectorPdConnectionStateChanged with the following parameter.<br><br>-  Params-&gt;ChargingState = UcmChargingStateSlowCharging  or UcmChargingStateTrickleCharging. |
| Power | A user connects a USB-C charger that is too weak to charge the system. | PC isn't charging<br><br>Use the recommended charger and cable, and make sure it's directly plugged in. | In response to UCSI command GET_CONNECTOR_STATUS, UCSI PPM returns with both of the following fields.<br><br>-  ConnectorStatusChange.BatteryChargingStatusChange = 1<br>-  BatteryChargingCapabilityStatus = 0 (Not Charging) | The UcmCx client driver calls UcmConnectorPdConnectionStateChanged with the following parameter.<br><br>-  Params-&gt;ChargingState = UcmChargingStateNotCharging |
| Power | A user connects a USB-C device which maximum power requirements are greater than what the system can ever provide. | USB device might need more power<br><br>Your PC might not provide enough power to the USB device.&nbsp;Please connect your device to external power, or try using a&nbsp;different PC. | In response to UCSI command GET_CONNECTOR_STATUS, UCSI PPM returns with the following field.<br><br>- RequestDataObject..CapabilityMismatch(B26) = 1<br><br>For more info of Request Data Object, please refer to the USB Power Delivery specification. | The UcmCx client driver calls UcmConnectorPdConnectionStateChanged with the following parameter. <br><br>-  Params-&gt;Rdo..CapabilityMismatch = 1<br><br>For more info of Request Data Object, please refer to the USB Power Delivery specification. |
| Power | A user connects a defective USB-C device which attempts to consume excessive power from a system, leading to the Type-C OverCurrent condition.<br><br>As of Windows 11 24H2, the support of this notification is not enabled by default. It's enabled by a registry value when test signing is on.<br><br>It's undergoing tests by one OEM. If anyone else would like to test this notification as well, please make sure that USB-C overcurrent is reported from UCSI PPM only, and not from USB host controller so that there won't be duplicated reports. | Power surge on the USB-C port<br><br>A USB-C device has malfunctioned and exceeded the power limits. You should disconnect the device. | 1. In response to UCSI command GET_CONNECTOR_STATUS, UCSI PPM returns the following field.<br><br>-  ConnectorStatusChange.Error = 1<br><br>2. In response to the subsequent UCSI command GET_ERROR_STATUS for the connector, UCSI PPM returns the following field.<br><br>-  GetErrorStatus.ErrorInformation.Overcurrent = 1 | Not Implemented |
| Mode | A user connects a USB4 device to a system that doesn't support USB4. | USB4 device functionality might be limited<br><br>Make sure the USB4 device you're connecting to is supported by your PC. Select this message for more troubleshooting info. | On the system that doesn't support USB4, the USB4 device enumerates a USB Billboard device with a Billboard Capability Descriptor which meets both of the following conditions.<br><br>1. USB4 mode SVID 0xFF00 is present in the wSVID field.<br>2. The corresponding entry in the bmConfigure field indicates the mode is not configured (value 0, 1 or 2). | (Same as the UCSI System case) |
| Mode | A user connects a USB4 device to a USB port that doesn't support USB4, but the system supports USB4 on other USB ports. | Use different USB port<br><br>The USB device might have limited functionality when connected to this port. Plug the device into a different USB port on your PC. | On the system that supports USB4, the USB4 device enumerates a USB Billboard device with a Billboard Capability Descriptor which meets both of the following conditions.<br><br>1. USB4 mode SVID 0xFF00 is present in the wSVID field.<br>2. The corresponding entry in the bmConfigure field indicates that the mode is "not attempted or exited" (value 1). | (Same as the UCSI System case) |
| Mode | A user connects a Thunderbolt device to a system that doesn't support Thunderbolt. | Thunderbolt device functionality might be limited<br><br>Make sure the Thunderbolt device you're connecting to is supported by your PC. Select this message for more troubleshooting info. | The Thunderbolt device enumerates a USB Billboard device with a Billboard Capability Descriptor which meets both the following conditions.<br><br>1. Thunderbolt Alternate Mode SVID 0x8087 is present in the wSVID field.<br>2. The corresponding entry in the bmConfigure field indicates that the mode is not configured (value 0, 1 or 2).<br><br>Note: If the USB-C device also supports USB4, its notifications will take precedence, or suppress this Thunderbolt notification as long as USB4 mode is configured. | (Same as the UCSI System case) |
| Mode | A user connects a USB-C DisplayPort or MHL device to a system that doesn't support DisplayPort or MHL over USB-C. | Display connection might be limited<br><br>Make sure the DisplayPort device you're connecting to is supported by your PC. Select this message for more troubleshooting info.<br><br>-OR-<br><br>MHL device functionality might be limited<br><br>Make sure the MHL device you're connecting to is supported by your PC. Select this message for more troubleshooting info. | The USB-C DisplayPort device enumerates a USB Billboard device with a Billboard Capability Descriptor which meets both of the following conditions.<br><br>1. DisplayPort Alternate Mode SVID 0xFF01 (or the MHL Alternate Mode SVID 0xFF02) is present in the wSVID field.<br>2. The corresponding entry in the bmConfigure field indicates that the mode is not configured (value 0, 1 or 2).<br><br>Note: If the USB-C device also supports USB4 or Thunderbolt, their notifications will take precedence, or suppress this DisplayPort or MHL notification if USB4 or Thunderbolt mode is configured. | (Same as the UCSI System case) |
| Mode | A user connects a USB-C device which supports an Alternate Mode that the system doesn't recognize, and the mode is not configured.<br><br>As of Windows 11 24H2, only Thunderbolt, DisplayPort and MHL alternate modes as well as USB4 mode are recognized. | USB device functionality might be limited<br><br>Make sure the device you're connecting to is supported by your PC. Select this message for more&nbsp;troubleshooting&nbsp;info. | The USB-C device enumerates a USB Billboard device with a Billboard Capability Descriptor which meets both of the following conditions.<br><br>1. An unrecognized Alternate Mode SVID is present in wSVID field.<br>2. The corresponding entry in the bmConfigure field indicates that the mode is not configured (value 0, 1 or 2).<br><br>Note: If the USB-C device also supports USB4, Thunderbolt or DisplayPort or MHL, their notifications will take precedence, or suppress the notification for this unrecognized Alternate Mode when any of these modes is configured. | (Same as the UCSI System case) |
| Mode | A user connects a Thunderbolt or DisplayPort USB-C device to a USB port that doesn't support Thunderbolt or DisplayPort, but the system supports Thunderbolt or DisplayPort on other USB ports. | Use different USB port<br><br>The USB device might have limited functionality when connected to this port. Plug the device into a different USB port on your PC. | 1. In response to UCSI command GET_ALTERNATE_MODES(Recipient=Connector) for each connector, UCSI PPM returns with a list of the Alternate Mode that is supported of a connector.<br>2. When the USB-C device is connected, in response to UCSI command GET_ALTERNATE_MODES(Recipient=SOP), UCSI PPM returns a list of the Alternate Modes supported by the USB-C device.<br>3. This notification is triggered when the above UCSI PPM returns indicate all of the following.<br>a. A USB-C device supports Thunderblot or DisployPort mode.<br>b. The connected USB-C connector does not support Thunderbolt or DisplayPort Altearnate Mode.<br>c. There's another USB-C connector that supports Thunderbolt or Displaymode Alternate Mode. | Not Implemented |
| Mode | A user connects a USB-C Analog Audio Adapter to a host device that only supports USB-C Digital Audio Adapters | Unsupported USB-C audio adapter<br><br>Connect a USB-C digital audio adapter instead. Select this message for more troubleshooting info. | 1. In response to UCSI command GET_CONNECTOR_CAPABILITY for a connector, UCSI PPM returns the following to indicate that audio accessory mode is not supported on this connector.<br><br>-  OperationMode.AudioAccessoryMode = 0<br><br>2. After the user connects a USB-C Analog Audio Adapter, in response to UCSI command GET_CONNECTOR_STATUS, UCSI PPM returns the following to indicate an analog audio adapter is connected.<br><br>-  ConnectorPartnerType.AudioAdapterAccessoryAttached = 1 | 1. The UcmCx client driver calls UcmConnectorCreate with the following parameter.<br><br>-  Config-&gt;TypeCConfig.AudioAccessoryCapable = FALSE<br><br>2. After the user connects a USB-C Analog Audio Adapter, the UcmCx client driver calls UcmConnectorTypeCAttach to report Type-C attach with the following paramete to indicate it supports "USB-C Analog Audio Adapter,"<br><br>-  Params-&gt;Partner-&gt;UcmTypeCPartnerAudioAccessory.<br> |

## Related topics

- [Windows support for USB Type-C connectors](oem-tasks-for-bringing-up-a-usb-typec.md)
- [Hardware design: USB Type-C systems](hardware-design-of-a-usb-type-c-system.md)
- [OEM tasks for USB Type-C systems](oem-tasks-for-usb-type-c-systems-running-windows.md)
- [USBTypeCCharging](/windows-hardware/test/hlk/testref/7f445d97-75e5-4a47-bbe2-dd191228ef44)
- [UCSI specification](https://www.intel.com/content/www/us/en/products/docs/io/universal-serial-bus/usb-type-c-ucsi-spec.html)
