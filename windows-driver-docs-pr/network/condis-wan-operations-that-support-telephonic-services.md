---
title: CoNDIS WAN Operations that Support Telephonic Services
description: CoNDIS WAN Operations that Support Telephonic Services
keywords:
- CoNDIS WAN drivers WDK networking , telephonic services
- telephonic services WDK WAN
- NDPROXY WDK networking
- CoNDIS TAPI WDK networking
- telephonic services WDK WAN , about telephonic services
- WAN miniport drivers WDK networking , telephonic services
- TAPI WDK networking
ms.date: 03/02/2023
---

# CoNDIS WAN Operations that Support Telephonic Services





This section describes how CoNDIS WAN miniport drivers implement telephonic services using NDIS functions in a connection-oriented environment. CoNDIS WAN miniport drivers communicate through NDIS with the NDPROXY and NDISWAN drivers. The NDPROXY driver communicates with telephony applications through a telephony service provider. For more information, see the [Telephony Application Programming Interface (TAPI)](/windows/win32/tapi/telephony-application-programming-interfaces).

The following topics describe the NDPROXY driver more fully. These topics also describe how a CoNDIS WAN miniport driver registers and enumerates its TAPI capabilities, how it brings up lines, and how it sets up and closes calls that are initiated by TAPI requests:

[NDPROXY Overview](ndproxy-overview.md)

[CoNDIS TAPI Registration](condis-tapi-registration.md)

[CoNDIS TAPI Initialization](condis-tapi-initialization.md)

[Making Outgoing Calls](making-outgoing-calls.md)

[Accepting Incoming Calls](accepting-incoming-calls.md)

[CoNDIS TAPI Shutdown](condis-tapi-shutdown.md)

[Call Manager Requirements for Voice Streaming](responding-to-an-oid-co-tapi-line-caps-query.md)

[Non-WAN-Specific Extensions to Support Telephonic Services Over Connection-Oriented NDIS](non-wan-specific-extensions-to-support-telephonic-services-over-connec.md)

These descriptions briefly discuss the concepts embodied in TAPI, but the reader should consult the Windows SDK for details about TAPI. For more information about how TAPI models line devices and how all WAN miniport drivers should maintain the state of their connections, see [Line Devices, Addresses, and Calls (NDIS 5.1)](/previous-versions/windows/hardware/network/ff549181(v=vs.85)) and [Maintaining State Information (NDIS 5.1)](/previous-versions/windows/hardware/network/ff549232(v=vs.85)).

 

