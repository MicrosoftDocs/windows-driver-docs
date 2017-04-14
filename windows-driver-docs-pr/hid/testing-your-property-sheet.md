---
title: Testing Your Property Sheet
author: windows-driver-content
description: Testing Your Property Sheet
ms.assetid: 9886a758-392b-451d-874d-5ffcc5f9f5cd
keywords: ["property sheets WDK DirectInput , testing", "game controllers WDK DirectInput , property sheet testing", "control panels WDK DirectInput , property sheet testing", "testing property sheets WDK DirectInput", "debugging control panel applications WDK DirectInput"]
---

# Testing Your Property Sheet


## <a href="" id="ddk-testing-your-property-sheet-di"></a>


It is highly recommended that you run the debug version of both DirectInput and the DirectInput control panel during the testing of your property sheet page. DirectX components are designed to issue useful errors and warning messages to the debug window/terminal.

Debugging a control panel application can be tricky. Use the following steps to debug a custom property sheet page in Microsoft Developer Studio 5.0 and newer (other compilers have similar behavior).

1.  From the **Project** menu, select **Settings**.

2.  Select the **Debug** tab.

3.  For the Executable for debug session, enter C:\\WINDOWS\\RUNDLL32.EXE (assuming C:\\WINDOWS is the Windows 95/98/Me directory) if you are running Windows 95/98/Me, or C:\\WINNT\\SYSTEM32\\RUNDLL32.EXE (assuming C:\\WINNT is the operating system directory) if you are running Windows NT 4.0 or later.

4.  For the Program arguments, enter **shell32.dll,Control\_RunDLL c:\\windows\\system\\joy.cpl**. Once again, this assumes that C:\\WINDOWS is your Windows directory. It is case sensitive, and must be entered exactly as shown.

Once that is done, set your breakpoints and, from the build menu, select **Start Debug**, then **Go**. You are now ready to debug a custom property sheet page.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Testing%20Your%20Property%20Sheet%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


