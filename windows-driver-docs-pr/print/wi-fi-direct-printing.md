---
title: Wi-Fi Direct Printing
description: Windows 8.1 and later versions of Windows support printing over Wi-Fi Direct (WFD).
ms.assetid: B2FC1293-F9E4-43A4-84BF-21EF8C3D27E0
ms.date: 06/15/2020
ms.localizationpriority: medium
---

# Wi-Fi Direct Printing

Windows 8.1 and later versions of Windows support printing over Wi-Fi Direct (WFD).

Print devices implementing Windows Wi-Fi Direct support for printing must implement the following:

- Wi-Fi Direct Vertical Pairing

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

General information about Wi-Fi Direct Printing support is described in the [Wi-Fi Direct Printing Overview](wfd-overview.md). See [Wi-Fi Direct Printing Implementation](wfd-implementation.md) for details about how to implement Wi-Fi Direct Printing.

## Certification Requirements

No new certification requirements are associated with this feature. See [Related Documents](#related-documents) below, for applicable existing requirements.

## HCK Requirements

Devices must have Wi-Fi Alliance Certification for Wi-Fi Direct if implemented.

All existing Certification Requirements for Print devices apply including requirement to run applicable HCK tests across all available transports. Partners should always refer to the official Certification Requirements documents published by the Windows Certification team in case there are any changes.

> [!NOTE]
> The Wi-Fi Alliance Certification requirement is for Wi-Fi Direct. Wi-Fi Alliance Wi-Fi Direct Services is a separate specification and is not supported in Windows at this time.

## Related Documents

[Overview of Container IDs](https://docs.microsoft.com/windows-hardware/drivers/install/overview-of-container-ids)

[PnP-X: Plug and Play Extensions for Windows Specification](https://docs.microsoft.com/previous-versions/gg463082(v=msdn.10))

[Wi-Fi Alliance - Wi-Fi Direct Industry Whitepaper](https://www.wi-fi.org)
