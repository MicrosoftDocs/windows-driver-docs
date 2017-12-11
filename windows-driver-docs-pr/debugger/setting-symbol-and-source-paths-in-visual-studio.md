---
title: Setting Symbol and Executable Image Paths in Visual Studio
description: The procedure covers Setting Symbol and Executable Image Paths in Visual Studio
ms.assetid: BFFF9BBC-C926-4974-A43E-C3A2DDA74AA4
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Setting Symbol and Executable Image Paths in Visual Studio


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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Setting%20Symbol%20and%20Executable%20Image%20Paths%20in%20Visual%20Studio%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




