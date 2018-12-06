---
title: Proximity Profile Implementation Details
description: To achieve a power-efficient design, device implementations must observe specific requirements to ensure that they remain compatible with Windows.
ms.assetid: 0FFDF345-EA14-4564-AA8A-7E44E9DB28DA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Proximity Profile Implementation Details


To achieve a power-efficient design, device implementations must observe specific requirements to ensure that they remain compatible with Windows.

The following subtopics examine device-side requirements to enable efficient use of power, as well as describe a technique by which the connection state can be monitored.

## <span id="Establishing_a_Connection"></span><span id="establishing_a_connection"></span><span id="ESTABLISHING_A_CONNECTION"></span>Establishing a Connection


Windows 8.1 will automatically connect to a device when an application has a registered a handler for the GattCharacteristic.ValueChanged event. However the basic definition of the services included in the Proximity Profile does not contain any indicatable or notifiable characteristics. A device can add a service that contains an indicatable or notifiable characteristic to the services included in the Proximity Profile. This means that a proximity device must support at least one indicatable or notifiable characteristic value and an application must register at least one handler to a GattCharacteristic.ValueChanged event for the connection to be automatically established.

## <span id="Detecting_Loss_of_Connection"></span><span id="detecting_loss_of_connection"></span><span id="DETECTING_LOSS_OF_CONNECTION"></span>Detecting Loss of Connection


As mentioned in [Bluetooth Proximity Profile](bluetooth-proximity-profile.md), Windows 8.1 does not expose the RSSI value of Bluetooth connections. Consequently, apps cannot use the RSSI value to calculate the connection path loss. Instead, we recommend that a device tie its proximity to the link loss event.

## <span id="Monitoring_the_connection_state"></span><span id="monitoring_the_connection_state"></span><span id="MONITORING_THE_CONNECTION_STATE"></span>Monitoring the connection state


Apps can monitor the connection state of GATT devices by using a PnpObjectWatcher and monitor the PnP "Connected" property of the service Device Object. This technique is demonstrated in the [Bluetooth Generic Attribute Profile - Heart Rate Service](http://go.microsoft.com/fwlink/p/?linkid=301978) sample.

 

 





