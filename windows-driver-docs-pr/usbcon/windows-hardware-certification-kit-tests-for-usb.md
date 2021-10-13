---
description: The Windows Hardware Lab Kit (HLK) tests can be used for additional testing of Systems, USB host controllers, hubs, and devices.
title: Windows Hardware Lab Kit (HLK) Tests for USB
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Windows Hardware Lab Kit (HLK) Tests for USB

The Windows Hardware Lab Kit (HLK) tests can be used for additional testing of Systems, USB host controllers, hubs, and devices. These tests cover basic device functionality, reliability, and compatibility with Windows.

## Prerequisites

Before you start running the logo tests make sure you meet the following requirements:

- To run these tests you will need at least two computers: a test server and a test client.
- The test client must have the latest version of Windows.
- The test client must have EHCI and xHCI controllers, either integrated or as add-in cards. The controllers must expose user-accessible root ports (no integrated hubs).
- Download the Windows HLK to the test server from [Windows Hardware Lab Kit Downloads](/windows-hardware/test/hlk/).

    For detailed information about how to install and use the Windows HLK, see [Windows HLK Getting Started](/windows-hardware/test/hlk/getstarted/windows-hlk-getting-started).

## Hardware requirements for running USB tests in the HLK

To run the HLK tests, you need:

- Your host controller (either integrated or as add-in cards), hubs, or device to certify.

    Open Device Manager on the test client and make sure that the USB controllers that you want to use expose user-accessible root ports (no integrated hubs).

    ![usb root port.](images/roothubports.png)

- USB-IF-compliant external SuperSpeed hub to evaluate system compatibility. We have tested HLK tests with these hubs:
  - [Texas Instruments SuperSpeed (USB 3.0) Hub reference design board (TUSB8040EVM)](https://www.ti.com/lit/ug/sllu130a/sllu130a.pdf).
  - SuperMUTT Pack. See [MUTT devices](microsoft-usb-test-tool--mutt--devices.md).
  - [MUTT devices](microsoft-usb-test-tool--mutt--devices.md) as test devices for hub and controller tests.

Complete set of requirements are given here:

- [USB Bus Controller Testing Prerequisites](/windows-hardware/test/hlk/testref/usb-bus-controller-testing-prerequisites#:~:text=%20USB%20Bus%20Controller%20Testing%20Prerequisites%20%201,is%20required%20for%20USB%20host%20controller...%20More%20)
- [USB Hub.Connectivity Testing Prerequisites](/windows-hardware/test/hlk/testref/usb-hubconnectivity-testing-prerequisites)

## HLK test selection for USB

The USB tests that apply to your system, host controller, hub, or device are automatically selected in HLK Studio.

After you follow steps 1-5 in [Windows HLK Getting Started](/windows-hardware/test/hlk/getstarted/windows-hlk-getting-started), make sure that:

- In step 5,the correct device is selected in the **Selection** tab of HLK Studio.
- In step 6, all the tests that apply to your device are displayed in the **Tests** tab in HLK studio. To run these tests, you must select the test in the left-hand check box and click **Run Selected**. The tests for USB testing are listed in the following section of this document.

For information about scheduling tests, see steps 2-6 in [Windows HLK Getting Started]( /windows-hardware/test/hlk/getstarted/windows-hlk-getting-started).

## Recommended Windows HLK tests

In addition to all of the USB tests that are automatically selected in HLK Studio, we recommend running the Fundamentals tests as well with a MUTT or SuperMUTT connected to system, controller or hub under test. For system submissions, these are the System Fundamentals (SysFund) Tests, for a controller, hub or device submission these are the Device Fundamentals (DevFund) Tests.

- [System Fundamentals (SysFund)](/windows-hardware/test/hlk/testref/system-fundamentals-tests)
- [Device Fundamentals (DevFund)](/windows-hardware/test/hlk/testref/device-devfund-tests)

## Related topics

[Overview of Microsoft USB Test Tool (MUTT) devices](./microsoft-usb-test-tool--mutt--devices.md)