---
title: Color Coding in the Source Code Pane
description: Color Coding in the Source Code Pane
ms.assetid: 1bc3635b-31ed-4453-aaef-cd5aac637df2
keywords: ["color coding WDK Static Driver Verifier", "Static Driver Verifier Report WDK , Source Code pane", "Source Code pane WDK Static Driver Verifier"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Color%20Coding%20in%20the%20Source%20Code%20Pane%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




