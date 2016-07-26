---
title: Invoking a Device Properties Dialog Box Programmatically in an Installation Application
description: Invoking a Device Properties Dialog Box Programmatically in an Installation Application
ms.assetid: c573acac-581e-44f1-b46b-eceb1f3d5484
keywords: ["device properties dialog box WDK device installations", "invoking device properties dialog box", "DeviceProperties_RunDLL WDK device installations", "programmatically invoke device properties dialog box WDK", "pDeviceProperties function pointer WDK", "machin"]
---

# Invoking a Device Properties Dialog Box Programmatically in an Installation Application


To invoke the device properties dialog box programmatically in an installation application, the application code should do the following:

-   Include macro definitions and type definitions in the application code that ensure that the appropriate version of [DeviceProperties\_RunDLL](deviceproperties-rundll-function-prototype.md) is linked when the application is built. Windows supports a Unicode version and an ASCII version.

-   Load *devmgr.dll*.

-   Obtain a pointer to the **DeviceProperties\_RunDLL** function.

-   Call **DeviceProperties\_RunDLL**, supplying the appropriate parameters.

The following code example shows how to define a *pDeviceProperties* function pointer that references the **DeviceProperties\_RunDLL** function. If the \_UNICODE macro is defined when the code is complied, *pDeviceProperties* is a pointer to the Unicode version of the function; otherwise *pDeviceProperties* is a pointer to the ASCII version of the function.

```
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

The following code example uses the definition of *pDeviceProperties* that was provided in the preceding code example and shows how to load *devmgr.dll* programmatically and how to obtain the function pointer to the appropriate version of **DeviceProperties\_RunDLL**.

```
HINSTANCE  hDevMgr = LoadLibrary(_TEXT("devmgr.dll"));
 if (hDevMgr) {
 pDeviceProperties = (PDEVICEPROPERTIES)GetProcAddress((HMODULE)hDevMgr, DeviceProperties_RunDLL);
}
```

After obtaining a *pDeviceProperties* function pointer, you must supply a computer name and [device instance identifier](device-instance-ids.md) in a call to **DeviceProperties\_RunDLL**. The following code example illustrates the appropriate format and requirements for these items:

-   (Windows XP and later) An optional *machine-name-parameter* field is not supplied, which indicates, by default, that the computer is the local computer. A required *device-instance-ID-parameter* field supplies the device instance identifier "root\\system\\0000".
    ```
    if (pDeviceProperties){
     pDeviceProperties(m_hWnd, NULL, _TEXT("/DeviceID root\\system\\0000"), NULL);
    };
    ```

-   (Windows XP and later) An optional *machine-name-parameter* field is not supplied, which indicates, by default, that the computer is the local computer. A required *device-instance-ID-parameter* field supplies the device instance identifier "PCI\\VEN\_8086&DEV\_2445 &SUBSYS\_010E1028&REV\_12\\3&172E68DD&0&FD".
    ```
    if (pDeviceProperties){
     pDeviceProperties(m_hWnd, NULL, _TEXT("/DeviceID PCI\\VEN_8086\&amp;DEV_2445\&amp;SUBSYS_010E1028\&amp;REV_12\\3\&amp;172E68DD\&amp;0\&amp;FD"), NULL);
    };
    ```

-   (Windows 2000 and later) A required *machine-name-parameter* field supplies a pair of double quotation marks ("") for *machine-name*, which indicates that the computer is the local computer. A required *device-instance-ID-parameter* field supplies the device instance identifier "root\\system\\0000".
    ```
    if (pDeviceProperties){
     pDeviceProperties(m_hWnd, NULL, _TEXT("/MachineName \"\" /DeviceID root\\system\\0000"), NULL);
    };
    ```

-   (Windows 2000 and later) A required *machine-name-parameter* field supplies the remote machine name "\\\\RemoteMachineAbc" and a required *device-instance-ID-parameter* field supplies the device instance identifier "root\\system\\0000".
    ```
    if (pDeviceProperties){
     pDeviceProperties(m_hWnd, NULL, _TEXT("/MachineName \\\\RemoteMachineAbc /DeviceID root\\system\\0000"), NULL);
    };
    ```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Invoking%20a%20Device%20Properties%20Dialog%20Box%20Programmatically%20in%20an%20Installation%20Application%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




