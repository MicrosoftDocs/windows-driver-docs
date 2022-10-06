---
title: Proximity Profile implementation details
description: To achieve a power-efficient design, device implementations must observe specific requirements to ensure that they remain compatible with Windows.
ms.date: 10/06/2022
---

# Proximity Profile implementation details

To achieve a power-efficient design, device implementations must observe specific requirements to ensure that they remain compatible with Windows.

The following subtopics examine device-side requirements to enable efficient use of power, as well as describe a technique by which the connection state can be monitored.

## Establishing a connection

Windows automatically connects to a device when an application has a registered a handler for the GattCharacteristic.ValueChanged event. However, the basic definition of the services included in the Proximity Profile does not contain any indicative or notifiable characteristics. A device can add a service that contains an indicative or notifiable characteristic to the services included in the Proximity Profile. This means that a proximity device must support at least one indicative or notifiable characteristic value and an application must register at least one handler to a GattCharacteristic.ValueChanged event for the connection to be automatically established.

## Detecting loss of connection

As mentioned in [Bluetooth Proximity Profile](bluetooth-proximity-profile.md), Windows 8.1 does not expose the RSSI value of Bluetooth connections. Consequently, apps cannot use the RSSI value to calculate the connection path loss. Instead, we recommend that a device tie its proximity to the link loss event.

## Monitoring the connection state

Apps can monitor the connection state of GATT devices by using a PnpObjectWatcher and monitor the PnP "Connected" property of the service device object.
