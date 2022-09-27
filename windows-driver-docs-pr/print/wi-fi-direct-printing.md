---
title: Wi-Fi Direct printing
description: Windows 8.1 and later versions support printing over Wi-Fi Direct (WFD).
ms.date: 09/09/2022
---

# Wi-Fi Direct printing

Windows 8.1 and later versions support printing over Wi-Fi Direct (WFD).

Print devices implementing Windows Wi-Fi Direct support for printing must implement the following:

- Wi-Fi Direct vertical pairing

- Matching Container ID's for all logical devices in the physical device

- WSD/WS-Print

Definitions used in this topic and its subtopics:

| Term | Description |
|--|--|
| WFD | Wi-Fi Direct |
| DAF | Device Association Framework |
| DAS | Device Association Service |
| GO | Group Owner |
| PBC | Push-Button Connect |

General information about Wi-Fi Direct printing support is described in the [Wi-Fi Direct printing overview](wfd-overview.md). See [Wi-Fi Direct printing implementation](wfd-implementation.md) for details about how to implement Wi-Fi Direct Printing.

## Certification requirements

No new certification requirements are associated with this feature. See [Related documents](#related-documents) below, for applicable existing requirements.

## HCK Requirements

Devices must have Wi-Fi Alliance Certification for Wi-Fi Direct if implemented.

All existing certification requirements for print devices apply including requirement to run applicable HCK tests across all available transports. Partners should always refer to the official certification requirements documents published by the Windows Certification team in case there are any changes.

> [!NOTE]
> The Wi-Fi Alliance certification requirement is for Wi-Fi Direct. Wi-Fi Alliance Wi-Fi Direct Services is a separate specification and is not supported in Windows at this time.

## Related documents

[Overview of Container IDs](../install/overview-of-container-ids.md)

[PnP-X: Plug and Play extensions for Windows specification](/previous-versions/gg463082(v=msdn.10))

[Wi-Fi Alliance - Wi-Fi Direct industry whitepaper](https://www.wi-fi.org)
