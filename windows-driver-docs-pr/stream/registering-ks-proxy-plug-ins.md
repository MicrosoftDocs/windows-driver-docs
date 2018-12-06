---
title: Registering KS Proxy Plug-ins
description: Registering KS Proxy Plug-ins
ms.assetid: 1f8691cb-5371-4039-a081-7c422dcac5a8
keywords:
- Kernel Streaming Proxy WDK AVStream , registering plug-ins
- registering Kernel Streaming Proxy plug-ins WDK AVStream
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




