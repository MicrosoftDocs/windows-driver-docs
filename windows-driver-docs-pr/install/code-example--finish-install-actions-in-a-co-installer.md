---
title: Code Example Finish-Install Actions in a Co-installer
description: Code Example Finish-Install Actions in a Co-installer
ms.assetid: 57d41fec-cedb-436e-858e-c010a8bd6506
keywords: ["finish-install actions WDK device installations", "co-installers WDK device installations , finish-install actions"]
---

# Code Example: Finish-Install Actions in a Co-installer


In this example, a co-installer performs the following operations to support finish-install actions:

-   When the co-installer receives a [**DIF\_NEWDEVICEWIZARD\_FINISHINSTALL**](https://msdn.microsoft.com/library/windows/hardware/ff543702) request, it calls the installer-supplied function *FinishInstallActionsNeeded* to determine whether there are finish-install actions to perform. (The code for the *FinishInstallActionsNeeded* function is not shown in this example).

    If *FinishInstallActionsNeeded* returns **TRUE**, the co-installer calls [**SetupDiGetDeviceInstallParams**](https://msdn.microsoft.com/library/windows/hardware/ff551104) to retrieve the device installation parameters for the device and then calls [**SetupDiSetDeviceInstallParams**](https://msdn.microsoft.com/library/windows/hardware/ff552141) to set the **FlagsEx** member of the [**SP\_DEVINSTALL\_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346) structure for the device with the DI\_FLAGSEX\_FINISHINSTALL\_ACTION flag. Setting this flag causes Windows to send a [**DIF\_FINISHINSTALL\_ACTION**](https://msdn.microsoft.com/library/windows/hardware/ff543684) request to all class installers, class co-installers, and device co-installers that are involved in the installation of this device. This request is sent after all installation operations, except the finish-install actions, have completed.

-   When the co-installer receives a DIF\_FINISHINSTALL\_ACTION request, the co-installer again calls *FinishInstallActionsNeeded* to determine whether it has finish-install actions to perform and, if so, performs the finish-install actions. The co-installer notifies the user that finish-install actions are in progress and waits for the finish-install actions to complete before returning from processing the DIF\_FINISHINSTALL\_ACTION request.

-   If the finish-install actions succeed, the co-installer notifies the user that finish-install actions succeeded.

-   If the finish-install actions required a system restart to complete the finish-install actions, the co-installer calls SetupDiGetDeviceInstallParams to retrieve the device installation parameters for the device and then calls SetupDiSetDeviceInstallParams to set the **Flags** member of the SP\_DEVINSTALL\_PARAMS structure for the device with the DI\_NEEDREBOOT flag. The installer also notifies the user that a system restart is required.

-   If the finish-install actions fail and the finish-install actions should be attempted again the next time the device is enumerated, the co-installer notifies the user of this situation.

    **Note**  Starting in Windows 8 a finish-install action is only run once. Windows will not automatically run it again, especially not the next time the device is enumerated because that is not when finish-install actions are run.

     

-   If the finish-install actions fail and the co-installer determines that the finish-install actions cannot succeed, the co-installer notifies the user of this situation.

-   By default, the co-installer returns NO\_ERROR in response to a DIF\_FINISHINSTALL\_ACTION request if the finish-install actions succeeded, or if the finish-install actions failed and the co-installer determine that the finish-install actions should not be attempted again. The co-installer returns a Win32 error code only if the finish-install actions fail and the finish-install actions should be attempted again the next time the device is enumerated in the context of an administrator.

    **Note**  Starting in Windows 8 a finish-install action is only run once. Windows will not automatically run it again, especially not the next time the device is enumerated because that is not when finish-install actions are run.

     

The following co-installer code example shows the basic structure of co-installer code that implements finish-install actions:

```
DWORD CALLBACK
SampleCoInstaller(
  IN DI_FUNCTION  InstallFunction,
  IN HDEVINFO  DeviceInfoSet,
  IN PSP_DEVINFO_DATA  DeviceInfoData,
  IN OUT PCOINSTALLER_CONTEXT_DATA  Context
  )
{
  SP_DEVINSTALL_PARAMS DeviceInstallParams;
  DWORD ReturnValue = NO_ERROR; // The default return value

  switch(InstallFunction)
  {
    case DIF_NEWDEVICEWIZARD_FINISHINSTALL:
      //
      // Processing for finish-install wizard pages
      //
      // Processing for finish-install actions
      if (FinishInstallActionsNeeded())
      {
        // Obtain the device install parameters for the device
        // and set the DI_FLAGSEX_FINISHINSTALL_ACTION flag
        DeviceInstallParams.cbSize = sizeof(DeviceInstallParams);
        if (SetupDiGetDeviceInstallParams(DeviceInfoSet, DeviceInfoData, &amp;DeviceInstallParams))
        {
          DeviceInstallParams.FlagsEx |= DI_FLAGSEX_FINISHINSTALL_ACTION;
          SetupDiSetDeviceInstallParams(DeviceInfoSet, DeviceInfoData, &amp;DeviceInstallParams);
        }
      }
      break;

    case DIF_FINISHINSTALL_ACTION:
      if (FinishInstallActionsNeeded())
      {
        //
        // Perform the finish-install actions,
        // notify the user that finish install actions
        // are in progress and wait for
        // the finish-install actions to complete
        //
        // If the finish-install actions succeed, notify the user
        //
        // If the finish install actions require a system restart: 
        // notify the user, call SetupDiGetDeviceInstallParams 
        // to obtain the device install parameters for the device in 
        // DeviceInstallParams, and call SetupDiSetInstallParams to set 
        // the DI_NEEDREBOOT flag in DeviceInstallParams.Flags
        // 
        // If the finish install actions failed, but
        // should be attempted again: clean up,
        // notify the user of the failure, and
        // set ReturnValue to an appropriate Win32 error code
        //
        // If the finish install actions failed and 
        // should not be attempted again: clean up
        // and notify the user of the failure
        //
        // Starting with Windows 8, a finish-install action
        // is only run once. Windows will not automatically
        // run it again, especially not the next time
        // the device is enumerated because that is not when
        // finish-install actions are run.
        //
      }
      break;
  }

  return ReturnValue;
}
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Code%20Example:%20Finish-Install%20Actions%20in%20a%20Co-installer%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




