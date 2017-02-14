---
title: Updated feature score directive in Windows 8
description: The updated feature score directive is a general installation setting that's required for all Windows 8 drivers that follow the Windows Display Driver Model (WDDM).
ms.assetid: E50E132A-DEC8-42F4-AAF8-05F658990CF5
---

# Updated feature score directive in Windows 8


The updated feature score directive is a general installation setting that's required for all Windows 8 drivers that follow the Windows Display Driver Model (WDDM).

This table shows the values that apply for Windows 8. Key changes are italicized.

**Feature scores for WDDM versions**

| Driver model                     | Feature score                |
|----------------------------------|------------------------------|
| *Windows 8 WHQL*                 | *E0*                         |
| *Windows 8 Pre-Release Driver*   | *E3*                         |
| Windows 7 WHQL                   | E6                           |
| Windows 7 inbox                  | EC                           |
| Windows Vista WHQL               | F6                           |
| Windows Vista inbox              | F8                           |
| *Microsoft Basic Display Driver* | *FB*                         |
| XDDM third-party                 | FC *(Not used in Windows 8)* |
| XDDM inbox in Windows Vista      | FD *(Not used in Windows 8)* |
| VGA                              | FE *(Not used in Windows 8)* |
| Default or No Score              | FF                           |
| Unsigned drivers                 | No feature score = FF        |

 

Each operating system release introduces a new feature score value. For Windows 8 this is *E3* for in-box and pre-release drivers, and *E0* for WHQL drivers. The feature score is used by Windows to determine which driver to install when multiple possible drivers exist. A driver with a higher ranked feature score is selected.

All Windows 8 in-box driver devices have a higher ranked feature score than all existing Windows 7 drivers because the in-box drivers are tested on Windows 8, and existing Windows 7Windows 7 drivers have not been. This results in the in-box Windows 8 driver replacing existing Windows 7 drivers. An independent hardware vendor (IHV) can use the E0 feature score with a Windows 7 driver if the following is true:

-   The driver has been tested for Windows 8.
-   The driver has fixes that make it better than the in-box driver.
-   The driver is intended to be retained on upgrade to Windows 8.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Updated%20feature%20score%20directive%20in%20Windows%208%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




