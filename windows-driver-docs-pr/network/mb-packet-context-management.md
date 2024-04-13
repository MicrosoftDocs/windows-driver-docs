---
title: MB Packet Context Management
description: MB Packet Context Management
ms.date: 04/20/2017
ms.custom: UpdateFrequency3
---

# MB Packet Context Management


This topic describes the management of packet contexts, which are a specific set of network configuration parameters for setting up a *virtual circuit* or *flow* on top of the physical MB connection at layer 2. In GSM-based devices, this corresponds to the concept of a Packet Data Protocol (PDP). In CDMA-based devices, this corresponds to a network profile.

In most cases, the detailed settings of a packet context are either pre-provisioned by IHVs and/or network providers of the MB device, or provisioned through the network over-the-air (OTA) or using SMS. In either case, the end user is generally not required to provide most of the settings (for example, quality of service (QoS), security codes, mobile IP, and so on). However, the end user may need to provide the network access string, username, and password. It is these user configurable settings that constitute the content of a packet context from the perspective of the MB Service.

The MB driver model does not provide an explicit OID to set up or tear down the layer-2 connection for WWAN. Instead, activating the first packet context results in setting up the underlying layer-2 connection and deactivating the last packet context will effectively tear down the underlying layer-2 connection.

The MB driver model builds on these two constraints regarding the number of active packet contexts at any given time in the following manner:

1.  Each packet context can be activated only one time.

2.  Only a single packet context can be activated at any given time.

It is mandatory that any miniport driver that conforms to the MB driver model sets the **MaxActivatedContexts** member of the [**WWAN\_DEVICE\_CAPS**](/windows-hardware/drivers/ddi/wwan/ns-wwan-_wwan_device_caps) structure to one, when responding to [OID\_WWAN\_DEVICE\_CAPS](./oid-wwan-device-caps.md) query requests. Even if a miniport driver sets this value to be greater than one, the MB Service ensures that, at most, only one packet context is activated at any given time.

Because each packet context can be activated no more than one time, a static packet context identifier can be used to identify the virtual circuit after being activated. The use of this static identifier is still valid as long as the first constraint still holds.

For more information about packet context management, see [OID\_WWAN\_PROVISIONED\_CONTEXTS](./oid-wwan-provisioned-contexts.md) and [OID\_WWAN\_CONNECT](./oid-wwan-connect.md).

 

