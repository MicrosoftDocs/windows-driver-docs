---
title: Calling SetupAPI Functions
description: Calling SetupAPI Functions
ms.assetid: 757AAF33-B57B-4ab8-A034-23B8AC0C5CB3
keywords:
- SetupAPI functions WDK , calling
- calling SetupAPI functions WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Calling SetupAPI Functions


This section provides guidelines that you should follow when you call the [SetupAPI](setupapi.md) functions from a [co-installer](writing-a-co-installer.md) or a [device installation application](writing-a-device-installation-application.md).

-   [Rules for calling SetupAPI functions](#calling-setupapi-functions)
-   [Rules for calling the default DIF code handler functions](#calling-the-default-dif-code-handler-functions)

### <a href="" id="calling-setupapi-functions"></a>Rules for calling SetupAPI functions

Class installers and co-installers must not call the following [SetupAPI](setupapi.md) functions:

-   **SetupQueueCopy**

-   **SetupQueueCopyIndirect**

-   **SetupQueueCopySection**

-   **SetupQueueDefaultCopy**

-   **SetupQueueDelete**

-   **SetupQueueDeleteSection**

-   **SetupQueueRename**

-   **SetupQueueRenameSection**

-   **SetupScanFileQueue**

    **Note**  Class installers and co-installers are prohibited from calling **SetupScanFileQueue** only when the SPQ_SCAN_PRUNE_COPY_QUEUE flag is set in the *Flags* parameter.

     

### <a href="" id="calling-the-default-dif-code-handler-functions"></a>Rules for calling the default DIF code handler functions

Default [device installation function (DIF) code](https://msdn.microsoft.com/library/windows/hardware/ff541307) handler functions perform system-defined default operations for certain DIF codes. As described in [Handling DIF Codes](handling-dif-codes.md), [**SetupDiCallClassInstaller**](https://msdn.microsoft.com/library/windows/hardware/ff550922) calls the default handler for a DIF request after the [*co-installer*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-co-installer) has first processed the DIF request, but before **SetupDiCallClassInstaller** calls the co-installers that registered for post-processing of the request.

[Co-installers](writing-a-co-installer.md) and [device installation applications](writing-a-device-installation-application.md) must not call the default DIF code handler functions. Direct calls to these handler functions bypass all registered co-installers and could invalidate any internal device state that these installers store.

The following table lists the DIF codes that have default DIF code handler functions.

| DIF code                                                             | Default DIF code handler function                                                  |
|----------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [**DIF_PROPERTYCHANGE**](https://msdn.microsoft.com/library/windows/hardware/ff543712)                | [**SetupDiChangeState**](https://msdn.microsoft.com/library/windows/hardware/ff550930)                               |
| [**DIF_FINISHINSTALL_ACTION**](https://msdn.microsoft.com/library/windows/hardware/ff543684)   | [**SetupDiFinishInstallAction**](https://msdn.microsoft.com/library/windows/hardware/ff551022)               |
| [**DIF_INSTALLDEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff543692)                  | [**SetupDiInstallDevice**](https://msdn.microsoft.com/library/windows/hardware/ff552039)                           |
| [**DIF_INSTALLINTERFACES**](https://msdn.microsoft.com/library/windows/hardware/ff543695)          | [**SetupDiInstallDeviceInterfaces**](https://msdn.microsoft.com/library/windows/hardware/ff552043)       |
| [**DIF_INSTALLDEVICEFILES**](https://msdn.microsoft.com/library/windows/hardware/ff543694)        | [**SetupDiInstallDriverFiles**](https://msdn.microsoft.com/library/windows/hardware/ff552048)                 |
| [**DIF_REGISTER_COINSTALLERS**](https://msdn.microsoft.com/library/windows/hardware/ff543715) | [**SetupDiRegisterCoDeviceInstallers**](https://msdn.microsoft.com/library/windows/hardware/ff552085) |
| [**DIF_REGISTERDEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff543713)                | [**SetupDiRegisterDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff552091)                 |
| [**DIF_REMOVE**](https://msdn.microsoft.com/library/windows/hardware/ff543717)                                | [**SetupDiRemoveDevice**](https://msdn.microsoft.com/library/windows/hardware/ff552097)                             |
| [**DIF_SELECTBESTCOMPATDRV**](https://msdn.microsoft.com/library/windows/hardware/ff543719)      | [**SetupDiSelectBestCompatDrv**](https://msdn.microsoft.com/library/windows/hardware/ff552112)               |
| [**DIF_SELECTDEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff543723)                    | [**SetupDiSelectDevice**](https://msdn.microsoft.com/library/windows/hardware/ff552115)                             |
| [**DIF_UNREMOVE**](https://msdn.microsoft.com/library/windows/hardware/ff543728)                            | [**SetupDiUnremoveDevice**](https://msdn.microsoft.com/library/windows/hardware/ff552193)                         |

 

 

 





