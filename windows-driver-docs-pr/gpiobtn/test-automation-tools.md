---
title: Test automation tools
author: windows-driver-content
description: GPIO test automation uses the MITT platform.
ms.assetid: F6C4FCC2-210B-4B6E-9D1A-77842E470025
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

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[gpiobtn\gpiobtn]:%20Test%20automation%20tools%20%20RELEASE:%20%289/25/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


