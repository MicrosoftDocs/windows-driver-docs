---
title: Handling Hardware Profile Change Events
description: Handling Hardware Profile Change Events
ms.assetid: ddb0f740-9b31-4ede-be84-c1f6eb60fb1a
keywords: ["notifications WDK PnP , hardware profile changes", "hardware profile change notifications WDK PnP", "EventCategoryHardwareProfileChange notification", "profile change notifications WDK PnP", "machine hardware profile change notifications WDK PnP"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Handling Hardware Profile Change Events





At specific times during a hardware profile change, the PnP manager calls notification callback routines that registered for **EventCategoryHardwareProfileChange**:

-   Before there is a change in the machine's hardware profile, the PnP manager calls registered notification callback routines and specifies a *NotificationStructure*.**Event** of GUID\_HWPROFILE\_QUERY\_CHANGE.

-   After the machine's hardware profile change is complete, the PnP manager calls registered notification callback routines and specifies a *NotificationStructure*.**Event** of GUID\_HWPROFILE\_CHANGE\_COMPLETE.

-   If the machine's hardware profile change is canceled, the PnP manager calls registered notification callback routines and specifies a *NotificationStructure*.**Event** of GUID\_HWPROFILE\_CHANGE\_CANCELLED.

For a GUID\_HWPROFILE\_QUERY\_CHANGE event the PnP manager calls user-mode callback routines and then calls kernel-mode callback routines. In response to a GUID\_HWPROFILE\_QUERY\_CHANGE event, a driver's notification callback routine typically just returns STATUS\_SUCCESS.

For a GUID\_HWPROFILE\_CHANGE\_COMPLETE event the PnP manager calls kernel-mode callback routines and then calls user-mode callback routines. In response to such an event, a driver's callback routine might refresh its hardware-profile-specific settings.

For a GUID\_HWPROFILE\_CHANGE\_CANCELLED event the PnP manager calls kernel-mode callback routines and then user-mode routines. In response to such an event, a driver's callback routine typically just returns STATUS\_SUCCESS. If the driver performed any operations in response to the GUID\_HWPROFILE\_QUERY\_CHANGE event, the driver would undo those operations in response to the cancellation event.

 

 




