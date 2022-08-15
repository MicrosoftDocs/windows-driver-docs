---
title: NDIS Interface for 5G Data Class Support
description: NDIS Interface for 5G Data Class Support
keywords:
- NDIS Interface for 5G Data Class Support
ms.date: 03/01/2021
ms.custom: 19H1
---

# NDIS Interface for 5G Data Class Support

NDIS supports a revision number in the NDIS_HEADER. This permits adding new members to an OID message, which NDIS uses the optional service caps table in [OID_WWAN_DEVICE_CAPS_EX](oid-wwan-device-caps-ex.md).

The following NDIS OIDs and their data structures have been updated for 5G data class support.

- [OID_WWAN_DEVICE_CAPS_EX](oid-wwan-device-caps-ex.md)
- [OID_WWAN_REGISTER_STATE](oid-wwan-register-state.md)
- [OID_WWAN_PACKET_SERVICE](oid-wwan-packet-service.md)
- [OID_WWAN_SIGNAL_STATE](oid-wwan-signal-state.md)

The equivalent MBIM CID messages for these OIDs are described in [MBIMEx 2.0 – 5G NSA support](mbimex-2.0-5g-nsa-support.md).
