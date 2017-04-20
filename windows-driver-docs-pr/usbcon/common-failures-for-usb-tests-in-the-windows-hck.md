---
Description: Common failures for USB tests in the Windows HCK.
title: Common failures for USB tests in the Windows HCK
author: windows-driver-content
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Common failures for USB tests in the Windows HCK


Common failures for USB tests in the Windows HCK.

## DevFund tests for USB


-   Error condition: Device Status Check fails with an error indicating that the MUTT device is not present.

    1.  SuperMUTT is running Winusb.sys or Usbtcd.sys as the driver. You can get the driver and the driver installation package files by installing the [MUTT Software Package](http://msdn.microsoft.com/windows/hardware/jj590752). For more information, see [Tools in the MUTT software package](mutt-software-package.md).
    2.  Make sure that Device manager shows the hardware ID of the SuperMUTT as "USB\\VID\_045E&PID\_078F".
        **Note**  PID\_078E is incorrect.

         

    3.  Make sure that Device manager (**View &gt; Devices by connection**) shows the SuperMUTT enumerated downstream of an xHCI controller.
    4.  In USBView, make sure that the SuperMUTT device is operating at SuperSpeed.
        **Note**  You can install USBView from the I**nstall Debugging Tools for Windows package** in the Microsoft Windows Software Development Kit (SDK). Alternatively, USBView is installed in the Debuggers folder in the Windows Driver Kit (WDK).

         

    5.  Make sure that MUTT firmware is up-to-date. From an elevated prompt run "muttutil -updatefirmware" in the directory where you installed the [MUTT Software Package](http://msdn.microsoft.com/windows/hardware/jj590752).

    If the issue persists, report the problem with these attachments:

    -   Screenshots of Device Manager and USBView showing items 1-4 in the preceding list.
    -   The output of the [MuttUtil](muttutil.md) command.
-   Error condition: DevFund fails during a simple I/O transfer.
    1.  In HCK Studio, select the **Optional** test level.
    2.  Run the **Diagnosability - Tracing Jobs - USB - Start USB trace collection** test.
    3.  Run the **System - Sleep and PNP (disable and enable) with IO Before and After (Certification)** test.
    4.  Run the **Diagnosability - Tracing Jobs - USB - Stop USB trace collection** test.
    5.  Attach all contents of %SystemDrive%\\USB\_Traces with your bug.
    6.  Save and attach the .hckx file for the preceding tests.
-   Error condition: The MUTT device is connected to the system but the correct drivers are not installed.

    Most likely driver installation failed or the device does not have the latest firmware. Install Winusb.sys or Usbtcd.sys as the driver. You can get the driver and the driver installation package files by installing the [MUTT Software Package](http://msdn.microsoft.com/windows/hardware/jj590752).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Common%20failures%20for%20USB%20tests%20in%20the%20Windows%20HCK%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


