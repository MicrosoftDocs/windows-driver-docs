---
title: Indicator testing
author: windows-driver-content
description: This topic describes common indicator step procedures and examples.
ms.assetid: 8FD5728C-30E3-4998-A01D-80894BDB379A
---

# Indicator testing


This topic describes common indicator step procedures and examples.

## <span id="touchkbd"></span><span id="TOUCHKBD"></span>Touch keyboard deployment steps


The following steps test whether the touch keyboard opens automatically (as opposed to the user opening it from the Taskbar). Apply the following steps each time the test instructs you to “Perform touch keyboard deployment steps”.

1.  Press the Windows button to navigate to **Start**.
2.  Slide to bring up the **Charms** menu and select **Search**.
3.  Tap into the edit field.

## <span id="conv"></span><span id="CONV"></span>Slate/laptop mode conversion steps


Convert to slate (or laptop) as indicated by the test.

**Note**  
If the system can convert to the slate mode by using more than one method, please repeat the test steps for each method.

Various form factors allow for different methods of conversion, such as the following:

-   Attach or detach keyboard
-   Flip the screen
-   Swivel the screen
-   Slide the screen to cover or uncover the keyboard

**Conversion examples:**

![keyboard attach and detach for convertible](images/keyboardattachdetachconvertible.jpg)

**Figure 1 Keyboard Attach and Detach Conversion**

![screen swivel convertible](images/screenswivelconvertible.jpg)

**Figure 2 Screen Swivel Conversion**

 

**Slate examples:**

-   Keyboard detached
-   Keyboard present but not accessible for typing comfortably
    -   Keyboard flapped underneath
    -   Slide underneath
    -   Swivelled

**Laptop mode:**

Keyboard is present and accessible for typing comfortably.

## <span id="Laptop_slate_mode_indicator_scenarios"></span><span id="laptop_slate_mode_indicator_scenarios"></span><span id="LAPTOP_SLATE_MODE_INDICATOR_SCENARIOS"></span>Laptop/slate mode indicator scenarios


It is important to perform end-to-end indicator testing for convertibles to expose any potential issues in the following areas:

-   Various timings when converting the system from one mode to another mode.
-   Mechanical specifics of the convertible.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[gpiobtn\gpiobtn]:%20Indicator%20testing%20%20RELEASE:%20%289/25/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


