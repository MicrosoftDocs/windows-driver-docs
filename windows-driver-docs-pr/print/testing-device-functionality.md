---
title: Testing Device Functionality
description: Testing Device Functionality
keywords:
- testing device functionality WDK printer
- device functionality testing WDK printer
- functionality testing WDK printer
ms.date: 01/30/2023
---

# Testing Device Functionality

[!include[Print Support Apps](../includes/print-support-apps.md)]

After you have completed all tests of device installation and Plug and Play functionality, verify that the device performs all functions as expected. Print test pages with as many applications and document types as possible.

You should also perform the following additional functionality tests:

1. **User Access:** Verify that users with different levels of system access can print to the device, including users who are logged into the system remotely using the Remote Desktop Connection application.

1. **Special Functionality:** Verify any special functionality that your device supports. For example, if a printer enables bidirectional (bidi) communication, verify that bidi requests from the printer work as expected, such as canceling print jobs from the device and duplex printing.

1. **Job Control:** Verify that print jobs can be paused, canceled, resumed, and restarted. Also verify that multiple print jobs can be started, printed, canceled, and restarted at the same time.
