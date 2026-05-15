---
title: Test Drivers Using Visual Studio and WDK
description: Learn how to test drivers using Visual Studio and the Windows Driver Kit (WDK). Deploy, install, and run driver tests on remote computers with step-by-step guidance.
ms.date: 12/15/2025
ms.topic: concept-article
---

# Testing a driver

Testing a driver is essential for ensuring reliability and performance. The Windows Driver Kit (WDK) adds a driver testing interface to Visual Studio that you can use to build, deploy, install, and test a driver on a remote test computer on your network. The WDK also provides a collection of device driver tests that you can use to test features and functions of your driver. You can also customize or write your own driver tests by using the Driver Test Template in Visual Studio.

## Video demonstration

This video demonstrates how to run driver-related tests in a test group.

> [!VIDEO bd04733f-896c-4fd6-a13f-fc5892586d79]

## Testing strategies

This section describes some strategies for testing drivers, and information about how you select and configure a remote computer to use for testing.

To prepare a driver for public distribution, run the [Windows Hardware Certification Kit (HCK)](/windows-hardware/test/hlk/). For information about the Windows Certification program and how to obtain the HCK, see [Windows Hardware Certification Program](/previous-versions/windows/hardware/hck/jj124227(v=vs.85)).

The WDK provides the test binaries and tools that make it easy to run the Device Fundamentals tests from the command line.
For more information, see [Run the DevFund Tests via the command-line](../devtest/run-devfund-tests-via-the-command-line.md).

| Topic | Description |
|-------|-------------|
| [Tips for testing drivers during development](strategies-for-testing-drivers-during-development.md) | **When should you start testing?** As soon as you have the requirements for your driver, begin to design test cases that verify the critical requirements. Studies show that finding and fixing defects in code becomes more expensive the longer the defects remain in the code. Finding and fixing defects early in the development cycle is less costly and disruptive than finding defects after the code is released and distributed. Creating your test cases early can also help you find problems in your design. |
| [How to test a driver at runtime using Visual Studio](testing-a-driver-at-runtime.md) | The WDK extensions to Visual Studio provide a device testing interface that enables you to conveniently build, deploy, install, and test a driver on a test computer on your network. The WDK provides a collection of device driver tests that you can use to test the features and functions of your driver. |

## Related topic

[Tools for Verifying Drivers](../devtest/static-and-dynamic-verification-tools.md)
