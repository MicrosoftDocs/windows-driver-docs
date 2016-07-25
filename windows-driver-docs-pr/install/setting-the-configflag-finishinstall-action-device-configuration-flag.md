---
title: Marking a Device as having a Finish-Install Action to Perform
description: Marking a Device as having a Finish-Install Action to Perform
ms.assetid: 7f2560e6-94a7-4dd0-aa2a-e6cdd96c6d9b
---

# Marking a Device as having a Finish-Install Action to Perform


An *installer* (a class installer, class co-installer, or device co-installer) indicates to Windows that it has finish-install actions to perform by setting the DI\_FLAGSEX\_FINISHINSTALL\_ACTION flag when the installer processes a [**DIF\_NEWDEVICEWIZARD\_FINISHINSTALL**](https://msdn.microsoft.com/library/windows/hardware/ff543702) request. This action will cause Windows to flag the device as needing to perform a finish install action. The steps are as follows:

1.  When an installer receives a [**DIF\_NEWDEVICEWIZARD\_FINISHINSTALL**](https://msdn.microsoft.com/library/windows/hardware/ff543702) request, the installer sets the DI\_FLAGSEX\_FINISHINSTALL\_ACTION flag if it has finish-install actions to perform.

    The installer then returns one of the following error codes:

    -   ERROR\_DI\_DO\_DEFAULT if the installer is a class installer that has no finish-install wizard pages.
    -   NO\_ERROR if the installer is a class installer that has finish-install wizard pages or a co-installer that either has or does not have finish-install wizard pages.

2.  If the DI\_FLAGSEX\_FINISHINSTALL\_ACTION flag is set for a device after all installers have processed the [**DIF\_NEWDEVICEWIZARD\_FINISHINSTALL**](https://msdn.microsoft.com/library/windows/hardware/ff543702) request for the device, Windows flags the device as needing to perform a finish install action.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Marking%20a%20Device%20as%20having%20a%20Finish-Install%20Action%20to%20Perform%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




