---
Description: The Windows Hardware Certification Kit (HCK) tests can be used for additional testing of Systems, USB host controllers, hubs, and devices. 
title: Windows Hardware Certification Kit (HCK) Tests for USB
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Windows Hardware Certification Kit (HCK) Tests for USB


The Windows Hardware Certification Kit (HCK) tests can be used for additional testing of Systems, USB host controllers, hubs, and devices. These tests cover basic device functionality, reliability, and compatibility with Windows.

## Prerequisites


Before you start running the logo tests make sure you meet the following requirements:

-   To run these tests you will need at least two computers: a test server and a test client.
-   The test client must have the latest version of Windows.
-   The test client must have EHCI and xHCI controllers, either integrated or as add-in cards. The controllers must expose user-accessible root ports (no integrated hubs).
-   Download the Windows HCK to the test server from [Windows Hardware Certification Kit Downloads](http://go.microsoft.com/fwlink/p/?linkid=285647).

    For detailed information about how to install and use the Windows HCK, see [Windows HCK Getting Started](http://go.microsoft.com/fwlink/p/?linkid=316504).

## Hardware requirements for running USB tests in the HCK


To run the HCK tests, you need:

-   Your host controller (either integrated or as add-in cards), hubs, or device to certify.

    Open Device Manager on the test client and make sure that the USB controllers that you want to use expose user-accessible root ports (no integrated hubs).

    ![usb root port](images/roothubports.png)

-   USB-IF-compliant external SuperSpeed hub to evaluate system compatibility. We have tested HCK tests with these hubs:
    -   [Texas Instruments SuperSpeed (USB 3.0) Hub reference design board (TUSB8040EVM)](http://go.microsoft.com/fwlink/p/?linkid=248509).
    -   SuperMUTT Pack. See [MUTT devices](microsoft-usb-test-tool--mutt--devices.md).
-   [MUTT devices](microsoft-usb-test-tool--mutt--devices.md) as test devices for hub and controller tests.
-   USB-IF certified cables and connectors to avoid signal integrity issues. See [USB-IF list of products](http://go.microsoft.com/fwlink/p/?linkid=617502).

Complete set of requirements are given here:

-   [USB Bus Controller Testing Prerequisites](http://go.microsoft.com/fwlink/p/?linkid=617477)
-   [USB Hub.Connectivity Testing Prerequisites](http://go.microsoft.com/fwlink/p/?linkid=617499)

## HCK test selection for USB


The USB tests that apply to your system, host controller, hub, or device are automatically selected in HCK Studio.

After you follow steps 1-5 in [Windows HCK Getting Started]( http://go.microsoft.com/fwlink/p/?linkid=617479), make sure that:

-   In step 5,the correct device is selected in the **Selection** tab of HCK Studio.
-   In step 6, all the tests that apply to your device are displayed in the **Tests** tab in HCK studio. To run these tests, you must select the test in the left-hand check box and click **Run Selected**. The tests for USB testing are listed in the following section of this document.

For information about scheduling tests, see steps 2-6 in [Windows HCK Getting Started]( http://go.microsoft.com/fwlink/p/?linkid=617479).

## Recommended Windows HCK tests for systems


OEMs should run these tests before certifying their system. The test system must include SuperSpeed port(s).

For tests that are marked with **\***, a SuperMUTT can be connected to the xHCI controller(s). For tests that are marked with **+**, a SuperMUTT must be connected to the xHCI controller(s).

**Functional tests**

-   [System Fundamentals (SysFund)](http://go.microsoft.com/fwlink/p/?linkid=617454)
-   [USB Exposed Port System Test](http://go.microsoft.com/fwlink/p/?linkid=617482)\*
-   [USB Internal Device Idle](http://go.microsoft.com/fwlink/p/?linkid=617480)
-   [USB xHCI Register System Test](http://go.microsoft.com/fwlink/p/?linkid=617492)
-   [USB xHCI Transfer Speed Test](http://go.microsoft.com/fwlink/p/?linkid=617453)+
-   [USB3 Termination](http://go.microsoft.com/fwlink/p/?linkid=617498)\*

**Certification tests**

-   [System Fundamentals (SysFund)](http://go.microsoft.com/fwlink/p/?linkid=617454)
-   [USB Exposed Port System Test]( http://go.microsoft.com/fwlink/p/?linkid=617482)\*
-   [USB Internal Device Idle](http://go.microsoft.com/fwlink/p/?linkid=617480)
-   [USB xHCI Register System Test](http://go.microsoft.com/fwlink/p/?linkid=617492)
-   [USB xHCI Transfer Speed Test](http://go.microsoft.com/fwlink/p/?linkid=617453)+
-   [USB3 Termination](http://go.microsoft.com/fwlink/p/?linkid=617498)\*

For more information, see [Recommended USB tests for system development](usb-tests-for-system-development.md).

## Recommended Windows HCK tests for USB controllers


USB host controller manufacturers should run these tests to test their controllers before they are embedded into systems. USB 3.0 and xHCI tests are only applicable to xHCI controllers, USB 3.0 hubs, and devices. For more information about each test, see the individual test reference topics in [Device.Connectivity Tests](https://msdn.microsoft.com/library/windows/hardware/jj123606) and [System.Fundamentals Tests](https://msdn.microsoft.com/library/windows/hardware/hh998390).

For tests that are marked with **\***, a SuperMUTT can be connected to the controller. For more information about the SuperMUTT, see [MUTT devices](microsoft-usb-test-tool--mutt--devices.md).

**Functional tests**

-   [Device.Fundamentals Tests](http://go.microsoft.com/fwlink/p/?linkid=617463)
-   [USB Exposed Port Controller Test](http://go.microsoft.com/fwlink/p/?linkid=617456)\*
-   [USB Host Controller Compliance Test]( http://go.microsoft.com/fwlink/p/?linkid=617491)
-   [USB Host Controller Enable Disable Test](http://go.microsoft.com/fwlink/p/?linkid=617484)\*
-   [USB xHCI Compliance Suite (ARM)](http://go.microsoft.com/fwlink/p/?linkid=617452)
-   [USB xHCI Register Test](http://go.microsoft.com/fwlink/p/?linkid=617483)
-   [USB xHCI Runtime Power Management Test](http://go.microsoft.com/fwlink/p/?linkid=617462)\*

**Certification tests**

-   [Device.Fundamentals Tests](http://go.microsoft.com/fwlink/p/?linkid=617463)
-   [USB Exposed Port Controller Test](http://go.microsoft.com/fwlink/p/?linkid=617456)\*
-   [USB Host Controller Compliance Test]( http://go.microsoft.com/fwlink/p/?linkid=617491)
-   [USB Host Controller Enable Disable Test](http://go.microsoft.com/fwlink/p/?linkid=617484)\*
-   [USB xHCI Compliance Suite (ARM)](http://go.microsoft.com/fwlink/p/?linkid=617452)
-   [USB xHCI Register Test]( http://go.microsoft.com/fwlink/p/?linkid=617483)
-   [USB xHCI Runtime Power Management Test](http://go.microsoft.com/fwlink/p/?linkid=617462)\*
-   [USB USB-IF Certification Validation Test (Controller)](http://go.microsoft.com/fwlink/p/?linkid=617497)

## Recommended Windows HCK tests for USB hubs


USB hub manufacturers should run these tests before their hubs can be embedded on systems. USB host controller manufacturers should also run these tests if their host controllers that contain embedded hubs.

Hubs must be connected to the xHCI controller for all tests. The [USB Topology Compatibility Test](http://go.microsoft.com/fwlink/p/?linkid=617458) requires that the hub is plugged into the EHCI controller and that the hub is connected to the root port during the test. For all tests that are marked with **\***, a SuperMUTT can be connected to the hub.

**Functional tests**

-   [Device.Fundamentals Tests](http://go.microsoft.com/fwlink/p/?linkid=617463)
-   All USB tests listed under [Devices.Connectivity Tests](http://go.microsoft.com/fwlink/p/?linkid=617485)
-   [USB 3.0 Hub Enumeration Stress](http://go.microsoft.com/fwlink/p/?linkid=617494)\*
-   [USB Hub Exposed Port Test](http://go.microsoft.com/fwlink/p/?linkid=617489)
-   [USB Hub Selective Suspend Test](http://go.microsoft.com/fwlink/p/?linkid=617500)\*

**Certification tests**

-   [Device.Fundamentals Tests](http://go.microsoft.com/fwlink/p/?linkid=617463)
-   All USB tests listed under [Devices.Connectivity Tests](http://go.microsoft.com/fwlink/p/?linkid=617485)
-   [USB 3.0 Hub Enumeration Stress](http://go.microsoft.com/fwlink/p/?linkid=617494)\*
-   [USB Hub Exposed Port Test](http://go.microsoft.com/fwlink/p/?linkid=617489)
-   [USB Hub Selective Suspend Test](http://go.microsoft.com/fwlink/p/?linkid=617500)\*

## Recommended Windows HCK tests for USB devices


All other USB device manufacturers should run these tests on their embedded or peripheral devices. USB hub manufacturers should also run these tests. Devices must be connected to an xHCI controller for all tests.

**Functional tests**

-   [Device.Fundamentals Tests](http://go.microsoft.com/fwlink/p/?linkid=617463)
-   [USB Device Connection S3+S4 Test](http://go.microsoft.com/fwlink/p/?linkid=617461)

**Certification tests**

-   [Device.Fundamentals Tests](http://go.microsoft.com/fwlink/p/?linkid=617463)
-   [USB (USBDEX) Verifier Test](http://go.microsoft.com/fwlink/p/?linkid=617460)
-   [USB 3.0 Insertion Test](http://go.microsoft.com/fwlink/p/?linkid=617487)
-   [USB 3.0 Speed Switch Test](http://go.microsoft.com/fwlink/p/?linkid=617493)
-   [USB 3.0 Suspend Test](http://go.microsoft.com/fwlink/p/?linkid=617501)
-   [USB Descriptor Test](http://go.microsoft.com/fwlink/p/?linkid=617457)
-   [USB Device Connection S3+S4 Test](http://go.microsoft.com/fwlink/p/?linkid=617461)
-   [USB Disable Enable Test](http://go.microsoft.com/fwlink/p/?linkid=617486)
-   [USB Enumeration Stress](http://go.microsoft.com/fwlink/p/?linkid=617455)
-   [USB Isochronous Alternate Interface Presence Test](http://go.microsoft.com/fwlink/p/?linkid=617490)
-   [USB MS OS Descriptor Test (xHCI)](http://go.microsoft.com/fwlink/p/?linkid=617478)
-   [USB Selective Suspend Test (xHCI)](http://go.microsoft.com/fwlink/p/?linkid=617495)
-   [USB Serial Number Test](http://go.microsoft.com/fwlink/p/?linkid=617459)
-   [USB Topology Compatibility Test](http://go.microsoft.com/fwlink/p/?linkid=617458)

    The test requires that the device is into the EHCI controller and the device is connected to the root port during the test. For some device tests, you can use the MUTT Pack as a full-speed hub as follows:

    1.  Attach the MUTT Pack in the desired topology.
    2.  Ensure the WinUSB driver is loaded for the device.
    3.  Execute the following from an elevated command prompt to switch the MUTT Pack to full-speed mode (the hub will revert to default high speed behavior when it loses power):

        **C:\\usbTest\\MuttUtil.exe –hubfs**

        For more information about the MUTT Pack, see [MUTT devices](microsoft-usb-test-tool--mutt--devices.md).

-   [USB-IF Certification Validation Test (Device)](http://go.microsoft.com/fwlink/p/?linkid=617496)

## Related topics
[Testing USB hardware, drivers, and apps in Windows](usb-driver-testing-guide.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Windows%20Hardware%20Certification%20Kit%20%28HCK%29%20Tests%20for%20USB%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


