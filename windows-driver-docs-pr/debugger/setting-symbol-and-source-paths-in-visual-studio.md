---
title: Setting Symbol and Executable Image Paths in Visual Studio
description: The procedure covers Setting Symbol and Executable Image Paths in Visual Studio
ms.assetid: BFFF9BBC-C926-4974-A43E-C3A2DDA74AA4
ms.author: domars
ms.date: 05/11/2018
ms.localizationpriority: medium
---

# Setting Symbol and Executable Image Paths in Visual Studio

> [!IMPORTANT]
> This feature is not available in Windows 10, version 1507 and later versions of the WDK.
>


The procedures shown in this topic require that you have the Windows Driver Kit integrated into Visual Studio. To get the integrated environment, first install Microsoft Visual Studio, and then install the Windows Driver Kit (WDK). For more information, see [Windows Driver Development](https://msdn.microsoft.com/library/windows/hardware/ff557573).

## <span id="Setting_the_Symbol_Path_by_Using_a_Property_Page"></span><span id="setting_the_symbol_path_by_using_a_property_page"></span><span id="SETTING_THE_SYMBOL_PATH_BY_USING_A_PROPERTY_PAGE"></span>Setting the Symbol Path by Using a Property Page


1.  On the host computer, in Visual Studio, choose **Options** from the **Tools** menu.
2.  In the **Options** property box, navigate to **Debugging&gt;Symbols**.
3.  If you want to get symbols from a Microsoft symbol server, check **Microsoft Symbol Servers**.
4.  If you want to get symbols from folders on the host computer, check **Environment Variable: \_NT\_SYMBOL\_PATH**. Then set the \_NT\_SYMBOL\_PATH [environment variable](general-environment-variables.md).

## <span id="Setting_the_Symbol_Path_by_Entering_a_Command"></span><span id="setting_the_symbol_path_by_entering_a_command"></span><span id="SETTING_THE_SYMBOL_PATH_BY_ENTERING_A_COMMAND"></span>Setting the Symbol Path by Entering a Command


In Visual Studio, in the Debugger Immediate Window, enter the [**.sympath (Set Symbol Path)**](-sympath--set-symbol-path-.md) command.

## <span id="Setting_the_Executable_Image_Path_by_Entering_a_Command"></span><span id="setting_the_executable_image_path_by_entering_a_command"></span><span id="SETTING_THE_EXECUTABLE_IMAGE_PATH_BY_ENTERING_A_COMMAND"></span>Setting the Executable Image Path by Entering a Command


In Visual Studio, in the Debugger Immediate Window, enter the [**.exepath (Set Executable Path)**](-exepath--set-executable-path-.md) command.

 

 





