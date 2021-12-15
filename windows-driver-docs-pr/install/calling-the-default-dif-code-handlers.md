---
title: Calling the Default DIF Code Handlers
description: Calling the Default DIF Code Handlers
ms.date: 04/20/2017
---

# Calling the Default DIF Code Handlers


Default DIF code handlers perform system-defined default operations for [DIF codes](/previous-versions//ff541307(v=vs.85)). As described in [Handling DIF Codes](handling-dif-codes.md), [**SetupDiCallClassInstaller**](/windows/win32/api/setupapi/nf-setupapi-setupdicallclassinstaller) calls the default handler for a DIF request after the *class installer* and *co-installer* have first processed the DIF request, but before **SetupDiCallClassInstaller** recalls the co-installers that registered for post-processing of the request.

**Note**  The operation of **SetupDiCallClassInstaller** cannot be configured to recall the class installer to post-process a DIF request.

 

In those situations where a *class installer* must perform operations for a DIF request after the default handler is called, the class installer must directly call the default handler when it processes the DIF request, as follows:

1.  Perform operations that must be done before calling the default handler.

2.  Call the default handler to perform the default operations.

    **Note**   The class installer must not attempt to supersede the operation of the default handler.

     

3.  Perform the operations that must be done after the default handler returns.

4.  Return NO_ERROR if the class installer successfully completed processing the DIF request or return a Win32 error if the processing failed.

**Important**  [Co-installers](writing-a-co-installer.md) and [device installation applications](writing-a-device-installation-application.md) must not call the default DIF code handlers.

 

For an example of a situation where this method must be used, see the information about calling the default handler [**SetupDiInstallDevice**](/windows/win32/api/setupapi/nf-setupapi-setupdiinstalldevice) on the [**DIF_INSTALLDEVICE**](./dif-installdevice.md) request reference page.

The following table lists the DIF codes that have default handlers.

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

 

