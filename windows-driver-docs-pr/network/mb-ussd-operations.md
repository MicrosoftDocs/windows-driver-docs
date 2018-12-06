---
title: MB USSD Operations
ms.assetid: 49D106BD-F938-4BF8-88EE-A4D0F0E2722A
description: Describes the operations to send and receive messages using the Unstructured Supplementary Service Data (USSD) capabilities of an MB device
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MB USSD Operations


This topic describes the operations to send and receive messages using the Unstructured Supplementary Service Data (USSD) capabilities of an MB device.

USSD support is optional and when supported is only available on GSM networks. Miniport drivers that support USSD must set the WWAN\_CTRL\_CAPS\_USSD capability flag as part of the **WwanControlCaps** member of the [**WWAN\_DEVICE\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/ff571204) structure when processing [OID\_WWAN\_DEVICE\_CAPS](https://msdn.microsoft.com/library/windows/hardware/ff569824) requests. If miniport drivers do not support USSD, they must not set this flag and should return WWAN\_STATUS\_NO\_DEVICE\_SUPPORT for all USSD-related OIDs.

The MB driver model supports the following USSD operations: Device initiated operations:

-   Sending a USSD message on a newly created USSD session

-   Sending a USSD message on a newly created USSD session

-   Sending a USSD message on an existing USSD session

-   Terminating the USSD session

For more information on device initiated operations, see [OID\_WWAN\_USSD](https://msdn.microsoft.com/library/windows/hardware/hh440100).

Network initiated operations:

-   Receiving a USSD message on a newly created USSD session

-   Receiving a USSD message on an existing USSD session

-   Termination the USSD session

For more information on network initiated operations, see [**NDIS\_STATUS\_WWAN\_USSD**](https://msdn.microsoft.com/library/windows/hardware/hh439822).

The USSD protocol only allows a single USSD session at any time. For device initiated operations, the **RequestType** member of the [**WWAN\_USSD\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/hh464138) structure indicates the purpose of the request OID:

-   **WwanUssdRequestInitiate** is used to create a new USSD session and send the provided USSD string to the network. If a USSD session already exists, the driver must fail the request with an event of type **WwanUssdEventOtherLocalClient**. A USSD string must be present. For example, the length must be between 1 and 160 bytes.

-   **WwanUssdRequestContinue** is used to send a USSD string on an existing session. A USSD string must be present. For example, the length must be between 1 and 160 bytes.

-   **WwanUssdRequestCancel** is used to terminate the existing session. The driver must respond with an event of type **WwanUssdEventTerminated**, even if no session existed (which may happen during a concurrent release of the session from the network and the local client). The content of the USSD string must be ignored for this request; the string length is set to zero to indicate that there is no USSD string.

For network initiated operations, the **EventType** member of the [**WWAN\_USSD\_EVENT**](https://msdn.microsoft.com/library/windows/hardware/hh464136) structure indicates the high level purpose of the indication:

-   The event **WwanUssdEventNoActionRequired** is used for network initiated USSD notifications, or when no further information is needed after a mobile initiated operation. The event **WwanUssdEventActionRequired** is used for network initiated USSD requests, or when further information is needed after a mobile initiated operation. Both events require a non-empty USSD string to be present. The **SessionState** member is used to indicate if the USSD string is the first message of a USSD session; it must be set to **WwanUssdSessionStateNew** for the first message of a network initiated USSD session and to **WwanUssdSessionStateExisting** in all other cases.

-   The event **WwanUssdEventActionRequired** also indicates that the session is still open. All other events indicate that the session has been closed.

-   The events **WwanUssdEventNoActionRequired** and **WwanUssdEventActionRequired** are the only events that contain a USSD string. All other events must set the USSD string length to 0 to indicate that the string is absent. The value of the **SessionState** member is ignored if no string is present.

-   The event **WwanUssdEventTerminated** is used to indicate that the USSD session has been terminated.

-   The event **WwanUssdEventOtherLocalClient** is used to indicate that a new USSD session cannot be established because there is already a session opened. This includes sessions that are invisible to the MB stack such as a USSD session termination in the SIM.

-   The event **WwanUssdEventOperationNotSupported** is used to indicate that the previous request is not supported by the driver or device.

-   The event **WwanUssdEventNetworkTimeOut** is used to indicate that the session was closed due to a session timeout either by the network or locally. The driver or device is responsible for timing out an inactive USSD session after an implementation specific timeout.

 

 





