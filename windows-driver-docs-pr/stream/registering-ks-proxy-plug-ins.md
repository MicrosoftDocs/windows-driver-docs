---
title: Registering KS Proxy Plug-ins
description: Registering KS Proxy Plug-ins
keywords:
- Kernel Streaming Proxy WDK AVStream , registering plug-ins
- registering Kernel Streaming Proxy plug-ins WDK AVStream
ms.date: 06/18/2020
ms.localizationpriority: medium
---

# Registering KS proxy plug-ins

Both interface and property page plug-ins must register with KS proxy as a provider of KS proxy extensions.

To register your plug-in, export functions called [DllRegisterServer](/windows/win32/api/olectl/nf-olectl-dllregisterserver) and [DllUnregisterServer](/windows/win32/api/olectl/nf-olectl-dllunregisterserver) in the DLL that implements the COM object. These functions are declared in *Olectl.h* but are user-defined.

You can reuse a property set's GUID as the CLSID of the component and the IID of the interface that the component supports.

Your implementation of **DllRegisterServer** should do the following:

1. Call [AMovieDllRegisterServer2](/previous-versions//ms778973(v=vs.85)) with a value of **TRUE** to register the filter.

1. Call [RegCreateKeyEx](/windows/win32/api/winreg/nf-winreg-regcreatekeyexa) to create and receive a handle to the HKLM\\System\\CurrentControlSet\\Control\\MediaInterfaces key.

1. Use [RegSetValueEx](/windows/win32/api/winreg/nf-winreg-regsetvalueexa) to set a value under the HKLM\\System\\CurrentControlSet\\Control\\MediaInterfaces key that maps your property set to an interface handler. For more information about interface handlers, see [Interface Handler Plug-in](interface-handler-plug-in.md).

1. Because the key is not one of the predefined registry keys, call [RegCloseKey](/windows/win32/api/winreg/nf-winreg-regclosekey) to close the handle to the key.

1. Call **RegCreateKeyEx**.

1. Use **RegSetValueEx** to set a value under the HKLM\\System\\CurrentControlSet\\Control\\MediaSets\\ key that maps your property set to a property page. For more information about property page plug-ins, see [Property Page Plug-in](property-page-plug-in.md).

1. Because the key is not one of the predefined registry keys, call **RegCloseKey** to close the handle to the key.

Your implementation of **DllUnregisterServer** should do the following:

1. Call **AMovieDllRegisterServer2** with a value of **FALSE** to unregister the filter.

1. Call **RegCreateKeyEx** to open the existing key.

1. Use [RegDeleteKey](/windows/win32/api/winreg/nf-winreg-regdeletekeya) to delete the subkey.

1. Call **RegCloseKey** to close the handle to the key.
