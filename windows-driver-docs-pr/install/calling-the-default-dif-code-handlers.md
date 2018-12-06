---
title: Calling the Default DIF Code Handlers
description: Calling the Default DIF Code Handlers
ms.assetid: bc168c30-2269-4760-bc0a-e3e6ee3ce720
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Calling the Default DIF Code Handlers


Default DIF code handlers perform system-defined default operations for [DIF codes](https://msdn.microsoft.com/library/windows/hardware/ff541307). As described in [Handling DIF Codes](handling-dif-codes.md), [**SetupDiCallClassInstaller**](https://msdn.microsoft.com/library/windows/hardware/ff550922) calls the default handler for a DIF request after the [*class installer*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-class-installer) and [*co-installer*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-co-installer) have first processed the DIF request, but before **SetupDiCallClassInstaller** recalls the co-installers that registered for post-processing of the request.

**Note**  The operation of **SetupDiCallClassInstaller** cannot be configured to recall the class installer to post-process a DIF request.

 

In those situations where a [*class installer*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-class-installer) must perform operations for a DIF request after the default handler is called, the class installer must directly call the default handler when it processes the DIF request, as follows:

1.  Perform operations that must be done before calling the default handler.

2.  Call the default handler to perform the default operations.

    **Note**   The class installer must not attempt to supersede the operation of the default handler.

     

3.  Perform the operations that must be done after the default handler returns.

4.  Return NO_ERROR if the class installer successfully completed processing the DIF request or return a Win32 error if the processing failed.

**Important**  [Co-installers](writing-a-co-installer.md) and [device installation applications](writing-a-device-installation-application.md) must not call the default DIF code handlers.

 

For an example of a situation where this method must be used, see the information about calling the default handler [**SetupDiInstallDevice**](https://msdn.microsoft.com/library/windows/hardware/ff552039) on the [**DIF_INSTALLDEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff543692) request reference page.

The following table lists the DIF codes that have default handlers.

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

 

 

 





