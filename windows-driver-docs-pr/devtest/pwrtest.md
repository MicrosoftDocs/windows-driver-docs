---
title: PwrTest
description: The power management test tool (PwrTest) is a test tool that enables developers, testers, and system integrators to exercise and record power management information from the system.
ms.assetid: 8c242d61-6c5b-44d9-84d1-f78ef9a56a6d
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PwrTest


The power management test tool (PwrTest) is a test tool that enables developers, testers, and system integrators to exercise and record power management information from the system. You can use PwrTest to automate sleep and resume transitions and record processor power management and battery information from the system over a period of time.

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Where can I download PwrTest?</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>PwrTest.exe is included in the Microsoft Windows Driver Kit (WDK). For information about getting the WDK, see <a href="http://go.microsoft.com/fwlink/p/?linkid=290798" data-raw-source="[Windows Driver Kit Downloads]( http://go.microsoft.com/fwlink/p/?linkid=290798)">Windows Driver Kit Downloads</a>.</p></td>
</tr>
</tbody>
</table>

 

## <span id="Running_PwrTest"></span><span id="running_pwrtest"></span><span id="RUNNING_PWRTEST"></span>Running PwrTest


PwrTest (PwrTest.exe) features robust logging and a command-line interface. PwrTest is capable of logging information to both a Microsoft Windows Test Technologies (WTL) and XML file format.

PwrTest functionality is separated into scenarios. For information about these scenarios, see [PwrTest Scenarios](pwrtest-scenarios.md).

**To run Pwrtest**

1.  To be able to use all PwrTest Scenarios, you must first provision a test computer for testing using Visual Studio and the WDK. For more information, see [Provision a computer for driver deployment and testing (WDK 8.1)](https://msdn.microsoft.com/library/windows/hardware/dn745909), or [Provision a computer for driver deployment and testing (WDK 8)](https://msdn.microsoft.com/library/windows/hardware/hh698272).

    Some scenarios require the power button driver that is part of Windows Driver Testing Framework (WDTF). WDTF (and the included power button driver) is automatically installed when you provision a system for testing using Visual Studio and the WDK.

2.  PwrTest.exe is installed with the WDK. To run Pwrtest on the test computer, you must copy PwrTest.exe from the computer where you installed the WDK.

    You can find PwrTest.exe in the Windows Driver Kit Tools directory (for example, C:\\Program Files (x86)\\Windows Kits\\*&lt;version&gt;*\\Tools\\*&lt;platform&gt;*\\PwrTest.exe).

3.  On the test computer that you have provisioned, open a Command Prompt window with elevated permissions ( **Run as Administrator**) and navigate to the directory where you copied PwrTest.exe.

    **Examples**

    ```
    pwrtest /? 
    ```

    ```
    pwrtest /battery /c:4 /i:1000
    ```

    For more information, see [PwrTest Syntax](pwrtest-syntax.md) and [PwrTest Scenarios](pwrtest-scenarios.md).

## <span id="related_topics"></span>Related topics


[PwrTest Syntax](pwrtest-syntax.md)

[PwrTest Log File](pwrtest-log-file.md)

[PwrTest Scenarios](pwrtest-scenarios.md)

[Provision a computer for driver deployment and testing (WDK 8.1)](https://msdn.microsoft.com/library/windows/hardware/dn745909)

[Provision a computer for driver deployment and testing (WDK 8)](https://msdn.microsoft.com/library/windows/hardware/hh698272)

 

 






