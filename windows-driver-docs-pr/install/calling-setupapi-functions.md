---
title: Calling SetupAPI Functions
description: Calling SetupAPI Functions
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

Default [device installation function (DIF) code](/previous-versions//ff541307(v=vs.85)) handler functions perform system-defined default operations for certain DIF codes. As described in [Handling DIF Codes](handling-dif-codes.md), [**SetupDiCallClassInstaller**](/windows/win32/api/setupapi/nf-setupapi-setupdicallclassinstaller) calls the default handler for a DIF request after the *co-installer* has first processed the DIF request, but before **SetupDiCallClassInstaller** calls the co-installers that registered for post-processing of the request.

[Co-installers](writing-a-co-installer.md) and [device installation applications](writing-a-device-installation-application.md) must not call the default DIF code handler functions. Direct calls to these handler functions bypass all registered co-installers and could invalidate any internal device state that these installers store.

The following table lists the DIF codes that have default DIF code handler functions.

| DIF code                                                             | Default DIF code handler function                                                  |
|----------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [**DIF_PROPERTYCHANGE**](./dif-propertychange.md)                | [**SetupDiChangeState**](/windows/win32/api/setupapi/nf-setupapi-setupdichangestate)                               |
| [**DIF_FINISHINSTALL_ACTION**](./dif-finishinstall-action.md)   | [**SetupDiFinishInstallAction**](/previous-versions/windows/hardware/previsioning-framework/ff551022(v=vs.85))               |
| [**DIF_INSTALLDEVICE**](./dif-installdevice.md)                  | [**SetupDiInstallDevice**](/windows/win32/api/setupapi/nf-setupapi-setupdiinstalldevice)                           |
| [**DIF_INSTALLINTERFACES**](./dif-installinterfaces.md)          | [**SetupDiInstallDeviceInterfaces**](/windows/win32/api/setupapi/nf-setupapi-setupdiinstalldeviceinterfaces)       |
| [**DIF_INSTALLDEVICEFILES**](./dif-installdevicefiles.md)        | [**SetupDiInstallDriverFiles**](/windows/win32/api/setupapi/nf-setupapi-setupdiinstalldriverfiles)                 |
| [**DIF_REGISTER_COINSTALLERS**](./dif-register-coinstallers.md) | [**SetupDiRegisterCoDeviceInstallers**](/windows/win32/api/setupapi/nf-setupapi-setupdiregistercodeviceinstallers) |
| [**DIF_REGISTERDEVICE**](./dif-registerdevice.md)                | [**SetupDiRegisterDeviceInfo**](/windows/win32/api/setupapi/nf-setupapi-setupdiregisterdeviceinfo)                 |
| [**DIF_REMOVE**](./dif-remove.md)                                | [**SetupDiRemoveDevice**](/windows/win32/api/setupapi/nf-setupapi-setupdiremovedevice)                             |
| [**DIF_SELECTBESTCOMPATDRV**](./dif-selectbestcompatdrv.md)      | [**SetupDiSelectBestCompatDrv**](/windows/win32/api/setupapi/nf-setupapi-setupdiselectbestcompatdrv)               |
| [**DIF_SELECTDEVICE**](./dif-selectdevice.md)                    | [**SetupDiSelectDevice**](/windows/win32/api/setupapi/nf-setupapi-setupdiselectdevice)                             |
| [**DIF_UNREMOVE**](./dif-unremove.md)                            | [**SetupDiUnremoveDevice**](/windows/win32/api/setupapi/nf-setupapi-setupdiunremovedevice)                         |

 

