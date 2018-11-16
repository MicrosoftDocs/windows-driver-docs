---
title: Convertible testing
description: This topic describes tests for convertibles.
ms.assetid: 8974F615-B979-4EF0-9E24-3AEA375516E4
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Convertible testing


This topic describes tests for convertibles.

**GPIO driver test**

1.  Open Device Manager and expand **Human Interface Devices**.
2.  Search for the GPIO indicator driver.

    *Validation*: "GPIO Laptop or Slate Indicator Driver" should show in the list.

**Determine whether the touchscreen is correctly detected**

-   The system must have a properly working touchscreen for all further testing; this test is a pre-condition.

    *Validation*: The Taskbar should display the Touchscreen Keyboard icon.

    If the Touchscreen Keyboard icon does not display, there must be an error in the touchscreen detection, or a problem higher in the stack that causes the touch keyboard to not function properly.

**Laptop to slate conversion**

1.  Reboot or power on with the system in laptop mode (keyboard accessible). This should be the system-provided keyboard rather than a port dock. Port docking is tested separately.
2.  Perform [Touch keyboard deployment steps](indicator-testing.md#touchkbd).

    *Validation*: The onscreen keyboard should not deploy.

3.  Rotate the system (Landscape to Portrait and back).

    *Validation*: Screen orientation should not change.

4.  Convert from laptop to slate (see [Slate/laptop mode conversion steps](indicator-testing.md#conv)).
5.  Perform [Touch keyboard deployment steps](indicator-testing.md#touchkbd).

    *Validation*: The onscreen keyboard should deploy.

6.  Rotate the system (Landscape to Portrait and back).

    *Validation*: The system should rotate.

7.  Repeat these test steps for each of distinct ways that the system can be converted into the slate mode.

**Slate to laptop conversion**

1.  Reboot or power on with the system in slate mode (keyboard not accessible).
2.  Hold the system in Portrait mode.
3.  Re-attach the keyboard (or flip it back) to convert to Laptop mode.

    *Validation*: The screen should automatically rotate to Landscape immediately after the keyboard becomes fully available, but not sooner.

4.  Perform [Touch keyboard deployment steps](indicator-testing.md#touchkbd).

    *Validation*: The onscreen keyboard should not deploy.

**Laptop to Slate conversion with sleep/Connected Standby**

1.  Start with the system in laptop mode (keyboard accessible).
2.  Perform [Touch keyboard deployment steps](indicator-testing.md#touchkbd).

    *Validation*: The onscreen keyboard should not deploy.

3.  Put the system to sleep (S3 systems) /Connected Standby (CS-capable system).

    Ways to put the system in the sleep state are as follows:

    -   Press the Power button one time.
    -   Close the lid (make sure that this is configured in **ControlPanel\\Power Control**).
    -   Use the **Charms\\Settings\\Power\\Sleep** feature.

    If the system has an LED or power indicator, confirm that it indicates that the system is sleeping.

4.  Convert from laptop to slate (see [Slate/laptop mode conversion steps](indicator-testing.md#conv)).
5.  Perform [Touch keyboard deployment steps](indicator-testing.md#touchkbd).

    *Validation*: The onscreen keyboard should deploy.

 

 




