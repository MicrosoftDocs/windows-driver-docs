---
title: WDI Property OIDs
description: This section contains WDI property OIDs.
ms.assetid: 1B1B54B8-6CE4-4C17-AAF8-7394210B09E8
ms.date: 07/18/2017
ms.localizationpriority: medium
---

# WDI Property OIDs


This section contains WDI property OIDs.

The Wi-Fi Driver Interface (WDI) object identifiers (OIDs) apply only to miniport drivers that implement WDI.

The following table specifies whether WDI OID query (Q), set (S), and NDIS 6.0 method (M) requests are required or optional to implement:

<a href="" id="r"></a>**R**  
Indicates that support for the object is required. The miniport driver must not fail set or query requests for the object by returning the status code NDIS\_STATUS\_NOT\_SUPPORTED from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

<a href="" id="o"></a>**O**  
Indicates that support for the object is optional. The miniport driver can either support query or set requests for the object, or the driver can fail the request by returning NDIS\_STATUS\_NOT\_SUPPORTED from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

| Name                                                                                                | Q   | S   | M   |
|-----------------------------------------------------------------------------------------------------|-----|-----|-----|
| [OID\_WDI\_ABORT\_TASK](oid-wdi-abort-task.md)                                                     |     |     | R   |
| [OID\_WDI\_GET\_ADAPTER\_CAPABILITIES](oid-wdi-get-adapter-capabilities.md)                        |     |     | R   |
| [OID\_WDI\_GET\_AUTO\_POWER\_SAVE](oid-wdi-get-auto-power-save.md)                                 |     |     | R   |
| [OID\_WDI\_GET\_BSS\_ENTRY\_LIST](oid-wdi-get-bss-entry-list.md)                                   |     |     | O   |
| [OID\_WDI\_GET\_NEXT\_ACTION\_FRAME\_DIALOG\_TOKEN](oid-wdi-get-next-action-frame-dialog-token.md) |     |     | O   |
| [OID\_WDI\_GET\_PM\_PROTOCOL\_OFFLOAD](oid-wdi-get-pm-protocol-offload.md)                         |     |     | O   |
| [OID\_WDI\_GET\_RECEIVE\_COALESCING\_MATCH\_COUNT](oid-wdi-get-receive-coalescing-match-count.md)  |     |     | O   |
| [OID\_WDI\_GET\_STATISTICS](oid-wdi-get-statistics.md)                                             |     |     | R   |
| [OID\_WDI\_IHV\_REQUEST](oid-wdi-ihv-request.md)                                                   |     |     | O   |
| [OID\_WDI\_SET\_ADAPTER\_CONFIGURATION](oid-wdi-set-adapter-configuration.md)                      |     |     | R   |
| [OID\_WDI\_SET\_ADD\_CIPHER\_KEYS](oid-wdi-set-add-cipher-keys.md)                                 |     |     | R   |
| [OID\_WDI\_SET\_ADD\_PM\_PROTOCOL\_OFFLOAD](oid-wdi-set-add-pm-protocol-offload.md)                |     |     | O   |
| [OID\_WDI\_SET\_ADD\_WOL\_PATTERN](oid-wdi-set-add-wol-pattern.md)                                 |     |     | O   |
| [OID\_WDI\_SET\_ADVERTISEMENT\_INFORMATION](oid-wdi-set-advertisement-information.md)              |     |     | O   |
| [OID\_WDI\_SET\_ASSOCIATION\_PARAMETERS](oid-wdi-set-association-parameters.md)                    |     |     | R   |
| [OID\_WDI\_SET\_CLEAR\_RECEIVE\_COALESCING](oid-wdi-set-clear-receive-coalescing.md)               |     |     | O   |
| [OID\_WDI\_SET\_CONNECTION\_QUALITY](oid-wdi-set-connection-quality.md)                            |     |     | R   |
| [OID\_WDI\_SET\_DEFAULT\_KEY\_ID](oid-wdi-set-default-key-id.md)                                   |     |     | R   |
| [OID\_WDI\_SET\_DELETE\_CIPHER\_KEYS](oid-wdi-set-delete-cipher-keys.md)                           |     |     | R   |
| [OID\_WDI\_SET\_ENCAPSULATION\_OFFLOAD](oid-wdi-set-encapsulation-offload.md)                      |     |     | O   |
| [OID\_WDI\_SET\_FLUSH\_BSS\_ENTRY](oid-wdi-set-flush-bss-entry.md)                                 |     |     | O   |
| [OID\_WDI\_SET\_MULTICAST\_LIST](oid-wdi-set-multicast-list.md)                                    |     |     | R   |
| [OID\_WDI\_SET\_NETWORK\_LIST\_OFFLOAD](oid-wdi-set-network-list-offload.md)                       |     |     | O   |
| [OID\_WDI\_SET\_P2P\_LISTEN\_STATE](oid-wdi-set-p2p-listen-state.md)                               |     |     | O   |
| [OID\_WDI\_SET\_P2P\_START\_BACKGROUND\_DISCOVERY](oid-wdi-set-p2p-start-background-discovery.md)  |     |     | O   |
| [OID\_WDI\_SET\_P2P\_STOP\_BACKGROUND\_DISCOVERY](oid-wdi-set-p2p-stop-background-discovery.md)    |     |     | O   |
| [OID\_WDI\_SET\_P2P\_WPS\_ENABLED](oid-wdi-set-p2p-wps-enabled.md)                                 |     |     | O   |
| [OID\_WDI\_SET\_POWER\_STATE](oid-wdi-set-power-state.md)                                          |     |     | R   |
| [OID\_WDI\_SET\_PRIVACY\_EXEMPTION\_LIST](oid-wdi-set-privacy-exemption-list.md)                   |     |     | R   |
| [OID\_WDI\_SET\_RECEIVE\_COALESCING](oid-wdi-set-receive-coalescing.md)                            |     |     | O   |
| [OID\_WDI\_SET\_RECEIVE\_PACKET\_FILTER](oid-wdi-set-receive-packet-filter.md)                     |     |     | R   |
| [OID\_WDI\_SET\_REMOVE\_PM\_PROTOCOL\_OFFLOAD](oid-wdi-set-remove-pm-protocol-offload.md)          |     |     | O   |
| [OID\_WDI\_SET\_REMOVE\_WOL\_PATTERN](oid-wdi-set-remove-wol-pattern.md)                           |     |     | O   |
| [OID\_WDI\_SET\_TCP\_OFFLOAD\_PARAMETERS](oid-wdi-set-tcp-offload-parameters.md)                   |     |     | O   |
| [OID\_WDI\_TCP\_RSC\_STATISTICS](oid-wdi-tcp-rsc-statistics.md)                                    |     |     | O   |

 

 

 




