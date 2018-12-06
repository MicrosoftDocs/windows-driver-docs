---
title: Test automation tools
description: GPIO test automation uses the MITT platform.
ms.assetid: F6C4FCC2-210B-4B6E-9D1A-77842E470025
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Test automation tools


GPIO test automation uses the MITT platform.

To get started, see [GPIO tests in MITT](https://msdn.microsoft.com/library/windows/hardware/dn919780). Download the installer, unpack its contents, and read the **ReadMe** file for a general overview of the tool.

To connect the tool to the system under test, the GPIO button and indicator pin-outs are required. After the board is set up and its related package is installed, you can use it in either of the following ways:

-   Run the existing automation tests for both GPIO buttons and indicator scenarios.
-   Use the pattern-generator to explore additional scenarios.

The test binaries are part of the MITT tool installer. To start the tests, follow the instructions under “Running the GPIO automation” section of the MITT documentation.

The MITT tool can directly generate the GPIO impulses that are needed to simulate the equivalent of various button press actions (press down, hold the button press and releasing the button). The tests are [SimpleIo](http://go.microsoft.com/fwlink/p/?linkid=296486)-based and can detect issues, such as the indicators coming out of sync after power transitions.

**Note**  
The MITT platform can easily accommodate customized input patterns. See the MITT Readme file for instructions on how to generate these.

 

 

 




