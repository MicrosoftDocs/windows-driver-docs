---
title: Hotspot 2.0
description: Hotspot 2.0
ms.date: 04/20/2017
---

# Hotspot 2.0

Hotspot 2.0 is a standard for seamless authentication to hotspots. Hotspot 2.0 offers an encrypted connection between the client and the access point. It uses IEEE 802.11u to communicate with the provider before it establishes a connection. Authentication and encryption are provided by using WPA2-Enterprise together with one of several EAP methods.

The following table describes common credential types that are defined by Hotspot 2.0:

|Credential|EAP method|EAP method supported|User can enter credentials|Operator can provision credentials|
|----|----|----|----|----|
|Username and password|EAP-TTLS|Yes|Yes|No|
|Certificate|EAP-TTLS|Yes|Yes|No|
|SIM|EAP-SIM or EAP-AKA|Yes|Yes|Yes|

\*User can select from certificates or the SIM is already present on the system.

Windows 8 and Windows 8.1 do not support the discovery or online sign-up portions of Hotspot 2.0, but they do support WPA2-Enterprise and all EAP methods that are required by the Hotspot 2.0 specification. Therefore, Windows 8 and Windows 8.1 can connect to a Hotspot 2.0 network when the user already has credentials.

Because Windows 8 and Windows 8.1 do not support 802.11u discovery, operators must provision Windows 8 or Windows 8.1 with wireless profiles that contain the applicable SSIDs for their networks.

Windows 10 fully supports Hotspot 2.0 Release 1, including discovery and profile creation.
