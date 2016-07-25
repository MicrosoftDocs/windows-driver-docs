---
title: Calling SetupAPI Functions
description: Calling SetupAPI Functions
ms.assetid: 757AAF33-B57B-4ab8-A034-23B8AC0C5CB3
keywords: ["SetupAPI functions WDK , calling", "calling SetupAPI functions WDK"]
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

    **Note**  Class installers and co-installers are prohibited from calling **SetupScanFileQueue** only when the SPQ\_SCAN\_PRUNE\_COPY\_QUEUE flag is set in the *Flags* parameter.

     

### <a href="" id="calling-the-default-dif-code-handler-functions"></a>Rules for calling the default DIF code handler functions

Default [device installation function (DIF) code](https://msdn.microsoft.com/library/windows/hardware/ff541307) handler functions perform system-defined default operations for certain DIF codes. As described in [Handling DIF Codes](handling-dif-codes.md), [**SetupDiCallClassInstaller**](https://msdn.microsoft.com/library/windows/hardware/ff550922) calls the default handler for a DIF request after the [*co-installer*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-co-installer) has first processed the DIF request, but before **SetupDiCallClassInstaller** calls the co-installers that registered for post-processing of the request.

[Co-installers](writing-a-co-installer.md) and [device installation applications](writing-a-device-installation-application.md) must not call the default DIF code handler functions. Direct calls to these handler functions bypass all registered co-installers and could invalidate any internal device state that these installers store.

The following table lists the DIF codes that have default DIF code handler functions.

| DIF code                                                             | Default DIF code handler function                                                  |
|----------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [**DIF\_PROPERTYCHANGE**](https://msdn.microsoft.com/library/windows/hardware/ff543712)                | [**SetupDiChangeState**](https://msdn.microsoft.com/library/windows/hardware/ff550930)                               |
| [**DIF\_FINISHINSTALL\_ACTION**](https://msdn.microsoft.com/library/windows/hardware/ff543684)   | [**SetupDiFinishInstallAction**](https://msdn.microsoft.com/library/windows/hardware/ff551022)               |
| [**DIF\_INSTALLDEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff543692)                  | [**SetupDiInstallDevice**](https://msdn.microsoft.com/library/windows/hardware/ff552039)                           |
| [**DIF\_INSTALLINTERFACES**](https://msdn.microsoft.com/library/windows/hardware/ff543695)          | [**SetupDiInstallDeviceInterfaces**](https://msdn.microsoft.com/library/windows/hardware/ff552043)       |
| [**DIF\_INSTALLDEVICEFILES**](https://msdn.microsoft.com/library/windows/hardware/ff543694)        | [**SetupDiInstallDriverFiles**](https://msdn.microsoft.com/library/windows/hardware/ff552048)                 |
| [**DIF\_REGISTER\_COINSTALLERS**](https://msdn.microsoft.com/library/windows/hardware/ff543715) | [**SetupDiRegisterCoDeviceInstallers**](https://msdn.microsoft.com/library/windows/hardware/ff552085) |
| [**DIF\_REGISTERDEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff543713)                | [**SetupDiRegisterDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff552091)                 |
| [**DIF\_REMOVE**](https://msdn.microsoft.com/library/windows/hardware/ff543717)                                | [**SetupDiRemoveDevice**](https://msdn.microsoft.com/library/windows/hardware/ff552097)                             |
| [**DIF\_SELECTBESTCOMPATDRV**](https://msdn.microsoft.com/library/windows/hardware/ff543719)      | [**SetupDiSelectBestCompatDrv**](https://msdn.microsoft.com/library/windows/hardware/ff552112)               |
| [**DIF\_SELECTDEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff543723)                    | [**SetupDiSelectDevice**](https://msdn.microsoft.com/library/windows/hardware/ff552115)                             |
| [**DIF\_UNREMOVE**](https://msdn.microsoft.com/library/windows/hardware/ff543728)                            | [**SetupDiUnremoveDevice**](https://msdn.microsoft.com/library/windows/hardware/ff552193)                         |

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Calling%20SetupAPI%20Functions%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




