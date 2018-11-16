---
title: Cellular COM API capabilities
description: This topic provides information on cellular COM API capabilities.
ms.assetid: f6172f25-9003-4b98-a87d-26dc193d40e3
keywords:
- Cellular COM API capabilities network drivers
ms.date: 11/07/2017
ms.localizationpriority: medium
---

# Cellular COM API capabilities

> [!WARNING]
> The Cellular COM API is deprecated in Windows 10. This content is provided to support maintenance of OEM and mobile operator created Windows Phone 8.1 applications.

To allow the cellular APIs to execute, capabilities must be added to the package file that contains the cellular application. For each method that your application calls, include the required capability.

All cellular COM interface methods require the ID_CAP_CELL_API_COMMON capability. Additional capability requirements are as follows:

| Method | Capabilities in addition to ID_CAP_CELL_API_COMMON |
| --- | --- |
| IOemCellularModem::SendModemOpaqueCommand | ID_CAP_CELL_API_OEM_PASSTHROUGH | 
| IOemCellularModem::RegisterForOpaqueModemNotifications | ID_CAP_CELL_API_OEM_PASSTHROUGH |
| IOemCellularModem::UnRegisterForOpaqueModemNotifications | ID_CAP_CELL_API_OEM_PASSTHROUGH |
| IOemCellularModem::SetRFState | ID_CAP_CELL_API_OEM_PASSTHROUGH | 
| IOemCellularModem::GetRFState | ID_CAP_CELL_API_OEM_PASSTHROUGH |
| IOemCan::GetPositionInfo | ID_CAP_CELL_API_LOCATION |
| IOemUiccApp::GetAppId | ID_CAP_CELL_API_UICC |
| IOemUiccApp::GetType | ID_CAP_CELL_API_UICC |
| IOemUiccApp::GetPinLockState | ID_CAP_CELL_API_UICC |
| IOemUiccApp::ReadRecord | ID_CAP_CELL_API_UICC, ID_CAP_CELL_API_UICC_LOWLEVEL |
| IOemUiccApp::WriteRecord | ID_CAP_CELL_API_UICC, ID_CAP_CELL_API_UICC_LOWLEVEL |
| IOemUiccApp::GetRecordStatusOnFilePath | ID_CAP_CELL_API_UICC |
| IOemUiccApp::ReadRecordOnFilePath | ID_CAP_CELL_API_UICC, ID_CAP_CELL_API_UICC_LOWLEVEL |
| IOemUiccApp::WriteRecordOnFilePath | ID_CAP_CELL_API_UICC, ID_CAP_CELL_API_UICC_LOWLEVEL |
| IOemUiccApp::GetIMSI | ID_CAP_CELL_API_UICC |
| IOemUiccApp::GetSIDNID | ID_CAP_CELL_API_UICC, ID_CAP_CELL_API_UICC_LOWLEVEL |
| IOemUiccApp::GetSubscriberNumbers | ID_CAP_CELL_API_UICC |
| IOemUiccAppEx2::GetNAI | ID_CAP_CELL_API_UICC |

## Related topics

[Cellular COM API design guide](cellular-com-api-design-guide.md)

[Cellular COM API reference](https://msdn.microsoft.com/library/windows/hardware/dn946508)

