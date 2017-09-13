---
title: WDI Property OIDs
author: windows-driver-content
description: This section contains WDI property OIDs.
ms.assetid: 1B1B54B8-6CE4-4C17-AAF8-7394210B09E8
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
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

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI%20Property%20OIDs%20%20RELEASE:%20%286/30/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


