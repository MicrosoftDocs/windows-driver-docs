---
title: Determining if a Debugger is Attached
description: Determining if a Debugger is Attached
ms.assetid: b40482c4-7186-4632-b1d9-3c91a415b7c8
keywords: ["debugging code WDK , attached debuggers", "attached debuggers WDK", "status information WDK debugging"]
---

# Determining if a Debugger is Attached


## <span id="ddk_determining_if_a_debugger_is_attached_tools"></span><span id="DDK_DETERMINING_IF_A_DEBUGGER_IS_ATTACHED_TOOLS"></span>


You may wish to take certain actions with your driver if a kernel debugger is currently attached.

To determine the status of kernel debugging, the following variables and routines are useful:

-   (Microsoft Windows XP and later) The [**KD\_DEBUGGER\_ENABLED**](https://msdn.microsoft.com/library/windows/hardware/ff548118) global kernel variable indicates whether kernel debugging is enabled.

-   (Windows XP and later) The [**KD\_DEBUGGER\_NOT\_PRESENT**](https://msdn.microsoft.com/library/windows/hardware/ff548125) global kernel variable indicates whether a kernel debugger is currently attached.

-   (Microsoft Windows Server 2003 and later) The [**KdRefreshDebuggerNotPresent**](https://msdn.microsoft.com/library/windows/hardware/ff548109) routine refreshes the value of KD\_DEBUGGER\_NOT\_PRESENT.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Determining%20if%20a%20Debugger%20is%20Attached%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




