---
title: Testing System Scenarios
description: This test is focused on making sure the ambient light sensor (ALS) is working properly after system power events such as sleep or hibernate.
ms.date: 01/11/2024
---

# Testing system scenarios

This test is focused on making sure the ambient light sensor (ALS) is working properly after system power events such as sleep or hibernate.

## Set up

Read through the [test requirements](testing-MALT-building-a-light-testing-tool.md) section to ensure you have met the requirements for the tests.

## Brightness stress test procedures

1. On the SUT, run `MALTUtil.exe /stress`.

1. Wait. This test will take approximately 15 minutes. The test will adjusting the brightness of the light while putting the system to sleep.  The test will be looking for how long it takes for the system to react to changes in light and if the sensor produces out of range values during initialization.

1. After the test completes, the results will be displayed on the screen.

See [Integrating Ambient Light Sensors with Computers Running Windows 10 Creators Update](/windows-hardware/design/whitepapers/integrating-ambient-light-sensors-with-computers-running-windows-10-creators-update) for Microsoft's full guidance on integrating light sensors and ambient light response curves.