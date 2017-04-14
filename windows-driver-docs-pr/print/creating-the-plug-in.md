---
title: Creating the Plug-In
author: windows-driver-content
description: Creating the Plug-In
ms.assetid: 4e52c855-f2c6-49b5-ac79-96dcac785579
keywords: ["COM interfaces WDK print , creating plug-ins", "plug-ins WDK print , creating"]
---

# Creating the Plug-In


## <a href="" id="ddk-creating-the-plug-in-gg"></a>


All printer driver plug-ins must define DllMain, DllGetClassObject, and DllCanUnloadNow functions. They must also implement the IClassFactory COM interface and one of the [IPrintOemUI](iprintoemui-com-interface.md), [IPrintOemUI2](iprintoemui2-com-interface.md), [IPrintOemUni](iprintoemuni-com-interface.md), [IPrintOemUni2](iprintoemuni2-com-interface.md), [IPrintOemUni3](iprintoemuni3-com-interface.md), [IPrintOemPS](iprintoemps-com-interface.md), or [IPrintOemPS2](iprintoemps2-com-interface.md) COM interfaces.

When you create either a [user interface plug-in](user-interface-plug-ins.md) or a [rendering plug-in](rendering-plug-ins.md), you should base your code on the [sample UI plug-in](sample-ui-plug-in.md) or the [sample rendering plug-ins](sample-rendering-plug-ins.md) provided in the WDK.

To create either type of plug-in, you must do the following:

1.  Define a DllMain function (described in the Windows SDK documentation).

    This is the entry point for all Win32 DLLs.

2.  Define and export a DllGetClassObject function (described in the Windows SDK documentation).

    The printer driver calls this function to obtain access to the plug-in's implementation of the IClassFactory interface (described in the Windows SDK documentation). When the driver calls DllGetClassObject, it specifies one of the following class identifiers (defined in prcomoem.h):

    CLSID\_OEMUI - for UI plug-ins

    CLSID\_OEMRENDER - for rendering plug-ins

    The driver also specifies an interface identifier of **IID\_IClassFactory**.

    The DllGetClassObject function must create an instance of its IClassFactory interface and return a pointer to it, as illustrated in the sample code.

3.  Implement the IClassFactory COM interface.

    The IClassFactory interface's CreateInstance method should create an instance of the plug-in's implementation of one of the following COM interfaces:

    [IPrintOemUI](iprintoemui-com-interface.md), [IPrintOemUI2](iprintoemui2-com-interface.md), [IPrintOemUni](iprintoemuni-com-interface.md), [IPrintOemUni2](iprintoemuni2-com-interface.md), [IPrintOemUni3](iprintoemuni3-com-interface.md), [IPrintOemPS](iprintoemps-com-interface.md), or [IPrintOemPS2](iprintoemps2-com-interface.md)

    One of the CreateInstance method's inputs is an interface identifier. The driver calls CreateInstance with an interface identifier of **IID\_IUnknown**, meaning the CreateInstance method must return a pointer to the created instance's IUnknown interface (described in the Windows SDK documentation), as illustrated in the sample code.

4.  Implement one of the IPrintOemUI, IPrintOemUI2, IPrintOemUni, IPrintOemUni2, IPrintOemUni3, IPrintOemPS, or IPrintOemPS2 COM interfaces, including the standard IUnknown interface, as illustrated in the sample code.

    The first of the implemented methods to be called by the driver is the IUnknown interface's QueryInterface method (described in the Windows SDK documentation). This method receives one of the [interface identifiers for printer drivers](interface-identifiers-for-printer-drivers.md) as an input argument. The driver calls the method to determine which version of the interface is supported by the plug-in and to receive a pointer to the supported interface.

5.  Define and export a DllCanUnloadNow function (described in the Windows SDK documentation).

    The DllCanUnloadNow function must return S\_OK if all instances of the plug-in-implemented IPrintOemUI, IPrintOemUI2, IPrintOemUni, IPrintOemUni2, IPrintOemUni3, IPrintOemPS, or IPrintOemPS2 COM interfaces have been released. The S\_OK return indicates to the driver that the plug-in can be unloaded.

    Note that when the printer driver unloads the plug-in DLL, it first calls the plug-in's DllCanUnloadNow function. Regardless of the value returned by DllCanUnloadNow, the printer driver then unloads the plug-in DLL by calling the FreeLibrary function. This is done to ensure that the plug-in DLL is unloaded before the driver is unloaded.

    If the plug-in DLL must remain loaded (for example, when it creates a thread that uses the plug-in DLL), the thread must load the DLL, using a call to the LoadLibrary function. When the thread is finished with the DLL, it should call the FreeLibraryAndExitThread function to unload it. In a situation in which a thread has called LoadLibrary, the driver's call to FreeLibrary merely decrements the DLL's reference count, thereby preventing it from being unloaded. The LoadLibrary, FreeLibrary, and FreeLibraryAndExitThread functions are described in the Windows SDK documentation.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Creating%20the%20Plug-In%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


