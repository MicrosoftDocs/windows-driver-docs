---
title: Running test passes
author: windows-driver-content
description: The MITT platform can test GPIO buttons by offering both test automation and the option to customize the GPIO patterns that are sent for targeted investigations.
ms.assetid: E24AD015-1E14-4EF9-8443-D0F38FA3321E
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

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[gpiobtn\gpiobtn]:%20Running%20test%20passes%20%20RELEASE:%20%289/25/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


