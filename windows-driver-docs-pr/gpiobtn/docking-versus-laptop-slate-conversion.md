---
title: Docking versus laptop slate conversion
author: windows-driver-content
description: This topic describes the distinctions for indicators between laptop slate conversion and docking actions.
ms.assetid: B6E33F63-5BEA-4588-80D2-F49821856708
---

# Docking versus laptop slate conversion


This topic describes the distinctions for indicators between laptop slate conversion and docking actions.

## <span id="Laptop_slate_conversion"></span><span id="laptop_slate_conversion"></span><span id="LAPTOP_SLATE_CONVERSION"></span>Laptop slate conversion


A laptop slate conversion is a user action that changes the keyboard availability at the same time that the user keeps the system portable (not physically attached). Examples of such actions are as follows:

-   Attach a portable keyboard accessory (with our without a battery pack).
-   Flips, swivels, or revolves a permanently attached keyboard.

## <span id="Docking"></span><span id="docking"></span><span id="DOCKING"></span>Docking


Docking is considered to be the user action of attaching the portable system to a stationary (non-portable) docking accessory. Examples of such actions are as follows:

-   Attach to a port replicator.
-   Attach to a stationary docking accessory that has integrated keyboard. In this case, both a docking action and a laptop/slate conversion occur, so both indicators must be implemented.

**Note**  
USB based docking accessories are outside the scope of the GPIO dock indicator implementation.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[gpiobtn\gpiobtn]:%20Docking%20versus%20laptop%20slate%20conversion%20%20RELEASE:%20%289/25/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


