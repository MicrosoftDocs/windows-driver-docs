---
Description: BIOS/UEFI testing validates USB boot and handoff of the controller to the operating system.
MS-HAID: buses.how\_to\_run\_bios\_uefi\_testing\_with\_the\_mutt\_device
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: BIOS/UEFI testing with the MUTT devices
---

# BIOS/UEFI testing with the MUTT devices


BIOS/UEFI testing validates USB boot and handoff of the controller to the operating system.

## USB boot configurations


Perform these tests on both USB 2.0 (EHCI) and USB 3.0 (xHCI) controllers with each of the primary USB media types (USB 2.0 BOT, USB 3.0 BOT, and USB 3.0 UASP, and USB DVD).

An expected result for each scenario is one of the following events:

-   When the user enters the correct key sequence, the attached keyboard allows the user to enter configuration mode (BIOS / UEFI configuration).
-   Boot from the USB device when the key sequence has not been pressed.

These scenarios assume that BIOS /UEFI is configured to boot from USB. Each of the attached USB storage devices is been formatted with a Windows recognized file system.

-   USB boot scenario 1 – USB 3.0 Hub

    ![usb 3.0 hub](images/fig16-usb-bootbehind30hub.png)

-   USB boot scenario 2 – USB 2.0 Hub

    ![usb 2.0 hub](images/fig17-usb-bootbehind20hub.png)

-   USB boot scenario 3 – Root port

    ![boot root port](images/fig18-usb-bootrootport.png)

## Non-USB boot configurations


In this scenario, it is assumed there is either no USB bootable media that is attached to the system or the BIOS/UEFI is configured to not boot from USB. Entering into configuration mode by using an attached USB keyboard / mouse is an expected scenario that is not listed here.

![usb controller handoff](images/fig19-usb-controllerhandoff.png)

Expected results for this scenario are that the SuperMUTT Pack and MUTT Pack are functional and operational after booting into the operating system and running the standard MUTT tests. After test devices are validated, the system should perform each of the supported system power states (S3, S4, and so on) and validate that the MUTT test devices remain functional after each system resume. Run MUTT tests after each resume event.

## Related topics


[USB](https://msdn.microsoft.com/library/windows/hardware/ff538930)

[Microsoft USB Test Tool (MUTT) devices](microsoft-usb-test-tool--mutt--devices.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20BIOS/UEFI%20testing%20with%20the%20MUTT%20devices%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




