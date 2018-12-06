---
title: CoNDIS TAPI Initialization
description: CoNDIS TAPI Initialization
ms.assetid: eabb2038-ab64-4f48-8c94-e47d1139727b
keywords:
- CoNDIS WAN drivers WDK networking , TAPI services
- telephonic services WDK WAN , initiliazing
- CoNDIS TAPI WDK networking , initializing
- initializing CoNDIS TAPI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# CoNDIS TAPI Initialization





This section discusses how a CoNDIS WAN miniport driver enumerates its TAPI capabilities for applications. These TAPI capabilities consist of:

-   Number of line devices the miniport driver supports--line devices include, for example, a modem, a fax board, and an ISDN card.

-   Information for specific lines--line information includes, for example, a line identifier and the number of channel addresses (telephone numbers) the line supports for simultaneous transmission of voice and data.

-   Information for specific channel addresses on lines of devices--address information includes, for example, the identity of a caller (Caller ID) and the number of active calls possible.

To retrieve information about underlying hardware, NDPROXY issues requests for line and channel-address capabilities. That is, the NDPROXY driver queries the TAPI capabilities of a CoNDIS WAN miniport driver. The NDPROXY driver calls the [**NdisCoOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561711) function to query the TAPI capabilities of the miniport driver. In this call, NDPROXY passes an NDIS\_OID\_REQUEST structure. NDPROXY specifies the following in NDIS\_OID\_REQUEST:

-   **NdisRequestQueryInformation** value in the **RequestType** member

-   Object identifier (OID) that specifies the TAPI capability to retrieve from the miniport driver in the **Oid** member

-   Buffer to hold the TAPI-capability information that is returned in the **InformationBuffer** member

All queries sent to a CoNDIS WAN miniport driver by the NDPROXY driver can be completed either synchronously or asynchronously. If a CoNDIS WAN miniport driver determines that it cannot complete the query immediately, then it can simply return NDIS\_STATUS\_PENDING and call the [**NdisMCmOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563551) function from within its *ProtocolCoOidRequest* function when it has completed the query.

After a CoNDIS WAN miniport driver notifies NDPROXY about the registration of a new address family as specified in [CoNDIS TAPI Registration](condis-tapi-registration.md), NDPROXY queries the following OIDs to determine the TAPI-specific capabilities of the CoNDIS WAN miniport driver and the miniport driver's NIC.

-   NDPROXY queries the miniport driver with [OID\_CO\_TAPI\_CM\_CAPS](https://msdn.microsoft.com/library/windows/hardware/ff569096) to determine the number of lines supported by the miniport driver's device (the device for which it provides TAPI services). This OID also requests the miniport driver to indicate whether these lines have dissimilar line capabilities.

-   NDPROXY next queries the miniport driver with [OID\_CO\_TAPI\_LINE\_CAPS](https://msdn.microsoft.com/library/windows/hardware/ff569098) to determine the telephony capabilities for the specified line. This OID also requests the miniport driver to indicate whether addresses on this line have dissimilar address capabilities.
    -   If the previous query of OID\_CO\_TAPI\_CM\_CAPS indicated that the miniport driver's device supports only one line, or if the device supports multiple lines that have the same line capabilities, NDPROXY has to query OID\_CO\_TAPI\_LINE\_CAPS only once to obtain the line capabilities of the device. In this case, the line capabilities returned by the miniport driver apply to all lines on the device.
    -   If the device supports multiple lines with dissimilar line capabilities, NDPROXY must query OID\_CO\_TAPI\_LINE\_CAPS once for each line to obtain the line capabilities of each line.
-   Finally, NDPROXY queries the miniport driver with [OID\_CO\_TAPI\_ADDRESS\_CAPS](https://msdn.microsoft.com/library/windows/hardware/ff569095) to determine the telephony capabilities for a specified address on a specified line.
    -   If the previous query of OID\_CO\_TAPI\_LINE\_CAPS indicated that the line supports only one address or that all addresses on the line have the same address capabilities, NDPROXY queries OID\_CO\_TAPI\_ADDRESS\_CAPS only once to determine the capabilities of all the addresses on the line.
    -   If a line supports multiple addresses that have dissimilar capabilities, NDPROXY queries OID\_CO\_TAPI\_ADDRESS\_CAPS once for each address on the line.

The NDPROXY driver uses the information obtained with the TAPI enumeration OIDs to do the following:

-   Create TAPI parameters for subsequent TAPI calls.

-   Determine whether to accept or reject subsequent incoming TAPI calls.

-   Register one or more TAPI service access points (SAPs) on which to receive subsequent incoming TAPI calls.

 

 





