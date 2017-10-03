---
title: Touchscreen laptop system testing
author: windows-driver-content
description: This topic describes tests for touchscreen laptop systems.
ms.assetid: 0DD7865F-C31C-48AD-8775-4AC1E469176F
---

# Touchscreen laptop system testing


This topic describes tests for touchscreen laptop systems.

**Onscreen keyboard deployment (touchscreen laptop systems only)**

1.  Power up the system and go to the **Start** screen.
2.  Perform [Touch keyboard deployment steps](indicator-testing.md#touchkbd).

    *Validation*: The onscreen keyboard should not deploy.

3.  Rotate the system (Landscape to Portrait and back).

    *Validation*: Screen orientation should not change.

## <span id="Docking_station_testing"></span><span id="docking_station_testing"></span><span id="DOCKING_STATION_TESTING"></span>Docking station testing


**Docking the system in slate mode (convertibles with docking system only)**

1.  Have the GPIO docking system available (with a USB keyboard attached if the slate device has no keyboard). For distinguishing between docking and laptops/slate conversion, see [Docking versus laptop slate conversion](docking-versus-laptop-slate-conversion.md). For convertibles, configure the system in slate mode (see [Slate/laptop mode conversion steps](indicator-testing.md#conv)).
2.  Start with the system in slate mode and attach it to the docking system.
3.  Perform [Touch keyboard deployment steps](indicator-testing.md#touchkbd).

    *Validation*: The onscreen keyboard should deploy.

4.  Rotate the system (Landscape to Portrait and back).

    *Validation*: Screen orientation should not change.

## <span id="Physical_buttons_testing"></span><span id="physical_buttons_testing"></span><span id="PHYSICAL_BUTTONS_TESTING"></span>Physical buttons testing


The system can expose the following set of buttons to the users:

-   Power button - required
-   Volume +/- buttons - required
-   Windows button - required
-   Rotation lock button - optional

**Button behavior**

-   For each of the buttons and button combinations that are listed in the following table, validate that the expected behavior occurs in all cases:

    <table>
    <colgroup>
    <col width="33%" />
    <col width="33%" />
    <col width="33%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th align="left">Button or combination</th>
    <th align="left">Press experience</th>
    <th align="left">Press and hold experience</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td align="left">Windows</td>
    <td align="left">Navigate to Start Screen</td>
    <td align="left">N/A</td>
    </tr>
    <tr class="even">
    <td align="left">Volume Up</td>
    <td align="left">Increase volume</td>
    <td align="left">Rapid volume increase</td>
    </tr>
    <tr class="odd">
    <td align="left">Volume Down</td>
    <td align="left">Decrease volume</td>
    <td align="left">Rapid volume decrease</td>
    </tr>
    <tr class="even">
    <td align="left">Rotation Lock</td>
    <td align="left">Rotation lock toggled</td>
    <td align="left">N/A</td>
    </tr>
    <tr class="odd">
    <td align="left">Power</td>
    <td align="left">Power on Connected Standby</td>
    <td align="left"><p>Connected Standby systems</p>
    <ul>
    <li>HoldTime&lt;2s : enter CS</li>
    <li>2&lt;=HoldTime&lt;=10s : slide to power off UX</li>
    <li>HoldTime&gt;10s : power off</li>
    </ul>
    <p>Non-connected Standby systems</p>
    <ul>
    <li>Holdtime&lt; 4s :enter sleep [optional]</li>
    <li>Holdtime&gt;=4s :power off the device</li>
    </ul></td>
    </tr>
    <tr class="even">
    <td align="left">Windows + Volume Up</td>
    <td align="left">Launch or exit Narrator</td>
    <td align="left">N/A</td>
    </tr>
    <tr class="odd">
    <td align="left">Windows + Volume Down</td>
    <td align="left">Perform a screen capture</td>
    <td align="left">N/A</td>
    </tr>
    <tr class="even">
    <td align="left">Windows + Power</td>
    <td align="left">Secure attention sequence (Display lock screen)</td>
    <td align="left">N/A</td>
    </tr>
    </tbody>
    </table>

     

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[gpiobtn\gpiobtn]:%20Touchscreen%20laptop%20system%20testing%20%20RELEASE:%20%289/25/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


