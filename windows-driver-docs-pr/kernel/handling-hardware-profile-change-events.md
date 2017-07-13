---
title: Handling Hardware Profile Change Events
author: windows-driver-content
description: Handling Hardware Profile Change Events
ms.assetid: ddb0f740-9b31-4ede-be84-c1f6eb60fb1a
keywords: ["notifications WDK PnP , hardware profile changes", "hardware profile change notifications WDK PnP", "EventCategoryHardwareProfileChange notification", "profile change notifications WDK PnP", "machine hardware profile change notifications WDK PnP"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Handling Hardware Profile Change Events


## <a href="" id="ddk-handling-hardware-profile-change-events-kg"></a>


At specific times during a hardware profile change, the PnP manager calls notification callback routines that registered for **EventCategoryHardwareProfileChange**:

-   Before there is a change in the machine's hardware profile, the PnP manager calls registered notification callback routines and specifies a *NotificationStructure*.**Event** of GUID\_HWPROFILE\_QUERY\_CHANGE.

-   After the machine's hardware profile change is complete, the PnP manager calls registered notification callback routines and specifies a *NotificationStructure*.**Event** of GUID\_HWPROFILE\_CHANGE\_COMPLETE.

-   If the machine's hardware profile change is canceled, the PnP manager calls registered notification callback routines and specifies a *NotificationStructure*.**Event** of GUID\_HWPROFILE\_CHANGE\_CANCELLED.

For a GUID\_HWPROFILE\_QUERY\_CHANGE event the PnP manager calls user-mode callback routines and then calls kernel-mode callback routines. In response to a GUID\_HWPROFILE\_QUERY\_CHANGE event, a driver's notification callback routine typically just returns STATUS\_SUCCESS.

For a GUID\_HWPROFILE\_CHANGE\_COMPLETE event the PnP manager calls kernel-mode callback routines and then calls user-mode callback routines. In response to such an event, a driver's callback routine might refresh its hardware-profile-specific settings.

For a GUID\_HWPROFILE\_CHANGE\_CANCELLED event the PnP manager calls kernel-mode callback routines and then user-mode routines. In response to such an event, a driver's callback routine typically just returns STATUS\_SUCCESS. If the driver performed any operations in response to the GUID\_HWPROFILE\_QUERY\_CHANGE event, the driver would undo those operations in response to the cancellation event.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Handling%20Hardware%20Profile%20Change%20Events%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


