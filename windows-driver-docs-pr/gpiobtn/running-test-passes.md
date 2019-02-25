---
title: Running test passes
description: The MITT platform can test GPIO buttons by offering both test automation and the option to customize the GPIO patterns that are sent for targeted investigations.
ms.assetid: E24AD015-1E14-4EF9-8443-D0F38FA3321E
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Running test passes


The MITT platform can test GPIO buttons by offering both test automation and the option to customize the GPIO patterns that are sent for targeted investigations.

For more information on the MITT testing tool, contact MittSupport@microsoft.com.

To get started, see [GPIO tests in MITT](https://msdn.microsoft.com/library/windows/hardware/dn919780). Download the installer, unpack its contents, and read the **ReadMe** file for a general overview of the tool.

## <span id="End-to-end_indicator_testing_for_convertibles"></span><span id="end-to-end_indicator_testing_for_convertibles"></span><span id="END-TO-END_INDICATOR_TESTING_FOR_CONVERTIBLES"></span>End-to-end indicator testing for convertibles


It is important to perform end-to-end indicator testing for convertibles to expose any potential issues in the following areas:

-   Various timings when converting the system from one mode to another mode.
-   Mechanical specifics of the convertible.

### <span id="Laptop_to_slate_conversion_test_scenario"></span><span id="laptop_to_slate_conversion_test_scenario"></span><span id="LAPTOP_TO_SLATE_CONVERSION_TEST_SCENARIO"></span>Laptop to slate conversion test scenario

Start with the system in laptop mode (keyboard accessible).

1.  Press the Window button to navigate to **Start**.
2.  Press a letter using the keyboard to start **Search**.
3.  Tap into the edit field. *Validation*: The on-screen-keyboard should not deploy.
4.  Rotate the system (Landscape to Portrait and back). *Validation*: The system should not rotate.
5.  Convert from laptop to slate (the keyboard becomes inaccessible). Example of such actions are: swivel or flip the screen, detach the keyboard, etc.
6.  Tap in the **Search** edit field. *Validation*: The on-screen-keyboard should deploy.
7.  Rotate the system (Landscape to Portrait and back). *Validation*: The system should rotate.

**Note**  
Repeat these steps for each of distinct ways that the system can be converted into the tablet mode.

 

 

 




