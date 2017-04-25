---
title: Ending a Debugging Session in KD
description: Ending a Debugging Session in KD
ms.assetid: 6CD39971-424D-4F29-9A36-CCD14187DEB0
---

# Ending a Debugging Session in KD


There are two different ways to exit KD.

-   Issue a [**q (Quit)**](https://msdn.microsoft.com/library/windows/hardware/ff553507) command in KD to save the log file, end the debugging session, and exit the debugger. The target computer remains locked.

-   Press [**CTRL+B**](https://msdn.microsoft.com/library/windows/hardware/ff540308) and then press ENTER to end the debugger abruptly. If you want the target computer to continue to run after the debugger is ended, you must use this method. Because CTRL+B does not remove breakpoints, you should use the following commands first.

    ``` syntax
    kd>  bc *
    kd>  g
    ```

Exiting the debugger by using CTRL+B does not clear kernel-mode breakpoints, but attaching a new kernel debugger does clear these breakpoints.

When you are performing remote debugging, [**q**](https://msdn.microsoft.com/library/windows/hardware/ff553507) ends the debugging session. CTRL+B exits the debugger but leaves the session active. This situation enables another debugger to connect to the session.

If the [**q (Quit)**](https://msdn.microsoft.com/library/windows/hardware/ff553507) command does not work, press [**CTRL+R**](https://msdn.microsoft.com/library/windows/hardware/ff540337) and then press ENTER on the host computer's keyboard, and then retry the **q** command. If this procedure does not work, you must use CTRL+B to exit the debugger.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Ending%20a%20Debugging%20Session%20in%20KD%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




