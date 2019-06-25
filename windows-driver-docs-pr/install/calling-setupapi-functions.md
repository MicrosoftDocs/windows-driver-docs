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

Default device installation function (DIF) code has first processed the DIF request, but before **SetupDiCallClassInstaller** calls the co-installers that registered for post-processing of the request.

[Co-installers](writing-a-co-installer.md) and [device installation applications](writing-a-device-installation-application.md) must not call the default DIF code handler functions. Direct calls to these handler functions bypass all registered co-installers and could invalidate any internal device state that these installers store.

The following table lists the DIF codes that have default DIF code handler functions.

| DIF code                                                             | Default DIF code handler function                                                  |
|----------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [**DIF_PROPERTYCHANGE**](https://docs.microsoft.com/windows-hardware/drivers/install/dif-propertychange)                | [**SetupDiChangeState**](https://docs.microsoft.com/windows/desktop/api/setupapi/nf-setupapi-setupdichangestate)                               |
| [**DIF_FINISHINSTALL_ACTION**](https://docs.microsoft.com/windows-hardware/drivers/install/dif-finishinstall-action)   | [**SetupDiFinishInstallAction**](https://docs.microsoft.com/previous-versions/windows/hardware/previsioning-framework/ff551022(v=vs.85))               |
| [**DIF_INSTALLDEVICE**](https://docs.microsoft.com/windows-hardware/drivers/install/dif-installdevice)                  | [**SetupDiInstallDevice**](https://docs.microsoft.com/windows/desktop/api/setupapi/nf-setupapi-setupdiinstalldevice)                           |
| [**DIF_INSTALLINTERFACES**](https://docs.microsoft.com/windows-hardware/drivers/install/dif-installinterfaces)          | [**SetupDiInstallDeviceInterfaces**](https://docs.microsoft.com/windows/desktop/api/setupapi/nf-setupapi-setupdiinstalldeviceinterfaces)       |
| [**DIF_INSTALLDEVICEFILES**](https://docs.microsoft.com/windows-hardware/drivers/install/dif-installdevicefiles)        | [**SetupDiInstallDriverFiles**](https://docs.microsoft.com/windows/desktop/api/setupapi/nf-setupapi-setupdiinstalldriverfiles)                 |
| [**DIF_REGISTER_COINSTALLERS**](https://docs.microsoft.com/windows-hardware/drivers/install/dif-register-coinstallers) | [**SetupDiRegisterCoDeviceInstallers**](https://docs.microsoft.com/windows/desktop/api/setupapi/nf-setupapi-setupdiregistercodeviceinstallers) |
| [**DIF_REGISTERDEVICE**](https://docs.microsoft.com/windows-hardware/drivers/install/dif-registerdevice)                | [**SetupDiRegisterDeviceInfo**](https://docs.microsoft.com/windows/desktop/api/setupapi/nf-setupapi-setupdiregisterdeviceinfo)                 |
| [**DIF_REMOVE**](https://docs.microsoft.com/windows-hardware/drivers/install/dif-remove)                                | [**SetupDiRemoveDevice**](https://docs.microsoft.com/windows/desktop/api/setupapi/nf-setupapi-setupdiremovedevice)                             |
| [**DIF_SELECTBESTCOMPATDRV**](https://docs.microsoft.com/windows-hardware/drivers/install/dif-selectbestcompatdrv)      | [**SetupDiSelectBestCompatDrv**](https://docs.microsoft.com/windows/desktop/api/setupapi/nf-setupapi-setupdiselectbestcompatdrv)               |
| [**DIF_SELECTDEVICE**](https://docs.microsoft.com/windows-hardware/drivers/install/dif-selectdevice)                    | [**SetupDiSelectDevice**](https://docs.microsoft.com/windows/desktop/api/setupapi/nf-setupapi-setupdiselectdevice)                             |
| [**DIF_UNREMOVE**](https://docs.microsoft.com/windows-hardware/drivers/install/dif-unremove)                            | [**SetupDiUnremoveDevice**](https://docs.microsoft.com/windows/desktop/api/setupapi/nf-setupapi-setupdiunremovedevice)                         |

 

 

 





