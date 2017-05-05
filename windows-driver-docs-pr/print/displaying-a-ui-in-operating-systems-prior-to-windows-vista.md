---
title: Displaying a UI in Operating Systems Prior to Windows Vista
author: windows-driver-content
description: Displaying a UI in Operating Systems Prior to Windows Vista
ms.assetid: de62310e-b10a-49b0-9bcc-b918318b2728
keywords:
- print spooler customizing WDK , pre-Windows Vista UI display
- spooler customizing WDK print , pre-Windows Vista UI display
- customizing print spooler components WDK , pre-Windows Vista UI display
- displaying UI for print component
- UI displaying WDK print
- user interface WDK print
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Displaying a UI in Operating Systems Prior to Windows Vista


## <a href="" id="ddk-displaying-ui-in-operating-systems-prior-to-windows-codename-longh"></a>


-   Do not display UI in any component that runs in the spooler's process.

    The spooler runs at a high-privilege security level; therefore, displaying UI opens the spooler to the risk of malicious user code.

-   Check for errors in the driver.

    Asynchronous notification calls fail in operating system releases prior to Windows Vista.

-   Display simple dialog boxes by using the [**SplPromptUIInUsersSession**](https://msdn.microsoft.com/library/windows/hardware/ff562679) function.

-   Display complex user interface elements by writing a status monitor.

    A status monitor is an application that the IHV develops and that the user installs. Because the status monitor runs in the user's context under the user's credentials, it is safe for the status monitor to display UI elements at any time. The status monitor can communicate with the spooler by using bidirectional communication or by using the TCPMON Xcv interface. For information, see [Adding Bidirectional Communication](adding-bidirectional-communication.md) and [TCPMON Xcv Interface](tcpmon-xcv-interface.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Displaying%20a%20UI%20in%20Operating%20Systems%20Prior%20to%20Windows%20Vista%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


