---
title: Installing an Advanced Properties Page for a COM Port
author: windows-driver-content
description: Installing an Advanced Properties Page for a COM Port
ms.assetid: 056fd245-a9d2-4a10-9e92-fe75e51f6770
keywords: ["advanced COM port properties page WDK serial devices", "COM ports WDK serial devices", "default user dialog box for COM port", "overriding default dialog box WDK serial devices", "port numbers WDK serial devices", "FIFO control parameters WDK serial devices", "COM port numbers WDK serial devices"]
---

# Installing an Advanced Properties Page for a COM Port


## <a href="" id="ddk-installing-an-advanced-properties-page-for-a-com-port-kg"></a>


The advanced property page displays a default user dialog box for setting FIFO control parameters and selecting a COM port number. However, you can override the default dialog box by supplying a custom dialog box.

To install the system-supplied property page and default dialog box for a COM port, do the following:

1.  Implement a Microsoft Win32 property page provider. For general information about installing property sheet dialogs, see [Providing Device Property Pages](https://msdn.microsoft.com/library/windows/hardware/ff549784).

    In the property page provider, call the system-supplied [**SerialDisplayAdvancedSettings**](https://msdn.microsoft.com/library/windows/hardware/ff547447) routine, which displays the system-supplied default dialog box.

2.  Install the property page provider by setting an **EnumPropPages32** value entry in an *add-registry-section* that is referenced by a device's [**DDInstall section**](https://msdn.microsoft.com/library/windows/hardware/ff547344). See the description of the **EnumPropPages32** value entry in [**INF AddReg Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320).

To override the default dialog box displayed by **SerialDisplayAdvancedSettings**, do the following:

1.  Implement a custom dialog [*DLL*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-dll). The entry point for the dialog is a [**PPORT\_ADVANCED\_DIALOG**](https://msdn.microsoft.com/library/windows/hardware/ff546956)-typed routine.

2.  Install the custom dialog DLL by setting an **EnumAdvancedDialog** entry value in an *add-registry-section* that is referenced by a device's [**DDInstall section**](https://msdn.microsoft.com/library/windows/hardware/ff547344). The type and format of the value entry is the same as that used for a **EnumPropPages32** value entry.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bserports\serports%5D:%20Installing%20an%20Advanced%20Properties%20Page%20for%20a%20COM%20Port%20%20RELEASE:%20%288/4/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


