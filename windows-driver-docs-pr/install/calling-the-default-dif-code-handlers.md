---
title: Calling the Default DIF Code Handlers
description: Calling the Default DIF Code Handlers
ms.assetid: bc168c30-2269-4760-bc0a-e3e6ee3ce720
---

# Calling the Default DIF Code Handlers


Default DIF code handlers perform system-defined default operations for [DIF codes](https://msdn.microsoft.com/library/windows/hardware/ff541307). As described in [Handling DIF Codes](handling-dif-codes.md), [**SetupDiCallClassInstaller**](https://msdn.microsoft.com/library/windows/hardware/ff550922) calls the default handler for a DIF request after the [*class installer*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-class-installer) and [*co-installer*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-co-installer) have first processed the DIF request, but before **SetupDiCallClassInstaller** recalls the co-installers that registered for post-processing of the request.

**Note**  The operation of **SetupDiCallClassInstaller** cannot be configured to recall the class installer to post-process a DIF request.

 

In those situations where a [*class installer*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-class-installer) must perform operations for a DIF request after the default handler is called, the class installer must directly call the default handler when it processes the DIF request, as follows:

1.  Perform operations that must be done before calling the default handler.

2.  Call the default handler to perform the default operations.

    **Note**   The class installer must not attempt to supersede the operation of the default handler.

     

3.  Perform the operations that must be done after the default handler returns.

4.  Return NO\_ERROR if the class installer successfully completed processing the DIF request or return a Win32 error if the processing failed.

**Important**  [Co-installers](writing-a-co-installer.md) and [device installation applications](writing-a-device-installation-application.md) must not call the default DIF code handlers.

 

For an example of a situation where this method must be used, see the information about calling the default handler [**SetupDiInstallDevice**](https://msdn.microsoft.com/library/windows/hardware/ff552039) on the [**DIF\_INSTALLDEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff543692) request reference page.

The following table lists the DIF codes that have default handlers.

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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Calling%20the%20Default%20DIF%20Code%20Handlers%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




