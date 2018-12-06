---
title: Invoke Device Properties Dialog Box in Installation Application
description: Invoking a Device Properties Dialog Box Programmatically in an Installation Application
ms.assetid: c573acac-581e-44f1-b46b-eceb1f3d5484
keywords:
- device properties dialog box WDK device installations
- invoking device properties dialog box
- DeviceProperties_RunDLL WDK device installations
- programmatically invoke device properties dialog box WDK
- pDeviceProperties function pointer WDK
- machin
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Invoking a Device Properties Dialog Box Programmatically in an Installation Application


To invoke the device properties dialog box programmatically in an installation application, the application code should do the following:

-   Include macro definitions and type definitions in the application code that ensure that the appropriate version of [DeviceProperties_RunDLL](deviceproperties-rundll-function-prototype.md) is linked when the application is built. Windows supports a Unicode version and an ASCII version.

-   Load *devmgr.dll*.

-   Obtain a pointer to the **DeviceProperties_RunDLL** function.

-   Call **DeviceProperties_RunDLL**, supplying the appropriate parameters.

The following code example shows how to define a *pDeviceProperties* function pointer that references the **DeviceProperties_RunDLL** function. If the _UNICODE macro is defined when the code is complied, *pDeviceProperties* is a pointer to the Unicode version of the function; otherwise *pDeviceProperties* is a pointer to the ASCII version of the function.

```cpp
#ifdef _UNICODE 
  #define DeviceProperties_RunDLL  "DeviceProperties_RunDLLW"
 typedef void (_stdcall *PDEVICEPROPERTIES)(
    HWND hwndStub,
    HINSTANCE hAppInstance,
    LPWSTR lpCmdLine,
 int nCmdShow
   ;
#else
  #define DeviceProperties_RunDLL  "DeviceProperties_RunDLLA"
 typedef void (_stdcall *PDEVICEPROPERTIES)(
    HWND hwndStub,
    HHINSTANCE hAppInstance,
    LPSTR lpCmdLine,
 int nCmdShow
  );
#endif

PDEVICEPROPERTIES pDeviceProperties;
```

The following code example uses the definition of *pDeviceProperties* that was provided in the preceding code example and shows how to load *devmgr.dll* programmatically and how to obtain the function pointer to the appropriate version of **DeviceProperties_RunDLL**.

```cpp
HINSTANCE  hDevMgr = LoadLibrary(_TEXT("devmgr.dll"));
 if (hDevMgr) {
 pDeviceProperties = (PDEVICEPROPERTIES)GetProcAddress((HMODULE)hDevMgr, DeviceProperties_RunDLL);
}
```

After obtaining a *pDeviceProperties* function pointer, you must supply a computer name and [device instance identifier](device-instance-ids.md) in a call to **DeviceProperties_RunDLL**. The following code example illustrates the appropriate format and requirements for these items:

-   (Windows XP and later) An optional *machine-name-parameter* field is not supplied, which indicates, by default, that the computer is the local computer. A required *device-instance-ID-parameter* field supplies the device instance identifier "root\\system\\0000".
    ```cpp
    if (pDeviceProperties){
     pDeviceProperties(m_hWnd, NULL, _TEXT("/DeviceID root\\system\\0000"), NULL);
    };
    ```

-   (Windows XP and later) An optional *machine-name-parameter* field is not supplied, which indicates, by default, that the computer is the local computer. A required *device-instance-ID-parameter* field supplies the device instance identifier "PCI\\VEN_8086&DEV_2445 &SUBSYS_010E1028&REV_12\\3&172E68DD&0&FD".
    ```cpp
    if (pDeviceProperties){
     pDeviceProperties(m_hWnd, NULL, _TEXT("/DeviceID PCI\\VEN_8086\&DEV_2445\&SUBSYS_010E1028\&REV_12\\3\&172E68DD\&0\&FD"), NULL);
    };
    ```

-   (Windows 2000 and later) A required *machine-name-parameter* field supplies a pair of double quotation marks ("") for *machine-name*, which indicates that the computer is the local computer. A required *device-instance-ID-parameter* field supplies the device instance identifier "root\\system\\0000".
    ```cpp
    if (pDeviceProperties){
     pDeviceProperties(m_hWnd, NULL, _TEXT("/MachineName \"\" /DeviceID root\\system\\0000"), NULL);
    };
    ```

-   (Windows 2000 and later) A required *machine-name-parameter* field supplies the remote machine name "\\\\RemoteMachineAbc" and a required *device-instance-ID-parameter* field supplies the device instance identifier "root\\system\\0000".
    ```cpp
    if (pDeviceProperties){
     pDeviceProperties(m_hWnd, NULL, _TEXT("/MachineName \\\\RemoteMachineAbc /DeviceID root\\system\\0000"), NULL);
    };
    ```

 

 





