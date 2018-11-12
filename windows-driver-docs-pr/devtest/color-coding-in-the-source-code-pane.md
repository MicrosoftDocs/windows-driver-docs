---
title: Color Coding in the Source Code Pane
description: Color Coding in the Source Code Pane
ms.assetid: 1bc3635b-31ed-4453-aaef-cd5aac637df2
keywords:
- color coding WDK Static Driver Verifier
- Static Driver Verifier Report WDK , Source Code pane
- Source Code pane WDK Static Driver Verifier
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Color Coding in the Source Code Pane


SDV uses color coding to help you recognize the code source quickly.

-   The *background color* helps you determine the type of file you are viewing.

-   The *text color* provide information about the code in the file.

-   A *blue highlight* indicates the line of source code that is associated with the element that is selected in the **Trace Tree** pane. It appears only when an element is selected in the **Trace Tree** pane.

### <span id="background_colors"></span><span id="BACKGROUND_COLORS"></span>Background Colors

The **Source Code Pane** includes two background colors, yellow and white.

-   **Yellow**: Indicates source code from the driver, such as C files, header files, and library files.

-   **White**: Indicates source code from SDV. This includes [rule files (.slic)](static-driver-verifier-rule.md) and the operating system model file, Sdv-harness.c.

### <span id="text_colors"></span><span id="TEXT_COLORS"></span>Text Colors

The following text colors are used in the **Source Code** pane:

-   **Green:** Comments.

-   **Red:** Code that is executed in the path to the rule violation.

-   **Black:** Code that is not executed in the path to the rule violation.

-   **Blue:** (Rule source file (\*.slic) only.) Indicates code that is not executed in the path to the rule violation.

 

 





