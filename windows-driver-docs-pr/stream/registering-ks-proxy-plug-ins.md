---
title: Registering KS Proxy Plug-ins
author: windows-driver-content
description: Registering KS Proxy Plug-ins
MS-HAID:
- 'ksproxy\_dg\_82aec31e-afd5-4669-a871-9f99c43d0e3c.xml'
- 'stream.registering\_ks\_proxy\_plug\_ins'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 1f8691cb-5371-4039-a081-7c422dcac5a8
keywords: ["Kernel Streaming Proxy WDK AVStream , registering plug-ins", "registering Kernel Streaming Proxy plug-ins WDK AVStream"]
---

# Registering KS Proxy Plug-ins


Both interface and property page plug-ins must register with KS proxy as a provider of KS proxy extensions.

To register your plug-in, export functions called [DllRegisterServer](http://go.microsoft.com/fwlink/p/?linkid=106441) and [DllUnregisterServer](http://go.microsoft.com/fwlink/p/?linkid=106443) in the DLL that implements the COM object. These functions are declared in *Olectl.h* but are user-defined.

You can reuse a property set's GUID as the CLSID of the component and the IID of the interface that the component supports.

Your implementation of **DllRegisterServer** should do the following:

1.  Call [AMovieDllRegisterServer2](http://go.microsoft.com/fwlink/p/?linkid=106448) with a value of **TRUE** to register the filter.

2.  Call [RegCreateKeyEx](http://go.microsoft.com/fwlink/p/?linkid=106454) to create and receive a handle to the HKLM\\System\\CurrentControlSet\\Control\\MediaInterfaces key.

3.  Use [RegSetValueEx](http://go.microsoft.com/fwlink/p/?linkid=106447) to set a value under the HKLM\\System\\CurrentControlSet\\Control\\MediaInterfaces key that maps your property set to an interface handler. For more information about interface handlers, see [Interface Handler Plug-in](interface-handler-plug-in.md).

4.  Because the key is not one of the predefined registry keys, call [RegCloseKey](http://go.microsoft.com/fwlink/p/?linkid=106444) to close the handle to the key.

5.  Call **RegCreateKeyEx**.

6.  Use **RegSetValueEx** to set a value under the HKLM\\System\\CurrentControlSet\\Control\\MediaSets\\ key that maps your property set to a property page. For more information about property page plug-ins, see [Property Page Plug-in](property-page-plug-in.md).

7.  Because the key is not one of the predefined registry keys, call **RegCloseKey** to close the handle to the key.

Your implementation of **DllUnregisterServer** should do the following:

1.  Call **AMovieDllRegisterServer2** with a value of **FALSE** to unregister the filter.

2.  Call **RegCreateKeyEx** to open the existing key.

3.  Use [RegDeleteKey](http://go.microsoft.com/fwlink/p/?linkid=106446) to delete the subkey.

4.  Call **RegCloseKey** to close the handle to the key.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Registering%20KS%20Proxy%20Plug-ins%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


