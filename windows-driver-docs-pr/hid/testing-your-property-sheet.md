---
title: Testing Your Property Sheet
description: Testing Your Property Sheet
ms.assetid: 9886a758-392b-451d-874d-5ffcc5f9f5cd
keywords: ["property sheets WDK DirectInput , testing", "game controllers WDK DirectInput , property sheet testing", "control panels WDK DirectInput , property sheet testing", "testing property sheets WDK DirectInput", "debugging control panel applications WDK DirectInput"]
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Testing Your Property Sheet





It is highly recommended that you run the debug version of both DirectInput and the DirectInput control panel during the testing of your property sheet page. DirectX components are designed to issue useful errors and warning messages to the debug window/terminal.

Debugging a control panel application can be tricky. Use the following steps to debug a custom property sheet page in Microsoft Developer Studio 5.0 and newer (other compilers have similar behavior).

1.  From the **Project** menu, select **Settings**.

2.  Select the **Debug** tab.

3.  For the Executable for debug session, enter C:\\WINDOWS\\RUNDLL32.EXE (assuming C:\\WINDOWS is the Windows 95/98/Me directory) if you are running Windows 95/98/Me, or C:\\WINNT\\SYSTEM32\\RUNDLL32.EXE (assuming C:\\WINNT is the operating system directory) if you are running Windows NT 4.0 or later.

4.  For the Program arguments, enter **shell32.dll,Control\_RunDLL c:\\windows\\system\\joy.cpl**. Once again, this assumes that C:\\WINDOWS is your Windows directory. It is case sensitive, and must be entered exactly as shown.

Once that is done, set your breakpoints and, from the build menu, select **Start Debug**, then **Go**. You are now ready to debug a custom property sheet page.

 

 




