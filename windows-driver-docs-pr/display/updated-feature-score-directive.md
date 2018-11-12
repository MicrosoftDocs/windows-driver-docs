---
title: Updated feature score directive in Windows 8
description: The updated feature score directive is a general installation setting that's required for all Windows 8 drivers that follow the Windows Display Driver Model (WDDM).
ms.assetid: E50E132A-DEC8-42F4-AAF8-05F658990CF5
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





