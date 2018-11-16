---
Description: BIOS/UEFI testing validates USB boot and handoff of the controller to the operating system.
title: BIOS/UEFI testing with the MUTT devices
ms.date: 04/20/2017
ms.localizationpriority: medium
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



